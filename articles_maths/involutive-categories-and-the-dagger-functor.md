
# __Involutive Categories and the Dagger Functor__

## Introduction

A **dagger category**, also called an involutive category, is a category together with a rule that
assigns to each morphism $f : A \to B$ a morphism $f^{\dagger} : B \to A$, the **adjoint** of $f$, in a
way that is an **involution on the morphisms**: $f^{\dagger\dagger} = f$, the identities are fixed,
and the adjoint of a composite reverses the factors, $(g \circ f)^{\dagger} = f^{\dagger} \circ
g^{\dagger}$. The rule is a contravariant functor ${}^{\dagger} : \mathcal{C}^{\mathrm{op}} \to
\mathcal{C}$, the **dagger functor**, which is the identity on objects and is its own inverse. The
morphisms fixed by the involution are the **self-adjoint** morphisms, and the morphisms invertible
with inverse their adjoint are the **unitary** ones. This article develops that involution on the
morphisms, its fixed part and the structure of the unitary and self-adjoint morphisms.

The article presupposes *Universal Properties and Categories* — categories, functors, natural
transformations, the opposite category and monomorphisms — and the involutive structures of this
category: the converse of a relation, treated in *Relation Algebras and the Converse*, which is the
dagger of the category of relations, and inversion in a groupoid, treated in *Groupoids with an
Involution*, which follows in this group.

Three boundaries are observed. The **adjoint** in the operator sense, on a Hilbert space with an inner
product, is Part II and the `* Operator Theory` group of this category, and is named only; here
"adjoint" means the morphism assigned by the dagger and needs no form. The **star** of an algebra with
involution is *Involutive Algebras* and the `- Algebras` group, a different layer, and is named only.
The **2-categorical** and higher structure of dagger categories is not developed; only the involution
and its fixed part are treated.

## Dagger Categories

### The Dagger Functor

**Definition.** A **dagger category** is a category $\mathcal{C}$ together with a functor ${}^{\dagger}
: \mathcal{C}^{\mathrm{op}} \to \mathcal{C}$ that is the identity on objects and satisfies
$({}^{\dagger}) \circ ({}^{\dagger})^{\mathrm{op}} = \mathrm{id}_{\mathcal{C}}$; equivalently, a rule
$f \mapsto f^{\dagger}$ with

$$
\mathrm{id}_A^{\dagger} = \mathrm{id}_A, \qquad (g \circ f)^{\dagger} = f^{\dagger} \circ g^{\dagger},
\qquad f^{\dagger\dagger} = f
$$

for all objects $A$ and all composable morphisms $f, g$. The morphism $f^{\dagger}$ is the **adjoint**
of $f$, and ${}^{\dagger}$ is the **dagger functor**.

A contravariant functor out of $\mathcal{C}^{\mathrm{op}}$ into $\mathcal{C}$ is a covariant functor
out of $\mathcal{C}$, so a dagger functor is equivalently a covariant functor ${}^{\dagger} :
\mathcal{C} \to \mathcal{C}$ that is the identity on objects, is the identity on the assignment
$A \mapsto A$, and satisfies $g \circ f \mapsto f^{\dagger} \circ g^{\dagger}$; the two descriptions
differ only in which way the composition is read, and the article uses the contravariant one.

**Proposition.** The dagger functor is an isomorphism of categories
$\mathcal{C}^{\mathrm{op}} \to \mathcal{C}$ whose inverse is the same functor read as
$\mathcal{C} \to \mathcal{C}^{\mathrm{op}}$; it is an involution of the category, and it carries every
morphism $f : A \to B$ to a morphism $B \to A$.

**Proof.** The two identities $f^{\dagger\dagger} = f$ and $(g \circ f)^{\dagger} = f^{\dagger} \circ
g^{\dagger}$ say that the two readings are mutually inverse on morphisms; being the identity on objects,
the functor is bijective on morphisms of each hom-set, hence an isomorphism of categories, and applying
it twice is the identity.

**Example (relations).** The category $\mathbf{Rel}$ has sets as objects and relations as morphisms,
composition being relational composition. Its dagger is the converse $R^{\dagger} = R^{-1}$ of *Relation
Algebras and the Converse*: the diagonal is fixed, the converse of a composite reverses the factors,
and the converse is an involution. The category $\mathbf{Rel}$ is the standard dagger category.

**Example (the discrete dagger).** Any category becomes a dagger category with $f^{\dagger} = f$ for
every morphism, that is, with the identity rule; this dagger is the **discrete** one, and it is the
involution that fixes every morphism. A dagger category in which every morphism is fixed is exactly a
category with the discrete dagger, so the discrete dagger carries no information.

### Unitary and Self-Adjoint Morphisms

**Definition.** Let $\mathcal{C}$ be a dagger category.

- $f : A \to B$ is an **isometry** if $f^{\dagger} \circ f = \mathrm{id}_A$;
- $f$ is a **coisometry** if $f \circ f^{\dagger} = \mathrm{id}_B$;
- $f$ is **unitary** if it is both, that is, if $f^{\dagger}$ is a two-sided inverse of $f$;
- $f$ is **self-adjoint** if $f^{\dagger} = f$, which requires $f$ to be an endomorphism.

**Proposition.** In a dagger category the unitary morphisms are closed under composition and under
adjoint, the identities are unitary, and every isomorphism that is unitary has unitary inverse; so the
unitary morphisms form a **groupoid** with the same objects. A morphism is unitary if and only if it is
an isomorphism and its inverse is its adjoint.

**Proof.** If $f$ and $g$ are unitary and composable then $(g \circ f)^{\dagger} = f^{\dagger} \circ
g^{\dagger}$ is a two-sided inverse of $g \circ f$, because $f^{\dagger}, g^{\dagger}$ are the inverses
of $f, g$; the adjoint of a unitary morphism is unitary with the same witness. The last statement is
the definition of the inverse in a category.

**Proposition.** The self-adjoint endomorphisms of an object are closed under addition when an additive
structure is present and are closed under the adjoint; they are not closed under composition in
general. The self-adjoint morphisms of $\mathbf{Rel}$ are the symmetric relations, and the composition
of two symmetric relations need not be symmetric, as *Relation Algebras and the Converse* records.

**Proof.** If $f^{\dagger} = f$ and $g^{\dagger} = g$ and $f, g$ are composable endomorphisms, then $(g
\circ f)^{\dagger} = f^{\dagger} \circ g^{\dagger} = f \circ g$, which need not equal $g \circ f$; the
example of the symmetric relations on a three-element set, whose composite is not symmetric, is
carried over.

**Definition.** A **dagger functor** between dagger categories is a functor $F$ with $F(f^{\dagger}) =
F(f)^{\dagger}$ for every morphism $f$. A dagger functor carries isometries to isometries, coisometries
to coisometries, unitaries to unitaries and self-adjoint morphisms to self-adjoint morphisms.

**Proof.** Apply $F$ to the defining identities and use $F(\mathrm{id}) = \mathrm{id}$ and the
compatibility $F(f^{\dagger}) = F(f)^{\dagger}$.

## The Fixed Part and the Unitary Groupoid

The **fixed part** of the dagger is the class of self-adjoint morphisms, and on each object it is the
set of self-adjoint endomorphisms, a subset of the endomorphism monoid closed under the adjoint and,
in the examples with an additive structure, under sums; the **unitary groupoid** is the groupoid of
unitary morphisms. The two are related by the involution: a unitary endomorphism $u$ is self-adjoint
exactly when $u = u^{\dagger} = u^{-1}$, that is, when $u$ is an involution of the object.

**Definition.** An **involution** on an object $A$ of a dagger category is a unitary endomorphism $u :
A \to A$ with $u \circ u = \mathrm{id}_A$ that is self-adjoint; equivalently $u = u^{\dagger} = u^{-1}$.

**Proposition.** In a dagger category the involutions on an object are exactly the unitary
self-adjoint endomorphisms, and they are the elements of order two of the unitary groupoid at the
object.

**Proof.** A unitary self-adjoint $u$ satisfies $u^{-1} = u^{\dagger} = u$, so $u^2 =
\mathrm{id}$; conversely $u^2 = \mathrm{id}$ and $u^{\dagger} = u^{-1} = u$.

**Example (a group as a dagger category).** A group $G$ becomes a dagger category with one object and
all morphisms invertible, the dagger being inversion $g^{\dagger} = g^{-1}$: inversion is an
involution, $\mathrm{id}^{\dagger} = \mathrm{id}$, and $(gh)^{-1} = h^{-1}g^{-1}$. The unitary
morphisms are all the elements, the self-adjoint elements are those of order at most two, and the
involutions are exactly the elements of order two. The dagger of a one-object groupoid is treated again
in *Groupoids with an Involution*.

**Example (a groupoid as a dagger category).** More generally every groupoid, in the sense of a
category in which every morphism is invertible, is a dagger category with inversion as dagger; the
fixed morphisms are the identities and the elements of order two, and the unitary morphisms are all
morphisms.

## Summary

A dagger category is a category with a contravariant involution on its morphisms: $f^{\dagger\dagger} =
f$, identities fixed, $(g \circ f)^{\dagger} = f^{\dagger} \circ g^{\dagger}$. The rule is the **dagger
functor**, an isomorphism $\mathcal{C}^{\mathrm{op}} \to \mathcal{C}$ that is its own inverse; it is the
formal counterpart on the morphisms of the converse of a relation and of the inversion in a groupoid.

The **unitary** morphisms, those with $f^{\dagger} = f^{-1}$, form a groupoid with the same objects;
the **self-adjoint** morphisms, those with $f^{\dagger} = f$, form the fixed part of the involution and
are closed under the adjoint but not under composition; and the self-adjoint unitaries are the
involutions of the objects, the elements of order two of the unitary groupoid. The category of
relations with the converse is the standard example, and the group with inversion is the
one-object example.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{C}$, ${}^{\dagger}$ | A dagger category and its dagger functor |
| $f^{\dagger}$ | The adjoint of $f$, the image of the involution |
| self-adjoint | $f^{\dagger} = f$; the fixed part of the dagger |
| isometry | $f^{\dagger} \circ f = \mathrm{id}$ |
| coisometry | $f \circ f^{\dagger} = \mathrm{id}$ |
| unitary | $f^{\dagger} = f^{-1}$; the unitary morphisms form a groupoid |
| involution on $A$ | A unitary self-adjoint $u : A \to A$; $u = u^{\dagger} = u^{-1}$, $u^2 = \mathrm{id}$ |

## Further Reading

- Francis Borceux, *Handbook of Categorical Algebra 1* (Cambridge University Press, 1994), for categories, functors, the opposite category and the duality of adjunctions.
- Jiří Adámek, Horst Herrlich and George Strecker, *Abstract and Concrete Categories* (Wiley, 1990), for categories, functors, adjunctions and the fixed part of an endofunctor.
- Michael Barr and Charles Wells, *Category Theory for Computing Science*, 3rd ed. (CRM, 1999), for dagger categories, the opposite category and the involutive structure on morphisms.
- Saunders Mac Lane, *Categories for the Working Mathematician*, 2nd ed. (Springer, 1998), for the basic categorical material on which the dagger structure is imposed.
