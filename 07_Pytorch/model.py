import pytorch_lightning as L  # type: ignore[import-not-found]
import torch  # type: ignore[import-not-found]
import torch.nn as nn  # type: ignore[import-not-found]
from data import CharTokenizer


class Generator(L.LightningModule):
    def __init__(self, vocab_size, embedding_dim, hidden_size, tokenizer):
        super().__init__()
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


if __name__ == "__main__":
    tokenizer = CharTokenizer.load("tokenizer.json")
    generator = Generator(tokenizer.vocab_size, 4, 5, tokenizer)

    fake_batch = torch.randint(0, tokenizer.vocab_size - 1, (3, 17))

    out = generator(fake_batch)
    print(out)
