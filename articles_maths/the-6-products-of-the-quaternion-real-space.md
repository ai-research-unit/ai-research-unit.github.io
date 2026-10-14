# __The 6 Products of the Quaternion Real Space__

## Introduction

Each of the two general products of *The Two General Products of the Quaternion $\mathbb{R}$ Space* has a **symmetric part** and an **antisymmetric part**, taken under the interchange of the two slots; because both products are $\mathbb{R}$-bilinear with both slots linear, the base ring carrying no nontrivial involution, the interchange is the bare exchange of the two arguments, and the split produces four further products from the two:

$$
\tilde p\tilde q , \qquad \tilde p\bullet\tilde q , \qquad \tilde p\wedge\tilde q , \qquad \tilde p^{\natural}\tilde q , \qquad N(\tilde p,\tilde q)e_0 , \qquad \tilde p\wedge^{\natural}\tilde q .
$$

The middle two of each triple are the symmetric and the antisymmetric halves: $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ is the **Jordan product**, the symmetric half of the plain product; $\tilde p\wedge\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)$ is the **cross product**, its antisymmetric half; $N(\tilde p,\tilde q)e_0=\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)$ is the **quaternion form read as a product**, the symmetric half of the quaternionic product; and $\tilde p\wedge^{\natural}\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)$ is the **quaternionic cross product**, its antisymmetric half. The six are the products of the six algebraic structures of the chapter, and the reconstruction $\tilde p\tilde q=\tilde p\bullet\tilde q+\tilde p\wedge\tilde q$ and $\tilde p^{\natural}\tilde q=N(\tilde p,\tilde q)e_0+\tilde p\wedge^{\natural}\tilde q$ recovers the general products from their halves.

This article defines the six, writes each on the coordinates, states the reconstruction and reads the **behaviour at the two equal arguments** of each. It assumes the two products from *The Two General Products of the Quaternion $\mathbb{R}$ Space* and the annihilation identity of *Relations Between the Two General Products*, both preceding this one; the structures the six define are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, below this article in this category, and the definitions of their vocabulary are *Definitions for the Study of the 6 Algebraic Structures*, below this article in this category.

**Conventions.** Throughout, $\tilde p=p_0e_0+\vec p$ and $\tilde q=q_0e_0+\vec q$ name elements, $(\vec p,\vec q)=\sum_kp_kq_k$ is the dot product and $\vec p\times\vec q$ is the cross product of the vector parts, and $\tilde q^{\natural}=q_0e_0-\vec q$ is the quaternion conjugation. The plain form is $B(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p\tilde q)$ and the quaternion form is $N(\tilde p,\tilde q)=\mathrm{Sc}(\tilde p^{\natural}\tilde q)$, read here as the coefficient of the product $N(\tilde p,\tilde q)e_0$.

## The Symmetric and the Antisymmetric Part

**Definition.** For a binary rule $f$ on $\mathbb{H}$, its **symmetric part** and its **antisymmetric part** are

$$
f^{\mathrm{s}}(\tilde p,\tilde q)=\tfrac12\bigl(f(\tilde p,\tilde q)+f(\tilde q,\tilde p)\bigr) , \qquad f^{\mathrm{a}}(\tilde p,\tilde q)=\tfrac12\bigl(f(\tilde p,\tilde q)-f(\tilde q,\tilde p)\bigr) ,
$$

and $f=f^{\mathrm{s}}+f^{\mathrm{a}}$. The rule is **symmetric** when $f^{\mathrm{a}}=0$ and **antisymmetric** when $f^{\mathrm{s}}=0$.

**Proposition (the split is the bare exchange).** For each of the two general products the split is taken under the plain interchange of the two arguments, and $f^{\mathrm{s}}$ is symmetric, $f^{\mathrm{a}}$ antisymmetric, and both $\mathbb{R}$-bilinear.

*Proof.* The two products are $\mathbb{R}$-bilinear in each slot, so $f(\tilde q,\tilde p)$ is the value of the same rule with the arguments exchanged and the difference $f(\tilde p,\tilde q)-f(\tilde q,\tilde p)$ is additive in each slot; no conjugation enters the exchange, the base ring having no nontrivial involution, and this is the point at which the split here is the bare interchange. Symmetry of $f^{\mathrm{s}}$ and antisymmetry of $f^{\mathrm{a}}$ are immediate from the definitions.

## The Six Products on the Coordinates

**Definition.** The six products are the two general products and their halves,

$$
\tilde p\tilde q , \quad \tilde p\bullet\tilde q , \quad \tilde p\wedge\tilde q , \quad \tilde p^{\natural}\tilde q , \quad N(\tilde p,\tilde q)e_0 , \quad \tilde p\wedge^{\natural}\tilde q ,
$$

and on the coordinates they are

| product | rule |
|---|---|
| $\tilde p\tilde q$ | $\bigl(p_0q_0-(\vec p,\vec q)\bigr)+p_0\vec q+q_0\vec p+\vec p\times\vec q$ |
| $\tilde p\bullet\tilde q$ | $\bigl(p_0q_0-(\vec p,\vec q)\bigr)+p_0\vec q+q_0\vec p$ |
| $\tilde p\wedge\tilde q$ | $\vec p\times\vec q$ |
| $\tilde p^{\natural}\tilde q$ | $\bigl(p_0q_0+(\vec p,\vec q)\bigr)+p_0\vec q-q_0\vec p-\vec p\times\vec q$ |
| $N(\tilde p,\tilde q)e_0$ | $\bigl(p_0q_0+(\vec p,\vec q)\bigr)e_0$ |
| $\tilde p\wedge^{\natural}\tilde q$ | $p_0\vec q-q_0\vec p-\vec p\times\vec q$ |

The plain triple is the general plain product, its symmetric half and its antisymmetric half; the quaternionic triple is the same three-fold split of the quaternionic product. The Jordan product is the symmetric part of the plain product and differs from it by the cross-product term; the cross product is the antisymmetric part of the plain product and is pure vector; the product $N(\tilde p,\tilde q)e_0$ is the symmetric part of the quaternionic product and is scalar; and the quaternionic cross product is its antisymmetric part and is pure vector.

**Proposition (the reconstruction).** For all $\tilde p,\tilde q$,

$$
\tilde p\tilde q=\tilde p\bullet\tilde q+\tilde p\wedge\tilde q , \qquad \tilde p^{\natural}\tilde q=N(\tilde p,\tilde q)e_0+\tilde p\wedge^{\natural}\tilde q .
$$

*Proof.* The two general products are the sums of their symmetric and antisymmetric parts by the definition of the split; the four halves are the four products of the table.

So the six products are read from the two general products by one and the same split, and the six are not independent: the two general products alone generate the four halves, and any four of the six determine the other two by the reconstruction. The quaternionic triple is the plain triple with the first factor conjugated, and the conjugation changes the sign of the antisymmetric terms; it leaves the symmetric term with the dot product changed to its negative, which is why the symmetric half of the quaternionic product is the scalar $N(\tilde p,\tilde q)e_0$ with the plus sign and not the Jordan product.

## The Behaviour at the Two Equal Arguments

The antisymmetric parts vanish at the two equal arguments, so the square of each general product is the algebraic norm of its symmetric half.

**Proposition (the algebraic norms).** For every $\tilde p=p_0e_0+\vec p$,

$$
\tilde p^2=B(\tilde p)e_0+2p_0\vec p , \qquad \tilde p\bullet\tilde p=\tilde p^2 , \qquad \tilde p\wedge\tilde p=0 ,
$$

$$
\tilde p^{\natural}\tilde p=N(\tilde p)e_0=|\tilde p|^2e_0 , \qquad N(\tilde p,\tilde p)e_0=N(\tilde p)e_0 , \qquad \tilde p\wedge^{\natural}\tilde p=0 ,
$$

with $B(\tilde p)=p_0^2-\lvert\vec p\rvert^2$ and $N(\tilde p)=p_0^2+\lvert\vec p\rvert^2$. The square of the plain product is read off the **plain form** $B$ and the square of the quaternionic product off the **quaternion form** $N$; the two antisymmetric products vanish at the two equal arguments, the cross products of a vector with itself being zero.

*Proof.* An antisymmetric rule has $f(\tilde p,\tilde p)=-f(\tilde p,\tilde p)=0$, so $\tilde p\wedge\tilde p=0$ and $\tilde p\wedge^{\natural}\tilde p=0$, and the algebraic norm of a rule is the algebraic norm of its symmetric half, $\tilde p\bullet\tilde p=\tilde p^2$ and $N(\tilde p,\tilde p)e_0=\tilde p^{\natural}\tilde p$. The two algebraic norms are the two squares of *Comparison Between the Two General Products*, the article preceding this one, namely $\tilde p^2=(p_0^2-\lvert\vec p\rvert^2)e_0+2p_0\vec p$ and $\tilde p^{\natural}\tilde p=\lvert\tilde p\rvert^2e_0$.

So the algebraic norm of the six products carries the two algebraic norms of the chapter: the square of the plain product and the square of the quaternionic product are read off the same two forms $B$ and $N$, the first giving a general quaternion and the second a scalar, and the two antisymmetric products vanish identically at the two equal arguments, giving no square and no norm. The two algebraic norms are *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*, below this article in this category.

## The Two Exchanges

The six products here are the six products of the six algebraic structures of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, below this article in this category; the antisymmetric ones are the two Lie-layer products, and the symmetric ones the two Jordan-layer products.

## Summary

The two general products of $\mathbb{H}$ split under the interchange of their two slots, which is the bare exchange of the two arguments. The six products are the two general products $\tilde p\tilde q$ and $\tilde p^{\natural}\tilde q$ and their four halves: the Jordan product $\tilde p\bullet\tilde q=(p_0q_0-(\vec p,\vec q))+p_0\vec q+q_0\vec p$, the cross product $\tilde p\wedge\tilde q=\vec p\times\vec q$, the quaternion form as a product $N(\tilde p,\tilde q)e_0=(p_0q_0+(\vec p,\vec q))e_0$ and the quaternionic cross product $\tilde p\wedge^{\natural}\tilde q=p_0\vec q-q_0\vec p-\vec p\times\vec q$. The reconstruction is $\tilde p\tilde q=\tilde p\bullet\tilde q+\tilde p\wedge\tilde q$ and $\tilde p^{\natural}\tilde q=N(\tilde p,\tilde q)e_0+\tilde p\wedge^{\natural}\tilde q$.

At the two equal arguments the antisymmetric products vanish and each general product equals its symmetric half: $\tilde p\bullet\tilde p=\tilde p^2=B(\tilde p)e_0+2p_0\vec p$ and $N(\tilde p,\tilde p)e_0=\tilde p^{\natural}\tilde p=N(\tilde p)e_0$, so the two squares are read off the two forms $B$ and $N$; the two antisymmetric products contribute no square.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\tilde q$ | the general plain bilinear product |
| $\tilde p\bullet\tilde q=\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ | the Jordan product, the symmetric half |
| $\tilde p\wedge\tilde q=\tfrac12(\tilde p\tilde q-\tilde q\tilde p)=\vec p\times\vec q$ | the cross product, the antisymmetric half |
| $\tilde p^{\natural}\tilde q$ | the general quaternionic bilinear product |
| $N(\tilde p,\tilde q)e_0=\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)$ | the quaternion form as a product |
| $\tilde p\wedge^{\natural}\tilde q=\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)$ | the quaternionic cross product |
| $\tilde p\tilde q=\tilde p\bullet\tilde q+\tilde p\wedge\tilde q$ | the reconstruction of the plain product |
| $\tilde p^{\natural}\tilde q=N(\tilde p,\tilde q)e_0+\tilde p\wedge^{\natural}\tilde q$ | the reconstruction of the quaternionic product |
| $\tilde p^2=B(\tilde p)e_0+2p_0\vec p$, $\tilde p^{\natural}\tilde p=N(\tilde p)e_0$ | the two algebraic norms |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, Colloquium Publications 39, 1968), for the symmetrisation of a bilinear product and the Jordan product.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the symmetric and antisymmetric parts of a bilinear rule and the Lie product of an associative algebra.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the quaternion product, its symmetrisation and the cross product of its vector part.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the products of the Clifford algebra $\mathrm{Cl}_{0,2}$ and the place of the cross product among them.
