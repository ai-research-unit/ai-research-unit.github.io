
# __Introduction to the Quaternioid Algebraic Structures__

## Introduction

The real quaternions $\mathbb{H}$ are a division algebra, and that algebra is the subject of *Quaternion Algebra* and *Introduction to the General Plain Algebra of Quaternions*. The same four-dimensional real carrier, with its single involution ${}^{\natural}$, carries five further algebras beside the plain one: the **general quaternionic algebra**, the two symmetric algebras built from the slot exchange, and the two antisymmetric ones. This category gathers those six structures, and this article states what they are and how they are counted.

The counting principle is the one of the whole synthetic part of the corpus: from one product and one involution the space generates its companions by the two operations that are always available, the exchange of the two slots and the adjunction of the involution to a slot. For $\mathbb{H}$ there are **two general products** and, under the slot exchange, **six products**; the six products are the multiplications of six algebras on the same carrier. That the count stops at two general products, and not four, is a feature of the quaternion layer: the base field is $\mathbb{R}$, so there is only one involution ${}^{\natural}$ and no coefficient conjugation, and the two slots offer the two settings $(\mathrm{id},\mathrm{id})$ and $({}^{\natural},\mathrm{id})$ alone.

**Conventions.** $\tilde p = p_0e_0+\vec p = \sum_{\mu=0}^{3}p_\mu e_\mu$ is a general quaternion, with $p_\mu\in\mathbb{R}$ and $\vec p = \sum_{k=1}^{3}p_ke_k$ the vector part; $e_0$ is the unit; ${}^{\natural}$ is the quaternion conjugation, $e_k^{\natural} = -e_k$ on the imaginary units, $e_0^{\natural} = e_0$; $(\vec p,\vec q) = \sum_k p_kq_k$ and $\vec p\times\vec q$ are the real dot and cross products. The plain bilinear product is written $\tilde p\tilde q$, the general quaternionic product $\tilde p^{\natural}\tilde q$. The tilde and the mark ${}^{\natural}$ are those of *Conventions in Mathematics*.

## The Two General Products

**Definition.** The **two general products** of the quaternion space are the **general plain bilinear** product and the **general quaternionic bilinear** product,

$$
\tilde p\tilde q = \bigl(p_0q_0 - (\vec p,\vec q)\bigr) + p_0\vec q + q_0\vec p + \vec p\times\vec q, \qquad
\tilde p^{\natural}\tilde q = \bigl(p_0q_0 + (\vec p,\vec q)\bigr) + p_0\vec q - q_0\vec p - \vec p\times\vec q .
$$

**Theorem.** Both products are $\mathbb{R}$-bilinear, and the second is the first with the first factor conjugated by ${}^{\natural}$; their sum and difference separate the scalar part of the first factor from its vector part,

$$
\tilde p\tilde q + \tilde p^{\natural}\tilde q = 2p_0\tilde q, \qquad\qquad \tilde p\tilde q - \tilde p^{\natural}\tilde q = 2\vec p\,\tilde q .
$$

The plain product makes $\mathbb{H}$ an associative division algebra with the two-sided unit $e_0$; the quaternionic product makes it a left-unital, non-associative algebra. The two have the same idempotents, $0$ and $e_0$, and neither has a zero divisor.

**Proof.** The two coordinate formulas are read from the multiplication table of $\mathbb{H}$; the second is the first with $\tilde p$ replaced by $\tilde p^{\natural} = p_0e_0-\vec p$, which flips the signs of $(\vec p,\vec q)$, of $q_0\vec p$ and of $\vec p\times\vec q$. Adding and subtracting the two displays kills the vector terms of the first factor, leaving $2p_0\tilde q$ and $2\vec p\tilde q$. Associativity, the unit and the division property of the plain product are *Introduction to the General Plain Algebra of Quaternions*; the left unit of the quaternionic product is $e_0$, since $e_0^{\natural}\tilde q = \tilde q$, and it is not a right unit, since $\tilde q^{\natural}e_0 = \tilde q^{\natural}$. The two products and their property table are *The Two General Products of the Quaternioid $\mathbb{R}$ Space* and *Relations Between the Two General Products*.

**Remark (why only two).** A general product is $\tilde p^{\,a}\tilde q^{\,b}$ with $a,b\in\{\mathrm{id},{}^{\natural}\}$ in the two slots, but the base field is $\mathbb{R}$: there is no coefficient conjugation, so the second slot offers no independent choice, and the two settings $({}^{\natural},{}^{\natural})$ and $(\mathrm{id},{}^{\natural})$ coincide with the two already listed after absorbing ${}^{\natural}$ into the product's argument. The count is *The Two General Products and the Reason There Are Only Two*.

## The Six Products and the Six Structures

**Definition.** The **six products** are the two general products together with their four halves under the slot exchange:

$$
\tilde p\bullet\tilde q = \bigl(p_0q_0 - (\vec p,\vec q)\bigr) + p_0\vec q + q_0\vec p, \qquad N(\tilde p,\tilde q)e_0 = \bigl(p_0q_0 + (\vec p,\vec q)\bigr)e_0,
$$

$$
\tilde p\wedge\tilde q = \vec p\times\vec q, \qquad\qquad \tilde p\wedge^{\natural}\tilde q = p_0\vec q - q_0\vec p - \vec p\times\vec q,
$$

the **Jordan product**, the **quaternion form as a product**, the **cross product** and the **quaternionic cross product**. The reconstruction is

$$
\tilde p\tilde q = \tilde p\bullet\tilde q + \tilde p\wedge\tilde q, \qquad\qquad \tilde p^{\natural}\tilde q = N(\tilde p,\tilde q)e_0 + \tilde p\wedge^{\natural}\tilde q .
$$

**Proof.** The symmetrisation $\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ of the plain product keeps the symmetric terms and the antisymmetrisation $\tfrac12(\tilde p\tilde q-\tilde q\tilde p)$ keeps $\vec p\times\vec q$; the same split on the quaternionic product gives the scalar form and the quaternionic cross product. The two reconstructions are the definitions read together, and at the two equal arguments the antisymmetric halves vanish, so $\tilde p\bullet\tilde p = \tilde p^2$ and $\tilde p^{\natural}\tilde p = N(\tilde p)e_0$. The six products are *The 6 Products of the Quaternioid Real Space*.

**Definition.** The **six algebraic structures** on the common carrier are the algebras of the six products:

| Structure | Product | Nature |
|---|---|---|
| general plain algebra (GPA) | $\tilde p\tilde q$ | associative unital division algebra |
| general quaternionic algebra (GQA) | $\tilde p^{\natural}\tilde q$ | non-associative, left-unital |
| symmetric plain algebra (SPA) | $\tilde p\bullet\tilde q$ | commutative Jordan algebra |
| symmetric quaternionic algebra (SQA) | $N(\tilde p,\tilde q)e_0$ | commutative scalar-valued rule |
| antisymmetric plain algebra (APA) | $\tilde p\wedge\tilde q$ | Lie algebra |
| antisymmetric quaternionic algebra (AQA) | $\tilde p\wedge^{\natural}\tilde q$ | alternating, non-Lie rule |

**Theorem (the two laws of the table).** Among the six, **the general plain algebra is the only associative one** and **the antisymmetric plain algebra is the only one satisfying the Jacobi identity**; the other four fail the corresponding law. The symmetric products are commutative, flexible and power-associative; the antisymmetric products are alternating, flexible and power-associative, with cubes zero; the general quaternionic product has a left unit alone and fails associativity, commutativity, flexibility and power-associativity.

**Proof.** Associativity of GPA is that of $\mathbb{H}$; the associator of GQA, the failure of the Jacobi identity for AQA and the laws of the remaining products are computed in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, from which the table is read; the algebraicity of the classification is *Algebras: A General Introduction* and *Symmetric Algebras* and *Anti-symmetric Algebras*.

## The Two Forms and the Two Algebraic Norms

**Theorem.** The two general products carry **two bilinear forms**, the plain form and the quaternion form,

$$
B(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p\tilde q) = p_0q_0 - (\vec p,\vec q), \qquad N(\tilde p,\tilde q) = \mathrm{Sc}(\tilde p^{\natural}\tilde q) = p_0q_0 + (\vec p,\vec q),
$$

symmetric and nondegenerate, of Gram matrices $\operatorname{diag}(1,-1,-1,-1)$ and $\mathrm I_4$ in the basis $e_0,e_1,e_2,e_3$, of signatures $(1,3)$ and $(4,0)$, differing by twice the dot product of the vector parts.

**Proof.** The scalar part of a product of basis elements is $\mathrm{Sc}(e_\mu e_\nu) = \varepsilon_\mu\delta_{\mu\nu}$ with $\varepsilon = (1,-1,-1,-1)$, and $\mathrm{Sc}(e_\mu^{\natural}e_\nu) = \delta_{\mu\nu}$; the two coordinate formulas follow by bilinearity, the Gram matrices are read from them, and the signatures are the counts of positive and negative diagonal entries. The forms are *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*.

**Theorem.** The two algebraic norms are the values at the two equal arguments, $N_P(\tilde p) = \tilde p^2$ and $N_Q(\tilde p) = \tilde p^{\natural}\tilde p = \lvert\tilde p\rvert^2e_0$; the first is indefinite and **not** multiplicative, the second is positive definite, zero only at the origin, and multiplicative, $N_Q(\tilde p\tilde q) = N_Q(\tilde p)N_Q(\tilde q)$. The criterion of invertibility is the second's: $\tilde p$ is invertible exactly when $N_Q(\tilde p)\neq0$, with $\tilde p^{-1} = \tilde p^{\natural}/\lvert\tilde p\rvert^2$.

**Proof.** $N_P(\tilde p) = (p_0^2-\lvert\vec p\rvert^2)e_0+2p_0\vec p$ takes $e_0$ at $e_0$ and $-e_0$ at $e_1$, hence is indefinite; $N_P(e_1e_2) = N_P(e_3) = -e_0$ against $N_P(e_1)N_P(e_2) = e_0$, so it is not multiplicative. $N_Q(\tilde p) = (p_0^2+\lvert\vec p\rvert^2)e_0$ is $\lvert\tilde p\rvert^2e_0$ with $\lvert\tilde p\rvert^2>0$ for $\tilde p\neq0$, and $N_Q(\tilde p\tilde q) = \lvert\tilde p\tilde q\rvert^2 e_0 = \lvert\tilde p\rvert^2\lvert\tilde q\rvert^2 e_0$ by multiplicativity of the quaternion norm. The inverse formula is $(\tilde p^{\natural}/N_Q(\tilde p))$, which is the division property of $\mathbb{H}$. The two algebraic norms are *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*.

**Corollary.** The quaternion layer is **not** the biquaternion layer collapsed: for $\mathbb{H}$ the two forms are $B$ and $N$ and the two algebraic norms are $N_P$ and $N_Q$, whereas the biquaternion $\mathbb{C}$-space carries four forms and four algebraic norms, one for each setting of the two slots. The reason is the base field: over $\mathbb{C}$ the coefficient conjugation is a second involution and doubles the count.

## The General and the Higher Structures

**Remark (the $\mathbb{C}$-readings).** The same carrier read over $\mathbb{C}$ is the biquaternions $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$; the passage from the six structures over $\mathbb{R}$ to the twelve over $\mathbb{C}$ is the complexification, and it is *The Realification and the Effect of the Change of Scalars* and the *Biquaternionoid Algebraic Structures* category. This category keeps the $\mathbb{R}$-base clean: the structures over $\mathbb{R}$ are the $\mathrm{GPA},\dots,\mathrm{AQA}$ of the table above, and their $\mathbb{C}$-companions belong to the biquaternion layer.

**Remark (the ternary product).** The general quaternionic product $\tilde p^{\natural}\tilde q$ is non-associative, and its associator is not confined as in the complex case: the ternary product of the quaternionic product has a non-vanishing associator defect, treated in *The Associator and the Ternary Product of the Quaternionic Product*. This is the non-commutative counterpart of the flat ternary product of the complexoid, and it is the reason the correction terms of the Jordan triple identity are essential here.

## Summary

The quaternion space $\mathbb{H}$, of real dimension four and with the single involution ${}^{\natural}$, carries two general products — the plain bilinear $\tilde p\tilde q$ and the quaternionic bilinear $\tilde p^{\natural}\tilde q$ — and, under the exchange of the two slots, six products and six algebraic structures on the same carrier. The count stops at two general products because the base field is $\mathbb{R}$: there is one involution and no coefficient conjugation, so the second slot offers no independent choice. The six structures are the general plain algebra (associative, unital, division), the general quaternionic algebra (left-unital, non-associative), the symmetric plain and symmetric quaternionic algebras, and the antisymmetric plain and antisymmetric quaternionic algebras; the general plain algebra is the only associative one, and the antisymmetric plain algebra the only one satisfying Jacobi.

The two general products carry two forms, $B$ of Gram $\operatorname{diag}(1,-1,-1,-1)$ and signature $(1,3)$, and $N$ of Gram $\mathrm I_4$ and signature $(4,0)$, and two algebraic norms $N_P(\tilde p) = \tilde p^2$, indefinite and not multiplicative, and $N_Q(\tilde p) = \lvert\tilde p\rvert^2e_0$, definite and multiplicative, the latter being the criterion of invertibility. The complexification of the carrier is the biquaternions, whose four forms and four algebraic norms double the two here; that doubling is the content of the biquaternion layer, not of this one.

| Structure | Product | Form | Algebraic norm |
|---|---|---|---|
| GPA | $\tilde p\tilde q$ | $B(\tilde p,\tilde q) = p_0q_0-(\vec p,\vec q)$ | $N_P(\tilde p) = \tilde p^2$, indefinite |
| GQA | $\tilde p^{\natural}\tilde q$ | $N(\tilde p,\tilde q) = p_0q_0+(\vec p,\vec q)$ | $N_Q(\tilde p) = \lvert\tilde p\rvert^2e_0$, definite |
| SPA | $\tilde p\bullet\tilde q$ | $B$ | — (indefinite half) |
| SQA | $N(\tilde p,\tilde q)e_0$ | $N$ | $N$ itself |
| APA | $\tilde p\wedge\tilde q$ | vanishing (antisymmetric) | vanishing |
| AQA | $\tilde p\wedge^{\natural}\tilde q$ | vanishing (antisymmetric) | vanishing |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p = p_0e_0+\vec p$ | general quaternion, $p_\mu\in\mathbb{R}$ |
| $\tilde p^{\natural}$ | quaternion conjugation, $e_k^{\natural} = -e_k$ |
| $\tilde p\tilde q$, $\tilde p^{\natural}\tilde q$ | the two general products |
| $\tilde p\bullet\tilde q$, $N(\tilde p,\tilde q)e_0$, $\tilde p\wedge\tilde q$, $\tilde p\wedge^{\natural}\tilde q$ | the four halves |
| GPA, GQA, SPA, SQA, APA, AQA | the six structures |
| $B(\tilde p,\tilde q)$, $N(\tilde p,\tilde q)$ | the plain form and the quaternion form |
| $N_P(\tilde p)$, $N_Q(\tilde p)$ | the plain and quaternion algebraic norms |
| $\operatorname{diag}(1,-1,-1,-1)$, $\mathrm I_4$ | Gram matrices of $B$ and $N$ |

## Further Reading

- *Introduction to the General Plain Algebra of Quaternions* (`articles_maths/introduction-to-the-quaternion-algebra.md`), for the algebra $\mathbb{H}$ itself, its basis rules, its centre and its presentation.
- *The Two General Products of the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-two-general-products-of-the-quaternioid-r-space.md`), *Relations Between the Two General Products* (`articles_maths/relations-between-the-two-general-products.md`) and *Comparison Between the Two General Products* (`articles_maths/comparison-between-the-two-general-products.md`), for the two products and their comparison.
- *The 6 Products of the Quaternioid Real Space* (`articles_maths/the-6-products-of-the-quaternioid-real-space.md`) and *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-algebraic-structures-over-the-quaternioid-r-space.md`), for the six products and the six named structures.
- *The 2 Forms over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternioid-r-space.md`) and *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-2-algebraic-norms-over-the-quaternioid-r-space.md`), for the two forms and the two algebraic norms.
- *The Associator and the Ternary Product of the Quaternionic Product* (`articles_maths/the-associator-and-the-ternary-product-of-the-quaternionic-product-of-quaternioid.md`), for the non-commutative ternary product.
- *Introduction to the General Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-general-quaternionic-algebra-of-quaternioid.md`), *Introduction to the Symmetric Plain Algebra of Quaternions* (`articles_maths/introduction-to-the-symmetric-plain-algebra-of-quaternioid.md`) and their companions, for the individual structures.
- *Algebras: A General Introduction*, *Symmetric Algebras*, *Anti-symmetric Algebras* and *Sesqualgebras*, for the general theory of the algebras the six structures instantiate.
