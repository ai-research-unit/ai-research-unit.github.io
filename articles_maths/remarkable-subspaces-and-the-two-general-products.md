# __Remarkable Subspaces and the Two General Products__

## Introduction

The quaternion algebra $\mathbb{H}$ carries two **remarkable subspaces**, the **scalar line** $\mathbb{R}_{\mathbb{H}}$ and the **vector subspace** $\operatorname{Vect}(\mathbb{H})$, the fixed and the anti-fixed space of the quaternion conjugation ${}^{\natural}$. Each of the two general products of *The Two General Products of the Quaternion $\mathbb{R}$ Space* is read on the two subspaces in this article, and the two questions asked of each are the same: **is the subspace closed under the product**, and **what are the products of two vectors**.

The products themselves, their laws and their coordinate rules are *The Two General Products of the Quaternion $\mathbb{R}$ Space*; the two subspaces, their bases and their dimensions are *Introduction to the Remarkable Subspaces of the Quaternions*, in the Linear Spaces group above. None of that is restated here: what the article adds is the reading of the two products on the two subspaces and the table of the restrictions. The symmetric and antisymmetric halves of the products, which are what makes the vector product the cross product and its twin, are *The 6 Products of the Quaternion Real Space*, below this article in this category; the restriction of the two forms to the same subspaces is *Remarkable Subspaces and the Two Forms*, below this article in this category.

**Conventions.** Throughout, $\tilde p=p_0e_0+\vec p$ and $\tilde q=q_0e_0+\vec q$ name elements, with $\vec p,\vec q$ the vector parts; the scalar line is $\mathbb{R}_{\mathbb{H}}=\{p_0e_0:p_0\in\mathbb{R}\}$, identified with $\mathbb{R}$, and the vector subspace is $\operatorname{Vect}(\mathbb{H})=\{\vec p\}$, of basis $e_1,e_2,e_3$. The plain product is $\tilde p\tilde q$, the quaternionic product is $\tilde p^{\natural}\tilde q$, the dot product is $(\vec p,\vec q)=\sum_kp_kq_k$ and the cross product is $\vec p\times\vec q$. The quaternion norm is $N(\tilde p)=\lvert\tilde p\rvert^2=\tilde p^{\natural}\tilde p$.

## The Product of Two Vector Elements

The product of two vector elements is the sharpest single computation of the article, and it is where the cross product enters the products of the algebra.

**Proposition (the vector products).** For purely vector elements $\tilde p=\vec p$ and $\tilde q=\vec q$,

$$
\vec p\vec q=-(\vec p,\vec q)+\vec p\times\vec q , \qquad \vec p^{\natural}\vec q=+(\vec p,\vec q)-\vec p\times\vec q .
$$

The plain product of two vectors is the scalar $-(\vec p,\vec q)$ together with the vector $\vec p\times\vec q$; the quaternionic product of the same two vectors is the same rule with the two signs reversed, being $-\vec p\vec q$ because the conjugation of a vector is its negative.

*Proof.* The plain rule of *The Two General Products of the Quaternion $\mathbb{R}$ Space* has scalar part $p_0q_0-(\vec p,\vec q)$ and vector part $p_0\vec q+q_0\vec p+\vec p\times\vec q$; setting $p_0=q_0=0$ leaves the scalar part $-(\vec p,\vec q)$ and the vector part $\vec p\times\vec q$. The quaternionic product is obtained from the plain one by conjugating the first factor, $\vec p^{\natural}=-\vec p$, so $\vec p^{\natural}\vec q=-\vec p\vec q=(\vec p,\vec q)-\vec p\times\vec q$.

So the product of two vectors is a scalar together with a vector, and the vector part is the cross product for the plain rule and its negative for the quaternionic one. The two products of two vectors are **opposite**, $\vec p^{\natural}\vec q=-\vec p\vec q$, and the two have the same scalar part up to sign.

## The Closure of the Two Subspaces

A subspace is **closed** under a product when the product of two of its elements lies in it again, and the two remarkable subspaces answer differently.

**Proposition (the closure table).** The scalar line is closed under both products; the vector subspace is closed under neither, and the product of two of its elements lies in the whole algebra, its scalar part being $\mp(\vec p,\vec q)$ and its vector part $\pm\vec p\times\vec q$.

*Proof.* On the scalar line, write $\tilde p=p_0e_0$ and $\tilde q=q_0e_0$ with $\vec p=\vec q=0$; then both rules give $p_0q_0e_0$, which is in the line, so the line is closed under both. On the vector subspace the preceding proposition gives the products $\vec p\vec q=-(\vec p,\vec q)+\vec p\times\vec q$ and $\vec p^{\natural}\vec q=(\vec p,\vec q)-\vec p\times\vec q$; each has a scalar part and a vector part in general, so the product of two vectors is not a vector and the subspace is closed under neither.

| subspace | basis | closed under $\tilde p\tilde q$? | closed under $\tilde p^{\natural}\tilde q$? |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{H}}$ | $e_0$ | yes | yes |
| $\operatorname{Vect}(\mathbb{H})$ | $e_1,e_2,e_3$ | no | no |

The scalar line is the centre of the algebra and the fixed space of the conjugation, and a product of two of its elements stays in it because the centre is a subalgebra for both rules: a real scalar commutes with everything and is fixed by ${}^{\natural}$, so $\tilde p^{\natural}\tilde q=\tilde p\tilde q=p_0\tilde q$ for real $\tilde p$. The vector subspace is the anti-fixed space, and its failure of closure is the statement that the anti-fixed space of an involution is not a subalgebra unless the involution is the identity on it.

## The Product of Two Orthogonal Vectors

The scalar part of the product of two vectors is $\mp(\vec p,\vec q)$, so the product of two vectors is again a vector exactly when the two are **perpendicular**, and then it is the cross product.

**Corollary (the perpendicular case).** For perpendicular vector elements $\vec p\perp\vec q$, that is $(\vec p,\vec q)=0$,

$$
\vec p\vec q=\vec p\times\vec q\in\operatorname{Vect}(\mathbb{H}) , \qquad \vec p^{\natural}\vec q=-\vec p\times\vec q\in\operatorname{Vect}(\mathbb{H}) .
$$

The subspace of the algebra spanned by two perpendicular vectors is closed under neither product as a plane, the product of its two generators being orthogonal to both.

*Proof.* Set $(\vec p,\vec q)=0$ in the vector-product proposition; the scalar parts $-(\vec p,\vec q)$ and $+(\vec p,\vec q)$ vanish and only the cross-product terms remain. The product $\vec p\times\vec q$ is perpendicular to $\vec p$ and to $\vec q$ by the defining property of the cross product, so the plane spanned by $\vec p$ and $\vec q$ is not closed.

So the vector subspace is not closed, but its products fill the whole algebra: two vectors give a scalar and a vector, the scalar being the dot product and the vector the cross product, and the same two ingredients with the signs reversed for the quaternionic rule. The two products of the vector subspace generate the whole algebra from the vector subspace alone: the scalar direction comes from the dot product, which is the whole of the square, $\vec p\vec p=-\lvert\vec p\rvert^2e_0$, and the vector direction comes from the cross product, which is the whole of the product when the two vectors are perpendicular; on such a pair the plain product is a vector and not a scalar, and no power of the pair reaches the identity.

## The Restriction Table

Collecting the sections gives the table of the two products restricted to the two subspaces.

| restriction | value of $\tilde p\tilde q$ | value of $\tilde p^{\natural}\tilde q$ |
|---|---|---|
| $\mathbb{R}_{\mathbb{H}}\times\mathbb{R}_{\mathbb{H}}\to\mathbb{R}_{\mathbb{H}}$ | $p_0q_0e_0$ | $p_0q_0e_0$ |
| $\mathbb{R}_{\mathbb{H}}\times\operatorname{Vect}(\mathbb{H})\to\operatorname{Vect}(\mathbb{H})$ | $p_0\vec q$ | $p_0\vec q$ |
| $\operatorname{Vect}(\mathbb{H})\times\mathbb{R}_{\mathbb{H}}\to\operatorname{Vect}(\mathbb{H})$ | $q_0\vec p$ | $-q_0\vec p$ |
| $\operatorname{Vect}(\mathbb{H})\times\operatorname{Vect}(\mathbb{H})\to\mathbb{H}$ | $-(\vec p,\vec q)+\vec p\times\vec q$ | $(\vec p,\vec q)-\vec p\times\vec q$ |

The first three rows are the closure of the scalar line and its two-sided action on the vector subspace: a real scalar multiplies a vector by its scalar on the left for both products, while on the right the quaternionic product multiplies by the scalar through the conjugation of the first factor and so changes the sign. The last row is the product of two vectors, the only entry of the table whose value leaves its two factors' subspaces. The table is the whole of the behaviour of the two products on the two subspaces: the square of a scalar is a scalar, the square of a vector is the scalar $-\lvert\vec p\rvert^2$ for the plain product and $+\lvert\vec p\rvert^2$ for the quaternionic one, and the vector part of the product of two vectors is the cross product, carried with its own sign by the plain product and with the sign reversed by the quaternionic one.

## Summary

The two general products of the quaternion space are read on the scalar line $\mathbb{R}_{\mathbb{H}}$ and the vector subspace $\operatorname{Vect}(\mathbb{H})$. The scalar line is closed under both products and is the centre of the algebra, a product of two reals being the real product $p_0q_0e_0$. The vector subspace is closed under neither, the product of two vectors being $\vec p\vec q=-(\vec p,\vec q)+\vec p\times\vec q$ for the plain product and $\vec p^{\natural}\vec q=(\vec p,\vec q)-\vec p\times\vec q$ for the quaternionic one: the scalar part is the dot product with the sign of the conjugation of the first factor, and the vector part is the cross product or its negative. Two vectors multiply to a vector again exactly when they are perpendicular, and then to the cross product, which is perpendicular to both, so no plane of vectors is closed.

The restriction table has four rows, giving the two closures of the scalar line, its two-sided action on the vector subspace — two-sided for the plain product and one-sided up to sign for the quaternionic one — and the single entry that leaves the two subspaces, the product of two vectors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{R}_{\mathbb{H}}=\{p_0e_0\}$ | the scalar line, the centre, the fixed space of ${}^{\natural}$ |
| $\operatorname{Vect}(\mathbb{H})=\{\vec p\}$ | the vector subspace, the anti-fixed space of ${}^{\natural}$ |
| $\vec p\vec q=-(\vec p,\vec q)+\vec p\times\vec q$ | the plain product of two vectors |
| $\vec p^{\natural}\vec q=(\vec p,\vec q)-\vec p\times\vec q$ | the quaternionic product of two vectors |
| $\vec p\perp\vec q\Rightarrow\vec p\vec q=\vec p\times\vec q$ | the perpendicular case |
| $\vec p\vec p=-\lvert\vec p\rvert^2e_0$ | the square of a vector |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the vector product, the cross product and the scalar and vector subspaces of the quaternion algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the fixed and anti-fixed spaces of the quaternion conjugation and the products of the Clifford algebra.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the centre of an algebra and the subalgebras carried by the fixed spaces of an involution.
- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for the involution, its fixed and anti-fixed spaces and the closure of a subspace under a product.
