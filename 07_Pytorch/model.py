import pytorch_lightning as L  # type: ignore[import-not-found]
import torch  # type: ignore[import-not-found]
import torch.nn as nn  # type: ignore[import-not-found]
import torch.optim as optim  # type: ignore[import-not-found]
from data import CharTokenizer


class Generator(L.LightningModule):
    def __init__(self, vocab_size, embedding_dim, hidden_size, tokenizer):
        super().__init__()
        self.save_hyperparameters(ignore=["tokenizer"])
        self.emb_layer = nn.Embedding(vocab_size, embedding_dim)
        self.rnn_layer = nn.LSTM(embedding_dim, hidden_size, batch_first=True)
        self.out_layer = nn.Linear(hidden_size, vocab_size)
        self.tokenizer = tokenizer

        self.loss_fn = nn.CrossEntropyLoss(ignore_index=tokenizer.pad_token)

    def forward(self, encoded, hidden=None):
        emb = self.emb_layer(encoded)
        rnn_out, hidden = self.rnn_layer(emb, hidden)
        out = self.out_layer(rnn_out)
        return out, hidden

    def prepend_bos(self, batch):
        bs = batch.shape[0]
        bos_tokens = torch.full((bs, 1), self.tokenizer.bos_token, device=batch.device)
        output = torch.cat((bos_tokens, batch), dim=1)[:, :-1]
        return output

    def training_step(self, batch, batch_idx):
        inp = self.prepend_bos(batch)
        out, _ = self(inp)
        loss = self.loss_fn(out.transpose(2, 1), batch)
        self.log("loss", loss, prog_bar=True)
        return loss

    def validation_step(self, batch, batch_idx):
        inp = self.prepend_bos(batch)
        out, _ = self(inp)
        loss = self.loss_fn(out.transpose(2, 1), batch)
        self.log("val_loss", loss, prog_bar=True)
        return loss

    def test_step(self, batch, batch_idx):
        inp = self.prepend_bos(batch)
        out, _ = self(inp)
        loss = self.loss_fn(out.transpose(2, 1), batch)
        self.log("test_loss", loss, prog_bar=True)
        return loss

    def configure_optimizers(self):
        return optim.Adam(self.parameters(), lr=1e-4)

    def generate(self, prompt, n_tokens=200):
        encoded_prompt = self.tokenizer.encode(prompt, add_bos_token=True)
        out, hidden = self(encoded_prompt)
        out = out[-1:]
        next_token = torch.distributions.Categorical(out.softmax(-1)).sample()
        generated_tokens = [next_token]
        for _ in range(n_tokens):
            out, hidden = self(next_token, hidden)
            next_token = torch.distributions.Categorical(out.softmax(-1)).sample()
            generated_tokens.append(next_token)
        generated_tokens = torch.cat(generated_tokens, dim=0)
        return self.tokenizer.decode(generated_tokens)


if __name__ == "__main__":
    from data import CharDataModule, load_bookcorpus_data

    data = load_bookcorpus_data()

    tokenizer = CharTokenizer.load("tokenizer.json")
    datamodule = CharDataModule(data, tokenizer)

    generator = Generator(tokenizer.vocab_size, 128, 512, tokenizer)
    trainer = L.Trainer(max_epochs=1)
    trainer.fit(model=generator, datamodule=datamodule)
    trainer.test(model=generator, datamodule=datamodule)

    # prompt = "a"
    # encoded = tokenizer.encode(prompt, add_bos_token=True)
    # out, _ = generator(encoded)
    # print(out)

    prompt = "i want to"
    output = generator.generate(prompt)
    print(output)
    # * a.d sdsoseel h  . y . nn bs r.e i6i mrd  tsdt e.re  ,fndsof$t oho i ep tiu iedv t scbdre rro lwtedeaae bnitrrd eross th hl  t$ t lid suagrord p'  n .on   s   tioaines  aeld t fh  ,e hght 'he  yb. hnsry

    # fake_batch = torch.randint(0, tokenizer.vocab_size - 1, (3, 17))
    # out = generator(fake_batch)
    # print(out)
