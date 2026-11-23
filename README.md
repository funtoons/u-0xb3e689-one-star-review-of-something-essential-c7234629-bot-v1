[![One-Star Review of Something Essential](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![Rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/funtoons/u-0xb3e689-one-star-review-of-something-essential-c7234629-bot-v1/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![Reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/funtoons/u-0xb3e689-one-star-review-of-something-essential-c7234629-bot-v1/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

# One-Star Review of Something Essential

Entry for the [One-Star Review of Something Essential](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629) bounty on make.fun.

`main.py` writes one single-line deadpan one-star review to `/output/entry.txt`:

> One star. Electricity gives no warning before it leaves and returns the moment you finish lighting the candles.

The review is 111 characters (limit 160). Electricity is the essential: everyone relies on it, it gives no warning when it goes out, and it always comes back the moment you have finished lighting the candles — a real complaint against a thing that cannot be fixed, held deadpan, with the sting in the last few words.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic and offline: standard library only, no network, no randomness, no timestamps. Two runs write byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
