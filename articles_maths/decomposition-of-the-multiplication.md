# __Decomposition of the Multiplication__

## Introduction

This article studies the two halves into which the product of two biquaternions splits. The product itself, its developed form and its scalar–vector form are *The Four Biquaternion Complex Products*; here the product is taken as known and read through its **order symmetry**, which separates it into a **symmetric part** and an **antisymmetric part**. The complex bilinear product is treated first and in full; the same split is then carried out for the three other products of *The Four Biquaternion Complex Products*, and the four splits are compared in §*The Four Products*.

The two halves are of different kinds. The antisymmetric part is a pure vector, the complex cross product of the vector parts of the two factors; its vanishing is the commutativity criterion, and it closes on the anti-Hermitian subspace. The symmetric part carries all of the scalar and the mixed scalar–vector terms; it is the polarisation of the square, it makes $\mathbb{B}$ a Jordan algebra, and it closes on the Hermitian subspace. That pair of closures is the origin of the Lie and the Jordan structures of the algebra. For the three other products the same interchange of the two factors is what governs the split, and its outcome is different in each case: the split of the $\natural$-product is its scalar–vector split, the split of the star-product is its Hermitian split, and the split of the quaternionic sesquilinear product respects none of the six subspaces.

The article assumes the four products from *The Four Biquaternion Complex Products* and the elements, the basis and the conjugations from *Biquaternions as a Vector Space over $\mathbb{C}$*; the product read as the multiplication of an algebra is *Biquaternions as a Bilinear Algebra over $\mathbb{C}$*, and with the real scalars *Biquaternions as a Bilinear Algebra over $\mathbb{R}$*. It defines no form of its own: the scalar parts that occur are the four scalar parts of *The Four Biquaternion Complex Products*, linked in *Relations Between the Four Biquaternion Products*. The behaviour of the product and of its two halves on each of the six subspaces is tabulated in *Biquaternion Relations Between Subspaces*; the Lie algebra carried by the antisymmetric part is *Biquaternion Lie Algebra*; the Jordan algebra carried by the symmetric part is *Biquaternion Jordan Algebra*; and the operators $L_{\tilde{P}}$ and $R_{\tilde{P}}$ are *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*.

Throughout, the product of two elements is written by juxtaposition, $\tilde{P}\tilde{Q}$, and $\tilde{P}=P_0+\mathbf{P}$ separates the complex scalar part $P_0$ from the complex vector part $\mathbf{P}=P_1e_1+P_2e_2+P_3e_3$.

## The Symmetric Part

### Definition

The **symmetric part**, also called the **symmetrised product** or the **Jordan product**, of two biquaternions is

$$
\tilde{P}\bullet\tilde{Q} := \tfrac{1}{2}\bigl(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}\bigr).
$$

In scalar–vector notation the antisymmetric terms of the product cancel and the mixed terms double:

$$
\tilde{P}\bullet\tilde{Q} = \bigl(P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr) + P_0\mathbf{Q} + Q_0\mathbf{P} .
$$

The symmetrised product is commutative and $\mathbb{C}$-bilinear, and it agrees with the ordinary square on the diagonal:

$$
\tilde{P}\bullet\tilde{Q} = \tilde{Q}\bullet\tilde{P} , \qquad \tilde{P}\bullet\tilde{P} = \tilde{P}^2 .
$$

### It Is the Polarisation of the Square

**Proposition.** The symmetrised product is the polarisation of the square:

$$
\tilde{P}\bullet\tilde{Q} = \tfrac{1}{2}\Bigl((\tilde{P}+\tilde{Q})^2 - \tilde{P}^2 - \tilde{Q}^2\Bigr).
$$

**Proof.** Expand $(\tilde{P}+\tilde{Q})^2=\tilde{P}^2+\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}+\tilde{Q}^2$ by bilinearity and divide by two.

The identity is the reason the symmetrised product, not the full product, is the product of the square: $\tilde{P}\bullet\tilde{P}=\tilde{P}^2$, and the symmetric part of $\tilde{P}\tilde{Q}$ is exactly the term that a squaring process can see. Directly,

$$
\tilde{P}^2 = \bigl(P_0^2-(\mathbf{P},\mathbf{P})\bigr) + 2P_0\mathbf{P} ,
$$

which is a scalar plus a scalar multiple of $\mathbf{P}$ and contains no cross-product term. Every square-root problem $\xi^2=\tilde{Q}$ is therefore a problem in the symmetric part alone, and the outer product plays no part in *Biquaternion Square Roots of Minus One, Zero and Plus One* and *Biquaternion Square Roots of a General Element*.

### It Is a Jordan Product

**Theorem.** With the product $\bullet$, the algebra $\mathbb{B}$ is a commutative Jordan algebra: $\bullet$ is commutative and bilinear, and the Jordan identity

$$
(\tilde{P}\bullet\tilde{Q})\bullet\tilde{P}^2 = \tilde{P}\bullet\bigl(\tilde{Q}\bullet\tilde{P}^2\bigr)
$$

holds for all $\tilde{P},\tilde{Q}$.

**Proof.** The product of an associative algebra satisfies the Jordan identity for the symmetrised product, by the associativity of the underlying product; commutativity and bilinearity are built into the definition. The general theory is *Jordan Algebras*.

Two consequences follow. First, the Hermitian subspace $\mathbb{M}_+$ is closed under $\bullet$: for $\tilde{P},\tilde{Q}\in\mathbb{M}_+$ the product $\tilde{P}\bullet\tilde{Q}$ is again Hermitian, so $\mathbb{M}_+$ is a Jordan subalgebra of $\mathbb{B}$. Second, the symmetrised product carries the same scalar part as the product itself,

$$
\mathrm{Sc}(\tilde{P}\bullet\tilde{Q}) = \mathrm{Sc}(\tilde{P}\tilde{Q}) = P_0Q_0-(\mathbf{P},\mathbf{Q}),
$$

since the antisymmetric part has no scalar part.

## The Antisymmetric Part

### Definition

The **antisymmetric part** of the product, or **outer product**, is

$$
\tilde{P}\wedge\tilde{Q} := \tfrac{1}{2}\bigl(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}\bigr).
$$

In scalar–vector notation the scalar parts cancel and the mixed terms too, leaving the cross product of the vector parts:

$$
\tilde{P}\wedge\tilde{Q} = \mathbf{P}\times\mathbf{Q} .
$$

The outer product is **alternating** and $\mathbb{C}$-bilinear, and it is skew:

$$
\tilde{P}\wedge\tilde{P} = 0 , \qquad \tilde{P}\wedge\tilde{Q} = -\,\tilde{Q}\wedge\tilde{P} .
$$

Its value is a pure vector: the scalar part of $\tilde{P}\wedge\tilde{Q}$ vanishes, for every pair of biquaternions, not only for vector-like ones.

### The Commutativity Criterion

Because the right-hand side of the outer product depends on the vector parts alone, the vanishing of the antisymmetric part is a criterion:

$$
\tilde{P}\tilde{Q} = \tilde{Q}\tilde{P} \quad\Longleftrightarrow\quad \mathbf{P}\times\mathbf{Q} = 0 .
$$

The cross product of two complex vectors vanishes exactly when the vectors are **linearly dependent**, so two biquaternions commute if and only if their vector parts are parallel. In particular a central element $\tilde{P}=P_0e_0$ commutes with every biquaternion, since its vector part is zero; the converse holds, so this recovers the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ as the set of elements that commute with all of $\mathbb{B}$.

### The Closure of the Two Sectors

The two halves of the product behave differently with respect to the Hermitian split, and the pattern is worth recording here because it is the origin of the Lie and Jordan structures of the algebra.

| $\tilde{P},\tilde{Q}$ | $\tilde{P}\wedge\tilde{Q}$ | $\tilde{P}\bullet\tilde{Q}$ |
|---|---|---|
| $\mathbb{M}_+$ (Hermitian) | lies in $\mathbb{M}_-$ | lies in $\mathbb{M}_+$ |
| $\mathbb{M}_-$ (anti-Hermitian) | lies in $\mathbb{M}_-$ | lies in $\mathbb{M}_+$ |

That is, the antisymmetric part closes on the anti-Hermitian subspace and carries the Hermitian one into it, so $\mathbb{M}_-$ is a Lie subalgebra; the symmetric part closes on the Hermitian subspace, so $\mathbb{M}_+$ is a Jordan subalgebra. The full subspace-by-subspace table, with the centre, the vector subspace, the quaternion subspace and the anti-quaternion subspace, is *Biquaternion Relations Between Subspaces*.

## The Two Parts Together

### The Split Is by Order Symmetry

The product is the sum of its two halves,

$$
\tilde{P}\tilde{Q} = \tilde{P}\bullet\tilde{Q} + \tilde{P}\wedge\tilde{Q} ,
$$

and the two halves are read in coordinates as

| part | scalar part | vector part | symmetry |
|---|---|---|---|
| $\tilde{P}\bullet\tilde{Q}$ | $P_0Q_0-(\mathbf{P},\mathbf{Q})$ | $P_0\mathbf{Q}+Q_0\mathbf{P}$ | symmetric, $\tilde{P}\bullet\tilde{Q}=\tilde{Q}\bullet\tilde{P}$ |
| $\tilde{P}\wedge\tilde{Q}$ | $0$ | $\mathbf{P}\times\mathbf{Q}$ | antisymmetric, $\tilde{P}\wedge\tilde{Q}=-\tilde{Q}\wedge\tilde{P}$ |

The antisymmetric part is pure vector and the symmetric part carries the scalar plus the mixed terms.

### The Operator Reading

The two halves are the balanced and the unbalanced one-sided multiplications. With $L_{\tilde{P}}(\tilde{Q})=\tilde{P}\tilde{Q}$ and $R_{\tilde{P}}(\tilde{Q})=\tilde{Q}\tilde{P}$ the left and right multiplications by $\tilde{P}$,

$$
\tilde{P}\bullet\tilde{Q} = \tfrac{1}{2}\bigl(L_{\tilde{P}}+R_{\tilde{P}}\bigr)(\tilde{Q}) , \qquad \tilde{P}\wedge\tilde{Q} = \tfrac{1}{2}\bigl(L_{\tilde{P}}-R_{\tilde{P}}\bigr)(\tilde{Q}) .
$$

The antisymmetric combination $L_{\tilde{P}}-R_{\tilde{P}}$ is the inner derivation of the algebra, so the outer product is half that derivation applied to the second factor, and the symmetric combination $L_{\tilde{P}}+R_{\tilde{P}}$ is twice the symmetrised multiplication by $\tilde{P}$. The operators themselves are *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*.

### Worked Example

Take $\tilde{P}=e_0+e_1$ and $\tilde{Q}=e_2$, so that $P_0=1$, $\mathbf{P}=e_1$, $Q_0=0$ and $\mathbf{Q}=e_2$. The dot product vanishes, $(\mathbf{P},\mathbf{Q})=0$, and the cross product is $\mathbf{P}\times\mathbf{Q}=e_1\times e_2=e_3$. Hence

$$
\tilde{P}\bullet\tilde{Q} = (1\cdot 0-0)+1\cdot e_2+0\cdot e_1 = e_2 , \qquad \tilde{P}\wedge\tilde{Q} = e_3 , \qquad \tilde{P}\tilde{Q} = e_2+e_3 .
$$

Interchanging the factors changes the sign of the outer product and leaves the symmetric part unchanged,

$$
\tilde{Q}\tilde{P} = e_2-e_3 , \qquad \tilde{Q}\bullet\tilde{P} = e_2 , \qquad \tilde{Q}\wedge\tilde{P} = -e_3 ,
$$

so $\tilde{P}\tilde{Q}\neq \tilde{Q}\tilde{P}$ while $\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P} = 2e_2 = 2(\tilde{P}\bullet\tilde{Q})$, and the difference is $\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}=2e_3=2(\tilde{P}\wedge\tilde{Q})$, in agreement with the identities above.

## The Four Products

The split above is a split of the complex bilinear product. Each of the three other products of *The Four Biquaternion Complex Products* carries the same split, and the four splits are worth comparing, because the interchange of the two factors acts on the four values in two different ways.

Write $\mathcal{A},\mathcal{B},\mathcal{C},\mathcal{D}$ for the four products as binary operations, $\mathcal{A}(\tilde{P},\tilde{Q})=\tilde{P}\tilde{Q}$, $\mathcal{B}(\tilde{P},\tilde{Q})=\tilde{P}^{\natural}\tilde{Q}$, $\mathcal{C}(\tilde{P},\tilde{Q})=\tilde{P}\tilde{Q}^{*}$ and $\mathcal{D}(\tilde{P},\tilde{Q})=\tilde{P}^{\natural}\tilde{Q}^{*}$, and for an arbitrary binary operation $f$ on $\mathbb{B}$ put

$$
f^{\mathrm{s}}(\tilde{P},\tilde{Q}):=\tfrac12\bigl(f(\tilde{P},\tilde{Q})+f(\tilde{Q},\tilde{P})\bigr),\qquad
f^{\mathrm{a}}(\tilde{P},\tilde{Q}):=\tfrac12\bigl(f(\tilde{P},\tilde{Q})-f(\tilde{Q},\tilde{P})\bigr).
$$

Then $f=f^{\mathrm{s}}+f^{\mathrm{a}}$, by definition; each symmetric half is symmetric in the two slots and each antisymmetric half is alternating, $f^{\mathrm{a}}(\tilde{P},\tilde{P})=0$, both properties following from the two projectors $\tfrac12(1\pm\sigma)$ of the interchange $\sigma$ of the pair.

### The Interchange of the Two Factors

The whole difference between the four splits is what the interchange does to a value. For two of the four products the swapped product is the same product with the slots exchanged under a conjugation of the value; for the other two no conjugation does this.

For the $\natural$-product and the star-product the identity is the one recorded in *Relations Between the Four Biquaternion Products*,

$$
\mathcal{B}(\tilde{Q},\tilde{P})=\mathcal{B}(\tilde{P},\tilde{Q})^{\natural},\qquad
\mathcal{C}(\tilde{Q},\tilde{P})=\mathcal{C}(\tilde{P},\tilde{Q})^{*},
$$

the first being $(\tilde{P}^{\natural}\tilde{Q})^{\natural}=\tilde{Q}^{\natural}\tilde{P}$ and the second $(\tilde{P}\tilde{Q}^{*})^{*}=\tilde{Q}\tilde{P}^{*}$. In both cases the conjugated value is a value of the same product, and no other conjugation of a value does it: a value has the four conjugates $\tilde{X}$, $\tilde{X}^{\natural}$, $\overline{\tilde{X}}$ and $\tilde{X}^{*}$, and the two identities above are the only ones among them that a swap can satisfy.

For the complex bilinear product and the quaternionic sesquilinear product no such identity holds. The swapped complex bilinear product is $\mathcal{A}(\tilde{Q},\tilde{P})=\tilde{Q}\tilde{P}$, the same two elements in the opposite order, which is no conjugate of $\tilde{P}\tilde{Q}$; and the swapped quaternionic sesquilinear product is

$$
\mathcal{D}(\tilde{Q},\tilde{P})=\tilde{Q}^{\natural}\tilde{P}^{*}=\bigl(\overline{\tilde{P}}\,\tilde{Q}\bigr)^{\natural},
$$

an element of the plain product, which again is no conjugate of $\mathcal{D}(\tilde{P},\tilde{Q})$. The two are exactly the products that carry the conjugation in no slot and in both slots, so **the interchange is a conjugation of the value for the two products whose two slots are treated differently, and a genuine reversal for the two whose slots are treated alike**. That is the dichotomy along which the four splits fall into two pairs.

### The Symmetric Halves

Averaging the two swaps gives the four symmetric halves. In scalar–vector notation, with $\overline{\mathbf{Q}}$ the coefficientwise conjugate of the vector part,

| $f$ | $\mathrm{Sc}\,f^{\mathrm{s}}$ | $\mathrm{Vec}\,f^{\mathrm{s}}$ |
|---|---|---|
| $\mathcal{A}=\tilde{P}\tilde{Q}$ | $P_0Q_0-(\mathbf{P},\mathbf{Q})$ | $P_0\mathbf{Q}+Q_0\mathbf{P}$ |
| $\mathcal{B}=\tilde{P}^{\natural}\tilde{Q}$ | $P_0Q_0+(\mathbf{P},\mathbf{Q})$ | $0$ |
| $\mathcal{C}=\tilde{P}\tilde{Q}^{*}$ | $\mathrm{Re}\bigl(P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr)$ | $i\,\mathrm{Im}\bigl(-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}\bigr)$ |
| $\mathcal{D}=\tilde{P}^{\natural}\tilde{Q}^{*}$ | $\mathrm{Re}\bigl(P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr)$ | $-\mathrm{Re}\bigl(P_0\overline{\mathbf{Q}}+Q_0\overline{\mathbf{P}}\bigr)+i\,\mathrm{Im}\bigl(\mathbf{P}\times\overline{\mathbf{Q}}\bigr)$ |

The two bilinear halves carry the two bilinear scalar parts of *Relations Between the Four Biquaternion Products*,

$$
\mathrm{Sc}\,\mathcal{A}^{\mathrm{s}}=P_0Q_0-(\mathbf{P},\mathbf{Q}),\qquad
\mathrm{Sc}\,\mathcal{B}^{\mathrm{s}}=P_0Q_0+(\mathbf{P},\mathbf{Q}),
$$

so their sum and their half-difference separate the scalar part of the pair from the vector part, $\mathrm{Sc}\,\mathcal{A}^{\mathrm{s}}+\mathrm{Sc}\,\mathcal{B}^{\mathrm{s}}=2P_0Q_0$ and $\mathrm{Sc}\,\mathcal{A}^{\mathrm{s}}-\mathrm{Sc}\,\mathcal{B}^{\mathrm{s}}=-2(\mathbf{P},\mathbf{Q})$. The symmetric half of $\mathcal{B}$ is scalar, $\mathcal{B}^{\mathrm{s}}=(\mathrm{Sc}\,\mathcal{B}^{\mathrm{s}})e_0$, whereas the symmetric half of $\mathcal{A}$ also carries the two mixed terms $P_0\mathbf{Q}+Q_0\mathbf{P}$, and that is the whole difference between the two bilinear symmetric halves.

The two sesquilinear symmetric halves are not $\mathbb{C}$-bilinear but only $\mathbb{R}$-bilinear, the interchange carrying a conjugate-linear slot into a linear one and back; their scalar parts are the real parts of the two sesquilinear scalar parts of *Relations Between the Four Biquaternion Products*; the vector part of the star-half is purely imaginary, that half being Hermitian, and that of the quaternionic half carries both a real and an imaginary term. The last row is the one that fits into no subspace of the algebra: the symmetrisation of the quaternionic sesquilinear product is not Hermitian, and not skew-Hermitian either.

### The Antisymmetric Halves

Subtracting the two swaps gives the four antisymmetric halves,

| $f$ | $\mathrm{Sc}\,f^{\mathrm{a}}$ | $\mathrm{Vec}\,f^{\mathrm{a}}$ |
|---|---|---|
| $\mathcal{A}=\tilde{P}\tilde{Q}$ | $0$ | $\mathbf{P}\times\mathbf{Q}$ |
| $\mathcal{B}=\tilde{P}^{\natural}\tilde{Q}$ | $0$ | $P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$ |
| $\mathcal{C}=\tilde{P}\tilde{Q}^{*}$ | $i\,\mathrm{Im}\bigl(P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr)$ | $\mathrm{Re}\bigl(-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}\bigr)$ |
| $\mathcal{D}=\tilde{P}^{\natural}\tilde{Q}^{*}$ | $i\,\mathrm{Im}\bigl(P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr)$ | $i\,\mathrm{Im}\bigl(-P_0\overline{\mathbf{Q}}+Q_0\overline{\mathbf{P}}\bigr)+\mathrm{Re}\bigl(\mathbf{P}\times\overline{\mathbf{Q}}\bigr)$ |

The two bilinear antisymmetric halves are pure vectors. The first is the outer product of the sections above, $\mathcal{A}^{\mathrm{a}}=\mathbf{P}\times\mathbf{Q}$, and the second is

$$
\mathcal{B}^{\mathrm{a}}=P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q},
$$

the vector part of $\mathcal{B}$. The two agree on the vector subspace and differ there only by sign, $\mathcal{B}^{\mathrm{a}}=-\mathcal{A}^{\mathrm{a}}$ for pure $\tilde{P},\tilde{Q}$, so on $\mathrm{Vect}(\mathbb{B})$ the two antisymmetric halves are the two signs of the same cross product. Off the subspace the two differ by the two mixed terms, which is the same difference as between the two symmetric halves.

The two sesquilinear antisymmetric halves carry a purely imaginary scalar part; the vector part of the star-half is real, that half being skew-Hermitian, and that of the quaternionic half carries both a real and an imaginary term. The star one lies in $\mathbb{M}_-$; the quaternionic one is confined to no subspace of the six, and neither of the two is produced by a bilinear product.

### The Two Involution Splits

For the two products whose interchange is a conjugation of the value, the split is nothing but the involution split of that value, and this is why their two halves are so simple.

For the $\natural$-product, with $\tilde{X}=\mathcal{B}(\tilde{P},\tilde{Q})$, the identity $\mathcal{B}(\tilde{Q},\tilde{P})=\tilde{X}^{\natural}$ gives

$$
\mathcal{B}^{\mathrm{s}}=\tfrac12\bigl(\tilde{X}+\tilde{X}^{\natural}\bigr),\qquad
\mathcal{B}^{\mathrm{a}}=\tfrac12\bigl(\tilde{X}-\tilde{X}^{\natural}\bigr),
$$

the natural-even and natural-odd parts of the value. The natural conjugation fixes the scalar part and reverses the vector part, so the natural-even part is the scalar part of the value and the natural-odd part is its vector part: **the split of the $\natural$-product is its scalar–vector split**. Hence the symmetric half of $\mathcal{B}$ lies in the scalar line, even in the centre $\mathbb{C}_{\mathbb{B}}$, and the antisymmetric half in the vector subspace $\mathrm{Vect}(\mathbb{B})$ — the statement recorded in *Biquaternions as a Quaternionic Bilinear Algebra over $\mathbb{C}$*.

For the star-product, with $\tilde{X}=\mathcal{C}(\tilde{P},\tilde{Q})$, the identity $\mathcal{C}(\tilde{Q},\tilde{P})=\tilde{X}^{*}$ gives

$$
\mathcal{C}^{\mathrm{s}}=\tfrac12\bigl(\tilde{X}+\tilde{X}^{*}\bigr),\qquad
\mathcal{C}^{\mathrm{a}}=\tfrac12\bigl(\tilde{X}-\tilde{X}^{*}\bigr),
$$

the Hermitian and the skew-Hermitian parts of the value: **the split of the star-product is its Hermitian split**, the split of *Biquaternions as a Sesquilinear Algebra over $\mathbb{C}$*. Hence the symmetric half of $\mathcal{C}$ lies in the Hermitian subspace $\mathbb{M}_+$ and the antisymmetric half in the anti-Hermitian subspace $\mathbb{M}_-$, the two halves that the involution cuts out.

For the two remaining products the value carries no involution that the interchange respects, and the split is a genuine two-way split: the two halves of $\mathcal{A}$ are the outer product of the sections above and the Jordan product of *Biquaternion Jordan Algebra*, and the two halves of $\mathcal{D}$ are new maps, tabulated above and Hermitian in neither half.

### The Four Ranges

Collecting the four splits, the halves fall into the distinguished subspaces as follows.

| $f$ | range of $f^{\mathrm{s}}$ | range of $f^{\mathrm{a}}$ |
|---|---|---|
| $\mathcal{A}$ | $\mathbb{B}$ | $\mathrm{Vect}(\mathbb{B})$ |
| $\mathcal{B}$ | $\mathbb{C}_{\mathbb{B}}$ (the centre) | $\mathrm{Vect}(\mathbb{B})$ |
| $\mathcal{C}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
| $\mathcal{D}$ | neither $\mathbb{M}_+$ nor $\mathbb{M}_-$ | neither $\mathbb{M}_+$ nor $\mathbb{M}_-$ |

The two bilinear products split into a symmetric half and a pure-vector half, and their ranges differ in the symmetric half alone: that of $\mathcal{A}$ fills the whole algebra while that of $\mathcal{B}$ collapses to the centre. The star-product is the one whose two halves are the two halves of the algebra itself, the Hermitian and the anti-Hermitian subspace. The quaternionic sesquilinear product is the one whose split respects no subspace of the six.

## Summary

The product of two biquaternions, defined in *The Four Biquaternion Complex Products*, always splits into a symmetric and an antisymmetric part,

$$
\tilde{P}\tilde{Q} = \tilde{P}\bullet\tilde{Q} + \tilde{P}\wedge\tilde{Q} , \qquad \tilde{P}\bullet\tilde{Q} = \tfrac{1}{2}(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}) , \qquad \tilde{P}\wedge\tilde{Q} = \tfrac{1}{2}(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}) .
$$

The **antisymmetric part** is the complex cross product of the vector parts, $\tilde{P}\wedge\tilde{Q}=\mathbf{P}\times\mathbf{Q}$; it is alternating, pure vector, and vanishes exactly when the vector parts are linearly dependent, which is the commutativity criterion.

The **symmetric part** is $\mathbb{C}$-bilinear and commutative, it agrees with the square on the diagonal, $\tilde{P}\bullet\tilde{P}=\tilde{P}^2$, and it is the polarisation of the square, $\tilde{P}\bullet\tilde{Q}=\tfrac{1}{2}((\tilde{P}+\tilde{Q})^2-\tilde{P}^2-\tilde{Q}^2)$. It makes $\mathbb{B}$ a Jordan algebra; it has the same scalar part as the product, $\mathrm{Sc}(\tilde{P}\bullet\tilde{Q})=\mathrm{Sc}(\tilde{P}\tilde{Q})=P_0Q_0-(\mathbf{P},\mathbf{Q})$; it contains all the powers and hence all the square-root problems; and it closes on the Hermitian subspace, which is a Jordan subalgebra. The antisymmetric part closes on the anti-Hermitian subspace, which is a Lie subalgebra.

Read on the operators, the symmetric part is the balanced multiplication $\tfrac{1}{2}(L_{\tilde{P}}+R_{\tilde{P}})$ and the antisymmetric part the derivation $\tfrac{1}{2}(L_{\tilde{P}}-R_{\tilde{P}})$.

Each of the three other products of *The Four Biquaternion Complex Products* carries the same split, $f=f^{\mathrm{s}}+f^{\mathrm{a}}$ with $f^{\mathrm{s}}=\tfrac12(f(\tilde{P},\tilde{Q})+f(\tilde{Q},\tilde{P}))$ and $f^{\mathrm{a}}=\tfrac12(f(\tilde{P},\tilde{Q})-f(\tilde{Q},\tilde{P}))$. The interchange of the two factors is a conjugation of the value for the two products whose two slots are treated differently, $\mathcal{B}(\tilde{Q},\tilde{P})=\mathcal{B}(\tilde{P},\tilde{Q})^{\natural}$ and $\mathcal{C}(\tilde{Q},\tilde{P})=\mathcal{C}(\tilde{P},\tilde{Q})^{*}$, and a genuine reversal for the two whose slots are treated alike, the complex bilinear product and the quaternionic sesquilinear product. Hence the split of the $\natural$-product is its scalar–vector split, its symmetric half lying in the centre and its antisymmetric half in the vector subspace, and the split of the star-product is its Hermitian split, its symmetric half lying in $\mathbb{M}_+$ and its antisymmetric half in $\mathbb{M}_-$. The two bilinear symmetric halves carry the two bilinear scalar forms, $P_0Q_0\mp(\mathbf{P},\mathbf{Q})$, the two bilinear antisymmetric halves are the two signs of the cross product on the vector subspace, and the two sesquilinear splits are only $\mathbb{R}$-bilinear; the quaternionic sesquilinear product is the one whose two halves respect no subspace of the six.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde{P}\tilde{Q}$ | the biquaternion product, defined in *The Four Biquaternion Complex Products* |
| $\mathcal{A},\mathcal{B},\mathcal{C},\mathcal{D}$ | the four products as binary operations, $\tilde{P}\tilde{Q}$, $\tilde{P}^{\natural}\tilde{Q}$, $\tilde{P}\tilde{Q}^{*}$, $\tilde{P}^{\natural}\tilde{Q}^{*}$ |
| $f^{\mathrm{s}},f^{\mathrm{a}}$ | the symmetric and the antisymmetric half of a binary operation $f$ |
| $\tilde{P}=P_0+\mathbf{P}$ | scalar part plus vector part |
| $\overline{\mathbf{P}}$ | the coefficientwise conjugate of the vector part |
| $(\mathbf{P},\mathbf{Q})$ | the complex bilinear dot product, $\sum_k P_kQ_k$ |
| $\mathbf{P}\times\mathbf{Q}$ | the complex bilinear cross product |
| $\tilde{P}\bullet\tilde{Q}=\tfrac{1}{2}(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P})$ | the symmetric or symmetrised (Jordan) product of $\mathcal{A}$ |
| $\tilde{P}\wedge\tilde{Q}=\tfrac{1}{2}(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P})$ | the antisymmetric part, or outer product, of $\mathcal{A}$ |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{M}_+$, $\mathbb{M}_-$ | the centre, the vector subspace and the Hermitian and anti-Hermitian subspaces |
| $L_{\tilde{P}}$, $R_{\tilde{P}}$ | left and right multiplications by $\tilde{P}$ |
| $\mathrm{Sc}$ | the scalar part of an element |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original product whose two halves are studied here.
- *The Four Biquaternion Complex Products* (`articles_maths/the-four-biquaternion-complex-products.md`), for the four products, their developed forms and their scalar–vector forms.
- *Relations Between the Four Biquaternion Products* (`articles_maths/relations-between-the-four-biquaternion-products.md`), for the conjugate of a product and the two identities $\mathcal{B}(\tilde{Q},\tilde{P})=\mathcal{B}(\tilde{P},\tilde{Q})^{\natural}$ and $\mathcal{C}(\tilde{Q},\tilde{P})=\mathcal{C}(\tilde{P},\tilde{Q})^{*}$.
- *Biquaternions as a Quaternionic Bilinear Algebra over $\mathbb{C}$* and *Biquaternions as a Sesquilinear Algebra over $\mathbb{C}$* (`articles_maths/`), for the scalar–vector split of the $\natural$-product and the Hermitian split of the star-product in their own settings.
