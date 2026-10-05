# __Biquaternion Jordan Algebras__

## Introduction

A Jordan algebra is not a property of a vector space; it is a property of a product on that space. The same space carries as many products as one gives it, and a symmetrisation that satisfies the Jordan identity on one subspace may fail it on a larger one. The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four products, and the question *is $\mathbb{B}$ a Jordan algebra* has no answer until the product is named. This article answers the question product by product, and shows that the four products carry **one** Jordan algebra and not four: on the whole space only the complex bilinear product works, and the other three do not give a second algebra but reproduce subalgebras of that one on the subspaces where they coincide with it.

The four products are from *The Four Biquaternion Complex Products*, and the symmetric and the antisymmetric part of each are from *Decomposition of the Biquaternion Complex Products*. The **symmetric part**, also called the **symmetrised product**, of a product $f$ is

$$
g(\tilde{P},\tilde{Q}) = \tfrac12\bigl(f(\tilde{P},\tilde{Q}) + f(\tilde{Q},\tilde{P})\bigr),
$$

always commutative and additive. Whether it is a **Jordan product** — commutative, bilinear over the right ring, and satisfying the Jordan identity — depends on the product and on the regime in which the product lives. Two regimes occur, and the distinction is the whole point:

- **Bilinear products.** If $f$ is bilinear over a commutative ring $R$, then $g$ is bilinear over $R$ as well, and $g$ satisfies the Jordan identity **as soon as $f$ is associative**; the symmetry of $g$ is the symmetry of the half-sum by construction. The symmetrisation of an associative algebra is the standard example of *Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*.
- **Sesquilinear products.** If $f$ is linear in one slot and conjugate-linear in the other, then $g$ is linear only over the fixed ring $R^{\varsigma}$, so it is at best a Jordan product over $R^{\varsigma}$ and never a product over the base ring; on the **Hermitian half**, where the second element is fixed by the involution, the derived operation coincides with the associative product and the identity is inherited. This is the setting of *Jordan Algebras of Sesquialgebras*, in the general framework of *Sesquialgebras*.

The four products of $\mathbb{B}$ fall into these regimes as follows.

- The **complex bilinear** product is associative, and its symmetrisation is the Jordan product $\bullet$ that makes $\mathbb{B}$ a commutative Jordan algebra over $\mathbb{C}$, special, of degree two. This is the main algebra of the article, and the sections below develop it.
- The **quaternionic bilinear** product is not associative, and its symmetrisation is central-valued; it is not a Jordan product on $\mathbb{B}$, and on the centre it coincides with $\bullet$, so it adds no algebra of its own.
- The **complex sesquilinear** product is not associative, and its symmetrisation is Hermitian-valued; it is not a Jordan product on $\mathbb{B}$, and on the Hermitian subspace $\mathbb{M}_+$ it coincides with $\bullet$, giving the real Jordan algebra $J(\mathbb{B})\cong H_2(\mathbb{C})$.
- The **quaternionic sesquilinear** product is not associative, and its symmetrisation is neither Hermitian nor anti-Hermitian; it is a Jordan product nowhere.

So the four products carry **one** Jordan algebra, $(\mathbb{B},\bullet)$, and not four: the complex bilinear product gives it on the whole space, the complex sesquilinear product reproduces it on the Hermitian subspace, the quaternionic bilinear product reproduces it on the centre, and the quaternionic sesquilinear product gives nothing.

The general theory of the bilinear symmetrisation is *Jordan Algebras*, and the general theory of the sesquilinear symmetrisation, which governs the two star-products, is *Jordan Algebras of Sesquialgebras*. The algebra, its basis and its two idempotents are from *Biquaternions as a Vector Space over $\mathbb{C}$*, *Biquaternions as an Algebra over $\mathbb{C}$* and *Biquaternion Idempotents and Projections*; the subspace-by-subspace behaviour is tabulated in *The Six Subspaces and the Four Complex Products*; and the antisymmetric parts, the four brackets, are *Biquaternion Lie Algebras*, the companion of this article.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. Throughout, a biquaternion is written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^3 Q_k e_k$, and $(\mathbf{P},\mathbf{Q})=\sum_k P_kQ_k$ is the complex bilinear dot product of the vector parts. The three involutions are the natural conjugation ${}^{\natural}$, the coefficientwise conjugation $\bar{\cdot}$ and the Hermitian conjugation ${}^{*}=\bar{\cdot}\circ{}^{\natural}$.

---

## The Symmetrisation and the Two Regimes

### The Bilinear Regime

Let $A$ be an associative algebra over a commutative ring $R$. Its **symmetrisation** is the commutative product

$$
x\bullet y = \tfrac12\bigl(xy+yx\bigr),
$$

and it satisfies the Jordan identity; $A$ with this product is the algebra $A^{+}$ of *Jordan Algebras*. Commutativity and bilinearity are immediate, and the identity is what survives of associativity once the order of the factors is forgotten. The symmetrisation of a bilinear but non-associative product is still commutative and bilinear, but it carries no identity to inherit, and it may fail the Jordan identity.

### The Sesquilinear Regime

Let $A$ be an associative $R$-algebra with a $\varsigma$-semilinear involution $*$, and let $x\star y=xy^{*}$ be the derived operation. Its symmetrisation

$$
x\circ y = \tfrac12\bigl(xy^{*}+yx^{*}\bigr)
$$

is commutative and additive, but a scalar $\lambda$ can be taken out of a sum only when it multiplies both terms, so $\circ$ is $R^{\varsigma}$-bilinear and not $R$-bilinear. On the **Hermitian half** $H(A)=\{x:x^{*}=x\}$ the derived operation is the associative product, $x\star y=xy$ for $y\in H(A)$, so there $\circ$ is the symmetrisation of an associative product and the Jordan identity is inherited; off $H(A)$ it fails, with a witness in $M_2(\mathbb{C})$. This is the criterion and the collapse theorem of *Jordan Algebras of Sesquialgebras*: for a product of full type the associativity of $\star$ forces the twist to be invisible, so the genuinely sesquilinear case is exactly the case where the failure occurs, and the Jordan structure lives on the Hermitian half.

---

## The Four Symmetrisations

The symmetric part of each of the four products is read in *Decomposition of the Biquaternion Complex Products*, where the four are tabulated. For a product $f$ write $g(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})+f(\tilde{Q},\tilde{P})\bigr)$; the four values of $g$, the regime, and the ring of scalars are as follows.

| product $f$ | symmetric part $g$ | regime | scalars |
|---|---|---|---|
| $\tilde{P}\tilde{Q}$ (complex bilinear) | $\tilde{P}\bullet\tilde{Q}$, a general biquaternion | bilinear | $\mathbb{C}$ |
| $\tilde{P}^{\natural}\tilde{Q}$ (quaternionic bilinear) | $\bigl(P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr)e_0$, central | bilinear | $\mathbb{C}$ |
| $\tilde{P}\tilde{Q}^{*}$ (complex sesquilinear) | Hermitian-valued | sesquilinear | $\mathbb{R}$ |
| $\tilde{P}^{\natural}\tilde{Q}^{*}$ (quaternionic sesquilinear) | neither Hermitian nor anti-Hermitian | sesquilinear | $\mathbb{R}$ |

### The Failure on the Whole Algebra

**Theorem.** Among the four symmetric parts exactly that of the complex bilinear product, the Jordan product $\bullet$, satisfies the Jordan identity on all of $\mathbb{B}$.

**Proof.** The Jordan product is the symmetric part of the associative product and satisfies the identity by the bilinear regime. For each of the other three one pair of elements is enough: with $g$ the symmetric part of the product in question, the Jordan identity reads $g\bigl(g(\tilde{P},\tilde{Q}),g(\tilde{P},\tilde{P})\bigr)=g\bigl(\tilde{P},g(\tilde{Q},g(\tilde{P},\tilde{P}))\bigr)$, and the two sides take the following values at $(\tilde{P},\tilde{Q})$.

| product | $\tilde{P},\tilde{Q}$ | $g\bigl(g(\tilde{P},\tilde{Q}),g(\tilde{P},\tilde{P})\bigr)$ | $g\bigl(\tilde{P},g(\tilde{Q},g(\tilde{P},\tilde{P}))\bigr)$ |
|---|---|---|---|
| $\tilde{P}^{\natural}\tilde{Q}$ | $e_1,\ e_1$ | $e_0$ | $0$ |
| $\tilde{P}\tilde{Q}^{*}$ | $e_1,\ e_1$ | $e_0$ | $0$ |
| $\tilde{P}^{\natural}\tilde{Q}^{*}$ | $e_1,\ e_0$ | $-e_1$ | $e_1$ |

**Remark.** The failure of the $\natural$-case has a one-line reason. Its symmetric part is central, $\tfrac12(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P})=\phi(\tilde{P},\tilde{Q})e_0$ with $\phi(\tilde{P},\tilde{Q})=P_0Q_0+(\mathbf{P},\mathbf{Q})$, so both sides of the Jordan identity are central multiples of $e_0$, and the identity reduces to $\phi(\tilde{P},\tilde{Q})\phi(\tilde{P},\tilde{P})=\phi(\tilde{P},\tilde{P})P_0Q_0$, which holds for all $\tilde{P},\tilde{Q}$ exactly when $\phi$ is the scalar-part form $P_0Q_0$; it is not. The witness above is the pair of pure vectors $e_1,e_1$, where $\phi(e_1,e_1)=1$ while the scalar part is $0$.

### The Jordan Algebras Found

The failure on the whole algebra does not remove the structures carried by the subspaces. Where the involution of a product fixes the elements, the derived product is the ordinary product, so the symmetrisation of that product coincides with $\bullet$ there; this is the mechanism of *Jordan Algebras of Sesquialgebras*. Each product is taken in turn.

**The complex bilinear product $\tilde{P}\tilde{Q}$.** Bilinear over $\mathbb{C}$ and associative. Its symmetric part is the Jordan product $\tilde{P}\bullet\tilde{Q}=\tfrac12(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P})$, which lands in all of $\mathbb{B}$ and satisfies the Jordan identity there. It is the symmetrisation of the associative algebra $\mathbb{B}$ of *Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*: commutative, special, of degree two, of envelope $\mathbb{B}$, with the Peirce decomposition $1+2+1$ developed below.

**The quaternionic bilinear product $\tilde{P}^{\natural}\tilde{Q}$.** Bilinear over $\mathbb{C}$ and not associative. Its symmetric part is the central element

$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P}\bigr)=\tfrac12\mathrm{Tr}\bigl(\tilde{P}^{\natural}\tilde{Q}\bigr)e_0=\bigl(P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr)e_0 .
$$

The Jordan identity fails at $e_1,e_1$, because the central form $P_0Q_0+(\mathbf{P},\mathbf{Q})$ is not the scalar-part form $P_0Q_0$; on the centre the product is the multiplication of $\mathbb{C}$, where it coincides with $\bullet$.

**The complex sesquilinear product $\tilde{P}\tilde{Q}^{*}$.** Linear in the first slot and conjugate-linear in the second, hence linear over $\mathbb{R}$ alone. Its symmetric part $\tfrac12(\tilde{P}\tilde{Q}^{*}+\tilde{Q}\tilde{P}^{*})$ is Hermitian and lands in $\mathbb{M}_+$, and the Jordan identity fails at $e_1,e_1$. On $\mathbb{M}_+$ the star acts trivially and the symmetrisation is again $\bullet$; the algebra is the Hermitian one $H_2(\mathbb{C})=J(\mathbb{B})$ of *The Hermitian Jordan Algebra* and *Jordan Algebras of Sesquialgebras*, a spin factor of degree two in the sense of *Jordan Algebras*, §*Spin Factors*.

**The quaternionic sesquilinear product $\tilde{P}^{\natural}\tilde{Q}^{*}$.** Linear over $\mathbb{R}$ and not associative. Its symmetric part is neither Hermitian nor anti-Hermitian, and its range lies in none of the six distinguished subspaces. The Jordan identity fails on every subspace; the pair $e_1,e_0$ is a witness, and it fails already on the centre, where $x=ie_0$ and $y=(1+i)e_0$ give $e_0$ on the left of the identity and $0$ on the right.

| the product | regime and scalars | where it is a Jordan product | the Jordan algebra it gives |
|---|---|---|---|
| $\tilde{P}\tilde{Q}$ | bilinear, $\mathbb{C}$, associative | all of $\mathbb{B}$ | the symmetrisation $(\mathbb{B},\bullet)$, degree two |
| $\tilde{P}^{\natural}\tilde{Q}$ | bilinear, $\mathbb{C}$ | the centre | the field $\mathbb{C}$ |
| $\tilde{P}\tilde{Q}^{*}$ | sesquilinear, $\mathbb{R}$ | the Hermitian subspace $\mathbb{M}_+$ | $H_2(\mathbb{C})=J(\mathbb{B})$, a spin factor, degree two |
| $\tilde{P}^{\natural}\tilde{Q}^{*}$ | sesquilinear, $\mathbb{R}$ | nowhere | none |

So the four products carry one Jordan algebra and not four: the first gives it on the whole space, the second reproduces its centre, the third its Hermitian subspace, and the fourth gives nothing. Which of the six distinguished subspaces are Jordan subalgebras of $(\mathbb{B},\bullet)$ is recorded in *The Six Subspaces and the Four Complex Products*, and not repeated here.

The rest of the article develops these objects in two stages. §*The Jordan Algebra $(\mathbb{B},\bullet)$* develops the one algebra of the table in full — its product, its identity, its powers, its trace form, its idempotents and its Peirce decomposition. §*The Two Subalgebras the Other Products Reproduce* develops the two subalgebras that the other products reach: the Hermitian subalgebra $(\mathbb{M}_+,\bullet)$, reproduced by product 3, and the central subalgebra $(\mathbb{C}_{\mathbb{B}},\bullet)$, reproduced by product 2; product 4 reproduces none.

---

## The Jordan Algebra $(\mathbb{B},\bullet)$

### The Jordan Product

The **symmetric part** of the complex bilinear product, also called the **symmetrised product** or the **Jordan product**, is

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

The full product is the sum of its two parts,

$$
\tilde{P}\tilde{Q} = \tilde{P}\bullet\tilde{Q} + \tilde{P}\wedge\tilde{Q} , \qquad \tilde{P}\wedge\tilde{Q} = \tfrac{1}{2}\bigl(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}\bigr),
$$

the second summand being the **outer product** of *Decomposition of the Biquaternion Complex Products*, which is the commutator up to the factor $2$ and is read in *Biquaternion Lie Algebras*.

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

### The Jordan Algebra

**Theorem.** With the product $\bullet$ the biquaternion algebra is a commutative Jordan algebra: $\bullet$ is commutative and $\mathbb{C}$-bilinear, and the Jordan identity

$$
(\tilde{P}\bullet\tilde{Q})\bullet\tilde{P}^2 = \tilde{P}\bullet\bigl(\tilde{Q}\bullet\tilde{P}^2\bigr)
$$

holds for all $\tilde{P},\tilde{Q}\in\mathbb{B}$.

**Proof.** The algebra $\mathbb{B}$ is associative, and the symmetrisation $a\bullet b=\tfrac12(ab+ba)$ of any associative algebra satisfies the Jordan identity, by the associativity of the underlying product (*Jordan Algebras*, §*The Symmetrisation of an Associative Algebra*). Commutativity and bilinearity are built into the definition.

A Jordan algebra obtained by symmetrising an associative algebra is called **special**, and the associative algebra is its **envelope**. The special Jordan algebra here is $\mathbb{B}$ with $\bullet$, and its envelope is the associative algebra $\mathbb{B}$ itself, so the envelope is finite-dimensional and four-dimensional over $\mathbb{C}$. No exceptional Jordan algebra arises: the exceptional ones have no such envelope, whereas every biquaternion computation is an ordinary associative computation in the envelope followed by symmetrisation.

### Powers and the Subalgebra Generated by One Element

A Jordan algebra is power-associative, so every power $\tilde{Q}^n$ is well defined without brackets, $\tilde{Q}^{n+1}=\tilde{Q}\bullet\tilde{Q}^n$, and the powers commute. The subalgebra generated by a single element $\tilde{Q}$ is the span of its powers,

$$
\mathbb{C}[\tilde{Q}] = \mathrm{span}_{\mathbb{C}}\{\tilde{Q},\tilde{Q}^2,\tilde{Q}^3,\dots\},
$$

which is commutative and closed under $\bullet$.

### The Trace Form

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

### The Idempotents

An **idempotent** of the Jordan algebra is an element $\tilde{E}$ with $\tilde{E}\bullet\tilde{E}=\tilde{E}$, and two idempotents are **Jordan orthogonal** when $\tilde{E}\bullet\tilde{F}=0$. The two idempotents of *Biquaternion Idempotents and Projections*,

$$
\tilde{\Pi}_1=\tfrac12(e_0+ie_3), \qquad \tilde{\Pi}_2=\tfrac12(e_0-ie_3),
$$

are idempotents of the Jordan algebra, they are Jordan orthogonal, and they sum to the unit:

$$
\tilde{\Pi}_1\bullet\tilde{\Pi}_2=0 , \qquad \tilde{\Pi}_1+\tilde{\Pi}_2=e_0 .
$$

A family of pairwise Jordan-orthogonal idempotents summing to the unit is **complete**, and the number of its members is the **degree** of the Jordan algebra. The two idempotents above are such a family, and a third can never be added: in the envelope $\mathbb{B}\cong M_2(\mathbb{C})$ a complete family of orthogonal idempotents has at most two members, their images being complementary subspaces of the defining two-dimensional module $S$ of *Modules over the Biquaternion Algebra*. The biquaternion Jordan algebra therefore has **degree two**.

### The Peirce Decomposition

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

**Proof.** The relations $\tilde{\Pi}_1\bullet\tilde{\Pi}_1=\tilde{\Pi}_1$ and $\tilde{\Pi}_1\bullet\tilde{\Pi}_2=0$ put $\tilde{\Pi}_1$ in the first space and $\tilde{\Pi}_2$ in the third. For the vector units, $\tilde{\Pi}_1\bullet e_1=\tfrac12 e_1$ and $\tilde{\Pi}_1\bullet e_2=\tfrac12 e_2$, so $e_1$ and $e_2$ span the middle space. The three spaces are independent and their dimensions sum to $1+2+1=4=\dim_{\mathbb{C}}\mathbb{B}$, so they exhaust the algebra.

The dimensions $1+2+1$ are the Jordan counterpart of the two minimal left ideals of *Biquaternion Ideals and Peirce Decomposition*: the middle space is two-dimensional there as well, and the two one-dimensional ends are the two idempotents.

---

## The Two Subalgebras the Other Products Reproduce

Product 3 of the table above reproduces the Hermitian subspace and product 2 reproduces the centre, so the two objects that follow are the subalgebras of $(\mathbb{B},\bullet)$ that the other products reach, and not algebras of their own; product 4 reproduces nothing.

### The Hermitian Subalgebra $(\mathbb{M}_+,\bullet)$

The Hermitian subspace $\mathbb{M}_+$ is closed under the Jordan product. If $\tilde{P},\tilde{Q}\in\mathbb{M}_+$ then $\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P}$ is again Hermitian, so $\tilde{P}\bullet\tilde{Q}\in\mathbb{M}_+$, and with the induced product $\mathbb{M}_+$ is itself a commutative Jordan algebra, this time over $\mathbb{R}$.

It is of real dimension four and of degree two, and it is isomorphic to the Jordan algebra $H_2(\mathbb{C})$ of *The Six Subspaces and the Four Complex Products*; that article reads the same structure from the side of the Hermitian elements, and *Jordan Algebras* treats the degree-two algebra in general under the heading of the spin factor. The Hermitian subspace is therefore a **Jordan subalgebra** of $\mathbb{B}$ of the special kind; with the centre and the quaternion subspace it is one of the three Jordan subalgebras of $(\mathbb{B},\bullet)$ among the six distinguished subspaces.

The Hermitian Jordan algebra is also what the **complex sesquilinear** product gives. Its symmetric part is Hermitian-valued for all arguments, and on the Hermitian half the derived operation $\tilde{X}\star\tilde{Y}=\tilde{X}\tilde{Y}^{*}$ of *Jordan Algebras of Sesquialgebras* coincides with the associative product, since $\tilde{Y}^{*}=\tilde{Y}$ for a Hermitian $\tilde{Y}$. So the symmetric part of the star-product restricted to $\mathbb{M}_+$ agrees with the Jordan product $\bullet$, and

$$
(\mathbb{M}_+,\bullet) = J(\mathbb{B})
$$

is the Hermitian Jordan algebra of that article: the Hermitian half is the one place where the star-product, which fails the Jordan identity on the whole algebra, becomes a Jordan product. Its scalar part is the real part of the sesquilinear scalar part $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})=P_0\overline{Q_0}+(\mathbf{P},\overline{\mathbf{Q}})$ of *Relations Between the Four Biquaternion Products*, and its vector part is the imaginary part of the mixed terms.

### The Central Subalgebra $(\mathbb{C}_{\mathbb{B}},\bullet)$

The symmetric part of the **quaternionic bilinear** product is central-valued,

$$
\tfrac12\bigl(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P}\bigr) = \bigl(\mathrm{Sc}\,\tfrac12(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P})\bigr)e_0 = \tfrac12\,\mathrm{Tr}\bigl(\tilde{P}^{\natural}\tilde{Q}\bigr)e_0 ,
$$

with scalar part $\mathrm{Sc}(\tilde{P}^{\natural}\tilde{Q})=P_0Q_0+(\mathbf{P},\mathbf{Q})$, the companion of $\mathrm{Sc}(\tilde{P}\tilde{Q})=P_0Q_0-(\mathbf{P},\mathbf{Q})$. The two bilinear scalar parts are thus the sum and the half-difference of $2P_0Q_0$ and $2(\mathbf{P},\mathbf{Q})$, and their symmetric parts are the two directions of that single trace: the Jordan product fills the algebra, and the symmetric part of the $\natural$-product retains only the trace direction.

Restricted to the centre the $\natural$-symmetrisation is the multiplication of $\mathbb{C}$, since $\tilde{P}^{\natural}=\tilde{P}$ and $\tilde{Q}^{\natural}=\tilde{Q}$ there, so $(\mathbb{C}_{\mathbb{B}},\bullet)$ is a commutative associative algebra, a Jordan algebra of degree one. Off the centre it fails the Jordan identity, by the theorem above; it is the smallest of the three algebras and a Jordan subalgebra of $(\mathbb{B},\bullet)$, while it is not contained in $\mathbb{M}_+$.

### The Quaternionic Sesquilinear Product Gives No Subalgebra

The symmetric part of the **quaternionic sesquilinear** product takes its values in neither $\mathbb{M}_+$ nor $\mathbb{M}_-$ for general arguments, and of the four symmetric parts it is the only one that satisfies the Jordan identity nowhere; like the $\natural$-symmetrisation it does stay inside the centre and the Hermitian subspace, where it is central, and it also stays inside the quaternion subspace, where it is the quaternion conjugate of the Jordan product.

---

## The Subspaces Under the Symmetrisation

The symmetrised product acts on the six distinguished subspaces in a way that is the mirror image of the outer product, and the contrast is sharpest on the two three-dimensional pieces of the centre decomposition of the Lie algebra. The vector subspace is closed under the outer product — it is the derived subalgebra $[\mathrm{G},\mathrm{G}]=\mathrm{Vect}(\mathbb{B})$ of *Biquaternion Lie Algebras* — and it is **not** closed under the Jordan product, since for two pure vectors

$$
\mathbf{P}\bullet\mathbf{Q} = -\bigl(\mathbf{P},\mathbf{Q}\bigr)e_0 ,
$$

a central scalar, so the Jordan product of two pure vectors leaves the vector subspace as soon as they are not orthogonal. The Hermitian subspace behaves in the mirror fashion: it is closed under the Jordan product and **not** under the outer product, since the outer product of two Hermitian elements is anti-Hermitian and lands in $\mathbb{M}_-$. The anti-Hermitian subspace $\mathbb{M}_-$ is mapped into $\mathbb{M}_+$ by the Jordan product, since the product of two anti-Hermitian elements is Hermitian. The action of the symmetrised product on all six distinguished subspaces is the corresponding row of the tables of *The Six Subspaces and the Four Complex Products*, cited and not repeated here.

---

## Summary

With the Jordan product $\tilde{P}\bullet\tilde{Q}=\tfrac12(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P})$, the symmetric part of the complex bilinear product, the biquaternion algebra is a commutative Jordan algebra, special, of degree two, whose envelope is the associative algebra $\mathbb{B}$ itself. The Jordan identity holds, the trace form $\mathrm{Tr}(\tilde{P}\bullet\tilde{Q})=\mathrm{Tr}(\tilde{P}\tilde{Q})$ is symmetric and associative, and the two idempotents $\tilde{\Pi}_1,\tilde{\Pi}_2$ are Jordan orthogonal and complete, with Peirce dimensions $1+2+1$. The Hermitian subspace $\mathbb{M}_+$ is a Jordan subalgebra isomorphic to $H_2(\mathbb{C})$, and it is also what the complex sesquilinear product gives on its Hermitian half; the centre is a degenerate Jordan subalgebra isomorphic to $\mathbb{C}$; and the other subspaces are treated in *The Six Subspaces and the Four Complex Products*. The vector subspace is closed under the outer product and not under the Jordan product, the Hermitian subspace is closed under the Jordan product and not under the outer product, so the symmetric and the antisymmetric parts of the product divide the distinguished subspaces between them.

The structures are relative to the products, and the count is the point. Of the four products only the complex bilinear one has a Jordan product as its symmetric part on the whole algebra, in agreement with the general criterion that a symmetrisation is a Jordan product as soon as the product is associative and that for a full-type sesquilinear product the Jordan identity holds on the Hermitian half alone. The symmetric parts of the $\natural$-, the star- and the quaternionic sesquilinear product are commutative but fail the Jordan identity on the whole algebra, at $(e_1,e_1)$ for the first two and at $(e_1,e_0)$ for the third; the three failures are of three kinds. The symmetric part of the $\natural$-product is central-valued, $\tfrac12(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P})=\tfrac12\mathrm{Tr}(\tilde{P}^{\natural}\tilde{Q})e_0$, and fails because its central form is not the scalar-part form; that of the star-product is Hermitian-valued and fills the Jordan subalgebra $\mathbb{M}_+$, where it becomes the same Jordan product again; and that of the quaternionic sesquilinear product closes on the centre, the quaternion subspace and the Hermitian subspace yet satisfies the identity nowhere. So the four symmetrisations yield one Jordan algebra and not four, and the companion article *Biquaternion Lie Algebras* reads the other half of the same products.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $g(\tilde{P},\tilde{Q})=\tfrac12\bigl(f(\tilde{P},\tilde{Q})+f(\tilde{Q},\tilde{P})\bigr)$ | symmetric part of a product $f$ |
| $\tilde{P}\bullet\tilde{Q}=\tfrac{1}{2}(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P})$ | Jordan product, the symmetric part of the complex bilinear product |
| $\tilde{P}\wedge\tilde{Q}=\tfrac{1}{2}(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P})$ | Outer product, the antisymmetric part; the commutator is twice it |
| $\tilde{P}^{\natural}\tilde{Q}$ | the $\natural$-product, defined in *The Four Biquaternion Complex Products* |
| $\tfrac12(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P})=\tfrac12\mathrm{Tr}(\tilde{P}^{\natural}\tilde{Q})e_0$ | the symmetric part of the $\natural$-product, central, a Jordan product on the centre alone |
| $\tfrac12(\tilde{P}\tilde{Q}^{*}+\tilde{Q}\tilde{P}^{*})$ | the symmetric part of the star-product, Hermitian-valued, a Jordan product on $\mathbb{M}_+$ alone |
| $\mathbb{B}$ with $\bullet$ | Commutative Jordan algebra, special, degree two, envelope $\mathbb{B}$ |
| $\mathbb{M}_+$ with $\bullet$ | Hermitian Jordan algebra $J(\mathbb{B})\cong H_2(\mathbb{C})$, over $\mathbb{R}$, degree two |
| $\mathbb{C}_{\mathbb{B}}$ with $\bullet$ | Degenerate central Jordan algebra, the field $\mathbb{C}$, of degree one |
| $(\tilde{P}\bullet\tilde{Q})\bullet\tilde{P}^2=\tilde{P}\bullet(\tilde{Q}\bullet\tilde{P}^2)$ | Jordan identity |
| $\mathrm{Tr}(\tilde{P}\bullet\tilde{Q})=\mathrm{Tr}(\tilde{P}\tilde{Q})$ | Trace form, symmetric and associative |
| $\tilde{\Pi}_1,\tilde{\Pi}_2$ | Jordan idempotents, Jordan orthogonal and complete, $\tilde{\Pi}_1+\tilde{\Pi}_2=e_0$ |
| $\mathbb{C}[\tilde{Q}]$ | Subalgebra generated by one element, the span of its powers |
| $\mathrm{J}_1\oplus\mathrm{J}_{1/2}\oplus\mathrm{J}_0$ | Peirce decomposition; dimensions $1+2+1$ |
| $\mathbf{P}\bullet\mathbf{Q}=-(\mathbf{P},\mathbf{Q})e_0$ | Jordan product of pure vectors; the vector subspace is not closed |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications 39 (1968), for the general theory of Jordan algebras, the Peirce decomposition and the degree.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the special Jordan algebras, the envelope and the trace form.
- *Sesquialgebras* and *Jordan Algebras of Sesquialgebras* (`articles_maths/`), for the general symmetrisation of a sesquilinear product, the obstruction to its being a Jordan product and the Hermitian Jordan algebra $J(A)$ that it carries on the Hermitian half; the biquaternion case is the worked example of that article.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the symmetrised product of quaternions and its idempotents.
- The companion articles of this series: *The Four Biquaternion Complex Products*, *Relations Between the Four Biquaternion Products*, *Decomposition of the Biquaternion Complex Products*, *Biquaternion Lie Algebras*, *Biquaternion Idempotents and Projections*, *The Six Subspaces and the Four Complex Products*, and *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*.
