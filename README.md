# Find Your FYP Prof

Run `python api.py` and go to http://127.0.0.1:5000/.

## To do:
- [ ] /api/profs    
- [ ] /api/profs/:id
- [ ] /api/review
- [ ] Home page
- [ ] Sign up
- [ ] Log in
- [ ] Prof page
- [ ] Submit review


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

