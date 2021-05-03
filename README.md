# tycro

my personal website, plan on adding small tinkering projects as i see fit i guess.

[![Docker](https://github.com/croozelberryTea/tycro/actions/workflows/GCP-Deploy.yml/badge.svg)](https://github.com/croozelberryTea/tycro/actions/workflows/GCP-Deploy.yml)

## CI/CD
Isn't this overkill?

Yes.
### Tests:
Maybe some day.

### Deployment: Github Actions to GCP Cloud Run

On push to main, Github Actions builds a container and pushes it to GCP Container Registry. Then it will deploy that container to GCP Cloud Run. 

#### Useful links:

Tutorial for setting up secrets on Github via [Google Cloud tutorials](https://cloud.google.com/community/tutorials/cicd-cloud-run-github-actions).

Useful tutorial for setting up GCP x Flask stuff via [Google Cloud tutorials](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python)

#### Relevant files:
Dockerfile, .github/workflows/GCP-Deploy
