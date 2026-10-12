# __The Square-Zero Elements of the Twelve Structures__

## Introduction

The square of an element of the biquaternion algebra vanishes on a set that depends sharply on the product, and the four sets are the subject of this article. They are the solutions of

$$
\tilde P\tilde P = 0 , \qquad \tilde P^{\natural}\tilde P = 0 , \qquad \tilde P\tilde P^{*} = 0 , \qquad \tilde P^{\natural}\tilde P^{*} = 0 ,
$$

and they range from a single point to the whole zero-divisor cone. The chains that contain them are known: the square-zero elements of the plain product are the pure isotropic vectors (*Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, *Zero Divisors of the General Plain Algebra*), those of the natural product are all the zero divisors of the algebra together with $0$ (*Nilpotents of the General Quaternionic Algebra*), those of the general plain sesquilinear product are the origin alone (*The Squares and the Positive Cone of the Biquaternion Sesqualgebra*), and those of the general quaternionic sesquilinear product are a proper subfamily of the zero-divisor set (*The Square of the General Quaternionic Sesquilinear Product and the Two Halves*). This article gathers the four solutions, separates the two families of the common denominator, the zero-divisor cone, according to which of the four square-zero sets meets them, and records the crossing of the plain and the general quaternionic sesquilinear sets, which meet only at the origin. The same equation is then read on the twelve structures of the space, in §*The Twelve Square-Zero Sets*.

The common denominator is the zero-divisor set of *The Annihilating Elements of the Twelve Structures*, the set of elements that admit a nonzero annihilating factor. Every square-zero element is a zero divisor or zero, since a vanishing square exhibits a nonzero annihilating factor, and so each of the four square-zero sets lies in the zero-divisor set together with the origin. The four general products place it differently inside the cone, and the article's content is the placement.

**Conventions.** $\tilde P = P_0e_0+\mathbf P$ with $P_0\in\mathbb{C}$ and $\mathbf P$ a vector; the natural conjugation is $\tilde P^{\natural} = P_0-\mathbf P$, the star is $\tilde P^{*} = \overline{\tilde P^{\natural}}$, and the **central square** is $\tilde P^{\natural}\tilde P = \tilde P\tilde P^{\natural} = \bigl(\sum_\mu P_\mu^{2}\bigr)e_0$. The zero-divisor set is the vanishing set of the central square with the origin removed, and the two families of the cone are the pure zero divisors, those with $P_0 = 0$, and the non-pure ones, those with $P_0\neq0$ (*Zero Divisors of the General Plain Algebra*). A square-zero element is written $\tilde\Upsilon$ where the nilpotency is the point, the generic letter $\tilde P$ being kept in the statements that hold for every element (§*The nilpotent convention* of *Conventions in Mathematics*).

## The Four Equations

Each of the four squares has a closed form, and setting it to zero gives one equation per product.

| product | square | square-zero equation |
|---|---|---|
| $\tilde P\tilde P$ | $\bigl(P_0^{2}-(\mathbf P,\mathbf P)\bigr)e_0 + 2P_0\mathbf P$ | $P_0^{2}-(\mathbf P,\mathbf P) = 0$ and $P_0\mathbf P = 0$ |
| $\tilde P^{\natural}\tilde P$ | $\tilde P^{\natural}\tilde P$, a central element | $\tilde P^{\natural}\tilde P = 0$ |
| $\tilde P\tilde P^{*}$ | Hermitian with $\mathrm{Sc} = \sum_\mu\lvert P_\mu\rvert^{2}$ | $\sum_\mu\lvert P_\mu\rvert^{2} = 0$ |
| $\tilde P^{\natural}\tilde P^{*}$ | Hermitian with $\mathrm{Sc} = \lvert P_0\rvert^{2}-\sum_k\lvert P_k\rvert^{2}$ | $\overline{\tilde P}\tilde P = 0$ |

The four equations are of four different types: a pair consisting of a complex equation and a vector equation for the plain product, a single complex equation for the natural product, a sum of modulus squares for the general plain sesquilinear product, and a matrix equation $\overline{\tilde P}\tilde P = 0$ for the fourth. The shapes already decide the answers, and the sections below read them one by one.

## The Plain Product: The Pure Isotropic Cone

**Theorem (the square-zero elements of the plain product).** In the associative product the square of $\tilde P$ vanishes exactly when $P_0 = 0$ and $(\mathbf P,\mathbf P) = 0$: the pure isotropic cone, of real dimension four. Written as $\tilde P = \mathbf u+i\mathbf v$ with $\mathbf u,\mathbf v$ real vectors, the two conditions are $\sum_k u_k^{2} = \sum_k v_k^{2}$ and $\sum_k u_kv_k = 0$, so that every nonzero element of the set is $r(\hat u+i\hat v)$ over a real pair with $\sum_k\hat u_k^{2} = \sum_k\hat v_k^{2} = 1$ and $\sum_k\hat u_k\hat v_k = 0$, and a positive real $r$.

**Proof.** The square is $\bigl(P_0^{2}-(\mathbf P,\mathbf P)\bigr)e_0+2P_0\mathbf P$, a sum of a central element and a vector element, so it vanishes exactly when both coefficients do: $2P_0\mathbf P = 0$ gives $P_0 = 0$ or $\mathbf P = 0$, and $\mathbf P = 0$ forces $P_0 = 0$ from the first equation, so $P_0 = 0$ and $(\mathbf P,\mathbf P) = 0$. For $\mathbf P = \mathbf u+i\mathbf v$ the vector-part square is $(\mathbf P,\mathbf P) = \sum_k u_k^{2}-\sum_k v_k^{2}+2i\sum_k u_kv_k$, giving the two real conditions. The parametrisation is *Zero Divisors of the General Plain Algebra*.

It is the only one of the four that is a cone of **pure** elements — every square-zero element of the plain product lies in the vector subspace — and it is one of the two of real dimension four, the other being the fourth product's set. The six-dimensional cone of *Zero Divisors of the General Plain Algebra* drops by two real dimensions here, and the square-zero set is the four-dimensional pure part, on which the two conditions of equal length and orthogonality are the two real equations. The set is the nilpotent cone of the algebra, of *Introduction to the Remarkable Subspaces*.

## The Natural Product: The Whole Cone

**Theorem (the square-zero elements of the natural product).** In the general quaternionic bilinear product the square of $\tilde P$ vanishes exactly when $\tilde P^{\natural}\tilde P = 0$: the whole zero-divisor set, of real dimension six, the origin included.

**Proof.** The square is the central element $\tilde P^{\natural}\tilde P$ (*Introduction to the General Quaternionic Algebra of Biquaternions*), which vanishes exactly when the zero-divisor criterion holds (*Zero Divisors of the General Plain Algebra*).

The natural product is the only one of the four whose square-zero set is the whole cone. Its square is the central square itself, so the equation is the defining equation of the zero-divisor set, and the square-zero elements of this product are all the elements that admit a nonzero annihilating factor. Both families of the cone belong to the set: the pure nilpotents of the plain product and the non-pure elements, which are the nonzero complex multiples of the nontrivial idempotents of the algebra (*The Idempotents of the Twelve Structures*).

## The General Plain Sesquilinear Product: The Origin Alone

**Theorem (the square-zero elements of the general plain sesquilinear product).** In the general plain sesquilinear product the square of $\tilde P$ vanishes exactly when $\tilde P = 0$.

**Proof.** The square is Hermitian with scalar part $\sum_\mu\lvert P_\mu\rvert^{2}$, a sum of non-negative real numbers, which vanishes exactly when every coordinate does (*The Squares and the Positive Cone of the Biquaternion Sesqualgebra*).

The set is the smallest possible, and its smallness is the definiteness of the sum of modulus squares. The same vanishing of the modulus squares gives the general plain sesquilinear product its empty root sets for the negative central values (*The Square Roots of a Central Value in the Twelve Structures*), and the two facts are one fact: the product's square has scalar part $\sum_\mu\lvert P_\mu\rvert^{2}$, which vanishes only at the origin. In the cone of the zero divisors the general plain sesquilinear product's square detects nothing.

## The General Quaternionic Sesquilinear Product: A Proper Subfamily

**Theorem (the square-zero elements of the fourth product).** In the general quaternionic sesquilinear product the square of $\tilde P$ vanishes exactly when $\overline{\tilde P}\tilde P = 0$. The set is a proper subfamily of the zero-divisor set, of positive codimension in it: the element $e_0+ie_1$ is square-zero, so the set is not $\{0\}$; the element $ie_0+e_1+e_2+ie_3$ is a zero divisor whose square is nonzero, so the set is not the whole cone.

**Proof.** The square is $\tilde P^{\natural}\tilde P^{*} = \bigl(\overline{\tilde P}\tilde P\bigr)^{\natural}$ (*The Square of the General Quaternionic Sesquilinear Product and the Two Halves*), which vanishes exactly when $\overline{\tilde P}\tilde P$ does, so a square-zero element is a zero divisor. The two displayed elements are computed in the same article: $(e_0+ie_1)\star(e_0+ie_1) = 0$ and $(ie_0+e_1+e_2+ie_3)\star(ie_0+e_1+e_2+ie_3)\neq0$.

The fourth product is the only one whose square-zero set is neither the cone, nor the pure part of it, nor a point: it is a set of a fourth kind, cut out of the cone by the matrix equation $\overline{\tilde P}\tilde P = 0$ and not by a single scalar one. It is the boundary case of the comparison, and the next section reads it against the other three.

## The Chain and the Incomparable Pair

Inside the cone the plain and the natural sets are nested and the fourth is nested in the natural one, while the plain and the fourth sets cross each other.

**Theorem (the order of the sets).** Write $Z_1,Z_2,Z_3,Z_4$ for the square-zero sets of the plain, natural, general plain sesquilinear and general quaternionic sesquilinear products. Then

$$
Z_3 = \{0\} \subsetneq Z_1 \subsetneq Z_2 , \qquad Z_3 \subsetneq Z_4 \subsetneq Z_2 , \qquad Z_1\cap Z_4 = \{0\} ,
$$

so that $Z_1$ and $Z_4$ are incomparable, and the four sets are ordered only by the two chains through $Z_2$.

**Proof.** The inclusions $Z_1\subseteq Z_2$ and $Z_4\subseteq Z_2$ are the two theorems above, and both are strict: $e_0+ie_1$ lies in $Z_2$ and not in $Z_1$, so $Z_1\subsetneq Z_2$, while $ie_0+e_1+e_2+ie_3$ lies in $Z_2$ and not in $Z_4$, so $Z_4\subsetneq Z_2$. The sets $Z_1$ and $Z_4$ are non-empty beyond the origin, $e_1+ie_2$ and $e_0+ie_1$ being witnesses, so each strictly contains $Z_3 = \{0\}$. The intersection is empty apart from the origin: a pure element of $Z_1$ is $\mathbf u+i\mathbf v$ with $\sum_k u_k^{2} = \sum_k v_k^{2}$ and $\sum_k u_kv_k = 0$, and for such an element

$$
\overline{\tilde P}\tilde P = -2\sum_k u_k^{2}\,e_0 + 2i\,\mathbf u\times\mathbf v ,
$$

which vanishes only when $\mathbf u$ and $\mathbf v$ are parallel, hence — the two being orthogonal with equal squares — only when both vanish.

The formula is the sharpest statement of the section. The plain square of a pure element forgets the cross product, because it is $\mathbf P^{2}$, while the fourth product's square keeps it, through the coefficientwise conjugation that turns $\overline{\tilde P}\tilde P$ into $-\sum_k u_k^{2}-\sum_k v_k^{2}+2i\,\mathbf u\times\mathbf v$. The two sets of square-zero elements are therefore transverse: an element is nilpotent for the plain product exactly when it is a pure isotropic bivector, and it is square-zero for the fourth product exactly when the conjugation reflects it into its own annihilator, and the two conditions meet only at the origin. The reader who wants the square-zero elements of the fourth product in the coordinates of the other three should read the matrix equation $\operatorname{adj}\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde P)^{\dagger} = 0$ of *The General Quaternionic Sesquilinear Product in the $2\times2$ Matrix Model*, which is the same condition in the model $\mathbb{B}\cong M_2(\mathbb{C})$.

## The Annihilators

The square-zero sets are the diagonal part of the annihilation theory: an element is square-zero when it annihilates itself. The general annihilators of a zero-divisor element are the four complex planes of *The Annihilating Elements of the Twelve Structures*, and the two notions are related by the two identities

$$
\tilde P\star\tilde P = 0 \iff \tilde P\in\{\tilde X : f(\tilde P,\tilde X) = 0\} \iff \tilde P\in\{\tilde X : f(\tilde X,\tilde P) = 0\} ,
$$

which hold for each of the four general products when the annihilator is read in the same product. The square-zero set of a product is therefore the set of elements that lie in their own annihilator, and the annihilator theory of the natural product gives the converse that fails for the fourth: for the natural product every zero divisor lies in its own annihilator, while for the fourth product the zero divisor $ie_0+e_1+e_2+ie_3$ does not.

## The Twelve Square-Zero Sets

The four products are four of the twelve structures of the space, and the equation $\tilde P\star\tilde P = 0$ is written in the operation of the structure, so each of the twelve carries a square-zero set of its own (*The 12 Products of the Biquaternion Complex Space*, *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*). The set is the diagonal of the zero-divisor theory, and it is read against the zero-divisor set of *The Zero Divisors and the Twelve Structures*.

| structure | the square-zero set | against its zero-divisor set |
|---|---|---|
| $\mathrm{GPA}$, $\mathrm{SPA}$ | the pure isotropic cone, $\{P_0=0,\ (\mathbf P,\mathbf P)=0\}$ | a proper subfamily of the cone |
| $\mathrm{GQA}$ | the whole cone $\{c=0\}$ | the zero-divisor set, with the origin |
| $\mathrm{SQA}$ | the whole cone $\{c=0\}$ | a proper subfamily of its zero-divisor set |
| $\mathrm{GPS}$, $\mathrm{SPS}$ | $\{0\}$ alone | a proper subfamily |
| $\mathrm{GQS}$, $\mathrm{SQS}$ | the subfamily $\overline{\tilde P}\tilde P = 0$ | a proper subfamily of the cone |
| $\mathrm{APA}$, $\mathrm{AQA}$ | the whole space | the zero-divisor set, with the origin |
| $\mathrm{APS}$ | the subfamily $\tilde P\tilde P^{*}$ central | not inside the cone; contains $e_0$ |
| $\mathrm{AQS}$ | the subfamily $\tilde P^{\natural}\tilde P^{*}$ real | not inside the cone; contains $e_0$ |

**Theorem (the twelve square-zero sets).** Among the twelve structures the square-zero set is the whole space for $\mathrm{APA}$ and $\mathrm{AQA}$; the whole cone $\{c=0\}$ for $\mathrm{GQA}$ and $\mathrm{SQA}$; the pure isotropic cone for $\mathrm{GPA}$ and $\mathrm{SPA}$; a proper subfamily of the cone for $\mathrm{GQS}$ and $\mathrm{SQS}$; the origin alone for $\mathrm{GPS}$ and $\mathrm{SPS}$; the set $\{\tilde P : \tilde P\tilde P^{*}\in\mathbb{C}_{\mathbb{B}}\}$ for $\mathrm{APS}$; and the set $\{\tilde P : \tilde P^{\natural}\tilde P^{*}\ \text{is real}\}$, equivalently the elements whose vector part is a complex multiple of a real vector, for $\mathrm{AQS}$. The last two leave the cone, since they contain the unit $e_0$. The sets for which the square-zero elements other than the origin are exactly the zero divisors are therefore three: the general quaternionic algebra and the two antisymmetric bilinear structures.

*Proof.* The plain square is the plain square of §*The Plain Product: The Pure Isotropic Cone* for $\mathrm{SPA}$ and the central square of §*The Natural Product: The Whole Cone* for $\mathrm{SQA}$, so the two symmetric bilinear structures inherit the sets of their general partners; the cone is $\mathrm{GQA}$'s own zero-divisor set with the origin, while $\mathrm{SQA}$'s zero-divisor set is the whole punctured space, so the cone is a proper subfamily of it. On the two antisymmetric bilinear structures the product is alternating, $\tilde P\wedge\tilde P = 0$, so every element is square-zero and — the zero-divisor set being the whole punctured space as well — the two sets coincide. On $\mathrm{APS}$ the square is the pure part of the Hermitian element $\tilde P\tilde P^{*}$, so it vanishes exactly when $\tilde P\tilde P^{*}$ is central. On $\mathrm{AQS}$ the square is the coefficientwise imaginary part of $\tilde P^{\natural}\tilde P^{*}$, whose scalar part is the real Krein value, so it vanishes exactly when $\tilde P^{\natural}\tilde P^{*}$ is fixed by the coefficientwise conjugation, equivalently when the vector part of $\tilde P$ is a complex multiple of a real vector (*The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*); the unit $e_0$ lies in both sets, and neither is a subfamily of the cone. On the two symmetric sesquilinear structures the square is the coefficientwise real part of $\tilde P^{\natural}\tilde P^{*}$, and the resulting equation is the one of the general quaternionic sesquilinear structure, a proper subfamily of the cone. On $\mathrm{GPS}$ and $\mathrm{SPS}$ the square has the scalar part $\sum_\mu\lvert P_\mu\rvert^{2}$, vanishing only at the origin.

**Remark (where the square detects the zero divisors).** The gap between "square-zero" and "zero divisor" is a property of the structure and not of the element, and among the twelve it is widest where the zero divisors are most numerous. The implication *square-zero implies zero divisor*, true by the vanishing square itself, is a theorem of only eight of the twelve: it fails for the four antisymmetric structures, whose centre — and in particular the unit $e_0$ — is square-zero while not being a zero divisor. The two antisymmetric bilinear structures give every element a vanishing square and every nonzero element a zero divisor, so there the two notions agree after the origin is excluded; the two antisymmetric sesquilinear structures make every nonzero element a zero divisor while their square-zero set, though it still contains the centre line, is a proper subfamily of the space. The general quaternionic algebra is the one non-degenerate structure whose square vanishes on the whole zero-divisor set: there an element is a zero divisor exactly when its square vanishes.

**Remark (the telescoping of the sets).** The four general sets of §*The Chain and the Incomparable Pair* sit on a lattice that the twelve-structure reading completes: the origin inside the pure isotropic cone inside the whole cone inside the whole space, with the subfamilies of $\mathrm{GQS}$ and $\mathrm{SQS}$ inside the cone, the subfamilies of $\mathrm{APS}$ and $\mathrm{AQS}$ outside it, each containing the centre line, and the two antisymmetric bilinear structures at the top. The plain and the fourth general sets, incomparable inside the cone, are separated once the antisymmetric bilinear structure is added, whose square-zero set is the whole space and meets every other set.

## Summary

The four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* have four square-zero sets, all contained in the common zero-divisor set, and they are of four kinds. The plain product's set is the pure isotropic cone $\{P_0 = 0,\ (\mathbf P,\mathbf P) = 0\}$, of real dimension four, whose nonzero elements are the $r(\hat u+i\hat v)$ over real pairs with $\sum_k\hat u_k^{2}=\sum_k\hat v_k^{2}=1$ and $\sum_k\hat u_k\hat v_k=0$; the natural product's set is the whole cone, of real dimension six; the general plain sesquilinear product's set is the origin alone; and the general quaternionic sesquilinear product's set is the proper subfamily cut out by $\overline{\tilde P}\tilde P = 0$, containing $e_0+ie_1$ and excluding $ie_0+e_1+e_2+ie_3$.

The sets are ordered by inclusion through the cone, $Z_3 = \{0\}\subsetneq Z_1\subsetneq Z_2$ and $\{0\}\subsetneq Z_4\subsetneq Z_2$, and the two middle sets are transverse: $Z_1\cap Z_4 = \{0\}$, because the plain square of a pure element is $\mathbf P^{2}$ and forgets the cross product of the two real parts while the fourth product's square is $\overline{\tilde P}\tilde P$ and keeps it. Every square-zero element is a zero divisor or zero, and the square-zero elements other than the origin are the zero divisors of the algebra; the four sets are the four different ways the products answer the question of where the square vanishes, and the table is *Comparison Between the Four General Products* §*The Squares, the Idempotents and the Roots*.

Read among the twelve structures the equation $\tilde P\star\tilde P = 0$ descends from the whole space to the origin in five steps. It holds on all of $\mathbb{B}$ for the two antisymmetric bilinear structures, on the whole cone for the general quaternionic algebra and its symmetric partner, on the pure isotropic cone for the plain structure and its symmetric partner, on a proper subfamily of the cone for the two general-sesquilinear and the two antisymmetric-sesquilinear structures, and at the origin alone for the two definite sesquilinear structures. The square-zero set equals the zero-divisor set for exactly three of the twelve, the general quaternionic algebra and the two antisymmetric bilinear structures; on the other nine the square discriminates inside the zero-divisor set.

## Summary of Notation

| symbol | meaning |
|---|---|
| $Z_1,Z_2,Z_3,Z_4$ | the square-zero sets of the plain, natural, general plain sesquilinear and general quaternionic sesquilinear products |
| $\tilde P^{\natural}\tilde P = 0$ | the vanishing of the central square, the condition of the zero-divisor set |
| $\hat u,\hat v$ | a real pair with $\sum_k\hat u_k^{2} = \sum_k\hat v_k^{2} = 1$ and $\sum_k\hat u_k\hat v_k = 0$ |
| $\overline{\tilde P}\tilde P$ | the coefficientwise conjugate times the element, the square of the fourth product up to ${}^{\natural}$ |
| $\mathrm{GPA},\dots,\mathrm{AQS}$ | the twelve structures of the space, the four general ones and the eight derived ones |

## Further Reading

- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the tabulation of the four square-zero sets.
- *The Annihilating Elements of the Twelve Structures* (`articles_maths/the-annihilating-elements-of-the-twelve-structures.md`), for the annihilators and the multiplicative laws of the central square.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the two families of the cone and the parametrisation of the pure part.
- *Nilpotents of the General Quaternionic Algebra* (`articles_maths/nilpotents-of-the-general-quaternionic-algebra.md`), for the square-zero set of the natural product and its annihilators.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the equation $\overline{\tilde P}\tilde P = 0$ and its two witnesses.
- *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* (`articles_maths/the-squares-and-the-positive-cone-of-the-biquaternion-sesqualgebra.md`), for the definiteness of the general plain sesquilinear square.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the roots of $0$ of the plain product.
- *The Square Roots of a Central Value in the Twelve Structures* (`articles_maths/the-square-roots-of-a-central-value-in-the-twelve-structures.md`), for the criterion that places every square-zero set inside the zero-divisor set.
- *The Idempotents of the Twelve Structures* (`articles_maths/the-idempotents-of-the-twelve-structures.md`), for the non-pure elements of the cone.
- *The General Quaternionic Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-quaternionic-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the square-zero equation in the matrix model.
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the four general products and their symmetric and antisymmetric parts.
- *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the twelve names and the class of each.
