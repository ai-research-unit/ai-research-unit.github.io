# __Biquaternion Jordan Algebra__

## Introduction

Every product of two biquaternions splits into a symmetric and an antisymmetric half, and each half carries a structure of its own. The antisymmetric half is half the commutator, read in *Biquaternion Lie Algebra*; the symmetric half is the **symmetrised product**, and with it the biquaternion algebra is a commutative **Jordan algebra**. This article reads that second structure: the Jordan product, the Jordan identity, the trace form, the idempotents and the Peirce decomposition, the Hermitian subspace as a Jordan subalgebra, and the way the two halves of the product divide the distinguished subspaces between them. The symmetrisation is carried out for all four products of *The Four Biquaternion Complex Products*, and only the complex bilinear one is a Jordan product; the three others are read in §*The Symmetrisation of the Four Products*.

The product is from *The Four Biquaternion Complex Products* and its four symmetrisations, together with the two halves of each, from *Decomposition of the Multiplication*; the general theory is *Jordan Algebras*, and the special case used throughout is its §*The Symmetrisation of an Associative Algebra*. The algebra, its basis and its two idempotents are from *Biquaternions as a Vector Space over $\mathbb{C}$*, *Biquaternions as a Bilinear Algebra over $\mathbb{C}$* and *Biquaternion Idempotents and Projections*; the subspace-by-subspace behaviour is tabulated in *Biquaternion Relations Between Subspaces*; and the other halves, the four brackets, are *Biquaternion Lie Algebra*.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. Throughout, a biquaternion is written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^3 Q_k e_k$, and $(\mathbf{P},\mathbf{Q})=\sum_k P_kQ_k$ is the complex bilinear dot product of the vector parts.

---

## The Jordan Product

### Definition

The **symmetric part** of the product, also called the **symmetrised product** or the **Jordan product**, is

$$
\tilde{P}\bullet\tilde{Q} := \tfrac{1}{2}\bigl(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}\bigr).
$$

It is $\mathbb{C}$-bilinear and commutative, and it agrees with the ordinary square on the diagonal:

$$
\tilde{P}\bullet\tilde{Q} = \tilde{Q}\bullet\tilde{P} , \qquad \tilde{P}\bullet\tilde{P} = \tilde{P}^2 .
$$

In scalar–vector notation the antisymmetric terms of the product cancel and the mixed terms double:

$$
\tilde{P}\bullet\tilde{Q} = \bigl(P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr) + P_0\mathbf{Q} + Q_0\mathbf{P} .
$$

The full product is the sum of its two halves,

$$
\tilde{P}\tilde{Q} = \tilde{P}\bullet\tilde{Q} + \tilde{P}\wedge\tilde{Q} , \qquad \tilde{P}\wedge\tilde{Q} = \tfrac{1}{2}\bigl(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}\bigr),
$$

the second summand being the **outer product** of *Decomposition of the Multiplication*, which is the commutator up to the factor $2$ and is read in *Biquaternion Lie Algebra*.

### The Polarisation of the Square

**Proposition.** The Jordan product is the polarisation of the square:

$$
\tilde{P}\bullet\tilde{Q} = \tfrac{1}{2}\Bigl((\tilde{P}+\tilde{Q})^2 - \tilde{P}^2 - \tilde{Q}^2\Bigr).
$$

**Proof.** Expand $(\tilde{P}+\tilde{Q})^2=\tilde{P}^2+\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}+\tilde{Q}^2$ by bilinearity and halve.

The square of a biquaternion is the scalar–vector expression

$$
\tilde{P}^2 = \bigl(P_0^2-(\mathbf{P},\mathbf{P})\bigr) + 2P_0\mathbf{P} ,
$$

a scalar plus a scalar multiple of $\mathbf{P}$, so the square carries no cross-product term; every square-root problem is therefore a problem in the Jordan product alone, as *Biquaternion Square Roots of a General Element* reads it.

## The Jordan Algebra

**Theorem.** With the product $\bullet$ the biquaternion algebra is a commutative Jordan algebra: $\bullet$ is commutative and $\mathbb{C}$-bilinear, and the Jordan identity

$$
(\tilde{P}\bullet\tilde{Q})\bullet\tilde{P}^2 = \tilde{P}\bullet\bigl(\tilde{Q}\bullet\tilde{P}^2\bigr)
$$

holds for all $\tilde{P},\tilde{Q}\in\mathbb{B}$.

**Proof.** The algebra $\mathbb{B}$ is associative, and the symmetrisation $a\bullet b=\tfrac12(ab+ba)$ of any associative algebra satisfies the Jordan identity, by the associativity of the underlying product (*Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*). Commutativity and bilinearity are built into the definition. Verified on random pairs.

A Jordan algebra obtained by symmetrising an associative algebra is called **special**, and the associative algebra is its **envelope**. The special Jordan algebra here is $\mathbb{B}$ with $\bullet$, and its envelope is the associative algebra $\mathbb{B}$ itself, so the envelope is finite-dimensional and four-dimensional over $\mathbb{C}$. No exceptional Jordan algebra arises: the exceptional ones have no such envelope, whereas every biquaternion computation is an ordinary associative computation in the envelope followed by symmetrisation.

### Powers and the Subalgebra Generated by One Element

A Jordan algebra is power-associative, so every power $\tilde{Q}^n$ is well defined without brackets, $\tilde{Q}^{n+1}=\tilde{Q}\bullet\tilde{Q}^n$, and the powers commute. The subalgebra generated by a single element $\tilde{Q}$ is the span of its powers,

$$
\mathbb{C}[\tilde{Q}] = \mathrm{span}_{\mathbb{C}}\{\tilde{Q},\tilde{Q}^2,\tilde{Q}^3,\dots\},
$$

which is commutative and closed under $\bullet$.

## The Trace Form

**Proposition.** The trace of the Jordan product is the trace of the product, and it is the symmetric $\mathbb{C}$-bilinear function

$$
\mathrm{Tr}\bigl(\tilde{P}\bullet\tilde{Q}\bigr) = \mathrm{Tr}\bigl(\tilde{P}\tilde{Q}\bigr) = 2\bigl(P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr).
$$

**Proof.** The trace is linear and vanishes on the outer product, $\mathrm{Tr}(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P})=0$, so the trace of the two halves is the same; the trace of a product is twice its scalar part, and the scalar part of $\tilde{P}\tilde{Q}$ is $P_0Q_0-(\mathbf{P},\mathbf{Q})$.

**Proposition (the trace form is associative).** For all $\tilde{P},\tilde{Q},\tilde{R}\in\mathbb{B}$,

$$
\mathrm{Tr}\Bigl(\bigl(\tilde{P}\bullet\tilde{Q}\bigr)\bullet\tilde{R}\Bigr) = \mathrm{Tr}\Bigl(\tilde{P}\bullet\bigl(\tilde{Q}\bullet\tilde{R}\bigr)\Bigr).
$$

**Proof.** Expanding both products by the definition gives $\tfrac14$ times the sum of four terms each; the two sums are $\mathrm{Tr}(\tilde{P}\tilde{Q}\tilde{R})+\mathrm{Tr}(\tilde{Q}\tilde{P}\tilde{R})+\mathrm{Tr}(\tilde{R}\tilde{P}\tilde{Q})+\mathrm{Tr}(\tilde{R}\tilde{Q}\tilde{P})$ and $\mathrm{Tr}(\tilde{P}\tilde{Q}\tilde{R})+\mathrm{Tr}(\tilde{P}\tilde{R}\tilde{Q})+\mathrm{Tr}(\tilde{Q}\tilde{R}\tilde{P})+\mathrm{Tr}(\tilde{R}\tilde{Q}\tilde{P})$, and the two agree term by term under the cyclic invariance $\mathrm{Tr}(XYZ)=\mathrm{Tr}(ZXY)$ of the trace.

The trace form is the symmetric bilinear function attached to the Jordan algebra. Read as a form rather than as a trace it is the object of *Biquaternion Norm and Invertibility*; the norm, its polar form and the topology they carry are not used here, and only the algebraic identity $\mathrm{Tr}(\tilde{P}\bullet\tilde{Q})=\mathrm{Tr}(\tilde{P}\tilde{Q})$ is needed below.

## Idempotents and the Peirce Decomposition

### Jordan Orthogonality

An **idempotent** of the Jordan algebra is an element $\tilde{E}$ with $\tilde{E}\bullet\tilde{E}=\tilde{E}$, and two idempotents are **Jordan orthogonal** when $\tilde{E}\bullet\tilde{F}=0$. The two idempotents of *Biquaternion Idempotents and Projections*,

$$
\tilde{\Pi}_1=\tfrac12(e_0+ie_3), \qquad \tilde{\Pi}_2=\tfrac12(e_0-ie_3),
$$

are idempotents of the Jordan algebra, they are Jordan orthogonal, and they sum to the unit:

$$
\tilde{\Pi}_1\bullet\tilde{\Pi}_2=0 , \qquad \tilde{\Pi}_1+\tilde{\Pi}_2=e_0 .
$$

A family of pairwise Jordan-orthogonal idempotents summing to the unit is **complete**, and the number of its members is the **degree** of the Jordan algebra. The two idempotents above are such a family, and a third can never be added: in the envelope $\mathbb{B}\cong M_2(\mathbb{C})$ a complete family of orthogonal idempotents has at most two members, their images being complementary subspaces of the defining two-dimensional module $S$ of *Modules over the Biquaternion Algebra*. The biquaternion Jordan algebra therefore has **degree two**.

### The Peirce Spaces

For an idempotent $\tilde{E}$ let $\mathrm{J}_\lambda(\tilde{E})$ be the $\lambda$-eigenspace of the multiplication operator $\tilde{X}\mapsto\tilde{E}\bullet\tilde{X}$. In a Jordan algebra this operator has the eigenvalues $1,\tfrac12,0$ and the algebra splits as

$$
\mathbb{B} = \mathrm{J}_1(\tilde{E}) \oplus \mathrm{J}_{1/2}(\tilde{E}) \oplus \mathrm{J}_0(\tilde{E}),
$$

the **Peirce decomposition** (*Jordan Algebras*, §*The Peirce Spaces*). For $\tilde{E}=\tilde{\Pi}_1$ the three spaces are computed from the products alone.

**Proposition.** For $\tilde{E}=\tilde{\Pi}_1$ the Peirce spaces are

| Peirce space | elements | dimension over $\mathbb{C}$ |
|---|---|---|
| $\mathrm{J}_1(\tilde{\Pi}_1)$ | $\mathbb{C}\tilde{\Pi}_1$ | $1$ |
| $\mathrm{J}_{1/2}(\tilde{\Pi}_1)$ | $\mathrm{span}_{\mathbb{C}}\{e_1,e_2\}$ | $2$ |
| $\mathrm{J}_0(\tilde{\Pi}_1)$ | $\mathbb{C}\tilde{\Pi}_2$ | $1$ |

**Proof.** The relations $\tilde{\Pi}_1\bullet\tilde{\Pi}_1=\tilde{\Pi}_1$ and $\tilde{\Pi}_1\bullet\tilde{\Pi}_2=0$ put $\tilde{\Pi}_1$ in the first space and $\tilde{\Pi}_2$ in the third. For the vector units, $\tilde{\Pi}_1\bullet e_1=\tfrac12 e_1$ and $\tilde{\Pi}_1\bullet e_2=\tfrac12 e_2$, so $e_1$ and $e_2$ span the middle space. The three spaces are independent and their dimensions sum to $1+2+1=4=\dim_{\mathbb{C}}\mathbb{B}$, so they exhaust the algebra. Verified on the basis.

The dimensions $1+2+1$ are the Jordan counterpart of the two minimal left ideals of *Biquaternion Ideals and Peirce Decomposition*: the middle space is two-dimensional there as well, and the two one-dimensional ends are the two idempotents.

## The Hermitian Subspace as a Jordan Subalgebra

The Hermitian subspace $\mathbb{M}_+$ is closed under the Jordan product. If $\tilde{P},\tilde{Q}\in\mathbb{M}_+$ then $\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}$ is again Hermitian, so $\tilde{P}\bullet\tilde{Q}\in\mathbb{M}_+$, and with the induced product $\mathbb{M}_+$ is itself a commutative Jordan algebra, this time over $\mathbb{R}$.

It is of real dimension four and of degree two, and it is isomorphic to the Jordan algebra $H_2(\mathbb{C})$ of *The Six Subspaces and the Jordan Algebra*; that article reads the same structure from the side of the Hermitian elements, and *Jordan Algebras* treats the degree-two algebra in general under the heading of the spin factor. The Hermitian subspace is therefore a **Jordan subalgebra** of $\mathbb{B}$ of the special kind, the one real form on which the symmetrised product closes.

## The Two Halves of the Product

The product of two biquaternions carries two structures at once: the outer product makes $\mathbb{B}$ a Lie algebra, read in *Biquaternion Lie Algebra*, and the Jordan product makes $\mathbb{B}$ a commutative Jordan algebra, read here. The two halves are the two parts of a single bilinear product, the general case being *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*.

On the distinguished subspaces the two structures behave in opposite ways, and the contrast is sharpest on the two three-dimensional pieces of the centre decomposition of the Lie algebra. The vector subspace is closed under the outer product — it is the derived subalgebra $[\mathrm{G},\mathrm{G}]=\mathrm{Vect}(\mathbb{B})$ — and it is **not** closed under the Jordan product, since for two pure vectors

$$
\mathbf{P}\bullet\mathbf{Q} = -\bigl(\mathbf{P},\mathbf{Q}\bigr)e_0 ,
$$

a central scalar, so the Jordan product of two pure vectors leaves the vector subspace as soon as they are not orthogonal. The Hermitian subspace behaves in the mirror fashion: it is closed under the Jordan product and **not** under the outer product, since the outer product of two Hermitian elements is anti-Hermitian and lands in $\mathbb{M}_-$. The action of the symmetrised product on all six distinguished subspaces is the corresponding row of the tables of *Biquaternion Relations Between Subspaces*, cited and not repeated here.

## The Symmetrisation of the Four Products

The symmetrisation $f^{\mathrm{s}}(\tilde{P},\tilde{Q})=\tfrac12(f(\tilde{P},\tilde{Q})+f(\tilde{Q},\tilde{P}))$ is defined for any binary operation $f$, and applied to the four products of *The Four Biquaternion Complex Products* it gives the four symmetric halves tabulated in *Decomposition of the Multiplication*. Only the first of the four is a Jordan product, and the sections above are the development of that one.

**Theorem.** Among the four symmetrisations exactly $\mathcal{A}^{\mathrm{s}}=\bullet$, the symmetrisation of the complex bilinear product, satisfies the Jordan identity.

**Proof.** $\mathcal{A}^{\mathrm{s}}$ is the symmetrisation of the associative product and satisfies the identity. For each of the other three one pair of elements is enough: putting $g=f^{\mathrm{s}}$, so that $g$ is symmetric and the Jordan identity reads $g\bigl(g(\tilde{P},\tilde{Q}),g(\tilde{P},\tilde{P})\bigr)=g\bigl(\tilde{P},g(\tilde{Q},g(\tilde{P},\tilde{P}))\bigr)$, the two sides take the following values at $(\tilde{P},\tilde{Q})$.

| $f$ | $\tilde{P},\tilde{Q}$ | $g\bigl(g(\tilde{P},\tilde{Q}),g(\tilde{P},\tilde{P})\bigr)$ | $g\bigl(\tilde{P},g(\tilde{Q},g(\tilde{P},\tilde{P}))\bigr)$ |
|---|---|---|---|
| $\mathcal{B}=\tilde{P}^{\natural}\tilde{Q}$ | $e_1,\ e_1$ | $e_0$ | $0$ |
| $\mathcal{C}=\tilde{P}\tilde{Q}^{*}$ | $e_1,\ e_1$ | $e_0$ | $0$ |
| $\mathcal{D}=\tilde{P}^{\natural}\tilde{Q}^{*}$ | $e_1,\ e_0$ | $-e_1$ | $e_1$ |

**Remark.** The failure of the $\natural$-case has a one-line reason. Its symmetrisation is central, $\mathcal{B}^{\mathrm{s}}(\tilde{P},\tilde{Q})=\phi(\tilde{P},\tilde{Q})e_0$ with $\phi(\tilde{P},\tilde{Q})=P_0Q_0+(\mathbf{P},\mathbf{Q})$, so both sides of the Jordan identity are central multiples of $e_0$, and the identity reduces to $\phi(\tilde{P},\tilde{Q})\phi(\tilde{P},\tilde{P})=\phi(\tilde{P},\tilde{P})P_0Q_0$, which holds for all $\tilde{P},\tilde{Q}$ exactly when $\phi$ is the scalar-part form $P_0Q_0$; it is not. The witness above is the pair of pure vectors $e_1,e_1$, where $\phi(e_1,e_1)=1$ while the scalar part is $0$.

The two remaining symmetrisations are the more degenerate ones: they are only $\mathbb{R}$-bilinear, the interchange of the two factors carrying a conjugate-linear slot into a linear one, so neither is a product over $\mathbb{C}$ at all, and the failure is read off the same way.

### The Centre and the Hermitian Subspace

The three failing symmetrisations do not all fail in the same way, and the ranges recorded in *Decomposition of the Multiplication* separate them.

The symmetrisation of the $\natural$-product is central, and it is the trace form of the $\natural$-product read as a central element:

$$
\mathcal{B}^{\mathrm{s}}(\tilde{P},\tilde{Q}) = \bigl(\mathrm{Sc}\,\mathcal{B}^{\mathrm{s}}\bigr)e_0 = \tfrac12\,\mathrm{Tr}\bigl(\tilde{P}^{\natural}\tilde{Q}\bigr)e_0 .
$$

Its scalar part is $\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q})=P_0Q_0+(\mathbf{P},\mathbf{Q})$, the companion of $\mathrm{Sc}(\tilde{P}\tilde{Q})=P_0Q_0-(\mathbf{P},\mathbf{Q})$ that the trace form $\mathrm{Tr}(\tilde{P}\bullet\tilde{Q})=2\bigl(P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr)$ of the sections above carries. So the two bilinear scalar parts are the sum and the half-difference of $2P_0Q_0$ and $2(\mathbf{P},\mathbf{Q})$, and their symmetrisations are the two directions of that single trace: the Jordan product fills the algebra, and the $\natural$-symmetrisation retains only the trace direction.

The symmetrisation of the star-product takes its values in the Hermitian subspace $\mathbb{M}_+$, the Jordan subalgebra of the section above, so that it never leaves it; its scalar part is the real part of the sesquilinear scalar part $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})=P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})$ of *Relations Between the Four Biquaternion Products*, and its vector part is the imaginary part of the mixed terms. The symmetrisation of the quaternionic sesquilinear product takes its values in neither $\mathbb{M}_+$ nor $\mathbb{M}_-$, and of the four symmetrisations it is the only one that respects no subspace of the six.

## Summary

With the Jordan product $\tilde{P}\bullet\tilde{Q}=\tfrac12(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P})$ the biquaternion algebra is a commutative Jordan algebra, special, of degree two, whose envelope is the associative algebra $\mathbb{B}$ itself. The Jordan identity holds, the trace form $\mathrm{Tr}(\tilde{P}\bullet\tilde{Q})=\mathrm{Tr}(\tilde{P}\tilde{Q})$ is symmetric and associative, and the two idempotents $\tilde{\Pi}_1,\tilde{\Pi}_2$ are Jordan orthogonal and complete, with Peirce dimensions $1+2+1$. The Hermitian subspace $\mathbb{M}_+$ is a Jordan subalgebra isomorphic to $H_2(\mathbb{C})$. The vector subspace is closed under the outer product and not under the Jordan product, the Hermitian subspace is closed under the Jordan product and not under the outer product, so the symmetric and the antisymmetric halves of the product divide the distinguished subspaces between them.

Of the four products of *The Four Biquaternion Complex Products* only the complex bilinear one has a Jordan symmetrisation; the symmetrisations of the $\natural$-, the star- and the quaternionic sesquilinear product are commutative but fail the Jordan identity, at $(e_1,e_1)$ for the first two and at $(e_1,e_0)$ for the third. The three failures are of three kinds: the $\natural$-symmetrisation is central-valued, $\mathcal{B}^{\mathrm{s}}=\tfrac12\mathrm{Tr}(\tilde{P}^{\natural}\tilde{Q})e_0$, and fails because its central form is not the scalar-part form; the star-symmetrisation is Hermitian-valued and fills the Jordan subalgebra $\mathbb{M}_+$; and the quaternionic sesquilinear symmetrisation fills no subspace of the six.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{P}\bullet\tilde{Q}=\tfrac{1}{2}(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P})$ | Jordan product, the symmetric part of the complex bilinear product |
| $\tilde{P}\wedge\tilde{Q}=\tfrac{1}{2}(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P})$ | Outer product, the antisymmetric part; the commutator is twice it |
| $\mathcal{A},\mathcal{B},\mathcal{C},\mathcal{D}$ | the four products as binary operations, $\tilde{P}\tilde{Q}$, $\tilde{P}^{\natural}\tilde{Q}$, $\tilde{P}\tilde{Q}^{*}$, $\tilde{P}^{\natural}\tilde{Q}^{*}$ |
| $f^{\mathrm{s}}$ | the symmetrisation $\tfrac12(f(\tilde{P},\tilde{Q})+f(\tilde{Q},\tilde{P}))$ of a binary operation $f$ |
| $\mathcal{B}^{\mathrm{s}}=\tfrac12\mathrm{Tr}(\tilde{P}^{\natural}\tilde{Q})e_0$ | the central symmetrisation of the $\natural$-product, not a Jordan product |
| $\mathcal{C}^{\mathrm{s}}$ | the symmetrisation of the star-product, with values in $\mathbb{M}_+$, not a Jordan product |
| $\mathbb{B}$ with $\bullet$ | Commutative Jordan algebra, special, degree two |
| $(\tilde{P}\bullet\tilde{Q})\bullet\tilde{P}^2=\tilde{P}\bullet(\tilde{Q}\bullet\tilde{P}^2)$ | Jordan identity |
| $\mathrm{Tr}(\tilde{P}\bullet\tilde{Q})=\mathrm{Tr}(\tilde{P}\tilde{Q})$ | Trace form, symmetric and associative |
| $\tilde{\Pi}_1,\tilde{\Pi}_2$ | Jordan idempotents, Jordan orthogonal and complete, $\tilde{\Pi}_1+\tilde{\Pi}_2=e_0$ |
| $\mathbb{C}[\tilde{Q}]$ | Subalgebra generated by one element, the span of its powers |
| $\mathrm{J}_1\oplus\mathrm{J}_{1/2}\oplus\mathrm{J}_0$ | Peirce decomposition; dimensions $1+2+1$ |
| $\mathbb{M}_+$ | Hermitian subspace, a Jordan subalgebra isomorphic to $H_2(\mathbb{C})$ |
| $\mathbf{P}\bullet\mathbf{Q}=-(\mathbf{P},\mathbf{Q})e_0$ | Jordan product of pure vectors; the vector subspace is not closed |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications 39 (1968), for the general theory of Jordan algebras, the Peirce decomposition and the degree.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the special Jordan algebras, the envelope and the trace form.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the symmetrised product of quaternions and its idempotents.
- The companion articles of this series: *The Four Biquaternion Complex Products*, *Relations Between the Four Biquaternion Products*, *Decomposition of the Multiplication*, *Biquaternion Lie Algebra*, *Biquaternion Idempotents and Projections*, *The Six Subspaces and the Jordan Algebra*, *Biquaternion Relations Between Subspaces*, and *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*.
