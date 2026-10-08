# __Scalar / Vector decomposition of the Biquaternion Complex Products__

## Introduction

Each of the four products of *The Four Biquaternion Complex Products* is an operation on a pair of biquaternions, and each is read here through its **order symmetry**, the interchange of the two elements of the pair, which separates it into a **symmetric part** and an **antisymmetric part**, the half-sum and the half-difference of the product on the pair $(\tilde{P},\tilde{Q})$ and on the pair $(\tilde{Q},\tilde{P})$. The four sections that follow treat one product each, in the order in which the products are defined: the general plain bilinear product $\tilde{P}\tilde{Q}$, the general quaternionic bilinear product $\tilde{P}^{\natural}\tilde{Q}$, the general plain sesquilinear product $\tilde{P}\tilde{Q}^{*}$ and the general quaternionic sesquilinear product $\tilde{P}^{\natural}\tilde{Q}^{*}$. Each section gives the product, its two parts, the scalar–vector form of each part, what the interchange of the two elements does to the value, and the subspaces the two parts fill. The two parts of the general plain bilinear product are the Jordan and the Lie products, the ones that carry the structures of the algebra, and they are the ones developed at length.

The article assumes the four products from *The Four Biquaternion Complex Products* and the elements, the basis and the conjugations from *Biquaternions as a Vector Space over $\mathbb{C}$*; the product read as the multiplication of an algebra is *Introduction to the General Plain Algebra of Biquaternions*, and with the real scalars *Biquaternions as an Algebra over $\mathbb{R}$*. It defines no form of its own: the scalar parts and the vector parts that occur are those of *The Four Biquaternion Complex Products*, linked in *Relations Between the Four Biquaternion Products*. The behaviour of the general plain bilinear product and of its two parts on each of the six subspaces is tabulated in *The Six Subspaces and the Four Complex Products*; the Lie algebra and the Jordan algebra carried by the antisymmetric and the symmetric part of the general plain bilinear product are *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*; and the operators $L_{\tilde{P}}$ and $R_{\tilde{P}}$ are *The Enveloping Algebra of the Biquaternion Algebra and the Bi-module Structure*.

Throughout, the product of two elements is written by juxtaposition, $\tilde{P}=P_0+\mathbf{P}$ separates the complex scalar part $P_0$ from the complex vector part $\mathbf{P}=P_1e_1+P_2e_2+P_3e_3$, $(\mathbf{P},\mathbf{Q})=\sum_kP_kQ_k$ is the complex bilinear dot product, $\mathbf{P}\times\mathbf{Q}$ the complex bilinear cross product, and $\overline{\mathbf{Q}}$ the coefficientwise conjugate of the vector part.

## The General Plain Bilinear Product

The first product is the general plain bilinear product of *The Four Biquaternion Complex Products*, written by juxtaposition, and it is $\mathbb{C}$-bilinear in both slots. It is the sum of its two parts,

$$
\tilde{P}\tilde{Q}=\tilde{P}\bullet\tilde{Q}+\tilde{P}\wedge\tilde{Q},\qquad
\tilde{P}\bullet\tilde{Q}:=\tfrac12\bigl(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}\bigr),\qquad
\tilde{P}\wedge\tilde{Q}:=\tfrac12\bigl(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}\bigr),
$$

the **symmetrised** (or **Jordan**) product and the **outer** product. Read on the coordinates,

| part | scalar part | vector part | order symmetry |
|---|---|---|---|
| $\tilde{P}\bullet\tilde{Q}$ | $P_0Q_0-(\mathbf{P},\mathbf{Q})$ | $P_0\mathbf{Q}+Q_0\mathbf{P}$ | symmetric, $\tilde{P}\bullet\tilde{Q}=\tilde{Q}\bullet\tilde{P}$ |
| $\tilde{P}\wedge\tilde{Q}$ | $0$ | $\mathbf{P}\times\mathbf{Q}$ | alternating, $\tilde{P}\wedge\tilde{Q}=-\,\tilde{Q}\wedge\tilde{P}$ |

The symmetric part is $\mathbb{C}$-bilinear and commutative and agrees with the square on the diagonal, $\tilde{P}\bullet\tilde{P}=\tilde{P}^2$; the antisymmetric part is $\mathbb{C}$-bilinear, alternating, and pure vector, its scalar part vanishing for every pair.

For this product the interchange of the two elements is a **genuine reversal**: the swapped product $\tilde{Q}\tilde{P}$ is the same two elements in the opposite order, and is not a conjugate of $\tilde{P}\tilde{Q}$, so the split is a genuine two-way split and not the split of a value by an involution. The symmetric part fills the whole algebra and the antisymmetric part the vector subspace $\mathrm{Vect}(\mathbb{B})$.

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

### The Commutativity Criterion

Because the right-hand side of the outer product depends on the vector parts alone, the vanishing of the antisymmetric part is a criterion:

$$
\tilde{P}\tilde{Q} = \tilde{Q}\tilde{P} \quad\Longleftrightarrow\quad \mathbf{P}\times\mathbf{Q} = 0 .
$$

The cross product of two complex vectors vanishes exactly when the vectors are **linearly dependent**, so two biquaternions commute if and only if their vector parts are parallel. In particular a central element $\tilde{P}=P_0e_0$ commutes with every biquaternion, since its vector part is zero; the converse holds, so this recovers the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$ as the set of elements that commute with all of $\mathbb{B}$.

### The Closure of the Two Sectors

The two parts of the product behave differently with respect to the Hermitian split, and the pattern is worth recording here because it is the origin of the Lie and the Jordan structures of the algebra.

| $\tilde{P},\tilde{Q}$ | $\tilde{P}\wedge\tilde{Q}$ | $\tilde{P}\bullet\tilde{Q}$ |
|---|---|---|
| $\mathbb{M}_+$ (Hermitian) | lies in $\mathbb{M}_-$ | lies in $\mathbb{M}_+$ |
| $\mathbb{M}_-$ (anti-Hermitian) | lies in $\mathbb{M}_-$ | lies in $\mathbb{M}_+$ |

That is, the antisymmetric part closes on the anti-Hermitian subspace and carries the Hermitian one into it, so $\mathbb{M}_-$ is a Lie subalgebra; the symmetric part closes on the Hermitian subspace, so $\mathbb{M}_+$ is a Jordan subalgebra. The full subspace-by-subspace table, with the centre, the vector subspace, the quaternion subspace and the anti-quaternion subspace, is *The Six Subspaces and the Four Complex Products*.

### The Operator Reading

The two parts are the balanced and the unbalanced one-sided multiplications. With $L_{\tilde{P}}(\tilde{Q})=\tilde{P}\tilde{Q}$ and $R_{\tilde{P}}(\tilde{Q})=\tilde{Q}\tilde{P}$ the left and right multiplications by $\tilde{P}$,

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

## The General Quaternionic Bilinear Product

The second product is the general quaternionic bilinear product $\tilde{P}^{\natural}\tilde{Q}$ of *The Four Biquaternion Complex Products*, the general plain bilinear product with the first element replaced by its natural conjugate, and it too is $\mathbb{C}$-bilinear in both slots. It is the sum of its two parts,

$$
\tilde{P}^{\natural}\tilde{Q}=\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P}\bigr)+\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P}\bigr),
$$

its symmetric part the first summand and its antisymmetric part the second. Read on the coordinates,

| part | scalar part | vector part | order symmetry |
|---|---|---|---|
| $\tfrac12(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P})$ | $P_0Q_0+(\mathbf{P},\mathbf{Q})$ | $0$ | symmetric |
| $\tfrac12(\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P})$ | $0$ | $P_0\mathbf{Q}-Q_0\mathbf{P}-\mathbf{P}\times\mathbf{Q}$ | alternating |

The symmetric part is central-valued: it is the scalar part of the product read as a central element,

$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P}\bigr) = \bigl(P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr)e_0 = \tfrac12\,\mathrm{Tr}\bigl(\tilde{P}^{\natural}\tilde{Q}\bigr)e_0 ,
$$

the trace form of the product. The antisymmetric part is the vector part of the product, $\tfrac12(\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P})=\mathrm{Vec}(\tilde{P}^{\natural}\tilde{Q})$, and it is a pure vector.

For this product the interchange of the two elements is a **conjugation of the value**,

$$
\tilde{Q}^{\natural}\tilde{P}=\bigl(\tilde{P}^{\natural}\tilde{Q}\bigr)^{\natural},
$$

so the split is the split of the value by the natural involution: the symmetric part is the natural-even part and the antisymmetric part the natural-odd part. The natural conjugation fixes the scalar part and reverses the vector part, so **the split of this product is its scalar–vector split**: the symmetric part lies in the scalar line, even in the centre $\mathbb{C}_{\mathbb{B}}$, and the antisymmetric part in the vector subspace $\mathrm{Vect}(\mathbb{B})$ — the statement recorded in *Introduction to the General Quaternionic Algebra of Biquaternions*.

The two antisymmetric parts of the two bilinear products differ on the vector subspace only by sign: for pure $\tilde{P},\tilde{Q}$ the mixed terms drop and the second is the negative of the first, so on $\mathrm{Vect}(\mathbb{B})$ the two are the two opposite signs of the same cross product. Off the vector subspace the two differ by the two mixed terms $P_0\mathbf{Q}-Q_0\mathbf{P}$, which is the same difference as between the two symmetric parts, the one carrying the mixed terms $P_0\mathbf{Q}+Q_0\mathbf{P}$ and the other not.

## The General Plain Sesquilinear Product

The third product is the general plain sesquilinear product $\tilde{P}\tilde{Q}^{*}$ of *The Four Biquaternion Complex Products*, the general plain bilinear product with the second element replaced by its star-conjugate. It is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second, so it is sesquilinear and not bilinear, and it is the sum of its two parts,

$$
\tilde{P}\tilde{Q}^{*}=\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+\tilde{Q}\tilde{P}^{*}\bigr)+\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}-\tilde{Q}\tilde{P}^{*}\bigr),
$$

its symmetric part the first summand and its antisymmetric part the second. Read on the coordinates,

| part | scalar part | vector part | order symmetry |
|---|---|---|---|
| $\tfrac12(\tilde{P}\tilde{Q}^{*}+\tilde{Q}\tilde{P}^{*})$ | $\mathrm{Re}\bigl(P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr)$ | $i\,\mathrm{Im}\bigl(-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}\bigr)$ | symmetric |
| $\tfrac12(\tilde{P}\tilde{Q}^{*}-\tilde{Q}\tilde{P}^{*})$ | $i\,\mathrm{Im}\bigl(P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})\bigr)$ | $\mathrm{Re}\bigl(-P_0\overline{\mathbf{Q}}+\overline{Q_0}\mathbf{P}-\mathbf{P}\times\overline{\mathbf{Q}}\bigr)$ | alternating |

Both parts are only $\mathbb{R}$-bilinear, not $\mathbb{C}$-bilinear: the interchange of the two elements carries a conjugate-linear slot into a linear one and back, so the sum and the difference of the two values are no longer $\mathbb{C}$-linear in either slot. The scalar parts are the real and the imaginary part of the sesquilinear scalar part $P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})$ of *Relations Between the Four Biquaternion Products*, and the vector part of the symmetric part is purely imaginary. The failure is the failure of this **exchange**, and the other exchange, by the coefficientwise conjugation, splits the same product into its scalar part and its vector part, which are sesquilinear again; the two splits are read side by side in §*The Other Exchange, and the Class It Keeps*.

For this product the interchange of the two elements is a **conjugation of the value**,

$$
\tilde{Q}\tilde{P}^{*}=\bigl(\tilde{P}\tilde{Q}^{*}\bigr)^{*},
$$

so the split is the split of the value by the star-involution: the symmetric part is the Hermitian part and the antisymmetric part the skew-Hermitian part. **The split of the general plain sesquilinear product is its Hermitian split**, the split of *Introduction to the General Plain Sesqualgebra of Biquaternions*: the symmetric part lies in the Hermitian subspace $\mathbb{M}_+$ and the antisymmetric part in the anti-Hermitian subspace $\mathbb{M}_-$, the two parts that the involution cuts out. Of the four products this is the one whose two parts are the two parts of the algebra itself.

Restricted to the Hermitian subspace $\mathbb{M}_+$ the symmetric part is the Hermitian Jordan algebra $J(\mathbb{B})$ of *Jordan Algebras of Sesqualgebras*: the derived operation $\tilde{X}\star\tilde{Y}=\tilde{X}\tilde{Y}^{*}$ of that article coincides there with the associative product, since $\tilde{Y}^{*}=\tilde{Y}$ for a Hermitian $\tilde{Y}$, so the symmetric part of the star-product restricted to $\mathbb{M}_+$ agrees with the Jordan product of the first section and is the same degree-two algebra over $\mathbb{R}$.

## The General Quaternionic Sesquilinear Product

The fourth product is the general quaternionic sesquilinear product $\tilde{P}^{\natural}\tilde{Q}^{*}$ of *The Four Biquaternion Complex Products*, the general plain bilinear product with both elements conjugated. It is sesquilinear, and it is the sum of its two parts,

$$
\tilde{P}^{\natural}\tilde{Q}^{*}=\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}+\tilde{Q}^{\natural}\tilde{P}^{*}\bigr)+\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{\natural}\tilde{P}^{*}\bigr),
$$

its symmetric part the first summand and its antisymmetric part the second. Read on the coordinates,

| part | scalar part | vector part | order symmetry |
|---|---|---|---|
| $\tfrac12(\tilde{P}^{\natural}\tilde{Q}^{*}+\tilde{Q}^{\natural}\tilde{P}^{*})$ | $\mathrm{Re}\bigl(P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr)$ | $-\mathrm{Re}\bigl(P_0\overline{\mathbf{Q}}+Q_0\overline{\mathbf{P}}\bigr)+i\,\mathrm{Im}\bigl(\mathbf{P}\times\overline{\mathbf{Q}}\bigr)$ | symmetric |
| $\tfrac12(\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{\natural}\tilde{P}^{*})$ | $i\,\mathrm{Im}\bigl(P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})\bigr)$ | $i\,\mathrm{Im}\bigl(-P_0\overline{\mathbf{Q}}+Q_0\overline{\mathbf{P}}\bigr)+\mathrm{Re}\bigl(\mathbf{P}\times\overline{\mathbf{Q}}\bigr)$ | alternating |

Both parts are only $\mathbb{R}$-bilinear, as for the general plain sesquilinear product, and their scalar parts are the real and the imaginary part of the sesquilinear scalar part $P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})$ of *Relations Between the Four Biquaternion Products*. Here the other exchange repairs the class too, and its two halves are the symmetrisation of $\tilde{P}^{\natural}$ with $\tilde{Q}^{*}$ and half their commutator, sesquilinear again; the two splits are read side by side in §*The Other Exchange, and the Class It Keeps*.

For this product the interchange of the two elements is a **genuine reversal**: the swapped product is the natural conjugate of the plain product of the conjugated first element with the second,

$$
\tilde{Q}^{\natural}\tilde{P}^{*}=\bigl(\overline{\tilde{P}}\,\tilde{Q}\bigr)^{\natural},
$$

and it is not a conjugate of $\tilde{P}^{\natural}\tilde{Q}^{*}$, so the value carries no involution that the interchange respects and the split is a genuine two-way split.

The two parts are confined to no subspace of the six. For a generic pair the symmetric part lies in neither $\mathbb{M}_+$ nor $\mathbb{M}_-$ — it is not Hermitian, and not skew-Hermitian either, its vector part carrying both a real and an imaginary term — and the antisymmetric part likewise, its vector part carrying both a real and an imaginary term. The product is the only one of the four for which this happens; the symmetrisation nonetheless keeps the Hermitian subspace inside itself, as the symmetrisation of every one of the four products does (*The Six Subspaces and the Four Complex Products* §*The Hermitian Subspace*).

## The Other Exchange, and the Class It Keeps

The split read in the four sections above uses the **plain exchange** $E(f)(\tilde{P},\tilde{Q})=f(\tilde{Q},\tilde{P})$, the swap of the two elements. It is the exchange of the twelve names of *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, and it is the exchange under which the two sesquilinear splits are only $\mathbb{R}$-bilinear.

There is a second exchange, and it keeps the class. Let $c$ be a **conjugation** of the algebra, additive and antilinear, $c(\lambda\tilde{Q})=\overline{\lambda}\,c(\tilde{Q})$, with $c^2=\mathrm{id}$. The **exchange of a product by $c$** is

$$
f^{c}(\tilde{P},\tilde{Q}):=c\bigl(f(\tilde{Q},\tilde{P})\bigr),
$$

and its two halves

$$
f^{c}_{+}:=\tfrac12\bigl(f+f^{c}\bigr),\qquad f^{c}_{-}:=\tfrac12\bigl(f-f^{c}\bigr)
$$

are the **conjugate-symmetric** and the **skew-conjugate-symmetric** part of $f$ (*The Conjugate-Symmetric and Skew-Conjugate-Symmetric Parts of a Sesquilinear Product*). The transposition of the two arguments carries a sesquilinear product to one of the **opposite parity**, $\mathbb{C}$-linear where the product was conjugate-linear; composing with $c$ repairs the parity, so $f^{c}$ is sesquilinear of the same parity as $f$ and $(f^{c})^{c}=f$. **The exchange by a conjugation stays inside the class of sesquilinear products**, and its two halves therefore do too.

On the biquaternions with $(\mathbb{C},\overline{\cdot})$ the coefficientwise conjugation $\overline{\cdot}$ is the conjugation that acts, and the plain sesquilinear product is the case where the two halves are the two parts of its own value:

$$
\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+\overline{\tilde{Q}\tilde{P}^{*}}\bigr)=\mathrm{Sc}\bigl(\tilde{P}\tilde{Q}^{*}\bigr),
\qquad
\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}-\overline{\tilde{Q}\tilde{P}^{*}}\bigr)=\mathrm{Vect}\bigl(\tilde{P}\tilde{Q}^{*}\bigr).
$$

The identity is $\overline{\tilde{Q}\tilde{P}^{*}}=\natural(\tilde{P}\tilde{Q}^{*})$, the natural conjugate of the value; it is **not** the identity $\tilde{P}^{\natural}\tilde{Q}^{*}$, with which it agrees on real elements and disagrees on the complex ones. So the **conjugate-symmetric part of $\tilde{P}\tilde{Q}^{*}$ is its scalar part, a multiple of $e_0$, and the skew-conjugate-symmetric part is its vector part**: centre-valued and vector-valued, in the centre $\mathbb{C}_{\mathbb{B}}$ and in the vector subspace $\mathrm{Vect}(\mathbb{B})$, and **both are sesquilinear over $\mathbb{C}$**. The three presentations of the same element are

$$
\tilde{P}\tilde{Q}^{*}=\underbrace{\mathrm{Sc}\bigl(\tilde{P}\tilde{Q}^{*}\bigr)}_{\text{conjugate-symmetric}}+\underbrace{\mathrm{Vect}\bigl(\tilde{P}\tilde{Q}^{*}\bigr)}_{\text{skew-conjugate-symmetric}}
=\underbrace{\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}+\tilde{Q}\tilde{P}^{*}\bigr)}_{\mathbb{M}_{+}}+\underbrace{\tfrac12\bigl(\tilde{P}\tilde{Q}^{*}-\tilde{Q}\tilde{P}^{*}\bigr)}_{\mathbb{M}_{-}} .
$$

The second is the plain split of §*The General Plain Sesquilinear Product* and the third is the adapted split; they are two splits of one value and not the same split.

For the general quaternionic sesquilinear product the same $c$ applies, with $\overline{\tilde{Q}^{\natural}}=\tilde{Q}^{*}$, and the two adapted halves are

$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}+\tilde{Q}^{*}\tilde{P}^{\natural}\bigr),
\qquad
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{*}\tilde{P}^{\natural}\bigr),
$$

the symmetrisation of $\tilde{P}^{\natural}$ with $\tilde{Q}^{*}$ and half their commutator; both are sesquilinear over $\mathbb{C}$, the skew half is the cross product $\mathbf{P}\times\overline{\mathbf{Q}}$ of the two vectors, and the symmetric half carries the form $K(\tilde{P},\tilde{Q})=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})$ in its scalar part.

**The two candidates for $c$, and why one is used.** On the biquaternions over $(\mathbb{C},\overline{\cdot})$ only the coefficientwise conjugation is available: the star gives $f^{*}(\tilde{P},\tilde{Q})=\tilde{Q}\tilde{P}^{**}=\tilde{P}\tilde{Q}^{*}$, an exchange that returns the product, so its split is trivial; and the natural conjugation ${}^{\natural}$ is $\mathbb{C}$-**linear**, not antilinear, so it is not a conjugation of the datum and its exchange does not keep the class. The choice is therefore forced, and it is $\overline{\cdot}$.

**What the two splits are, side by side.** Under the plain exchange the two parts of the four products are the ones computed above. Under the adapted exchange they are these:

| product | plain exchange $E$ | adapted exchange $E_{\overline{\cdot}}$ |
|---|---|---|
| $\tilde{P}\tilde{Q}$ | Jordan product, outer product ($\mathbb{C}$-bilinear) | no class to keep; the bilinear product is already sesquilinear over the trivially-involuted datum |
| $\tilde{P}^{\natural}\tilde{Q}$ | scalar part, vector part | the same reading is the plain one here |
| $\tilde{P}\tilde{Q}^{*}$ | Hermitian part $\mathbb{M}_{+}$, skew-Hermitian part $\mathbb{M}_{-}$ ($\mathbb{R}$-bilinear) | scalar part, vector part (**sesquilinear**) |
| $\tilde{P}^{\natural}\tilde{Q}^{*}$ | genuine reversal ($\mathbb{R}$-bilinear) | symmetrisation, commutator of $\tilde{P}^{\natural}$ with $\tilde{Q}^{*}$ (**sesquilinear**) |

The two sesquilinear rows are the ones the second exchange repairs, and the repair is the reading of the value: the adapted split of the plain sesquilinear product is the scalar–vector split, which is the shape the general quaternionic bilinear product already had under the plain exchange.

## Summary

Each of the four products of *The Four Biquaternion Complex Products* is the sum of a symmetric part and an antisymmetric part, the half-sum and the half-difference of the product on the pair and on the pair with the two elements exchanged. The interchange of the two elements is a conjugation of the value for the general quaternionic bilinear product and for the general plain sesquilinear product, whose splits are therefore their scalar–vector split and their Hermitian split, and a genuine reversal for the general plain bilinear product and for the general quaternionic sesquilinear product, whose splits are genuine two-way splits.

The symmetric part of the general plain bilinear product is the Jordan product $\tilde{P}\bullet\tilde{Q}=\tfrac12(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P})$: $\mathbb{C}$-bilinear, commutative, agreeing with the square on the diagonal, the polarisation of the square, and making $\mathbb{B}$ a Jordan algebra with $\mathbb{M}_+$ as a Jordan subalgebra. Its antisymmetric part is the outer product $\tilde{P}\wedge\tilde{Q}=\mathbf{P}\times\mathbf{Q}$: alternating, pure vector, its vanishing the commutativity criterion, and closing on $\mathbb{M}_-$ as a Lie subalgebra. Read on the operators, the two are the balanced multiplication $\tfrac12(L_{\tilde{P}}+R_{\tilde{P}})$ and the derivation $\tfrac12(L_{\tilde{P}}-R_{\tilde{P}})$.

The symmetric parts of the two bilinear products carry the two bilinear scalar forms $P_0Q_0\mp(\mathbf{P},\mathbf{Q})$, the first filling the whole algebra and the second collapsing to the centre; the two antisymmetric parts are the two signs of the same cross product on the vector subspace, and off it they differ by the two mixed terms. The general plain sesquilinear product is the one whose two parts are the two parts of the algebra itself, the Hermitian and the anti-Hermitian subspace. The general quaternionic sesquilinear product is the one whose two parts are confined to no subspace of the six. The two sesquilinear splits are only $\mathbb{R}$-bilinear.

That is the plain exchange. Under the exchange by the coefficientwise conjugation the two sesquilinear products split again, and that second split keeps the class: the plain sesquilinear product splits into its scalar part, a multiple of $e_0$, and its vector part, and the general quaternionic sesquilinear product into the symmetrisation of $\tilde{P}^{\natural}$ with $\tilde{Q}^{*}$ and half their commutator. The four halves are sesquilinear over $\mathbb{C}$, and **they are the four operations the twelve names carry**, $\mathrm{SPS}$, $\mathrm{APS}$, $\mathrm{SQS}$ and $\mathrm{AQS}$: the split that keeps the class is the one the twelve belong to, and the plain split is the other, whose halves are the operations of *The Sesquilinear Symmetrised Product* and *The Sesquilinear Commutator*. Both are read in §*The Other Exchange, and the Class It Keeps* and in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Method of the Decomposition*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde{P}\tilde{Q}$, $\tilde{P}^{\natural}\tilde{Q}$, $\tilde{P}\tilde{Q}^{*}$, $\tilde{P}^{\natural}\tilde{Q}^{*}$ | the four products, defined in *The Four Biquaternion Complex Products* |
| $f^{c}(\tilde{P},\tilde{Q})=c(f(\tilde{Q},\tilde{P}))$ | the exchange of a product by a conjugation $c$, and its two halves $f^{c}_{\pm}$ |
| $\tilde{P}=P_0+\mathbf{P}$ | scalar part plus vector part |
| $\overline{\mathbf{P}}$ | the coefficientwise conjugate of the vector part |
| $(\mathbf{P},\mathbf{Q})$ | the complex bilinear dot product, $\sum_k P_kQ_k$ |
| $\mathbf{P}\times\mathbf{Q}$ | the complex bilinear cross product |
| $\tilde{P}\bullet\tilde{Q}=\tfrac{1}{2}(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P})$ | the symmetric (Jordan, symmetrised) part of $\tilde{P}\tilde{Q}$ |
| $\tilde{P}\wedge\tilde{Q}=\tfrac{1}{2}(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P})$ | the antisymmetric part, or outer product, of $\tilde{P}\tilde{Q}$ |
| $\tfrac12(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P})$ | the symmetric part of $\tilde{P}^{\natural}\tilde{Q}$, central |
| $\tfrac12(\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P})$ | the antisymmetric part of $\tilde{P}^{\natural}\tilde{Q}$ |
| $\tfrac12(\tilde{P}\tilde{Q}^{*}+\tilde{Q}\tilde{P}^{*})$ | the symmetric part of $\tilde{P}\tilde{Q}^{*}$, Hermitian |
| $\tfrac12(\tilde{P}\tilde{Q}^{*}-\tilde{Q}\tilde{P}^{*})$ | the antisymmetric part of $\tilde{P}\tilde{Q}^{*}$, skew-Hermitian |
| $\tfrac12(\tilde{P}^{\natural}\tilde{Q}^{*}+\tilde{Q}^{\natural}\tilde{P}^{*})$ | the symmetric part of $\tilde{P}^{\natural}\tilde{Q}^{*}$ |
| $\tfrac12(\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{\natural}\tilde{P}^{*})$ | the antisymmetric part of $\tilde{P}^{\natural}\tilde{Q}^{*}$ |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{M}_+$, $\mathbb{M}_-$ | the centre, the vector subspace and the Hermitian and anti-Hermitian subspaces |
| $L_{\tilde{P}}$, $R_{\tilde{P}}$ | left and right multiplications by $\tilde{P}$ |
| $\mathrm{Sc}$ | the scalar part of an element |
| $\mathrm{Vec}$ | the vector part of an element |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original product whose two parts are studied here.
- *The Four Biquaternion Complex Products* (`articles_maths/the-four-biquaternion-complex-products.md`), for the four products, their developed forms and their scalar–vector forms.
- *Relations Between the Four Biquaternion Products* (`articles_maths/relations-between-the-four-biquaternion-products.md`), for the conjugate of a product and the two identities $\tilde{Q}^{\natural}\tilde{P}=(\tilde{P}^{\natural}\tilde{Q})^{\natural}$ and $\tilde{Q}\tilde{P}^{*}=(\tilde{P}\tilde{Q}^{*})^{*}$.
- *Introduction to the General Quaternionic Algebra of Biquaternions* and *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/`), for the scalar–vector split of the $\natural$-product and the Hermitian split of the star-product in their own settings.
