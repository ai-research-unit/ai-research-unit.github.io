# __The 6 Products of the Quaternioid Real Space__

## Introduction

Each of the two general products of *The Two General Products of the Quaternioid $\mathbb{R}$ Space* has a **symmetric part** and an **antisymmetric part**, taken under the interchange of the two slots; because both products are $\mathbb{R}$-bilinear with both slots linear, the base ring carrying no nontrivial involution, the interchange is the bare exchange of the two arguments, and the split produces four further products from the two:

$$
\tilde q_1\tilde q_2 , \qquad \tilde q_1^{\natural}\tilde q_2 , \qquad \tilde q_1\bullet\tilde q_2 , \qquad \langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t , \qquad \tilde q_1\wedge\tilde q_2 , \qquad \tilde q_1\wedge^{\natural}\tilde q_2 .
$$

The first two of the six are the two general products, then come their two symmetric halves and then their two antisymmetric halves: $\tilde q_1\bullet\tilde q_2=\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)$ is the **Jordan product**, the symmetric half of the plain product; $\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t=\tfrac12(\tilde q_1^{\natural}\tilde q_2+\tilde q_2^{\natural}\tilde q_1)$ is the **quaternion form read as a product**, the symmetric half of the quaternionic product; $\tilde q_1\wedge\tilde q_2=\tfrac12(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)$ is the **cross product**, the antisymmetric half of the plain product; and $\tilde q_1\wedge^{\natural}\tilde q_2=\tfrac12(\tilde q_1^{\natural}\tilde q_2-\tilde q_2^{\natural}\tilde q_1)$ is the **quaternionic cross product**, the antisymmetric half of the quaternionic product. The six are the products of the carrier, and the reconstruction $\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\wedge\tilde q_2$ and $\tilde q_1^{\natural}\tilde q_2=\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t+\tilde q_1\wedge^{\natural}\tilde q_2$ recovers the general products from their halves. Three of the six are the products of the structures of this category, the symmetric plain, the antisymmetric plain and the general quaternionic; the algebra product belongs to the *Quaternions* category, and the two quaternionic halves carry no separate structure here.

This article defines the six, writes each on the coordinates, states the reconstruction and reads the **behaviour at the two equal arguments** of each. It assumes the two products from *The Two General Products of the Quaternioid $\mathbb{R}$ Space* and the annihilation identity of *Relations Between the Two General Products*, both preceding this one; the structures the six define are *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, below this article in this category, and the definitions of their vocabulary are *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, below this article in this category.

**Conventions.** Throughout, $\tilde q_1=q_{1t}e_t+\vec q_1$ and $\tilde q_2=q_{2t}e_t+\vec q_2$ name elements, $(\vec q_1,\vec q_2)=\sum_kq_{1k}q_{2k}$ is the dot product and $\vec q_1\times\vec q_2$ is the cross product of the vector parts, and $\tilde q^{\natural}=q_te_t-\vec q$ is the quaternion conjugation. The plain form is $\langle\tilde q_1,\tilde q_2\rangle=\mathrm{Sc}(\tilde q_1\tilde q_2)$ and the quaternion form is $\langle\tilde q_1,\tilde q_2\rangle_{\natural}=\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)$, read here as the coefficient of the product $\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t$.

## The Symmetric and the Antisymmetric Part

**Definition.** For a binary rule $f$ on $\mathbb{H}$, its **symmetric part** and its **antisymmetric part** are

$$
f^{\mathrm{s}}(\tilde q_1,\tilde q_2)=\tfrac12\bigl(f(\tilde q_1,\tilde q_2)+f(\tilde q_2,\tilde q_1)\bigr) , \qquad f^{\mathrm{a}}(\tilde q_1,\tilde q_2)=\tfrac12\bigl(f(\tilde q_1,\tilde q_2)-f(\tilde q_2,\tilde q_1)\bigr) ,
$$

and $f=f^{\mathrm{s}}+f^{\mathrm{a}}$. The rule is **symmetric** when $f^{\mathrm{a}}=0$ and **antisymmetric** when $f^{\mathrm{s}}=0$.

**Proposition (the split is the bare exchange).** For each of the two general products the split is taken under the plain interchange of the two arguments, and $f^{\mathrm{s}}$ is symmetric, $f^{\mathrm{a}}$ antisymmetric, and both $\mathbb{R}$-bilinear.

*Proof.* The two products are $\mathbb{R}$-bilinear in each slot, so $f(\tilde q_2,\tilde q_1)$ is the value of the same rule with the arguments exchanged and the difference $f(\tilde q_1,\tilde q_2)-f(\tilde q_2,\tilde q_1)$ is additive in each slot; no conjugation enters the exchange, the base ring having no nontrivial involution, and this is the point at which the split here is the bare interchange. Symmetry of $f^{\mathrm{s}}$ and antisymmetry of $f^{\mathrm{a}}$ are immediate from the definitions.

## The Six Products on the Coordinates

**Definition.** The six products are the two general products and their halves,

$$
\tilde q_1\tilde q_2 , \quad \tilde q_1^{\natural}\tilde q_2 , \quad \tilde q_1\bullet\tilde q_2 , \quad \langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t , \quad \tilde q_1\wedge\tilde q_2 , \quad \tilde q_1\wedge^{\natural}\tilde q_2 ,
$$

and on the coordinates they are

| product | rule |
|---|---|
| $\tilde q_1\tilde q_2$ | $\bigl(q_{1t}q_{2t}-(\vec q_1,\vec q_2)\bigr)+q_{1t}\vec q_2+q_{2t}\vec q_1+\vec q_1\times\vec q_2$ |
| $\tilde q_1^{\natural}\tilde q_2$ | $\bigl(q_{1t}q_{2t}+(\vec q_1,\vec q_2)\bigr)+q_{1t}\vec q_2-q_{2t}\vec q_1-\vec q_1\times\vec q_2$ |
| $\tilde q_1\bullet\tilde q_2$ | $\bigl(q_{1t}q_{2t}-(\vec q_1,\vec q_2)\bigr)+q_{1t}\vec q_2+q_{2t}\vec q_1$ |
| $\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t$ | $\bigl(q_{1t}q_{2t}+(\vec q_1,\vec q_2)\bigr)e_t$ |
| $\tilde q_1\wedge\tilde q_2$ | $\vec q_1\times\vec q_2$ |
| $\tilde q_1\wedge^{\natural}\tilde q_2$ | $q_{1t}\vec q_2-q_{2t}\vec q_1-\vec q_1\times\vec q_2$ |

The plain triple is the general plain product, its symmetric half and its antisymmetric half; the quaternionic triple is the same three-fold split of the quaternionic product. The Jordan product is the symmetric part of the plain product and differs from it by the cross-product term; the product $\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t$ is the symmetric part of the quaternionic product and is scalar; the cross product is the antisymmetric part of the plain product and is pure vector; and the quaternionic cross product is the antisymmetric part of the quaternionic product and is pure vector.

**Proposition (the reconstruction).** For all $\tilde q_1,\tilde q_2$,

$$
\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\wedge\tilde q_2 , \qquad \tilde q_1^{\natural}\tilde q_2=\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t+\tilde q_1\wedge^{\natural}\tilde q_2 .
$$

*Proof.* The two general products are the sums of their symmetric and antisymmetric parts by the definition of the split; the four halves are the four products of the table.

So the six products are read from the two general products by one and the same split, and the six are not independent: the two general products alone generate the four halves, and any four of the six determine the other two by the reconstruction. The quaternionic triple is the plain triple with the first factor conjugated, and the conjugation changes the sign of the antisymmetric terms; it leaves the symmetric term with the dot product changed to its negative, which is why the symmetric half of the quaternionic product is the scalar $\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t$ with the plus sign and not the Jordan product.

## The Behaviour at the Two Equal Arguments

The antisymmetric parts vanish at the two equal arguments, so the square of each general product is the algebraic norm of its symmetric half.

**Proposition (the algebraic norms).** For every $\tilde q=q_te_t+\vec q$,

$$
\tilde q^2=\langle\tilde q\rangle e_t+2q_t\vec q , \qquad \tilde q\bullet\tilde q=\tilde q^2 , \qquad \tilde q\wedge\tilde q=0 ,
$$

$$
\tilde q^{\natural}\tilde q=\langle\tilde q\rangle_{\natural}e_t=|\tilde q|^2e_t , \qquad \langle\tilde q,\tilde q\rangle_{\natural}e_t=\langle\tilde q\rangle_{\natural}e_t , \qquad \tilde q\wedge^{\natural}\tilde q=0 ,
$$

with $\langle\tilde q\rangle=q_t^2-\lvert\vec q\rvert^2$ and $\langle\tilde q\rangle_{\natural}=q_t^2+\lvert\vec q\rvert^2$. The square of the plain product is read off the **plain form** $\langle\cdot,\cdot\rangle$ and the square of the quaternionic product off the **quaternion form** $\langle\cdot,\cdot\rangle_{\natural}$; the two antisymmetric products vanish at the two equal arguments, the cross products of a vector with itself being zero.

*Proof.* An antisymmetric rule has $f(\tilde q,\tilde q)=-f(\tilde q,\tilde q)=0$, so $\tilde q\wedge\tilde q=0$ and $\tilde q\wedge^{\natural}\tilde q=0$, and the algebraic norm of a rule is the algebraic norm of its symmetric half, $\tilde q\bullet\tilde q=\tilde q^2$ and $\langle\tilde q,\tilde q\rangle_{\natural}e_t=\tilde q^{\natural}\tilde q$. The two algebraic norms are the two squares of *Comparison Between the Two General Products*, the article preceding this one, namely $\tilde q^2=(q_t^2-\lvert\vec q\rvert^2)e_t+2q_t\vec q$ and $\tilde q^{\natural}\tilde q=\lvert\tilde q\rvert^2e_t$.

So the algebraic norm of the six products carries the two algebraic norms of the chapter: the square of the plain product and the square of the quaternionic product are read off the same two forms $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$, the first giving a general quaternion and the second a scalar, and the two antisymmetric products vanish identically at the two equal arguments, giving no square and no norm. The two algebraic norms are *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*, below this article in this category.

## The Two Exchanges

The products here are those of *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, below this article in this category. Of the six, the antisymmetric plain product is the Lie-layer product and the symmetric plain product the Jordan-layer product; the antisymmetric plain algebra is the only one of the structures satisfying the Jacobi identity, and the general quaternionic product is not a Lie product.

## Summary

The two general products of $\mathbb{H}$ split under the interchange of their two slots, which is the bare exchange of the two arguments. The six products are the two general products $\tilde q_1\tilde q_2$ and $\tilde q_1^{\natural}\tilde q_2$ and their four halves: the Jordan product $\tilde q_1\bullet\tilde q_2=(q_{1t}q_{2t}-(\vec q_1,\vec q_2))+q_{1t}\vec q_2+q_{2t}\vec q_1$, the quaternion form as a product $\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t=(q_{1t}q_{2t}+(\vec q_1,\vec q_2))e_t$, the cross product $\tilde q_1\wedge\tilde q_2=\vec q_1\times\vec q_2$ and the quaternionic cross product $\tilde q_1\wedge^{\natural}\tilde q_2=q_{1t}\vec q_2-q_{2t}\vec q_1-\vec q_1\times\vec q_2$. The reconstruction is $\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\wedge\tilde q_2$ and $\tilde q_1^{\natural}\tilde q_2=\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t+\tilde q_1\wedge^{\natural}\tilde q_2$.

At the two equal arguments the antisymmetric products vanish and each general product equals its symmetric half: $\tilde q\bullet\tilde q=\tilde q^2=\langle\tilde q\rangle e_t+2q_t\vec q$ and $\langle\tilde q,\tilde q\rangle_{\natural}e_t=\tilde q^{\natural}\tilde q=\langle\tilde q\rangle_{\natural}e_t$, so the two squares are read off the two forms $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$; the two antisymmetric products contribute no square.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde q_1\tilde q_2$ | the general plain bilinear product |
| $\tilde q_1^{\natural}\tilde q_2$ | the general quaternionic bilinear product |
| $\tilde q_1\bullet\tilde q_2=\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)$ | the Jordan product, the symmetric half |
| $\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t=\tfrac12(\tilde q_1^{\natural}\tilde q_2+\tilde q_2^{\natural}\tilde q_1)$ | the quaternion form as a product |
| $\tilde q_1\wedge\tilde q_2=\tfrac12(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)=\vec q_1\times\vec q_2$ | the cross product, the antisymmetric half |
| $\tilde q_1\wedge^{\natural}\tilde q_2=\tfrac12(\tilde q_1^{\natural}\tilde q_2-\tilde q_2^{\natural}\tilde q_1)$ | the quaternionic cross product |
| $\tilde q_1\tilde q_2=\tilde q_1\bullet\tilde q_2+\tilde q_1\wedge\tilde q_2$ | the reconstruction of the plain product |
| $\tilde q_1^{\natural}\tilde q_2=\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t+\tilde q_1\wedge^{\natural}\tilde q_2$ | the reconstruction of the quaternionic product |
| $\tilde q^2=\langle\tilde q\rangle e_t+2q_t\vec q$, $\tilde q^{\natural}\tilde q=\langle\tilde q\rangle_{\natural}e_t$ | the two algebraic norms |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, Colloquium Publications 39, 1968), for the symmetrisation of a bilinear product and the Jordan product.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the symmetric and antisymmetric parts of a bilinear rule and the Lie product of an associative algebra.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion product, its symmetrisation and the cross product of its vector part.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the products of the Clifford algebra $\mathrm{Cl}_{0,2}$ and the place of the cross product among them.
