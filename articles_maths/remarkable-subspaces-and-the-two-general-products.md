# __Remarkable Subspaces and the Two General Products__

## Introduction

The quaternion algebra $\mathbb{H}$ carries two **remarkable subspaces**, the **scalar line** $\mathbb{R}_{\mathbb{H}}$ and the **vector subspace** $\operatorname{Vect}(\mathbb{H})$, the fixed and the anti-fixed space of the quaternion conjugation ${}^{\natural}$. Each of the two general products of *The Two General Products of the Quaternioid $\mathbb{R}$ Space* is read on the two subspaces in this article, and the two questions asked of each are the same: **is the subspace closed under the product**, and **what are the products of two vectors**.

The products themselves, their laws and their coordinate rules are *The Two General Products of the Quaternioid $\mathbb{R}$ Space*; the two subspaces, their bases and their dimensions are *Introduction to the Remarkable Subspaces of the Quaternions*, in the Linear Spaces group above. None of that is restated here: what the article adds is the reading of the two products on the two subspaces and the table of the restrictions. The symmetric and antisymmetric halves of the products, which are what makes the vector product the cross product and its twin, are *The 6 Products of the Quaternioid Real Space*, below this article in this category; the restriction of the two forms to the same subspaces is *Remarkable Subspaces and the Two Forms*, below this article in this category.

**Conventions.** Throughout, $\tilde q_1=q_{1t}e_t+\vec q_1$ and $\tilde q_2=q_{2t}e_t+\vec q_2$ name elements, with $\vec q_1,\vec q_2$ the vector parts; the scalar line is $\mathbb{R}_{\mathbb{H}}=\{q_te_t:q_t\in\mathbb{R}\}$, identified with $\mathbb{R}$, and the vector subspace is $\operatorname{Vect}(\mathbb{H})=\{\vec q\}$, of basis $\vec e_x,\vec e_y,\vec e_z$. The plain product is $\tilde q_1\tilde q_2$, the quaternionic product is $\tilde q_1^{\natural}\tilde q_2$, the dot product is $(\vec q_1,\vec q_2)=\sum_kq_{1k}q_{2k}$ and the cross product is $\vec q_1\times\vec q_2$. The quaternion norm is $\langle\tilde q\rangle_{\natural}=|\tilde q|^2=\tilde q^{\natural}\tilde q$.

## The Product of Two Vector Elements

The product of two vector elements is the sharpest single computation of the article, and it is where the cross product enters the products of the algebra.

**Proposition (the vector products).** For purely vector elements $\tilde q_1=\vec q_1$ and $\tilde q_2=\vec q_2$,

$$
\vec q_1\vec q_2=-(\vec q_1,\vec q_2)+\vec q_1\times\vec q_2 , \qquad \vec q_1^{\natural}\vec q_2=+(\vec q_1,\vec q_2)-\vec q_1\times\vec q_2 .
$$

The plain product of two vectors is the scalar $-(\vec q_1,\vec q_2)$ together with the vector $\vec q_1\times\vec q_2$; the quaternionic product of the same two vectors is the same rule with the two signs reversed, being $-\vec q_1\vec q_2$ because the conjugation of a vector is its negative.

*Proof.* The plain rule of *The Two General Products of the Quaternioid $\mathbb{R}$ Space* has scalar part $q_{1t}q_{2t}-(\vec q_1,\vec q_2)$ and vector part $q_{1t}\vec q_2+q_{2t}\vec q_1+\vec q_1\times\vec q_2$; setting $q_{1t}=q_{2t}=0$ leaves the scalar part $-(\vec q_1,\vec q_2)$ and the vector part $\vec q_1\times\vec q_2$. The quaternionic product is obtained from the plain one by conjugating the first factor, $\vec q_1^{\natural}=-\vec q_1$, so $\vec q_1^{\natural}\vec q_2=-\vec q_1\vec q_2=(\vec q_1,\vec q_2)-\vec q_1\times\vec q_2$.

So the product of two vectors is a scalar together with a vector, and the vector part is the cross product for the plain rule and its negative for the quaternionic one. The two products of two vectors are **opposite**, $\vec q_1^{\natural}\vec q_2=-\vec q_1\vec q_2$, and the two have the same scalar part up to sign.

## The Closure of the Two Subspaces

A subspace is **closed** under a product when the product of two of its elements lies in it again, and the two remarkable subspaces answer differently.

**Proposition (the closure table).** The scalar line is closed under both products; the vector subspace is closed under neither, and the product of two of its elements lies in the whole algebra, its scalar part being $\mp(\vec q_1,\vec q_2)$ and its vector part $\pm\vec q_1\times\vec q_2$.

*Proof.* On the scalar line, write $\tilde q_1=q_{1t}e_t$ and $\tilde q_2=q_{2t}e_t$ with $\vec q_1=\vec q_2=0$; then both rules give $q_{1t}q_{2t}e_t$, which is in the line, so the line is closed under both. On the vector subspace the preceding proposition gives the products $\vec q_1\vec q_2=-(\vec q_1,\vec q_2)+\vec q_1\times\vec q_2$ and $\vec q_1^{\natural}\vec q_2=(\vec q_1,\vec q_2)-\vec q_1\times\vec q_2$; each has a scalar part and a vector part in general, so the product of two vectors is not a vector and the subspace is closed under neither.

| subspace | basis | closed under $\tilde q_1\tilde q_2$? | closed under $\tilde q_1^{\natural}\tilde q_2$? |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{H}}$ | $e_t$ | yes | yes |
| $\operatorname{Vect}(\mathbb{H})$ | $\vec e_x,\vec e_y,\vec e_z$ | no | no |

The scalar line is the centre of the algebra and the fixed space of the conjugation, and a product of two of its elements stays in it because the centre is a subalgebra for both rules: a real scalar commutes with everything and is fixed by ${}^{\natural}$, so $\tilde q_1^{\natural}\tilde q_2=\tilde q_1\tilde q_2=q_{1t}\tilde q_2$ for real $\tilde q_1$. The vector subspace is the anti-fixed space, and its failure of closure is the statement that the anti-fixed space of an involution is not a subalgebra unless the involution is the identity on it.

## The Product of Two Orthogonal Vectors

The scalar part of the product of two vectors is $\mp(\vec q_1,\vec q_2)$, so the product of two vectors is again a vector exactly when the two are **perpendicular**, and then it is the cross product.

**Corollary (the perpendicular case).** For perpendicular vector elements $\vec q_1\perp\vec q_2$, that is $(\vec q_1,\vec q_2)=0$,

$$
\vec q_1\vec q_2=\vec q_1\times\vec q_2\in\operatorname{Vect}(\mathbb{H}) , \qquad \vec q_1^{\natural}\vec q_2=-\vec q_1\times\vec q_2\in\operatorname{Vect}(\mathbb{H}) .
$$

The subspace of the algebra spanned by two perpendicular vectors is closed under neither product as a plane, the product of its two generators being orthogonal to both.

*Proof.* Set $(\vec q_1,\vec q_2)=0$ in the vector-product proposition; the scalar parts $-(\vec q_1,\vec q_2)$ and $+(\vec q_1,\vec q_2)$ vanish and only the cross-product terms remain. The product $\vec q_1\times\vec q_2$ is perpendicular to $\vec q_1$ and to $\vec q_2$ by the defining property of the cross product, so the plane spanned by $\vec q_1$ and $\vec q_2$ is not closed.

So the vector subspace is not closed, but its products fill the whole algebra: two vectors give a scalar and a vector, the scalar being the dot product and the vector the cross product, and the same two ingredients with the signs reversed for the quaternionic rule. The two products of the vector subspace generate the whole algebra from the vector subspace alone: the scalar direction comes from the dot product, which is the whole of the square, $\vec q\vec q=-\lvert\vec q\rvert^2e_t$, and the vector direction comes from the cross product, which is the whole of the product when the two vectors are perpendicular; on such a pair the plain product is a vector and not a scalar, and no power of the pair reaches the identity.

## The Restriction Table

Collecting the sections gives the table of the two products restricted to the two subspaces.

| restriction | value of $\tilde q_1\tilde q_2$ | value of $\tilde q_1^{\natural}\tilde q_2$ |
|---|---|---|
| $\mathbb{R}_{\mathbb{H}}\times\mathbb{R}_{\mathbb{H}}\to\mathbb{R}_{\mathbb{H}}$ | $q_{1t}q_{2t}e_t$ | $q_{1t}q_{2t}e_t$ |
| $\mathbb{R}_{\mathbb{H}}\times\operatorname{Vect}(\mathbb{H})\to\operatorname{Vect}(\mathbb{H})$ | $q_{1t}\vec q_2$ | $q_{1t}\vec q_2$ |
| $\operatorname{Vect}(\mathbb{H})\times\mathbb{R}_{\mathbb{H}}\to\operatorname{Vect}(\mathbb{H})$ | $q_{2t}\vec q_1$ | $-q_{2t}\vec q_1$ |
| $\operatorname{Vect}(\mathbb{H})\times\operatorname{Vect}(\mathbb{H})\to\mathbb{H}$ | $-(\vec q_1,\vec q_2)+\vec q_1\times\vec q_2$ | $(\vec q_1,\vec q_2)-\vec q_1\times\vec q_2$ |

The first three rows are the closure of the scalar line and its two-sided action on the vector subspace: a real scalar multiplies a vector by its scalar on the left for both products, while on the right the quaternionic product multiplies by the scalar through the conjugation of the first factor and so changes the sign. The last row is the product of two vectors, the only entry of the table whose value leaves its two factors' subspaces. The table is the whole of the behaviour of the two products on the two subspaces: the square of a scalar is a scalar, the square of a vector is the scalar $-\lvert\vec q\rvert^2$ for the plain product and $+\lvert\vec q\rvert^2$ for the quaternionic one, and the vector part of the product of two vectors is the cross product, carried with its own sign by the plain product and with the sign reversed by the quaternionic one.

## Summary

The two general products of the quaternion space are read on the scalar line $\mathbb{R}_{\mathbb{H}}$ and the vector subspace $\operatorname{Vect}(\mathbb{H})$. The scalar line is closed under both products and is the centre of the algebra, a product of two reals being the real product $q_{1t}q_{2t}e_t$. The vector subspace is closed under neither, the product of two vectors being $\vec q_1\vec q_2=-(\vec q_1,\vec q_2)+\vec q_1\times\vec q_2$ for the plain product and $\vec q_1^{\natural}\vec q_2=(\vec q_1,\vec q_2)-\vec q_1\times\vec q_2$ for the quaternionic one: the scalar part is the dot product with the sign of the conjugation of the first factor, and the vector part is the cross product or its negative. Two vectors multiply to a vector again exactly when they are perpendicular, and then to the cross product, which is perpendicular to both, so no plane of vectors is closed.

The restriction table has four rows, giving the two closures of the scalar line, its two-sided action on the vector subspace — two-sided for the plain product and one-sided up to sign for the quaternionic one — and the single entry that leaves the two subspaces, the product of two vectors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{R}_{\mathbb{H}}=\{q_te_t\}$ | the scalar line, the centre, the fixed space of ${}^{\natural}$ |
| $\operatorname{Vect}(\mathbb{H})=\{\vec q\}$ | the vector subspace, the anti-fixed space of ${}^{\natural}$ |
| $\vec q_1\vec q_2=-(\vec q_1,\vec q_2)+\vec q_1\times\vec q_2$ | the plain product of two vectors |
| $\vec q_1^{\natural}\vec q_2=(\vec q_1,\vec q_2)-\vec q_1\times\vec q_2$ | the quaternionic product of two vectors |
| $\vec q_1\perp\vec q_2\Rightarrow\vec q_1\vec q_2=\vec q_1\times\vec q_2$ | the perpendicular case |
| $\vec q\vec q=-\lvert\vec q\rvert^2e_t$ | the square of a vector |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the vector product, the cross product and the scalar and vector subspaces of the quaternion algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the fixed and anti-fixed spaces of the quaternion conjugation and the products of the Clifford algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the centre of an algebra and the subalgebras carried by the fixed spaces of an involution.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for the involution, its fixed and anti-fixed spaces and the closure of a subspace under a product.
