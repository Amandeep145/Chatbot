import psycopg2
import os



DB_CONFIGS = {
    # Company Name:Avante
    'http://43.241.69.35:8080': {
        'host': '43.241.69.37',
        'port': '5433',
        'database': 'avante_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },

     # Company Name:Innowave
    'http://103.248.60.168:8080': {
        'host': '103.248.60.168',
        'port': '5432',
        'database': 'csc_mp_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },

    # Company Name:egovernance
    'http://43.240.66.152:8080': {
        'host': '43.240.66.154',
        'port': '5432',
        'database': 'egov_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },

     # Company Name:GAGSP
    'http://43.241.69.35:9999': {
        'host': '43.241.69.37',
        'port': '5434',
        'database': 'gagsp_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },
    
    # Company Name:Aksentech
    'http://115.124.114.197:8080': {
        'host': '115.124.114.197',
        'port': '5434',
        'database': 'payroll_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },
     
     # Company Name:biomining
    'http://115.124.114.197:9999': {
        'host': '115.124.114.197',
        'port': '5434',
        'database': 'payroll_prod_bio',
        'user': 'test_read',
        'password': 'Admin@2021',
    },
    
    # Company Name:hit travel
    'http://103.248.60.169:9999': {
        'host': '103.248.60.169',
        'port': '5433',
        'database': 'css_healthcare_wellness_db',
        'user': 'test_read',
        'password': 'Admin@2021',
    },

     # Company Name:INP
    'http://103.248.60.168:9999': {
        'host': '103.248.60.168',
        'port': '5433',
        'database': 'inip_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },
    
    # Company Name:Lifility
    'http://115.124.114.70:9999': {
        'host': '103.248.60.169',
        'port': '5432',
        'database': 'lifility_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },

     # Company Name:MMTSL
    'http://43.241.69.36:9999': {
        'host': '43.241.69.37',
        'port': '5435',
        'database': 'mmtsl_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },
    
    # Company Name:S2 Infotech
    'http://43.241.69.36:8080': {
        'host': '43.241.69.37',
        'port': '5432',
        'database': 's2_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },
    #max
     # Company Name:APMC
    'http://115.124.114.100:8080': {
        'host': '10.10.89.21',
        'port': '5436',
        'database': 'apmc_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },
    
    # Company Name:SVD
    'http://115.124.114.27:8080': {
        'host': '10.10.89.21',
        'port': '5434',
        'database': 'svd_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },

     # Company Name:Rural
    'http://115.124.114.24:9999': {
        'host': '10.10.89.21',
        'port': '5433',
        'database': 'rul_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },

    # Company Name:Vansh
    'http://115.124.114.24:8080': {
        'host': '10.10.89.21',
        'port': '5432',
        'database': 'vap_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },

     # Company Name:One Global Service provider
    'http://43.240.66.152:9999': {
        'host': '43.240.66.154',
        'port': '5433',
        'database': 'ogb_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },

    # Company Name:mequisys
    'http://115.124.114.70:8080': {
        'host': '10.10.89.24',
        'port': '5432',
        'database': 'mequisys_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },

     # Company Name:plus_care_prod
    'http://103.248.60.169:8080': {
        'host': '10.10.89.24',
        'port': '5433',
        'database': 'pluscare_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    },
    
    # Company Name:Global Business Advisory
    'http://115.124.114.27:9999': {
        'host': '10.10.89.21',
        'port': '5435',
        'database': 'gba_prod',
        'user': 'test_read',
        'password': 'Admin@2021',
    }
    # Add more URLs and database configurations as needed
}




def create_connection_now(url):
    db_config = DB_CONFIGS.get(url)
    if db_config is None:
        # URL not found in DB_CONFIGS
        raise ValueError(f"No database configuration found for URL {url}")
    conn = psycopg2.connect(**db_config)
    return conn






#  'http://127.0.0.1:8000': {
#         'host': '10.10.89.12',
#         'port': '5433',
#         'database': 'payroll',
#         'user': 'amandeep_read',
#         'password': 'Amandeep2@23',
#     },
#     'file:///C:/Aman/chat-widget/index.html': {
#         'host': '10.10.89.12',
#         'port': '5433',
#         'database': 'payroll',
#         'user': 'amandeep_read',
#         'password': 'Amandeep2@23',
#     },
