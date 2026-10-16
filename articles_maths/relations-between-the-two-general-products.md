# __Relations Between the Two General Products__

## Introduction

The two general products of the quaternion space are defined independently in *The Two General Products of the Quaternioid $\mathbb{R}$ Space*, each on the coordinates of the two elements of a pair:

$$
\tilde p\tilde q , \qquad \tilde p^{\natural}\tilde q .
$$

This article collects the identities that link the two. The two rules are not unrelated: they are read on one and the same pair, the second differing from the first only by the conjugation of the first factor, and every link below is a consequence of that single distinction. The **exchange relation** moves the conjugation from one factor to the other and reads the quaternionic product of one order as the conjugate of the plain product of the other; the plain product is recovered from the quaternionic one and conversely by the separation of the scalar part of the first factor; the **agreement** of the two products is the annihilation of the second factor by the vector part of the first, so that they agree on the real axis and disagree everywhere else; and the scalar parts of the two are symmetric and differ by twice the dot product of the vector parts.

The article assumes the two products and their coordinate rules from *The Two General Products of the Quaternioid $\mathbb{R}$ Space*, the article preceding this one, and the conjugation from *The Group of Involutions of the Quaternioid*. It uses the separation identities of that article for the reading of one product through the other. The property table is *Comparison Between the Two General Products*, below this article in this category; the symmetric and antisymmetric halves are *The 6 Products of the Quaternioid Real Space*, below this article in this category.

**Conventions.** Throughout, $\tilde p=p_0e_0+\vec p$ and $\tilde q=q_0e_0+\vec q$ name elements, $(\vec p,\vec q)=\sum_kp_kq_k$ is the dot product of the vector parts and $\tilde q^{\natural}=q_0e_0-\vec q$ is the quaternion conjugation. The scalar part is $\mathrm{Sc}$. The two products are read as in *The Two General Products of the Quaternioid $\mathbb{R}$ Space*.

## The Exchange Relation

The two products are read on the same pair with the conjugation in the first slot for the second product and in no slot for the first, and the conjugation is an anti-automorphism: it reverses the order of a product and conjugates the two factors.

**Proposition (the conjugate of a product).** For all $\tilde p,\tilde q$,

$$
(\tilde p\tilde q)^{\natural}=\tilde q^{\natural}\tilde p^{\natural} , \qquad (\tilde p^{\natural}\tilde q)^{\natural}=\tilde q^{\natural}\tilde p .
$$

The first identity conjugates both the factors of the plain product and transposes them; the second conjugates the first factor alone, and transposes the two factors.

*Proof.* The quaternion conjugation is an anti-automorphism, $(\tilde x\tilde y)^{\natural}=\tilde y^{\natural}\tilde x^{\natural}$, and an involution, $(\tilde x^{\natural})^{\natural}=\tilde x$. Applying it to $\tilde p\tilde q$ gives the first identity, and applying it to $\tilde p^{\natural}\tilde q$ gives $(\tilde p^{\natural}\tilde q)^{\natural}=\tilde q^{\natural}(\tilde p^{\natural})^{\natural}=\tilde q^{\natural}\tilde p$.

**Theorem (the exchange relation).** For all $\tilde p,\tilde q$,

$$
\tilde q^{\natural}\tilde p=(\tilde p^{\natural}\tilde q)^{\natural} , \qquad \tilde p^{\natural}\tilde q=(\tilde q^{\natural}\tilde p)^{\natural} .
$$

The two are the same identity read from its two sides, and they read the quaternionic product of the pair $(\tilde q,\tilde p)$ as the conjugate of the plain product of the pair $(\tilde p,\tilde q)$, with the two orders exchanged.

*Proof.* The second identity of the proposition applied to the pair $(\tilde q,\tilde p)$ gives $(\tilde q^{\natural}\tilde p)^{\natural}=\tilde p^{\natural}(\tilde q^{\natural})^{\natural}=\tilde p^{\natural}\tilde q$; conjugating both sides gives $\tilde q^{\natural}\tilde p=(\tilde p^{\natural}\tilde q)^{\natural}$.

It also shows that the two products carry the same information: one of them at the pair $(\tilde p,\tilde q)$ determines the other at the reversed pair, and conversely.

## Reading One Product Through the Other

The conjugation of the first factor changes only its vector part, so each product is recovered from the other by the separation of the scalar and the vector part of the first factor.

**Proposition (the two readings).** For all $\tilde p,\tilde q$,

$$
\tilde p\tilde q+\tilde p^{\natural}\tilde q=2p_0\,\tilde q , \qquad \tilde p\tilde q-\tilde p^{\natural}\tilde q=2\,\vec p\,\tilde q ,
$$

and therefore

$$
\tilde p\tilde q=2p_0\,\tilde q-\tilde p^{\natural}\tilde q , \qquad \tilde p^{\natural}\tilde q=2p_0\,\tilde q-\tilde p\tilde q .
$$

*Proof.* The separation identities are those of *The Two General Products of the Quaternioid $\mathbb{R}$ Space*, the article preceding this one; solving the two linear relations for $\tilde p\tilde q$ and $\tilde p^{\natural}\tilde q$ gives the two readings.

The reading is the algebraic form of the relation $\tilde p^{\natural}=2p_0e_0-\tilde p$: the conjugate of the first factor is the reflection of the first factor in the scalar axis, and the two products differ by twice the reflection of $\tilde p$ across that axis, applied to $\tilde q$. A computation in the quaternionic product is turned into a computation in the plain one by replacing $\tilde p$ with $\tilde p^{\natural}$ and keeping the second factor, and conversely.

**Corollary (the scalar parts).** The scalar parts of the two products on the same pair are

$$
\mathrm{Sc}\bigl(\tilde p\tilde q\bigr)=p_0q_0-(\vec p,\vec q) , \qquad \mathrm{Sc}\bigl(\tilde p^{\natural}\tilde q\bigr)=p_0q_0+(\vec p,\vec q) ,
$$

whence

$$
\mathrm{Sc}\bigl(\tilde p\tilde q\bigr)+\mathrm{Sc}\bigl(\tilde p^{\natural}\tilde q\bigr)=2p_0q_0 , \qquad \mathrm{Sc}\bigl(\tilde p\tilde q\bigr)-\mathrm{Sc}\bigl(\tilde p^{\natural}\tilde q\bigr)=-2(\vec p,\vec q) .
$$

Both scalar parts are symmetric in the two slots, and the difference of the two is twice the dot product of the vector parts; the two are the two bilinear forms $B$ and $N$ of *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*, below this article in this category, read on the pair.

## The Annihilation Identity

The difference of the two products is the term $2\vec p\tilde q$, and its vanishing is the agreement of the two products.

**Theorem (the annihilation identity).** For all $\tilde p,\tilde q$,

$$
\tilde p^{\natural}\tilde q=\tilde p\tilde q \quad\Longleftrightarrow\quad \vec p\tilde q=0 ,
$$

and for a fixed $\tilde q\neq0$ this holds exactly when $\tilde p$ is real, $\tilde p=p_0e_0$. If $\tilde p$ is real then the two products agree on every second factor, $\tilde p\tilde q=\tilde p^{\natural}\tilde q=p_0\tilde q$.

*Proof.* The difference is $2\vec p\tilde q$ by the reading proposition, so the two agree exactly when $\vec p\tilde q=0$. For $\tilde q\neq0$ the element $\tilde q$ is invertible in $\mathbb{H}$, and multiplying $\vec p\tilde q=0$ on the right by $\tilde q^{-1}$ gives $\vec p=0$, that is $\tilde p=p_0e_0$; conversely $\vec p=0$ makes $\tilde p^{\natural}=\tilde p$ and the two products equal. For a real $\tilde p$, $\tilde p^{\natural}=\tilde p$ and the two products are the same rule.

So the two products **agree on the real axis** — on every pair whose first factor is scalar — and **disagree everywhere else**: on a pair with $\tilde q\neq0$ and $\tilde p$ not real the difference $2\vec p\tilde q$ is nonzero. The disagreement is witnessed on the pair $(e_1,e_2)$, where $\tilde p\tilde q=e_3$ and $\tilde p^{\natural}\tilde q=-e_3$, and on the pair $(e_1,e_0)$, where $\tilde p\tilde q=e_1$ and $\tilde p^{\natural}\tilde q=-e_1$; the second pair shows that the two products already differ on the units when the second factor is the unit itself.

**Corollary (the products on the units).** On the pairs of units the two products agree exactly when the first factor is $e_0$: for every unit $\tilde q$ one has $e_0\tilde q=e_0^{\natural}\tilde q=\tilde q$, while for a first factor $e_k$ with $k\neq0$ the two values are $e_k\tilde q$ and $e_k^{\natural}\tilde q=-e_k\tilde q$, which are opposite and therefore distinct, the second factor being a unit and $e_k$ nonzero.

*Proof.* The annihilation identity requires $\vec p\tilde q=0$; on the pairs of units both factors are nonzero and invertible, so it is equivalent to $\vec p=0$, that is to $\tilde p$ real, which among the units leaves only $\tilde p=e_0$. The two values on a pair with first factor $e_k$, $k\neq0$, are read from the two multiplication tables of *The Two General Products of the Quaternioid $\mathbb{R}$ Space*, that of the plain product and that of the quaternionic product.

## Summary

The two products of the quaternion space are linked by the exchange relation $\tilde q^{\natural}\tilde p=(\tilde p^{\natural}\tilde q)^{\natural}$, the conjugate of a product being $(\tilde p\tilde q)^{\natural}=\tilde q^{\natural}\tilde p^{\natural}$ for the plain product and $(\tilde p^{\natural}\tilde q)^{\natural}=\tilde q^{\natural}\tilde p$ for the quaternionic one. Each product is read from the other by the separation of the scalar part of the first factor, $\tilde p\tilde q=2p_0\tilde q-\tilde p^{\natural}\tilde q$ and $\tilde p^{\natural}\tilde q=2p_0\tilde q-\tilde p\tilde q$, and their scalar parts are $\mathrm{Sc}(\tilde p\tilde q)=p_0q_0-(\vec p,\vec q)$ and $\mathrm{Sc}(\tilde p^{\natural}\tilde q)=p_0q_0+(\vec p,\vec q)$, symmetric in the two slots and differing by twice the dot product of the vector parts.

The annihilation identity $\tilde p^{\natural}\tilde q=\tilde p\tilde q\iff\vec p\tilde q=0$ states the agreement of the two products: they agree on the real axis and disagree everywhere else, and for a nonzero second factor their agreement forces the first factor to be real. On the units they agree exactly on the pairs whose first factor is $e_0$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\tilde p\tilde q)^{\natural}=\tilde q^{\natural}\tilde p^{\natural}$ | the conjugate of the plain product |
| $(\tilde p^{\natural}\tilde q)^{\natural}=\tilde q^{\natural}\tilde p$ | the conjugate of the quaternionic product |
| $\tilde q^{\natural}\tilde p=(\tilde p^{\natural}\tilde q)^{\natural}$ | the exchange relation |
| $\tilde p\tilde q=2p_0\tilde q-\tilde p^{\natural}\tilde q$ | the plain product read from the quaternionic one |
| $\tilde p^{\natural}\tilde q=2p_0\tilde q-\tilde p\tilde q$ | the quaternionic product read from the plain one |
| $\mathrm{Sc}(\tilde p\tilde q)=p_0q_0-(\vec p,\vec q)$ | the scalar part of the plain product |
| $\mathrm{Sc}(\tilde p^{\natural}\tilde q)=p_0q_0+(\vec p,\vec q)$ | the scalar part of the quaternionic product |
| $\tilde p^{\natural}\tilde q=\tilde p\tilde q\iff\vec p\tilde q=0$ | the annihilation identity, the agreement condition |
| $\tilde p$ real $\iff$ the two products agree for every $\tilde q$ | agreement on the real axis |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the conjugation of the quaternion product and the vector reading of the two rules.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the conjugation as an anti-automorphism and the place of the two products among the Clifford products.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the trace of a product, its symmetry and the separation of the scalar part.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for anti-automorphisms, involutions and the elementary identities of a non-commutative ring.
