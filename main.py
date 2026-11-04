import pandas as pd
import numpy as np

def process_data():
    # 1. Extract (Membaca file dari folder data/input/)
    df = pd.read_csv('data/input/data_input_dqthon-participants-mock.csv')

    # 2. Transform: Kode Pos & Kota
    df['postal_code'] = df['address'].str.extract(r'(\d+)$')
    df['city'] = df['address'].str.extract(r'(?<=\n)(\w.+)(?=,)') 

    # 3. Transform: Github & Nomor HP
    df['github_profile'] = 'https://github.com/' + df['first_name'].str.lower() + df['last_name'].str.lower()
    df['cleaned_phone_number'] = df['phone_number'].str.replace(r'^(\+62|62)', '0', regex=True)
    df['cleaned_phone_number'] = df['cleaned_phone_number'].str.replace(r'[()-]', '', regex=True)
    df['cleaned_phone_number'] = df['cleaned_phone_number'].str.replace(r'\s+', '', regex=True)

    # 4. Transform: Nama Tim
    def func_team(col):
        abbrev_name = "%s%s" % (col['first_name'][0], col['last_name'][0])
        country = col['country']
        abbrev_institute = '%s' % (''.join(list(map(lambda word: word[0], col['institute'].split()))))
        return "%s-%s-%s" % (abbrev_name, country, abbrev_institute)
    df['team_name'] = df.apply(func_team, axis=1)

    # 5. Transform: Email
    def func_email(col):
        first_name_lower = col['first_name'].lower()
        last_name_lower = col['last_name'].lower()
        institute = ''.join(list(map(lambda word: word[0], str(col['institute']).lower().split())))
        
        if 'Universitas' in str(col['institute']):
            if len(str(col['country']).split()) > 1:
                country = ''.join(list(map(lambda word: word[0], str(col['country']).lower().split())))
            else:
                country = str(col['country'])[:3].lower()
            return "%s%s@%s.ac.%s" % (first_name_lower, last_name_lower, institute, country)
        return "%s%s@%s.com" % (first_name_lower, last_name_lower, institute)
    df['email'] = df.apply(func_email, axis=1)

    # 6. Transform: Format Tanggal (MySQL)
    df['birth_date'] = pd.to_datetime(df['birth_date'], format='%d %b %Y', errors='coerce')
    df['register_at'] = pd.to_datetime(df['register_time'], unit='s')

    # 7. Load (Menyimpan hasil ke folder data/output/)
    df.to_csv('data/output/dqthon-participants-cleaned.csv', index=False)
    print("Data berhasil diproses dan disimpan di data/output/dqthon-participants-cleaned.csv")

if __name__ == "__main__":
    process_data()