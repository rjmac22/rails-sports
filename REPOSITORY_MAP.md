# Repository map (human + AI navigation)

A fast directory for finding the actual source files. This map supplements the [README research index](README.md); it does **not** replace that index or define a new process.

## Start here by task

| Goal | Go to |
| --- | --- |
| Purpose, study topics and editorial research index | [README.md](README.md) |
| Analytical and editorial principles | [docs/PROJECT_PRINCIPLES.md](docs/PROJECT_PRINCIPLES.md) |
| Penalty shootout research | [Study 01](notebooks/01_penalty_shootout_sudden_death.ipynb), [Study 02](notebooks/02_sudden_death_length.ipynb) |
| Snooker match formats and dependence | [Studies 03–04](notebooks/03_snooker_match_length.ipynb) (then `04_snooker_frame_dependence.ipynb`) |
| Snooker uncertainty and variation | [Studies 05–06](notebooks/05_snooker_parameter_uncertainty.ipynb) |
| Snooker changes in ability / form | [Studies 07–17](notebooks/07_snooker_stale_history.ipynb) |
| Snooker game structure | [Study 18](notebooks/18_snooker_game_structure.ipynb) |
| Reusable Python code | [src/rails_sports/](src/rails_sports/) |
| Tests | [tests/](tests/) |
| Research outputs | [outputs/](outputs/) |

## Directory guide

| Path | Purpose |
| --- | --- |
| [notebooks/](notebooks/) | Numbered sports analyses; names show topic. Look at README for question/story grouping |
| [docs/](docs/) | Project principles; reserved space for documentation |
| [src/rails_sports/](src/rails_sports/) | Reusable code |
| [tests/](tests/) | Test suite |
| [data/raw/](data/raw/) | Raw data location |
| [data/processed/](data/processed/) | Processed data location |
| [outputs/figures/](outputs/figures/) | Figures |
| [outputs/tables/](outputs/tables/) | Tables |
| [pyproject.toml](pyproject.toml) | Python project configuration |

## AI retrieval instructions

1. Open [README.md](README.md) for study inventory and topic grouping; read the particular notebook before describing what it proved.
2. Check [docs/PROJECT_PRINCIPLES.md](docs/PROJECT_PRINCIPLES.md) before designing analysis or editing editorial work.
3. Do not treat notebook numbers as publication order; research can support multiple articles.
4. Do not infer that a local or separate-branch draft exists on the default branch when it is not in this tree.
5. Update this map if the structure changes materially, rather than maintaining an exhaustive file-by-file list.
6. Focus on **publishing work already under way**, not opening extra research tracks.

Related separate repository: [Inside Rails Horse Racing](https://github.com/rjmac22/inside-rails-horse-racing).
