import json

import pytorch_lightning as L  # type: ignore[import-not-found]
import torch  # type: ignore[import-not-found]
from datasets import load_dataset  # type: ignore[import-not-found]
from torch.nn.utils.rnn import pad_sequence  # type: ignore[import-not-found]
from torch.utils.data import DataLoader, Dataset  # type: ignore[import-not-found]


# def load_bookcorpus_data(n=1000000):
def load_bookcorpus_data(n=10000):
    data = load_dataset("bookcorpus", split="train", trust_remote_code=True)[:n]
    return data["text"]


def find_characters_in_data(data):
    characters = set()
    for sentence in data:
        characters.update(set(sentence))
    return sorted(list(characters))


class CharTokenizer:
    def __init__(self, characters):
        self.characters = characters

        self.pad_token = 0
        self.bos_token = 1
        self.unk_token = 2

        self.vocab_size = len(characters) + 3

    def encode(self, sentence):
        encoded = []
        for char in sentence:
            if char not in self.characters:
                encoded.append(self.unk_token)
            else:
                encoded.append(self.characters.index(char) + 3)

        return torch.LongTensor(encoded)

    def decode(self, encoded):
        output = ""
        for idx in encoded:
            if idx < 3:
                continue
            char = self.characters[idx - 3]
            output += char
        return output

    def save(self, path):
        with open(path, "w") as file:
            json.dump(self.characters, file)

    @staticmethod
    def load(path):
        with open(path, "r") as file:
            characters = json.load(file)
        return CharTokenizer(characters)


class CharDataset(Dataset):
    def __init__(self, data, tokenizer):
        super().__init__()
        self.data = data
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        sentence = self.data[index]
        encoded = self.tokenizer.encode(sentence)
        return encoded


class CharDataModule(L.LightningDataModule):
    def __init__(self, data, tokenizer, batch_size=128):
        super().__init__()
        self.tokenizer = tokenizer
        self.batch_size = batch_size

        train_data, val_data, test_data = self.split(data)

        self.train_dataset = CharDataset(train_data, tokenizer)
        self.val_dataset = CharDataset(val_data, tokenizer)
        self.test_dataset = CharDataset(test_data, tokenizer)

    def split(self, data):
        n_train = int(len(data) * 0.8)
        n_val = int(len(data) * 0.1)

        train_data = data[:n_train]
        val_data = data[n_train : n_train + n_val]
        test_data = data[n_train + n_val :]
        return train_data, val_data, test_data

    def collate_fn(self, samples):
        return pad_sequence(
            samples, batch_first=True, padding_value=self.tokenizer.pad_token
        )

    def common_dataloader(self, split):
        dataset = getattr(self, f"{split}_dataset")
        return DataLoader(
            dataset,
            batch_size=self.batch_size,
            shuffle=(split == "train"),
            collate_fn=self.collate_fn,
        )

    def train_dataloader(self):
        return self.common_dataloader("train")

    def val_dataloader(self):
        return self.common_dataloader("val")

    def test_dataloader(self):
        return self.common_dataloader("test")


if __name__ == "__main__":
    data = load_bookcorpus_data()
    # print(data)
    characters = find_characters_in_data(data)
    # print(characters)

    tokenizer = CharTokenizer(characters)
    # sentence = "i like dogs"
    # encoded = tokenizer.encode(sentence)
    # # print(encoded)

    # decoded = tokenizer.decode(encoded)
    # # print(decoded)

    # tokenizer.save("tokenizer.json")
    # loaded_tokenizer = CharTokenizer.load("tokenizer.json")

    # dataset = CharDataset(data, tokenizer)
    # print(dataset[0])

    datamodule = CharDataModule(data, tokenizer)
    print(datamodule)
