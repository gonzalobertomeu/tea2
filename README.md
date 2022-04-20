# TEA -- Trastorno de espectro autista

## PARA LEVANTAR DOCKER
	
	docker start tea-db

## PARA SABER SI SE ESTA ANDANDO
	
	docker ps

## PARA VER LA IP A LA CUAL CONECTAR
	
	docker inspect tea-db

## PARA DETENER EL CONTENEDOR
	
	docker stop tea-db

## IMPORTANTE
	
	No hacer "docker run --"
	No hacer "docker rm tea-db"

---

#Instalación
- Levantar un MongoDB (descargar desde pagina oficial o levantar un container con MongoDB como se explica arriba).
- Instalar Python 3.7 y PIP
- Instalar con PIP: ´´´pip install mongoengine numpy opencv-pyhon cmake dlib´´´
- Si hay problemas al instalar dlib, instalar Anaconda y herramientas de compilación de C (cmake) en el sistema operativo correpondiente (Instalar de paginas oficiales)
- Apuntar 
- Ejecutar python start.py



