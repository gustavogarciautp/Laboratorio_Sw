# Generated by Django 2.2 on 2019-06-10 22:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombres', models.CharField(default='', max_length=30, verbose_name='Nombres')),
                ('apellidos', models.CharField(default='', max_length=30, verbose_name='Apellidos')),
                ('pais', models.CharField(choices=[['Afganistán', 'Afganistán'], ['Akrotiri', 'Akrotiri'], ['Albania', 'Albania'], ['Alemania', 'Alemania'], ['Andorra', 'Andorra'], ['Angola', 'Angola'], ['Anguila', 'Anguila'], ['Antártida', 'Antártida'], ['Antigua y Barbuda', 'Antigua y Barbuda'], ['Antillas Neerlandesas', 'Antillas Neerlandesas'], ['Arabia Saudí', 'Arabia Saudí'], ['Arctic Ocean', 'Arctic Ocean'], ['Argelia', 'Argelia'], ['Argentina', 'Argentina'], ['Armenia', 'Armenia'], ['Aruba', 'Aruba'], ['Ashmore andCartier Islands', 'Ashmore andCartier Islands'], ['Atlantic Ocean', 'Atlantic Ocean'], ['Australia', 'Australia'], ['Austria', 'Austria'], ['Azerbaiyán', 'Azerbaiyán'], ['Bahamas', 'Bahamas'], ['Bahráin', 'Bahráin'], ['Bangladesh', 'Bangladesh'], ['Barbados', 'Barbados'], ['Bélgica', 'Bélgica'], ['Belice', 'Belice'], ['Benín', 'Benín'], ['Bermudas', 'Bermudas'], ['Bielorrusia', 'Bielorrusia'], ['Birmania Myanmar', 'Birmania Myanmar'], ['Bolivia', 'Bolivia'], ['Bosnia y Hercegovina', 'Bosnia y Hercegovina'], ['Botsuana', 'Botsuana'], ['Brasil', 'Brasil'], ['Brunéi', 'Brunéi'], ['Bulgaria', 'Bulgaria'], ['Burkina Faso', 'Burkina Faso'], ['Burundi', 'Burundi'], ['Bután', 'Bután'], ['Cabo Verde', 'Cabo Verde'], ['Camboya', 'Camboya'], ['Camerún', 'Camerún'], ['Canadá', 'Canadá'], ['Chad', 'Chad'], ['Chile', 'Chile'], ['China', 'China'], ['Chipre', 'Chipre'], ['Clipperton Island', 'Clipperton Island'], ['Colombia', 'Colombia'], ['Comoras', 'Comoras'], ['Congo', 'Congo'], ['Coral Sea Islands', 'Coral Sea Islands'], ['Corea del Norte', 'Corea del Norte'], ['Corea del Sur', 'Corea del Sur'], ['Costa de Marfil', 'Costa de Marfil'], ['Costa Rica', 'Costa Rica'], ['Croacia', 'Croacia'], ['Cuba', 'Cuba'], ['Dhekelia', 'Dhekelia'], ['Dinamarca', 'Dinamarca'], ['Dominica', 'Dominica'], ['Ecuador', 'Ecuador'], ['Egipto', 'Egipto'], ['El Salvador', 'El Salvador'], ['El Vaticano', 'El Vaticano'], ['Emiratos Árabes Unidos', 'Emiratos Árabes Unidos'], ['Eritrea', 'Eritrea'], ['Eslovaquia', 'Eslovaquia'], ['Eslovenia', 'Eslovenia'], ['España', 'España'], ['Estados Unidos', 'Estados Unidos'], ['Estonia', 'Estonia'], ['Etiopía', 'Etiopía'], ['Filipinas', 'Filipinas'], ['Finlandia', 'Finlandia'], ['Fiyi', 'Fiyi'], ['Francia', 'Francia'], ['Gabón', 'Gabón'], ['Gambia', 'Gambia'], ['Gaza Strip', 'Gaza Strip'], ['Georgia', 'Georgia'], ['Ghana', 'Ghana'], ['Gibraltar', 'Gibraltar'], ['Granada', 'Granada'], ['Grecia', 'Grecia'], ['Groenlandia', 'Groenlandia'], ['Guam', 'Guam'], ['Guatemala', 'Guatemala'], ['Guernsey', 'Guernsey'], ['Guinea', 'Guinea'], ['Guinea Ecuatorial', 'Guinea Ecuatorial'], ['Guinea-Bissau', 'Guinea-Bissau'], ['Guyana', 'Guyana'], ['Haití', 'Haití'], ['Honduras', 'Honduras'], ['Hong Kong', 'Hong Kong'], ['Hungría', 'Hungría'], ['India', 'India'], ['Indian Ocean', 'Indian Ocean'], ['Indonesia', 'Indonesia'], ['Irán', 'Irán'], ['Iraq', 'Iraq'], ['Irlanda', 'Irlanda'], ['Isla Bouvet', 'Isla Bouvet'], ['Isla Christmas', 'Isla Christmas'], ['Isla Norfolk', 'Isla Norfolk'], ['Islandia', 'Islandia'], ['Islas Caimán', 'Islas Caimán'], ['Islas Cocos', 'Islas Cocos'], ['Islas Cook', 'Islas Cook'], ['Islas Feroe', 'Islas Feroe'], ['Islas Georgia del Sur y Sandwich del Sur', 'Islas Georgia del Sur y Sandwich del Sur'], ['Islas Heard y McDonald', 'Islas Heard y McDonald'], ['Islas Malvinas', 'Islas Malvinas'], ['Islas Marianas del Norte', 'Islas Marianas del Norte'], ['IslasMarshall', 'IslasMarshall'], ['Islas Pitcairn', 'Islas Pitcairn'], ['Islas Salomón', 'Islas Salomón'], ['Islas Turcas y Caicos', 'Islas Turcas y Caicos'], ['Islas Vírgenes Americanas', 'Islas Vírgenes Americanas'], ['Islas Vírgenes Británicas', 'Islas Vírgenes Británicas'], ['Israel', 'Israel'], ['Italia', 'Italia'], ['Jamaica', 'Jamaica'], ['Jan Mayen', 'Jan Mayen'], ['Japón', 'Japón'], ['Jersey', 'Jersey'], ['Jordania', 'Jordania'], ['Kazajistán', 'Kazajistán'], ['Kenia', 'Kenia'], ['Kirguizistán', 'Kirguizistán'], ['Kiribati', 'Kiribati'], ['Kuwait', 'Kuwait'], ['Laos', 'Laos'], ['Lesoto', 'Lesoto'], ['Letonia', 'Letonia'], ['Líbano', 'Líbano'], ['Liberia', 'Liberia'], ['Libia', 'Libia'], ['Liechtenstein', 'Liechtenstein'], ['Lituania', 'Lituania'], ['Luxemburgo', 'Luxemburgo'], ['Macao', 'Macao'], ['Macedonia', 'Macedonia'], ['Madagascar', 'Madagascar'], ['Malasia', 'Malasia'], ['Malaui', 'Malaui'], ['Maldivas', 'Maldivas'], ['Malí', 'Malí'], ['Malta', 'Malta'], ['Man, Isle of', 'Man, Isle of'], ['Marruecos', 'Marruecos'], ['Mauricio', 'Mauricio'], ['Mauritania', 'Mauritania'], ['Mayotte', 'Mayotte'], ['México', 'México'], ['Micronesia', 'Micronesia'], ['Moldavia', 'Moldavia'], ['Mónaco', 'Mónaco'], ['Mongolia', 'Mongolia'], ['Montserrat', 'Montserrat'], ['Mozambique', 'Mozambique'], ['Namibia', 'Namibia'], ['Nauru', 'Nauru'], ['Navassa Island', 'Navassa Island'], ['Nepal', 'Nepal'], ['Nicaragua', 'Nicaragua'], ['Níger', 'Níger'], ['Nigeria', 'Nigeria'], ['Niue', 'Niue'], ['Noruega', 'Noruega'], ['Nueva Caledonia', 'Nueva Caledonia'], ['Nueva Zelanda', 'Nueva Zelanda'], ['Omán', 'Omán'], ['Pacific Ocean', 'Pacific Ocean'], ['Países Bajos', 'Países Bajos'], ['Pakistán', 'Pakistán'], ['Palaos', 'Palaos'], ['Panamá', 'Panamá'], ['Papúa-Nueva Guinea', 'Papúa-Nueva Guinea'], ['Paracel Islands', 'Paracel Islands'], ['Paraguay', 'Paraguay'], ['Perú', 'Perú'], ['Polinesia Francesa', 'Polinesia Francesa'], ['Polonia', 'Polonia'], ['Portugal', 'Portugal'], ['Puerto Rico', 'Puerto Rico'], ['Qatar', 'Qatar'], ['Reino Unido', 'Reino Unido'], ['República Centroafricana', 'República Centroafricana'], ['República Checa', 'República Checa'], ['República Democrática del Congo', 'República Democrática del Congo'], ['República Dominicana', 'República Dominicana'], ['Ruanda', 'Ruanda'], ['Rumania', 'Rumania'], ['Rusia', 'Rusia'], ['Sáhara Occidental', 'Sáhara Occidental'], ['Samoa', 'Samoa'], ['Samoa Americana', 'Samoa Americana'], ['San Cristóbal y Nieves', 'San Cristóbal y Nieves'], ['San Marino', 'San Marino'], ['San Pedro y Miquelón', 'San Pedro y Miquelón'], ['San Vicente y las Granadinas', 'San Vicente y las Granadinas'], ['Santa Helena', 'Santa Helena'], ['Santa Lucía', 'Santa Lucía'], ['Santo Tomé y Príncipe', 'Santo Tomé y Príncipe'], ['Senegal', 'Senegal'], ['Seychelles', 'Seychelles'], ['Sierra Leona', 'Sierra Leona'], ['Singapur', 'Singapur'], ['Siria', 'Siria'], ['Somalia', 'Somalia'], ['Southern Ocean', 'Southern Ocean'], ['Spratly Islands', 'Spratly Islands'], ['Sri Lanka', 'Sri Lanka'], ['Suazilandia', 'Suazilandia'], ['Sudáfrica', 'Sudáfrica'], ['Sudán', 'Sudán'], ['Suecia', 'Suecia'], ['Suiza', 'Suiza'], ['Surinam', 'Surinam'], ['Svalbard y Jan Mayen', 'Svalbard y Jan Mayen'], ['Tailandia', 'Tailandia'], ['Taiwán', 'Taiwán'], ['Tanzania', 'Tanzania'], ['Tayikistán', 'Tayikistán'], ['TerritorioBritánicodel Océano Indico', 'TerritorioBritánicodel Océano Indico'], ['Territorios Australes Franceses', 'Territorios Australes Franceses'], ['Timor Oriental', 'Timor Oriental'], ['Togo', 'Togo'], ['Tokelau', 'Tokelau'], ['Tonga', 'Tonga'], ['Trinidad y Tobago', 'Trinidad y Tobago'], ['Túnez', 'Túnez'], ['Turkmenistán', 'Turkmenistán'], ['Turquía', 'Turquía'], ['Tuvalu', 'Tuvalu'], ['Ucrania', 'Ucrania'], ['Uganda', 'Uganda'], ['Unión Europea', 'Unión Europea'], ['Uruguay', 'Uruguay'], ['Uzbekistán', 'Uzbekistán'], ['Vanuatu', 'Vanuatu'], ['Venezuela', 'Venezuela'], ['Vietnam', 'Vietnam'], ['Wake Island', 'Wake Island'], ['Wallis y Futuna', 'Wallis y Futuna'], ['West Bank', 'West Bank'], ['World', 'World'], ['Yemen', 'Yemen'], ['Yibuti', 'Yibuti'], ['Zambia', 'Zambia'], ['Zimbabue', 'Zimbabue']], default='', max_length=30, verbose_name='Pais')),
                ('email', models.EmailField(default='', max_length=255, unique=True, verbose_name='Email')),
                ('genero', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otros', 'Otros')], default='', max_length=10, null=True, verbose_name='Genero')),
                ('contraseña', models.CharField(default='', max_length=128, verbose_name='Contraseña')),
                ('id_restablecimiento', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Id Recuperacion')),
                ('log', models.BooleanField(blank=True, default=False, null=True, verbose_name='logueo')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Interes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=30, null=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Interes',
                'verbose_name_plural': 'Interes',
            },
        ),
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('iso', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('pais', models.CharField(default='', max_length=20)),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('telefono', models.IntegerField(blank=True, default='', null=True, verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=30, verbose_name='Direccion')),
                ('ciudad', models.CharField(max_length=30, verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Administrador',
                'verbose_name_plural': 'Administradores',
            },
            bases=('app_core.user',),
        ),
        migrations.CreateModel(
            name='Egresado',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('activacion', models.BooleanField(default=False, null=True, verbose_name='Activacion')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
            ],
            options={
                'verbose_name': 'Egresado',
                'verbose_name_plural': 'Egresados',
            },
            bases=('app_core.user',),
        ),
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(default='', max_length=20)),
                ('pais_iso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_core.Paises')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Intereses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_core.Interes')),
                ('egresado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_core.Egresado')),
            ],
            options={
                'verbose_name': 'Intereses',
                'verbose_name_plural': 'Intereses',
            },
        ),
    ]