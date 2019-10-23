# Smithsonian Backend

## NOTE: For now, we only have a production environment

## Local
### Management Command to create initial db
```bash
# Create user role
psql -U postgres
create role openday with login encrypted password 'openday';
alter user openday createdb;

# Create db
python manage.py create_db
```

### Create Superuser
```bash
python manage.py createsuperuser
```

## Production
### Deploy
```bash
zappa deploy production
zappa update production
zappa manage production create_db
zappa invoke --raw production "from openday.users.models import CustomUser; CustomUser.objects.create_superuser('admin@admin.com', 'admin')"
zappa manage production migrate (if needed)
```
