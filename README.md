# Find Your FYP Prof

Run `python api.py` and go to http://127.0.0.1:5000/.

## To do:
- [x] /api/profs
- [x] /api/profs/:id
- [x] /api/review
- [x] Include rating for prof
- [x] Include average meet up for prof
- [ ] Home page
- [x] Log in
- [x] Profs page
- [x] Prof page
- Submit review
- - [ ] POST /api/review
- - [ ] Submit review page


## APIs

| Method | Endpoint           | Auth  | Returns                 |
|--------|--------------------|-------|-------------------------|
| GET    | /api/profs         | false | List of all profs       |
| GET    | /api/profs/:id     | false | Prof with matching id   |
| POST   | /api/review        | true  | Review                  |

## Database schema

### Prof

| Property | Type             |
|----------|------------------|
| id       | string           |
| name     | string           |
| school   | string           |
| research | Array of strings |

Overall rating and meetup are aggregated by querying related reviews

### Student

| Property | Type             |
|----------|------------------|
| id       | string           |
| email    | string           |

### Review

| Property  | Type             |
|-----------|------------------|
| id        | string           |
| createdAt | datetime         |
| rating    | float            |
| comment   | string           |
| advice    | string           |
| meetup    | int              |
| studentId | string           |
| profId    | string           |

