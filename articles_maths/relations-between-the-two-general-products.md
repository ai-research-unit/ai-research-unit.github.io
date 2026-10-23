# __Relations Between the Two General Products__

## Introduction

The two general products of the quaternion space are defined independently in *The Two General Products of the Quaternioid $\mathbb{R}$ Space*, each on the coordinates of the two elements of a pair:

$$
\tilde q_1\tilde q_2 , \qquad \tilde q_1^{\natural}\tilde q_2 .
$$

This article collects the identities that link the two. The two rules are not unrelated: they are read on one and the same pair, the second differing from the first only by the conjugation of the first factor, and every link below is a consequence of that single distinction. The **exchange relation** moves the conjugation from one factor to the other and reads the quaternionic product of one order as the conjugate of the plain product of the other; the plain product is recovered from the quaternionic one and conversely by the separation of the scalar part of the first factor; the **agreement** of the two products is the annihilation of the second factor by the vector part of the first, so that they agree on the real axis and disagree everywhere else; and the scalar parts of the two are symmetric and differ by twice the dot product of the vector parts.

The article assumes the two products and their coordinate rules from *The Two General Products of the Quaternioid $\mathbb{R}$ Space*, the article preceding this one, and the conjugation from *The Group of Involutions of the Quaternioid*. It uses the separation identities of that article for the reading of one product through the other. The property table is *Comparison Between the Two General Products*, below this article in this category; the symmetric and antisymmetric halves are *The 6 Products of the Quaternioid Real Space*, below this article in this category.

## The Exchange Relation

The two products are read on the same pair with the conjugation in the first slot for the second product and in no slot for the first, and the conjugation is an anti-automorphism: it reverses the order of a product and conjugates the two factors.

**Proposition (the conjugate of a product).** For all $\tilde q_1,\tilde q_2$,

$$
\boxed{\;(\tilde q_1\tilde q_2)^{\natural}=\tilde q_2^{\natural}\tilde q_1^{\natural} , \qquad (\tilde q_1^{\natural}\tilde q_2)^{\natural}=\tilde q_2^{\natural}\tilde q_1\;}.
$$

The first identity conjugates both the factors of the plain product and transposes them; the second conjugates the first factor alone, and transposes the two factors.

*Proof.* The quaternion conjugation is an anti-automorphism, $(\tilde q_1\tilde q_2)^{\natural}=\tilde q_2^{\natural}\tilde q_1^{\natural}$, and an involution, $(\tilde q^{\natural})^{\natural}=\tilde q$. Applying it to $\tilde q_1\tilde q_2$ gives the first identity, and applying it to $\tilde q_1^{\natural}\tilde q_2$ gives $(\tilde q_1^{\natural}\tilde q_2)^{\natural}=\tilde q_2^{\natural}(\tilde q_1^{\natural})^{\natural}=\tilde q_2^{\natural}\tilde q_1$.

**Theorem (the exchange relation).** For all $\tilde q_1,\tilde q_2$,

$$
\boxed{\;\tilde q_2^{\natural}\tilde q_1=(\tilde q_1^{\natural}\tilde q_2)^{\natural} , \qquad \tilde q_1^{\natural}\tilde q_2=(\tilde q_2^{\natural}\tilde q_1)^{\natural}\;}.
$$

The two are the same identity read from its two sides, and they read the quaternionic product of the pair $(\tilde q_2,\tilde q_1)$ as the conjugate of the plain product of the pair $(\tilde q_1,\tilde q_2)$, with the two orders exchanged.

*Proof.* The second identity of the proposition applied to the pair $(\tilde q_2,\tilde q_1)$ gives $(\tilde q_2^{\natural}\tilde q_1)^{\natural}=\tilde q_1^{\natural}(\tilde q_2^{\natural})^{\natural}=\tilde q_1^{\natural}\tilde q_2$; conjugating both sides gives $\tilde q_2^{\natural}\tilde q_1=(\tilde q_1^{\natural}\tilde q_2)^{\natural}$.

It also shows that the two products carry the same information: one of them at the pair $(\tilde q_1,\tilde q_2)$ determines the other at the reversed pair, and conversely.

## Reading One Product Through the Other

The conjugation of the first factor changes only its vector part, so each product is recovered from the other by the separation of the scalar and the vector part of the first factor.

**Proposition (the two readings).** For all $\tilde q_1,\tilde q_2$,

$$
\tilde q_1\tilde q_2+\tilde q_1^{\natural}\tilde q_2=2q_{1t}\,\tilde q_2 , \qquad \tilde q_1\tilde q_2-\tilde q_1^{\natural}\tilde q_2=2\,\vec q_1\,\tilde q_2 ,
$$

and therefore

$$
\tilde q_1\tilde q_2=2q_{1t}\,\tilde q_2-\tilde q_1^{\natural}\tilde q_2 , \qquad \tilde q_1^{\natural}\tilde q_2=2q_{1t}\,\tilde q_2-\tilde q_1\tilde q_2 .
$$

*Proof.* The separation identities are those of *The Two General Products of the Quaternioid $\mathbb{R}$ Space*, the article preceding this one; solving the two linear relations for $\tilde q_1\tilde q_2$ and $\tilde q_1^{\natural}\tilde q_2$ gives the two readings.

The reading is the algebraic form of the relation $\tilde q_1^{\natural}=2q_{1t}e_t-\tilde q_1$: the conjugate of the first factor is the reflection of the first factor in the scalar axis, and the two products differ by twice the reflection of $\tilde q_1$ across that axis, applied to $\tilde q_2$. A computation in the quaternionic product is turned into a computation in the plain one by replacing $\tilde q_1$ with $\tilde q_1^{\natural}$ and keeping the second factor, and conversely.

**Corollary (the scalar parts).** The scalar parts of the two products on the same pair are

$$
\mathrm{Sc}\bigl(\tilde q_1\tilde q_2\bigr)=q_{1t}q_{2t}-(\vec q_1,\vec q_2) , \qquad \mathrm{Sc}\bigl(\tilde q_1^{\natural}\tilde q_2\bigr)=q_{1t}q_{2t}+(\vec q_1,\vec q_2) ,
$$

whence

$$
\boxed{\mathrm{Sc}\bigl(\tilde q_1\tilde q_2\bigr)+\mathrm{Sc}\bigl(\tilde q_1^{\natural}\tilde q_2\bigr)=2q_{1t}q_{2t} , \qquad \mathrm{Sc}\bigl(\tilde q_1\tilde q_2\bigr)-\mathrm{Sc}\bigl(\tilde q_1^{\natural}\tilde q_2\bigr)=-2(\vec q_1,\vec q_2)}.
$$

Both scalar parts are symmetric in the two slots, and the difference of the two is twice the dot product of the vector parts; the two are the two bilinear forms $B$ and $N$ of *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*, below this article in this category, read on the pair.

## The Annihilation Identity

The difference of the two products is the term $2\vec q_1\tilde q_2$, and its vanishing is the agreement of the two products.

**Theorem (the annihilation identity).** For all $\tilde q_1,\tilde q_2$,

$$
\boxed{\;\tilde q_1^{\natural}\tilde q_2=\tilde q_1\tilde q_2 \quad\Longleftrightarrow\quad \vec q_1\tilde q_2=0\;},
$$

and for a fixed $\tilde q_2\neq0$ this holds exactly when $\tilde q_1$ is real, $\tilde q_1=q_{1t}e_t$. If $\tilde q_1$ is real then the two products agree on every second factor, $\tilde q_1\tilde q_2=\tilde q_1^{\natural}\tilde q_2=q_{1t}\tilde q_2$.

*Proof.* The difference is $2\vec q_1\tilde q_2$ by the reading proposition, so the two agree exactly when $\vec q_1\tilde q_2=0$. For $\tilde q_2\neq0$ the element $\tilde q_2$ is invertible in $\mathbb{H}$, and multiplying $\vec q_1\tilde q_2=0$ on the right by $\tilde q_2^{-1}$ gives $\vec q_1=0$, that is $\tilde q_1=q_{1t}e_t$; conversely $\vec q_1=0$ makes $\tilde q_1^{\natural}=\tilde q_1$ and the two products equal. For a real $\tilde q_1$, $\tilde q_1^{\natural}=\tilde q_1$ and the two products are the same rule.

So the two products **agree on the real axis** — on every pair whose first factor is scalar — and **disagree everywhere else**: on a pair with $\tilde q_2\neq0$ and $\tilde q_1$ not real the difference $2\vec q_1\tilde q_2$ is nonzero. The disagreement is witnessed on the pair $(\vec e_x,\vec e_y)$, where $\tilde q_1\tilde q_2=\vec e_z$ and $\tilde q_1^{\natural}\tilde q_2=-\vec e_z$, and on the pair $(\vec e_x,e_t)$, where $\tilde q_1\tilde q_2=\vec e_x$ and $\tilde q_1^{\natural}\tilde q_2=-\vec e_x$; the second pair shows that the two products already differ on the units when the second factor is the unit itself.

**Corollary (the products on the units).** On the pairs of units the two products agree exactly when the first factor is $e_t$: for every unit $\tilde q$ one has $e_t\tilde q=e_t^{\natural}\tilde q=\tilde q$, while for a first factor $\vec e_\mu$ with $\mu\neq t$ the two values are $\vec e_\mu\tilde q$ and $\vec e_\mu^{\natural}\tilde q=-\vec e_\mu\tilde q$, which are opposite and therefore distinct, the second factor being a unit and $\vec e_\mu$ nonzero.

*Proof.* The annihilation identity requires $\vec q_1\tilde q_2=0$; on the pairs of units both factors are nonzero and invertible, so it is equivalent to $\vec q_1=0$, that is to $\tilde q_1$ real, which among the units leaves only $\tilde q_1=e_t$. The two values on a pair with first factor $\vec e_\mu$, $\mu\neq t$, are read from the two multiplication tables of *The Two General Products of the Quaternioid $\mathbb{R}$ Space*, that of the plain product and that of the quaternionic product.

## Summary

The two products of the quaternion space are linked by the exchange relation $\tilde q_2^{\natural}\tilde q_1=(\tilde q_1^{\natural}\tilde q_2)^{\natural}$, the conjugate of a product being $(\tilde q_1\tilde q_2)^{\natural}=\tilde q_2^{\natural}\tilde q_1^{\natural}$ for the plain product and $(\tilde q_1^{\natural}\tilde q_2)^{\natural}=\tilde q_2^{\natural}\tilde q_1$ for the quaternionic one. Each product is read from the other by the separation of the scalar part of the first factor, $\tilde q_1\tilde q_2=2q_{1t}\tilde q_2-\tilde q_1^{\natural}\tilde q_2$ and $\tilde q_1^{\natural}\tilde q_2=2q_{1t}\tilde q_2-\tilde q_1\tilde q_2$, and their scalar parts are $\mathrm{Sc}(\tilde q_1\tilde q_2)=q_{1t}q_{2t}-(\vec q_1,\vec q_2)$ and $\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)=q_{1t}q_{2t}+(\vec q_1,\vec q_2)$, symmetric in the two slots and differing by twice the dot product of the vector parts.

The annihilation identity $\tilde q_1^{\natural}\tilde q_2=\tilde q_1\tilde q_2\iff\vec q_1\tilde q_2=0$ states the agreement of the two products: they agree on the real axis and disagree everywhere else, and for a nonzero second factor their agreement forces the first factor to be real. On the units they agree exactly on the pairs whose first factor is $e_t$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\tilde q_1\tilde q_2)^{\natural}=\tilde q_2^{\natural}\tilde q_1^{\natural}$ | the conjugate of the plain product |
| $(\tilde q_1^{\natural}\tilde q_2)^{\natural}=\tilde q_2^{\natural}\tilde q_1$ | the conjugate of the quaternionic product |
| $\tilde q_2^{\natural}\tilde q_1=(\tilde q_1^{\natural}\tilde q_2)^{\natural}$ | the exchange relation |
| $\tilde q_1\tilde q_2=2q_{1t}\tilde q_2-\tilde q_1^{\natural}\tilde q_2$ | the plain product read from the quaternionic one |
| $\tilde q_1^{\natural}\tilde q_2=2q_{1t}\tilde q_2-\tilde q_1\tilde q_2$ | the quaternionic product read from the plain one |
| $\mathrm{Sc}(\tilde q_1\tilde q_2)=q_{1t}q_{2t}-(\vec q_1,\vec q_2)$ | the scalar part of the plain product |
| $\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)=q_{1t}q_{2t}+(\vec q_1,\vec q_2)$ | the scalar part of the quaternionic product |
| $\tilde q_1^{\natural}\tilde q_2=\tilde q_1\tilde q_2\iff\vec q_1\tilde q_2=0$ | the annihilation identity, the agreement condition |
| $\tilde q_1$ real $\iff$ the two products agree for every $\tilde q_2$ | agreement on the real axis |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the conjugation of the quaternion product and the vector reading of the two rules.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the conjugation as an anti-automorphism and the place of the two products among the Clifford products.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the trace of a product, its symmetry and the separation of the scalar part.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for anti-automorphisms, involutions and the elementary identities of a non-commutative ring.
