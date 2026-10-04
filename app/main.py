from fastapi import FastAPI 
from app.core.config import  get_settings
from app.core.database import init_db
from app.routers import  health, shop_admin
from app.models import cart_item , category, product,adress,cart,payment,order, role, shop_admin,user,shop,user_role
from app.routers import role,products,categories,adress,cart,cart_item,payment,order,user,shop,user_role,shop_admin

settings=get_settings()
app=FastAPI(title=settings.project_name)
app = FastAPI( title="mo.shop API", description="API E-Commerce Backend", version="1.0.0" ) 

@app.get("/health") 
def health_check(): 
    return { "status": "healthy", "service": "mo.shop API", "version": "1.0.0" }

app.include_router(health.router, prefix=settings.api_prefix)
app.include_router(products.router, prefix=settings.api_prefix)
app.include_router(adress.router, prefix=settings.api_prefix)
app.include_router(cart.router, prefix=settings.api_prefix)
app.include_router(cart_item.router, prefix=settings.api_prefix)
app.include_router(categories.router, prefix=settings.api_prefix)
app.include_router(payment.router, prefix=settings.api_prefix)
app.include_router(order.router, prefix=settings.api_prefix)
app.include_router(user.router, prefix=settings.api_prefix)
app.include_router(shop.router, prefix=settings.api_prefix)
app.include_router(shop_admin.router, prefix=settings.api_prefix)
app.include_router(user_role.router, prefix=settings.api_prefix)
app.include_router(role.router, prefix=settings.api_prefix)

@app.on_event("startup")
def on_startup():
    init_db()      # crée les tables si elles n'existent pas


