from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table, Text, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Tablas de asociación many-to-many
attribute_product = Table(
    'attribute_product', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('attribute_id', Integer, ForeignKey('attributes.id')),
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('created_at', DateTime),
    Column('updated_at', DateTime),
    Column('deleted_at', DateTime)
)

category_product = Table(
    'category_product', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('category_id', Integer, ForeignKey('categories.id')),
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('created_at', DateTime),
    Column('updated_at', DateTime),
    Column('deleted_at', DateTime)
)

color_product = Table(
    'color_product', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('color_id', Integer, ForeignKey('colors.id')),
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('created_at', DateTime),
    Column('updated_at', DateTime),
    Column('deleted_at', DateTime)
)

gender_product = Table(
    'gender_product', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('gender_id', Integer, ForeignKey('genders.id')),
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('created_at', DateTime),
    Column('updated_at', DateTime),
    Column('deleted_at', DateTime)
)

material_product = Table(
    'material_product', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('material_id', Integer, ForeignKey('materials.id')),
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('created_at', DateTime),
    Column('updated_at', DateTime),
    Column('deleted_at', DateTime)
)

product_size = Table(
    'product_size', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('size_id', Integer, ForeignKey('sizes.id')),
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('created_at', DateTime),
    Column('updated_at', DateTime),
    Column('deleted_at', DateTime)
)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    second_last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    email_verified_at = Column(DateTime)
    phone_number = Column(String(255), unique=True)
    password = Column(String(255), nullable=False)
    two_factor_secret = Column(Text)
    two_factor_recovery_codes = Column(Text)
    two_factor_confirmed_at = Column(DateTime)
    remember_token = Column(String(100))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    address_id = Column(Integer, ForeignKey('addresses.id'), nullable=False)
    gender_id = Column(Integer, ForeignKey('genders.id'))

    address = relationship("Address", backref="users")
    gender = relationship("Gender", backref="users")


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    street = Column(String(255), nullable=False)
    street_number = Column(String(255), nullable=False)
    unit_number = Column(String(255))
    neighborhood_id = Column(Integer, ForeignKey('neighborhoods.id'), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    neighborhood = relationship("Neighborhood", backref="addresses")


class Neighborhood(Base):
    __tablename__ = 'neighborhoods'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    city = Column(String(50))
    municipality_id = Column(Integer, ForeignKey('municipalities.id'), nullable=False)
    settlement = Column(String(25))
    postal_code = Column(Integer)

    municipality = relationship("Municipality", backref="neighborhoods")


class Municipality(Base):
    __tablename__ = 'municipalities'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    latitude = Column(Float(10, 7))
    longitude = Column(Float(10, 7))

    state = relationship("State", backref="municipalities")


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)

    country = relationship("Country", backref="states")


class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    brand_id = Column(Integer, ForeignKey('brands.id'), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    user = relationship("User", backref="products")
    brand = relationship("Brand", backref="products")
    categories = relationship("Category", secondary=category_product, back_populates="products")
    colors = relationship("Color", secondary=color_product, back_populates="products")
    genders = relationship("Gender", secondary=gender_product, back_populates="products")
    materials = relationship("Material", secondary=material_product, back_populates="products")
    sizes = relationship("Size", secondary=product_size, back_populates="products")
    attributes = relationship("Attribute", secondary=attribute_product, back_populates="products")


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    products = relationship("Product", secondary=category_product, back_populates="categories")


class Color(Base):
    __tablename__ = 'colors'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    products = relationship("Product", secondary=color_product, back_populates="colors")


class Gender(Base):
    __tablename__ = 'genders'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    products = relationship("Product", secondary=gender_product, back_populates="genders")


class Material(Base):
    __tablename__ = 'materials'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    products = relationship("Product", secondary=material_product, back_populates="materials")


class Size(Base):
    __tablename__ = 'sizes'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    products = relationship("Product", secondary=product_size, back_populates="sizes")


class Attribute(Base):
    __tablename__ = 'attributes'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    value = Column(Float, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

    products = relationship("Product", secondary=attribute_product, back_populates="attributes")


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    url = Column(String(255), nullable=False)
    description = Column(String(255))
    order = Column(Integer, default=1)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    product = relationship("Product", backref="images")