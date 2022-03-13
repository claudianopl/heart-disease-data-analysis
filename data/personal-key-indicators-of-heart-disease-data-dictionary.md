Personal key indicators of heart disease → dataset dictionary

| atributo | descrição | tipo de dado | restrições de domínio (PK, FK, Not Null, Check, Default, Identity) | valores possíveis | tamanho | campo verificado |
| --- | --- | --- | --- | --- | --- | --- |
| Race | Indica a raça/etnicidade  | string | Not Null |  |  | ✅ |
| Diabetic | Indica se a pessoa teve ou possui diabetes | string | Not Null | No, Yes, “No, borderline diabetes”, “Yes (during pregnancy)” |  | ✅ |
| PhysicalActivity | indica quanto dias foi praticado atividade física nos ultimos 30 dias | string | Not Null | Yes, No | 3 | ✅ |
| Genhealth | Saúde geral | string | Not Null | Excellent, Fair, Good, Poor, Very good | 9 | ✅ |
| SleepTime | Em média, quantas horas de sono você dorme em um período de 24 horas? | float | Not Null | de 0.0 a 24.0 |  | ✅ |
| Asthma | Indica se a pessoa teve ou tem asma? | string | Not Null | No, Yes |  | ✅ |
| KidneyDisease | Não incluindo pedra no rim, infecção da bexiga ou incontinência, você já foi informado de que tinha doença renal? | string | Not Null | No, Yes |  | ✅ |
| SkinCancer | ja teve ou tem cancer de pele? | string | Not Null | No, Yes | 3 | ✅ |
| HeartDisease | Entrevistados que já relataram ter doença cardíaca coronária (DAC) ou infarto do miocárdio (IM) | string | Not Null | No, Yes | 3 | ✅ |
| BMI | Índice de Massa Corporal (IMC) | float | Not Null | 00.00 | 4 | ✅ |
| Smoking | Você fumou pelo menos 100 cigarros em toda a sua vida? [Nota: 5 maços = 100 cigarros] | string | Not Null | No, Yes | 3 | ✅ |
| AlcoholDrinking | Bebedores pesados (homens adultos que bebem mais de 14 bebidas por semana e mulheres adultas que bebem mais de 7 bebidas por semana | string | Not Null | No, Yes | 3 | ✅ |
| Stroke | indica se o entrevistado já teve um derrame | string | Not Null | No, Yes | 3 | ✅ |
| PhysicalHealth | indica a quantidade de dias, nos últimos 30 dias, em que o entrevistado se sentiu fisicamente saudável | int | Not Null | 0 a 30 | 3 | ✅ |
| MentalHealth | Pensando em sua saúde mental, por quantos dias nos últimos 30 dias sua saúde mental não foi boa? | int | Not Null | 0 a 30 |  | ✅ |
| DiffWalking | Você tem sérias dificuldades para caminhar ou subir escadas? | string | Not Null | No, Yes | 3 | ✅ |
| Sex | indica o sexo do entrevistado | string | Not Null | Male, Female |  | ✅ |
| AgeCategory | indica a faixa idade do entrevistado |  | Not Null | 18-24, 25-29, 80 or older |  | ✅ |