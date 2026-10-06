# __The Square-Zero Elements of the Four Products__

## Introduction

The square of an element of the biquaternion algebra vanishes on a set that depends sharply on the product, and the four sets are the subject of this article. They are the solutions of

$$
\tilde P\tilde P = 0 , \qquad \tilde P^{\natural}\tilde P = 0 , \qquad \tilde P\tilde P^{*} = 0 , \qquad \tilde P^{\natural}\tilde P^{*} = 0 ,
$$

and they range from a single point to the whole zero-divisor cone. The chains that contain them are known: the square-zero elements of the plain product are the pure isotropic vectors (*Biquaternion Square Roots of Minus One, Zero and Plus One*, *Biquaternion Zero Divisors*), those of the natural product are all the zero divisors of the algebra together with $0$ (*The Nilpotents and the Zero Divisors of the Quaternionic Product*), those of the complex sesquilinear product are the origin alone (*The Squares and the Positive Cone of the Biquaternion Sesquialgebra*), and those of the complex quaternionic sesquilinear product are a proper subfamily of the zero-divisor set (*The Square of the Quaternionic Sesquilinear Product and the Two Halves*). This article gathers the four solutions, separates the two families of the common denominator, the zero-divisor cone, according to which of the four square-zero sets meets them, and records the crossing of the plain and the complex quaternionic sesquilinear sets, which meet only at the origin.

The common denominator is the zero-divisor set of *The Annihilating Elements of the Four Products*, the set of elements that admit a nonzero annihilating factor. Every square-zero element is a zero divisor or zero, since a vanishing square exhibits a nonzero annihilating factor, and so each of the four square-zero sets lies in the zero-divisor set together with the origin. The four products place it differently inside the cone, and the article's content is the placement.

**Conventions.** $\tilde P = P_0e_0+\mathbf P$ with $P_0\in\mathbb{C}$ and $\mathbf P$ a vector; the natural conjugation is $\tilde P^{\natural} = P_0-\mathbf P$, the star is $\tilde P^{*} = \overline{\tilde P^{\natural}}$, and the **central square** is $\tilde P^{\natural}\tilde P = \tilde P\tilde P^{\natural} = \bigl(\sum_\mu P_\mu^{2}\bigr)e_0$. The zero-divisor set is the vanishing set of the central square with the origin removed, and the two families of the cone are the pure zero divisors, those with $P_0 = 0$, and the non-pure ones, those with $P_0\neq0$ (*Biquaternion Zero Divisors*).

## The Four Equations

Each of the four squares has a closed form, and setting it to zero gives one equation per product.

| product | square | square-zero equation |
|---|---|---|
| $\tilde P\tilde P$ | $\bigl(P_0^{2}-(\mathbf P,\mathbf P)\bigr)e_0 + 2P_0\mathbf P$ | $P_0^{2}-(\mathbf P,\mathbf P) = 0$ and $P_0\mathbf P = 0$ |
| $\tilde P^{\natural}\tilde P$ | $\tilde P^{\natural}\tilde P$, a central element | $\tilde P^{\natural}\tilde P = 0$ |
| $\tilde P\tilde P^{*}$ | Hermitian with $\mathrm{Sc} = \sum_\mu\lvert P_\mu\rvert^{2}$ | $\sum_\mu\lvert P_\mu\rvert^{2} = 0$ |
| $\tilde P^{\natural}\tilde P^{*}$ | Hermitian with $\mathrm{Sc} = \lvert P_0\rvert^{2}-\sum_k\lvert P_k\rvert^{2}$ | $\overline{\tilde P}\tilde P = 0$ |

The four equations are of four different types: a pair consisting of a complex equation and a vector equation for the plain product, a single complex equation for the natural product, a sum of modulus squares for the complex sesquilinear product, and a matrix equation $\overline{\tilde P}\tilde P = 0$ for the fourth. The shapes already decide the answers, and the sections below read them one by one.

## The Plain Product: The Pure Isotropic Cone

**Theorem (the square-zero elements of the plain product).** In the associative product the square of $\tilde P$ vanishes exactly when $P_0 = 0$ and $(\mathbf P,\mathbf P) = 0$: the pure isotropic cone, of real dimension four. Written as $\tilde P = \mathbf u+i\mathbf v$ with $\mathbf u,\mathbf v$ real vectors, the two conditions are $\sum_k u_k^{2} = \sum_k v_k^{2}$ and $\sum_k u_kv_k = 0$, so that every nonzero element of the set is $r(\hat u+i\hat v)$ over a real pair with $\sum_k\hat u_k^{2} = \sum_k\hat v_k^{2} = 1$ and $\sum_k\hat u_k\hat v_k = 0$, and a positive real $r$.

**Proof.** The square is $\bigl(P_0^{2}-(\mathbf P,\mathbf P)\bigr)e_0+2P_0\mathbf P$, a sum of a central element and a vector element, so it vanishes exactly when both coefficients do: $2P_0\mathbf P = 0$ gives $P_0 = 0$ or $\mathbf P = 0$, and $\mathbf P = 0$ forces $P_0 = 0$ from the first equation, so $P_0 = 0$ and $(\mathbf P,\mathbf P) = 0$. For $\mathbf P = \mathbf u+i\mathbf v$ the vector-part square is $(\mathbf P,\mathbf P) = \sum_k u_k^{2}-\sum_k v_k^{2}+2i\sum_k u_kv_k$, giving the two real conditions. The parametrisation is *Biquaternion Zero Divisors*. $\square$

It is the only one of the four that is a cone of **pure** elements — every square-zero element of the plain product lies in the vector subspace — and it is one of the two of real dimension four, the other being the fourth product's set. The six-dimensional cone of *Biquaternion Zero Divisors* drops by two real dimensions here, and the square-zero set is the four-dimensional pure part, on which the two conditions of equal length and orthogonality are the two real equations. The set is the nilpotent cone of the algebra, of *The Six Subspaces and the Elements*.

## The Natural Product: The Whole Cone

**Theorem (the square-zero elements of the natural product).** In the complex quaternionic bilinear product the square of $\tilde P$ vanishes exactly when $\tilde P^{\natural}\tilde P = 0$: the whole zero-divisor set, of real dimension six, the origin included.

**Proof.** The square is the central element $\tilde P^{\natural}\tilde P$ (*Biquaternions as a Quaternionic Algebra over $\mathbb{C}$*), which vanishes exactly when the zero-divisor criterion holds (*Biquaternion Zero Divisors*). $\square$

The natural product is the only one of the four whose square-zero set is the whole cone. Its square is the central square itself, so the equation is the defining equation of the zero-divisor set, and the square-zero elements of this product are all the elements that admit a nonzero annihilating factor. Both families of the cone belong to the set: the pure nilpotents of the plain product and the non-pure elements, which are the nonzero complex multiples of the nontrivial idempotents of the algebra (*The Idempotents of the Four Products*).

## The Complex Sesquilinear Product: The Origin Alone

**Theorem (the square-zero elements of the complex sesquilinear product).** In the complex sesquilinear product the square of $\tilde P$ vanishes exactly when $\tilde P = 0$.

**Proof.** The square is Hermitian with scalar part $\sum_\mu\lvert P_\mu\rvert^{2}$, a sum of non-negative real numbers, which vanishes exactly when every coordinate does (*The Squares and the Positive Cone of the Biquaternion Sesquialgebra*). $\square$

The set is the smallest possible, and its smallness is the definiteness of the sum of modulus squares. The same vanishing of the modulus squares gives the complex sesquilinear product its empty root sets for the negative central values (*The Square Roots of a Central Value in the Four Products*), and the two facts are one fact: the product's square has scalar part $\sum_\mu\lvert P_\mu\rvert^{2}$, which vanishes only at the origin. In the cone of the zero divisors the complex sesquilinear product's square detects nothing.

## The Complex Quaternionic Sesquilinear Product: A Proper Subfamily

**Theorem (the square-zero elements of the fourth product).** In the complex quaternionic sesquilinear product the square of $\tilde P$ vanishes exactly when $\overline{\tilde P}\tilde P = 0$. The set is a proper subfamily of the zero-divisor set, of positive codimension in it: the element $e_0+ie_1$ is square-zero, so the set is not $\{0\}$; the element $ie_0+e_1+e_2+ie_3$ is a zero divisor whose square is nonzero, so the set is not the whole cone.

**Proof.** The square is $\tilde P^{\natural}\tilde P^{*} = \bigl(\overline{\tilde P}\tilde P\bigr)^{\natural}$ (*The Square of the Quaternionic Sesquilinear Product and the Two Halves*), which vanishes exactly when $\overline{\tilde P}\tilde P$ does, so a square-zero element is a zero divisor. The two displayed elements are computed in the same article: $(e_0+ie_1)\star(e_0+ie_1) = 0$ and $(ie_0+e_1+e_2+ie_3)\star(ie_0+e_1+e_2+ie_3)\neq0$. $\square$

The fourth product is the only one whose square-zero set is neither the cone, nor the pure part of it, nor a point: it is a set of a fourth kind, cut out of the cone by the matrix equation $\overline{\tilde P}\tilde P = 0$ and not by a single scalar one. It is the boundary case of the comparison, and the next section reads it against the other three.

## The Chain and the Incomparable Pair

Inside the cone the plain and the natural sets are nested and the fourth is nested in the natural one, while the plain and the fourth sets cross each other.

**Theorem (the order of the sets).** Write $Z_1,Z_2,Z_3,Z_4$ for the square-zero sets of the plain, natural, complex sesquilinear and complex quaternionic sesquilinear products. Then

$$
Z_3 = \{0\} \subsetneq Z_1 \subsetneq Z_2 , \qquad Z_3 \subsetneq Z_4 \subsetneq Z_2 , \qquad Z_1\cap Z_4 = \{0\} ,
$$

so that $Z_1$ and $Z_4$ are incomparable, and the four sets are ordered only by the two chains through $Z_2$.

**Proof.** The inclusions $Z_1\subseteq Z_2$ and $Z_4\subseteq Z_2$ are the two theorems above, and both are strict: $e_0+ie_1$ lies in $Z_2$ and not in $Z_1$, so $Z_1\subsetneq Z_2$, while $ie_0+e_1+e_2+ie_3$ lies in $Z_2$ and not in $Z_4$, so $Z_4\subsetneq Z_2$. The sets $Z_1$ and $Z_4$ are non-empty beyond the origin, $e_1+ie_2$ and $e_0+ie_1$ being witnesses, so each strictly contains $Z_3 = \{0\}$. The intersection is empty apart from the origin: a pure element of $Z_1$ is $\mathbf u+i\mathbf v$ with $\sum_k u_k^{2} = \sum_k v_k^{2}$ and $\sum_k u_kv_k = 0$, and for such an element

$$
\overline{\tilde P}\tilde P = -2\sum_k u_k^{2}\,e_0 + 2i\,\mathbf u\times\mathbf v ,
$$

which vanishes only when $\mathbf u$ and $\mathbf v$ are parallel, hence — the two being orthogonal with equal squares — only when both vanish. $\square$

The formula is the sharpest statement of the section. The plain square of a pure element forgets the cross product, because it is $\mathbf P^{2}$, while the fourth product's square keeps it, through the coefficientwise conjugation that turns $\overline{\tilde P}\tilde P$ into $-\sum_k u_k^{2}-\sum_k v_k^{2}+2i\,\mathbf u\times\mathbf v$. The two sets of square-zero elements are therefore transverse: an element is nilpotent for the plain product exactly when it is a pure isotropic bivector, and it is square-zero for the fourth product exactly when the conjugation reflects it into its own annihilator, and the two conditions meet only at the origin. The reader who wants the square-zero elements of the fourth product in the coordinates of the other three should read the matrix equation $\operatorname{adj}\Phi(\tilde P)\Phi(\tilde P)^{\dagger} = 0$ of *The Quaternionic Sesquilinear Product in the $2\times2$ Matrix Model*, which is the same condition in the model $\mathbb{B}\cong M_2(\mathbb{C})$.

## The Annihilators

The square-zero sets are the diagonal part of the annihilation theory: an element is square-zero when it annihilates itself. The general annihilators of a zero-divisor element are the four complex planes of *The Annihilating Elements of the Four Products*, and the two notions are related by the two identities

$$
\tilde P\star\tilde P = 0 \iff \tilde P\in\{\tilde X : f(\tilde P,\tilde X) = 0\} \iff \tilde P\in\{\tilde X : f(\tilde X,\tilde P) = 0\} ,
$$

which hold for each of the four products when the annihilator is read in the same product. The square-zero set of a product is therefore the set of elements that lie in their own annihilator, and the annihilator theory of the natural product gives the converse that fails for the fourth: for the natural product every zero divisor lies in its own annihilator, while for the fourth product the zero divisor $ie_0+e_1+e_2+ie_3$ does not.

## Summary

The four products of *The Four Biquaternion Complex Products* have four square-zero sets, all contained in the common zero-divisor set, and they are of four kinds. The plain product's set is the pure isotropic cone $\{P_0 = 0,\ (\mathbf P,\mathbf P) = 0\}$, of real dimension four, whose nonzero elements are the $r(\hat u+i\hat v)$ over real pairs with $\sum_k\hat u_k^{2}=\sum_k\hat v_k^{2}=1$ and $\sum_k\hat u_k\hat v_k=0$; the natural product's set is the whole cone, of real dimension six; the complex sesquilinear product's set is the origin alone; and the complex quaternionic sesquilinear product's set is the proper subfamily cut out by $\overline{\tilde P}\tilde P = 0$, containing $e_0+ie_1$ and excluding $ie_0+e_1+e_2+ie_3$.

The sets are ordered by inclusion through the cone, $Z_3 = \{0\}\subsetneq Z_1\subsetneq Z_2$ and $\{0\}\subsetneq Z_4\subsetneq Z_2$, and the two middle sets are transverse: $Z_1\cap Z_4 = \{0\}$, because the plain square of a pure element is $\mathbf P^{2}$ and forgets the cross product of the two real parts while the fourth product's square is $\overline{\tilde P}\tilde P$ and keeps it. Every square-zero element is a zero divisor or zero, and the square-zero elements other than the origin are the zero divisors of the algebra; the four sets are the four different ways the products answer the question of where the square vanishes, and the table is *Comparison Between the Four Biquaternion Products* §*The Squares, the Idempotents and the Roots*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $Z_1,Z_2,Z_3,Z_4$ | the square-zero sets of the plain, natural, complex sesquilinear and complex quaternionic sesquilinear products |
| $\tilde P^{\natural}\tilde P = 0$ | the vanishing of the central square, the condition of the zero-divisor set |
| $\hat u,\hat v$ | a real pair with $\sum_k\hat u_k^{2} = \sum_k\hat v_k^{2} = 1$ and $\sum_k\hat u_k\hat v_k = 0$ |
| $\overline{\tilde P}\tilde P$ | the coefficientwise conjugate times the element, the square of the fourth product up to ${}^{\natural}$ |

## Further Reading

- *Comparison Between the Four Biquaternion Products* (`articles_maths/comparison-between-the-four-biquaternion-products.md`), for the tabulation of the four square-zero sets.
- *The Annihilating Elements of the Four Products* (`articles_maths/the-annihilating-elements-of-the-four-products.md`), for the annihilators and the multiplicative laws of the central square.
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the two families of the cone and the parametrisation of the pure part.
- *The Nilpotents and the Zero Divisors of the Quaternionic Product* (`articles_maths/the-nilpotents-and-the-zero-divisors-of-the-quaternionic-product.md`), for the square-zero set of the natural product and its annihilators.
- *The Square of the Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the equation $\overline{\tilde P}\tilde P = 0$ and its two witnesses.
- *The Squares and the Positive Cone of the Biquaternion Sesquialgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesquialgebra.md`), for the definiteness of the complex sesquilinear square.
- *Biquaternion Square Roots of Minus One, Zero and Plus One* (`articles_maths/biquaternion-square-roots-of-minus-one-zero-and-plus-one.md`), for the roots of $0$ of the plain product.
- *The Square Roots of a Central Value in the Four Products* (`articles_maths/the-square-roots-of-a-central-value-in-the-four-products.md`), for the criterion that places every square-zero set inside the zero-divisor set.
- *The Idempotents of the Four Products* (`articles_maths/the-idempotents-of-the-four-products.md`), for the non-pure elements of the cone.
- *The Biquaternion Quaternionic Sesquialgebra in the $2\times2$ Matrix Representation* (`articles_maths/the-biquaternion-quaternionic-sesquialgebra-in-the-2x2-matrix-representation.md`), for the square-zero equation in the matrix model.
