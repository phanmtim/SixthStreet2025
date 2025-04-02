### DISCUSSION.md

```markdown
# Discussion

## Compromises Due to Time Constraints

- **Error Handling & Robustness:** The implementation includes basic error checking (e.g., missing date or insufficient data points) but does not cover all edge cases or implement advanced logging.
- **Caching:** A simple in-memory cache is used to reduce duplicate API calls. In a production system, a more robust caching solution might be necessary.
- **Testing:** Minimal testing is included. A full solution would include comprehensive unit tests and integration tests.

## Versioning

I would adopt [Semantic Versioning](https://semver.org/) (MAJOR.MINOR.PATCH) to communicate changes clearly and maintain backward compatibility.

## Publishing the Library

- **PyPI:** Package the library using `setuptools` and publish it on PyPI with tools like `twine`.
- **Documentation:** Provide thorough documentation and usage examples.
- **CI/CD:** Set up continuous integration (e.g., GitHub Actions) to automate testing and package builds.

## Service-Oriented Design

If designed as a service rather than a library:
- **REST API:** Wrap the functionality in a RESTful API using a framework such as Flask or FastAPI.
- **Concurrency & Scaling:** Implement asynchronous processing and possibly a worker queue to handle concurrent requests.
- **Caching and Rate Limiting:** Use a robust caching mechanism (e.g., Redis) and implement rate limiting to handle API call quotas.
- **Deployment:** Containerize the service (e.g., with Docker) and deploy using orchestration tools like Kubernetes.

## Implementation Comments

- **API Key Security:** In production, API keys should be managed securely (e.g., using environment variables or secret management systems).
- **Data Validation:** More comprehensive data validation and error handling would improve reliability.
- **Extensibility:** The design is modular, making it straightforward to add support for additional endpoints (e.g., intraday data) if needed.

## Time Spent

Approximately 2–3 hours were spent on this exercise, including planning, coding, and preparing the documentation.

## Feedback on the Exercise

- **Clarity:** The problem statement was clear and allowed for creative design decisions.
- **Time-Boxing:** The exercise was well scoped for a couple of hours; additional requirements (e.g., unit tests, CI/CD integration) could simulate a more production-like environment.
- **Practicality:** This exercise effectively tests the ability to design a reusable library that interacts with a real-world API.