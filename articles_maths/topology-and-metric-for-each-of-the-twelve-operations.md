# __Topology and Metric for Each of the Twelve Operations__

## Introduction

The complex space of the biquaternion algebra carries twelve operations — the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and the symmetric and antisymmetric part of each (*The 12 Products of the Biquaternion Complex Space*) — and this article answers two questions for each of the twelve: what its situation is with respect to **topology**, and what its situation is with respect to **metric**. The two answers are different in kind, and keeping them apart is the whole content of the article.

- On the side of **topology** the answer is one and the same for all twelve. The space is a finite-dimensional real vector space; all norms on it are equivalent; it therefore carries exactly one Hausdorff vector-space topology, and every one of the twelve operations is read inside that one topology (*Topology in the Space of Biquaternions*, §*The Topology*). The twelve operations do not carry twelve topologies, and no operation introduces a second one.
- On the side of **metric** the answer differs from operation to operation, and it is read from the **scalar part** of the operation. Taking the scalar part of a product turns the product into a form; the form is the metric; and the twelve operations distribute over **eight distinct non-vanishing scalar forms and two vanishing ones**, because two pairs of operations share a form.

The distribution is the result the article establishes, and it is worth stating before the walk. Of the twelve operations, two — $\mathrm{APA}$ and $\mathrm{AQA}$ — have a scalar part that vanishes identically and therefore carry no metric of the kind read from a scalar part. Two pairs — $\mathrm{GPA}$ with $\mathrm{SPA}$, and $\mathrm{GQA}$ with $\mathrm{SQA}$ — carry one form each, the general plain bilinear and the general quaternionic bilinear form, shared because the scalar part of a bilinear product is symmetric in its two arguments and so survives symmetrisation unchanged. Two — $\mathrm{GPS}$ and $\mathrm{GQS}$ — carry the two Hermitian forms, and their symmetric halves $\mathrm{SPS}$ and $\mathrm{SQS}$ carry the two real forms those Hermitian forms induce; the antisymmetric halves $\mathrm{APS}$ and $\mathrm{AQS}$ carry the two alternating forms those Hermitian forms induce. **Exactly one of the eight is a positive definite symmetric real form, and it is the one carried by $\mathrm{SPS}$**, the symmetric half of the plain sesquilinear product; it is the Euclidean form of the region, and its complex companion is the Hermitian form carried by $\mathrm{GPS}$, positive definite in the Hermitian sense and the same metric data.

The article is organised as follows. The next section fixes what the scalar part of an operation is and states the two facts that decide the distribution. A table of the eight non-vanishing forms follows. Then the twelve operations are read one by one, in the order of *The 12 Products of the Biquaternion Complex Space*, each with its form, its inertia, its level set and its group, and its metric verdict. A summary table, a section on the one topology, and a section on the indefinite forms and their groups of motions close the article.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with units $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, central scalar imaginary, and a general element $\tilde{Q}=\sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The real and the imaginary part of the coefficient $Q_\mu$ are written $q_\mu$ and $q'_\mu$, and those of $P_\mu$ are written $p_\mu$ and $p'_\mu$; every form below is written in these eight real coordinates. The four forms of the region are written with one bracket, whose subscript records the conjugation entering the argument (*The Four Pairings of the Biquaternion Algebra*):

$$
\langle\tilde{P},\tilde{Q}\rangle=\sum_\mu\varepsilon_\mu P_\mu Q_\mu,\qquad
\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\sum_\mu P_\mu Q_\mu,\qquad
\langle\tilde{P},\tilde{Q}\rangle_{*}=\sum_\mu P_\mu\overline{Q_\mu},\qquad
\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu},
$$

with $\varepsilon=(1,-1,-1,-1)$. They are the **general plain bilinear form**, the **general quaternionic bilinear form**, the **Hermitian form** and the **Krein form**; each is the scalar part of the product the corpus names with the same letters, and each is non-degenerate. The last two are the Hermitian forms of the region, the Hermitian form being positive definite and the Krein form indefinite.

**Conventions.** Two words are fixed here, because both are used in two senses in the literature and both are needed below.

- **Inertia is quoted over $\mathbb{R}$.** For a real symmetric or a real alternating form the inertia (the pair of the numbers of positive and of negative eigenvalues) is an invariant, by Sylvester's law. For a **complex symmetric bilinear** form it is not: over $\mathbb{C}$ the form $\operatorname{diag}(1,-1,-1,-1)$ is congruent to the identity, since the change of basis $e_k\mapsto (\text{the central imaginary})e_k$ flips the three negative signs, so the only invariant is the rank. For a **complex Hermitian** form the signature is an invariant again. So in the tables below the inertias are always the realified ones, and a complex signature is given only for the two Hermitian forms, where it is an invariant.
- **Two objects carry the name *norm*, and they are complementary.** The **biquaternion norm** is
  $$N(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_\mu Q_\mu^{2},$$
  a complex-valued quadratic form on $\mathbb{B}\cong\mathbb{C}^{4}$; it is **multiplicative**, $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$, it is the reduced norm $\det\Phi(\tilde Q)$, and its zeros are exactly the zero divisors. It is the norm of the algebra in the algebraic sense (a norm on an algebra need only be multiplicative), and it is what the corpus calls the semi-norm of the literature: of the analytic axioms it keeps only the sign, since it is complex-valued and not positive definite and the scaling axiom fails for complex $\lambda$. The **Euclidean norm** $\lVert\tilde Q\rVert_E=\bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\bigr)^{1/2}=\bigl(\mathrm{Sc}(\tilde Q\tilde Q^{*})\bigr)^{1/2}$ is a genuine norm, positive definite and homogeneous, and it is **not** multiplicative. So the two are complementary: the multiplicative one is indefinite, the definite one is not multiplicative. When this article says "a norm" of the analytic kind it means $\lVert\cdot\rVert_E$; the biquaternion norm is always named in full.
- **Realification, not *real form*.** Reading a complex form on the $8$ real coordinates is called here the **realification** of the form, and the resulting real form is its real part. The phrase "real form" is avoided for this, because in Lie theory a *real form* of a complex Lie algebra is a real Lie algebra whose complexification returns it, a different notion.

The **Euclidean norm** is $\lVert\tilde{Q}\rVert_E=\bigl(\sum_\mu\lvert Q_\mu\rvert^{2}\bigr)^{1/2}$. The two parts of a product $f$ are $f_{+}=\tfrac12(f+E(f))$ and $f_{-}=\tfrac12(f-E(f))$, with $E(f)(\tilde{P},\tilde{Q})=f(\tilde{Q},\tilde{P})$, and the twelve codes $\mathrm{GPA},\mathrm{SPA},\mathrm{APA},\mathrm{GQA},\mathrm{SQA},\mathrm{AQA},\mathrm{GPS},\mathrm{SPS},\mathrm{APS},\mathrm{GQS},\mathrm{SQS},\mathrm{AQS}$ are those of *The 12 Products of the Biquaternion Complex Space*. The vector subspace, the centre and the two sectors $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$ are those of *Introduction to the Six Subspaces*.

## The Scalar Part, and the Two Facts That Distribute the Twelve

**Definition (the scalar part of an operation).** Let $f$ be one of the four general products or one of its two halves. Its **scalar part** is the map

$$
(\tilde{P},\tilde{Q})\mapsto\text{the scalar coordinate of }f(\tilde{P},\tilde{Q}),
$$

a form on $\mathbb{B}\times\mathbb{B}$ with values in $\mathbb{C}$ for the four general products, in $\mathbb{C}$ for the two halves of a bilinear product and in the real or the purely imaginary numbers for the two halves of a sesquilinear product. The scalar part is the object from which the metric is read, and it is the object the corpus takes when it quotes the four pairings above: each of the four brackets **is** the scalar part of the product of the same name (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*, §*The scalar–vector form*).

Two facts decide how the twelve distribute over the forms, and both are immediate from the definitions.

**Fact 1 (the scalar part of the two bilinear products is symmetric).** For the plain product $\tilde{P}\tilde{Q}$ and the quaternionic product $\tilde{P}^{\natural}\tilde{Q}$ the scalar part is unchanged when the two arguments are exchanged:

$$
\langle\tilde{Q},\tilde{P}\rangle=\langle\tilde{P},\tilde{Q}\rangle,\qquad
\langle\tilde{Q},\tilde{P}\rangle_{\natural}=\langle\tilde{P},\tilde{Q}\rangle_{\natural}.
$$

Consequently the symmetric half of a bilinear product has the **same** scalar part as the product, and the antisymmetric half has the **zero** scalar part. This is why $\mathrm{APA}$ and $\mathrm{AQA}$ carry no form, and why the two bilinear forms of the table below are each carried by two operations.

**Fact 2 (the scalar part of the two sesquilinear products is Hermitian, not symmetric).** For the plain sesquilinear product $\tilde{P}\tilde{Q}^{*}$ and the general quaternionic sesquilinear product $\tilde{P}^{\natural}\tilde{Q}^{*}$ the exchanged scalar part is the conjugate:

$$
\langle\tilde{Q},\tilde{P}\rangle_{*}=\overline{\langle\tilde{P},\tilde{Q}\rangle_{*}},\qquad
\langle\tilde{Q},\tilde{P}\rangle_{\natural*}=\overline{\langle\tilde{P},\tilde{Q}\rangle_{\natural*}}.
$$

Consequently the scalar part of the symmetric half is the **half-sum of the form with its conjugate**, a real form, and the scalar part of the antisymmetric half is the **half-difference**, a purely imaginary alternating form:

$$
\text{scalar part of }\mathrm{SPS}:(\tilde{P},\tilde{Q})\mapsto\tfrac12\bigl(\langle\tilde{P},\tilde{Q}\rangle_{*}+\langle\tilde{Q},\tilde{P}\rangle_{*}\bigr),
\qquad
\text{scalar part of }\mathrm{APS}:(\tilde{P},\tilde{Q})\mapsto\tfrac12\bigl(\langle\tilde{P},\tilde{Q}\rangle_{*}-\langle\tilde{Q},\tilde{P}\rangle_{*}\bigr),
$$

and the same with the Krein form for $\mathrm{SQS}$ and $\mathrm{AQS}$. The half-sum is the real part of the Hermitian form; the half-difference, divided by the central imaginary, is the alternating form of the Hermitian form. This is why the four sesquilinear-row operations contribute four forms and not two.

**Remark (the metric is read from the scalar part, and the topology is not).** The scalar part gives the *metric* of an operation. It does not give the topology: a form on a finite-dimensional real space, definite or indefinite, is read inside the one vector-space topology, and its own topology, when it is definite, is that same topology (*Topology in the Space of Biquaternions*, §*The Topological Norm: Equivalence and Uniqueness*).

## The Eight Non-Vanishing Forms

The twelve operations carry the eight forms collected here. Each row names the form, the operations that carry it and the kind of object it is. All inertias are over $\mathbb{R}$; the complex signature is quoted only for the two Hermitian forms, where it is an invariant.

| # | form | carried by | kind | inertia | definite? |
|---|---|---|---|---|---|
| 1 | general plain bilinear $\langle\tilde{P},\tilde{Q}\rangle$ | $\mathrm{GPA}$, $\mathrm{SPA}$ | complex-valued, symmetric | $(4,4)$ (rank $4$ over $\mathbb{C}$) | no |
| 2 | general quaternionic bilinear $\langle\tilde{P},\tilde{Q}\rangle_{\natural}$ | $\mathrm{GQA}$, $\mathrm{SQA}$ | complex-valued, symmetric | $(4,4)$ (rank $4$ over $\mathbb{C}$) | no |
| 3 | Hermitian $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | $\mathrm{GPS}$ | complex Hermitian | $(8,0)$, complex signature $(4,0)$ | **yes** |
| 4 | real part of the Hermitian form | $\mathrm{SPS}$ | real-valued, symmetric | $(8,0)$ | **yes** |
| 5 | alternating form of the Hermitian form | $\mathrm{APS}$ | purely imaginary, alternating | rank $8$ | not a quadratic form |
| 6 | Krein $\langle\tilde{P},\tilde{Q}\rangle_{\natural*}$ | $\mathrm{GQS}$ | complex Hermitian | $(2,6)$, complex signature $(1,3)$ | no |
| 7 | real part of the Krein form | $\mathrm{SQS}$ | real-valued, symmetric | $(2,6)$ | no |
| 8 | alternating form of the Krein form | $\mathrm{AQS}$ | purely imaginary, alternating | rank $8$ | not a quadratic form |

The two remaining operations, $\mathrm{APA}$ and $\mathrm{AQA}$, carry the zero form, by Fact 1. The bold rows are the positive definite ones, and there is exactly one positive definite real symmetric form on the list, row 4, carried by $\mathrm{SPS}$. Row 3 is the same metric data in complex Hermitian form: the real form of row 3 is row 4.

## The Twelve, One by One

Each operation is read in the fixed order: the operation and its scalar part; the inertia and the definiteness of that form; the **topological objects it owns** — its level set and its isometry group; and its **metric verdict**, which is a statement about the diagonal route and the symmetry route of *The Four Pairings of the Biquaternion Algebra*.

### GPA — general plain algebra

The operation is the multiplication $\tilde{P}\tilde{Q}$ itself. Its scalar part is the general plain bilinear form $\langle\tilde{P},\tilde{Q}\rangle=\sum_\mu\varepsilon_\mu P_\mu Q_\mu$, whose coefficient Gram matrix is $\operatorname{diag}(1,-1,-1,-1)$: realification $(4,4)$ and no complex inertia (over $\mathbb{C}$ this form is the standard one, of rank $4$ alone, and it is congruent to the general quaternionic bilinear form), **indefinite**, with non-zero null elements, the first witness being $\langle e_0+e_1,e_0+e_1\rangle=1-1=0$.

**Topology.** The operation introduces no topology; its scalar part owns the level set $\{\langle\tilde{Q},\tilde{Q}\rangle=1\}$, a non-compact complex quadric of real dimension $6$ that is not a group, and the isometry group $O_4(\mathbb{C})$ of real dimension $12$ (*The Four Pairings of the Biquaternion Algebra*). The values of the operation fill the whole space.

**Metric.** The diagonal route stops at the indefiniteness, and with the null element it stops twice (*The Four Pairings of the Biquaternion Algebra*, §*The Forms in Comparison*). The form is nevertheless a metric: through its symmetry, the Hermitian conjugation, its distance is the Euclidean one. So $\mathrm{GPA}$ carries an **indefinite metric** and no norm.

### SPA — symmetric plain algebra

The operation is the half-sum $\tfrac12(\tilde{P}\tilde{Q}+\tilde{Q}\tilde{P})$, the commutative product of the plain row, the Jordan product of *The 12 Products of the Biquaternion Complex Space*. By Fact 1 its scalar part is **the same general plain bilinear form** as that of $\mathrm{GPA}$, with the same realification $(4,4)$ and the same null elements; the symmetrisation adds the cross term away but leaves the scalar part untouched, the cross term being of trace zero.

**Topology.** The same level set and the same isometry group as $\mathrm{GPA}$. The operation's own topological interest is elsewhere: being commutative and satisfying the Jordan identity, it makes of the form a Jordan product, and its Hermitian subspace is the Hermitian Jordan algebra $J(\mathbb{B})$.

**Metric.** The same indefinite metric as $\mathrm{GPA}$, and no norm by the diagonal; the same Euclidean distance by the symmetry. $\mathrm{GPA}$ and $\mathrm{SPA}$ are **two operations with one metric**.

### APA — antisymmetric plain algebra

The operation is the half-difference $\tfrac12(\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P})=\mathbf{P}\times\mathbf{Q}$, the cross product of the two vector parts. By Fact 1 its scalar part **vanishes identically**: the operation carries no form at all, and neither the diagonal route nor the symmetry route applies to it.

**Topology.** The operation owns no level set and no isometry group, its values lying in the vector subspace. What it does own is the whole Lie structure of the algebra: it is the one operation of the twelve that is alternating and satisfies the Jacobi identity, and its bracket is the Lie bracket of *The Unitary Lie Algebra*.

**Metric.** No metric from a scalar part. The bracket nevertheless owns a metric of its own kind, the **Killing form** of the Lie algebra it defines (*The Killing Form Operator*). On the six real dimensions of the vector subspace the Killing form is non-degenerate of inertia $(3,3)$, and on the two real dimensions of the centre it vanishes, so the Killing form of the bracket has inertia $(3,3)$ with a two-dimensional radical, the centre. It is a second metric, not read from the scalar part of the operation, and the contrast with $\mathrm{SQA}$ is exact: each of the two operations that satisfies the identity of its name owns a canonical metric, the commutative one through its trace form, which is its scalar part, and the alternating one through its Killing form, which is not.

### GQA — general quaternionic algebra

The operation is $\tilde{P}^{\natural}\tilde{Q}$, the plain product with the first factor read through the natural conjugation. Its scalar part is the general quaternionic bilinear form $\langle\tilde{P},\tilde{Q}\rangle_{\natural}=\sum_\mu P_\mu Q_\mu$, of Gram matrix the identity: realification $(4,4)$, and no complex inertia, since over $\mathbb{C}$ it is congruent to the general plain bilinear form above, **indefinite**, with null cone the zero-divisor cone of the algebra, the witness being $\langle e_1+ie_2,e_1+ie_2\rangle_{\natural}=1+(\text{the central imaginary})^{2}=0$. Its diagonal is the **biquaternion norm** $N(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$, which is multiplicative, $N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q)$, and which decides invertibility: $\tilde Q$ is invertible exactly when $N(\tilde Q)\neq0$ (*Biquaternion Norm and Invertibility*). The multiplicativity belongs to the norm and to its polar form taken on the diagonal; the polar bilinear form itself is not multiplicative in either argument.

**Topology.** Its level set $\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=1\}$ is a non-compact real $6$-manifold homotopy equivalent to $S^{3}$, and it is the only level set of the twelve that is a group, the norm-one group $\mathbb{B}^{\times}_{1}$. Its isometry group is $O_4(\mathbb{C})$, the same group as that of the general plain bilinear form, the two forms being equivalent over $\mathbb{C}$.

**Metric.** No norm by the diagonal, at the null cone and at the negative value $\langle e_1,e_1\rangle_{\natural*}$ of the companion form; the metric is indefinite, and its distance is the Euclidean one through its symmetry, the complex conjugation.

### SQA — symmetric quaternionic algebra

The operation is $\tfrac12(\tilde{P}^{\natural}\tilde{Q}+\tilde{Q}^{\natural}\tilde{P})$, which by Fact 1 has scalar part **$P_0Q_0+(\mathbf{P},\mathbf{Q})$**, the same general quaternionic bilinear form as that of $\mathrm{GQA}$. Its values lie in the centre, so it is the operation that *is* the bilinear form read as a product: a commutative product with values in the two-dimensional centre $\mathbb{C}_{\mathbb{B}}$ and with no unit.

**Topology.** The same level set, the norm-one group, and the same isometry group $O_4(\mathbb{C})$ as $\mathrm{GQA}$; the two operations are two readings of one object, the form as a pairing and the form as a product.

**Metric.** The same indefinite metric as $\mathrm{GQA}$, with the same verdict: no norm by the diagonal, the Euclidean distance by the symmetry. $\mathrm{GQA}$ and $\mathrm{SQA}$ are the second **pair of operations with one metric**.

### AQA — antisymmetric quaternionic algebra

The operation is $\tfrac12(\tilde{P}^{\natural}\tilde{Q}-\tilde{Q}^{\natural}\tilde{P})$, the quaternionic product with its scalar part removed; its values are in the vector subspace. By Fact 1 its scalar part **vanishes identically**, so it carries no form, no level set and no metric. It is alternating but **fails** the Jacobi identity, with witness $(e_0,e_1,e_2)$, and therefore owns no Killing form either: of the two operations with no scalar part, $\mathrm{APA}$ owns a canonical metric and $\mathrm{AQA}$ does not.

**Topology and metric.** No topological object of its own beyond its image, the vector subspace; and no metric from its scalar part and no Killing form. It is the operation of the twelve with the least geometric content, and that is a fact about it, not a defect of the reading.

### GPS — general plain sesqualgebra

The operation is the sesquilinear product $\tilde{P}\tilde{Q}^{*}$, the multiplication of *Introduction to the General Plain Sesqualgebra of Biquaternions*. Its scalar part is the Hermitian form $\langle\tilde{P},\tilde{Q}\rangle_{*}=\sum_\mu P_\mu\overline{Q_\mu}$, of Gram matrix the identity and signature $(8,0)$: **positive definite**, and it is the only one of the four general products whose scalar part is.

**Topology.** Its level set is the sphere $S^{7}$, compact, not a group, and meeting the null cone of the general quaternionic bilinear form in a compact $5$-manifold; its isometry group is $U(4)$, of real dimension $16$ and compact (*The Euclidean Topology of the Biquaternion Algebra*, *The Unitary Group of the Biquaternion Algebra*).

**Metric.** The diagonal route **succeeds**: $\bigl(\langle\tilde{Q},\tilde{Q}\rangle_{*}\bigr)^{1/2}=\lVert\tilde{Q}\rVert_E$ is a norm, the Euclidean norm of the region. So $\mathrm{GPS}$ carries the positive definite metric, and every other metric of the twelve is compared with this one.

### SPS — symmetric plain sesqualgebra

The operation is the half-sum $\tfrac12(\tilde{P}\tilde{Q}^{*}+\tilde{Q}\tilde{P}^{*})$, the Hermitian part of the value of the sesquilinear product; its values lie in the Hermitian subspace $\mathbb{M}_{+}$. By Fact 2 its scalar part is the half-sum of the Hermitian form with its conjugate, a **real** form, and that form is the Euclidean form: at $\tilde{P}=\tilde{Q}$ it reads $p_0^{2}+p_0^{\prime2}+p_1^{2}+p_1^{\prime2}+p_2^{2}+p_2^{\prime2}+p_3^{2}+p_3^{\prime2}=\lVert\tilde{P}\rVert_E^{2}$, of signature $(8,0)$.

**Topology.** The same level set $S^{7}$ and the same group $U(4)$ as $\mathrm{GPS}$, since the real part of the Hermitian form has the same isometries as the Hermitian form.

**Metric.** This is the one operation of the twelve whose scalar part is **both symmetric, hence a quadratic form on the whole real space, and positive definite**. It is the operation that carries the positive definite metric as an operation of the twelve, in the same sense in which $\mathrm{SQA}$ carries the bilinear form as a product: $\mathrm{GPS}$ carries the form as a pairing, $\mathrm{SPS}$ carries it as a symmetric operation. The two carry the same metric data, and the same norm.

### APS — antisymmetric plain sesqualgebra

The operation is the half-difference $\tfrac12(\tilde{P}\tilde{Q}^{*}-\tilde{Q}\tilde{P}^{*})$, the skew-Hermitian part of the value of the sesquilinear product; its values lie in the anti-Hermitian subspace $\mathbb{M}_{-}$. By Fact 2 its scalar part is the half-difference of the Hermitian form with its conjugate, which is purely imaginary and, divided by the central imaginary, is the **alternating form**

$$
\omega(\tilde{P},\tilde{Q})=p'_0q_0-p_0q'_0+p'_1q_1-p_1q'_1+p'_2q_2-p_2q'_2+p'_3q_3-p_3q'_3 .
$$

It is alternating, non-degenerate, of rank $8$ over the real space, and it satisfies no definiteness condition of any kind: an alternating form has no diagonal.

**Topology.** An alternating form owns no quadratic level set and no sphere. Its isometry group is the real symplectic group $Sp(8,\mathbb{R})$ of real dimension $36$, and the part of it that is complex-linear is exactly the unitary group $U(4)$: if a complex-linear $A$ preserves the form, then $\operatorname{Im}(\tilde{P}^{\dagger}A^{\dagger}A\tilde{Q})=\operatorname{Im}(\tilde{P}^{\dagger}\tilde{Q})$ for all $\tilde{P},\tilde{Q}$, and the map $M\mapsto\bigl[(\tilde{P},\tilde{Q})\mapsto\operatorname{Im}(\tilde{P}^{\dagger}M\tilde{Q})\bigr]$ is injective on Hermitian matrices, since $\operatorname{Im}(\tilde{P}^{\dagger}M\tilde{Q})=0$ for all $\tilde{P},\tilde{Q}$ forces the Hermitian form $\tilde{P}^{\dagger}M\tilde{Q}$ to be real-valued, hence $M=0$; so $A^{\dagger}A=\mathrm{I}$ and $A\in U(4)$. Its isotropic subspaces are the Lagrangian planes, of real dimension $4$.

**Metric.** No norm **on the diagonal**, because the diagonal of an alternating form vanishes identically; and no symmetric metric tensor, because the form is skew. The operation carries a **symplectic form**, the imaginary part of the Hermitian form, which measures oriented area rather than length, and its compatible structure is the complex structure of multiplication by the central imaginary: $\omega(\tilde P,\tilde Q)=\operatorname{Re}\langle\tilde P\ (\text{the central imaginary})\tilde Q\rangle_{*}$, and the inner product on the right is the Euclidean one, so the symmetry route returns the same norm $\lVert\cdot\rVert_E$ and the same distance as the other eleven operations. This is the operation that shows that the scalar part of an operation of the twelve need not be a symmetric metric at all, and that even so it carries the one norm of the algebra.

### GQS — general quaternionic sesqualgebra

The operation is $\tilde{P}^{\natural}\tilde{Q}^{*}$, both slots read through a conjugation. Its scalar part is the Krein form $\langle\tilde{P},\tilde{Q}\rangle_{\natural*}=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$, of Gram matrix $\operatorname{diag}(1,-1,-1,-1)$ in the coefficient basis: realification $(2,6)$ and complex signature $(1,3)$, both invariants, **indefinite**, with the centre as its positive part of complex dimension one and the vector subspace as its negative part of complex dimension three.

**Topology.** Its level sets are the hyperboloids $S^{1}\times\mathbb{R}^{6}$ and $S^{5}\times\mathbb{R}^{2}$, with the null set between them, of real dimension $7$, and its isometry group is $U(1,3)$, of real dimension $16$ and non-compact (*The Krein Gram Matrix and the Restrictions of the Form*, *The Krein Level Sets and the Hyperbolic Structure*). Its signature is the one the algebra carries as a Pontryagin space, of negative index $3$ over $\mathbb{C}$.

**Metric.** No norm by the diagonal — the diagonal vanishes on $e_0+e_1$ and is negative on $e_1$ — and an indefinite metric by the form itself; the distance is the Euclidean one through its symmetry, the natural conjugation (*The Fundamental Symmetry of the Biquaternion Algebra*).

### SQS — symmetric quaternionic sesqualgebra

The operation is the half-sum $\tfrac12(\tilde{P}^{\natural}\tilde{Q}^{*}+\tilde{Q}^{\natural}\tilde{P}^{*})$, whose values lie in no subspace of the six. By Fact 2 its scalar part is the half-sum of the Krein form with its conjugate, a **real** form of signature $(2,6)$: at $\tilde{P}=\tilde{Q}$ it reads

$$
p_0^{2}+p_0^{\prime2}-p_1^{2}-p_1^{\prime2}-p_2^{2}-p_2^{\prime2}-p_3^{2}-p_3^{\prime2},
$$

the real part of the Krein form, indefinite with one positive and three negative complex dimensions.

**Topology.** The same level sets — $S^{1}\times\mathbb{R}^{6}$ for the value $1$, $S^{5}\times\mathbb{R}^{2}$ for the value $-1$, the null cone between them — and the same group $U(1,3)$ as $\mathrm{GQS}$.

**Metric.** No norm by the diagonal; an indefinite metric whose distance is the Euclidean one through the symmetry. So $\mathrm{SQS}$ is the operator that carries the indefinite Krein metric as a symmetric operation, the exact counterpart of $\mathrm{SPS}$ in the other sesquilinear row. Together, $\mathrm{SPS}$ and $\mathrm{SQS}$ are the two of the twelve whose scalar parts are symmetric **and** non-complex-valued on the whole space, and they are the definite and the indefinite cases of one construction.

### AQS — antisymmetric quaternionic sesqualgebra

The operation is the half-difference $\tfrac12(\tilde{P}^{\natural}\tilde{Q}^{*}-\tilde{Q}^{\natural}\tilde{P}^{*})$, whose values lie in no subspace of the six. By Fact 2 its scalar part is the half-difference of the Krein form with its conjugate, purely imaginary, and divided by the central imaginary it is the **alternating form of the Krein form**,

$$
\omega_{\natural}(\tilde{P},\tilde{Q})=p'_0q_0-p_0q'_0-p'_1q_1+p_1q'_1-p'_2q_2+p_2q'_2-p'_3q_3+p_3q'_3 ,
$$

alternating, of rank $8$, with the signs of the vector part reversed against the alternating form of the Hermitian form; the two alternating forms of the twelve are the two sign patterns of one expression.

**Topology.** As for $\mathrm{APS}$, no quadratic level set; the isometry group is $Sp(8,\mathbb{R})$, complex-linear part $U(4)$; the isotropic subspaces are Lagrangian.

**Metric.** A symplectic form and no metric. With $\mathrm{AQS}$ the list of the twelve is closed, and the count of the metrics among them is complete: **one definite metric, three indefinite real symmetric forms, two symplectic forms, and two operations with no form at all**.

## The Table of the Twelve

The situation of each operation, in one table. The fourth column is the form of the third; the last two columns are read from that form.

| operation | scalar part | form | realification | definite? | level set | isometry group (complex-linear) |
|---|---|---|---|---|---|---|
| $\mathrm{GPA}$ | complex | general plain bilinear | $(4,4)$ | no | complex quadric, dim $6$ | $O_4(\mathbb{C})$ |
| $\mathrm{SPA}$ | complex | general plain bilinear | $(4,4)$ | no | complex quadric, dim $6$ | $O_4(\mathbb{C})$ |
| $\mathrm{APA}$ | zero | — | — | — | — | — |
| $\mathrm{GQA}$ | complex | general quaternionic bilinear | $(4,4)$ | no | norm-one group $\simeq S^{3}$ | $O_4(\mathbb{C})$ |
| $\mathrm{SQA}$ | complex | general quaternionic bilinear | $(4,4)$ | no | norm-one group $\simeq S^{3}$ | $O_4(\mathbb{C})$ |
| $\mathrm{AQA}$ | zero | — | — | — | — | — |
| $\mathrm{GPS}$ | complex Hermitian | Hermitian | $(8,0)$ | **yes** | sphere $S^{7}$ | $U(4)$ |
| $\mathrm{SPS}$ | real | real part of the Hermitian form | $(8,0)$ | **yes** | sphere $S^{7}$ | $U(4)$ |
| $\mathrm{APS}$ | purely imaginary | alternating form of the Hermitian form | rank $8$ | — | — | $Sp(8,\mathbb{R})$ |
| $\mathrm{GQS}$ | complex Hermitian | Krein | $(2,6)$ | no | $S^{1}\times\mathbb{R}^{6}$, $S^{5}\times\mathbb{R}^{2}$ | $U(1,3)$ |
| $\mathrm{SQS}$ | real | real part of the Krein form | $(2,6)$ | no | $S^{1}\times\mathbb{R}^{6}$, $S^{5}\times\mathbb{R}^{2}$ | $U(1,3)$ |
| $\mathrm{AQS}$ | purely imaginary | alternating form of the Krein form | rank $8$ | — | — | $Sp(8,\mathbb{R})$ |

**Remark (two isometry groups of one form).** The group quoted in the tables is the group of isometries that are **complex-linear**, the group with which the level sets are read and the group the corpus names in *The Four Pairings of the Biquaternion Algebra*. The realification of the same form is a real form on $\mathbb{R}^{8}$, and its isometry group is the larger real group: $O(4,4)$ of real dimension $28$ for the two bilinear forms, $O(8)$ of real dimension $28$ for the Hermitian form, $O(2,6)$ of real dimension $28$ for the Krein form, against $Sp(8,\mathbb{R})$ of real dimension $36$ for the alternating forms. One form therefore carries two isometry groups, one complex-linear and one real, and the two are quoted apart in the literature: a reader who meets $O_4(\mathbb{C})$ and $O(4,4)$ for the same form has met the two, not a contradiction.

Two readings of the table are worth naming. The **rows pair up**: the two operations of a bilinear row share one row of the table, and the two operations that split a sesquilinear form share the level sets and the group of their general product while carrying different forms. The **columns separate the two questions**: the last two columns, the level set and the isometry group, are the topological objects an operation owns, and they are genuinely distinct spaces and distinct groups; the column of the realification is the metric datum, and it is the column the article is about.

## One Topology for the Twelve

The twelve operations give one topology, and the reasons are two: every form of the list is non-degenerate and of finite dimension, so every one of them supplies a distance through a symmetry; and all norms on a finite-dimensional real space are equivalent, so any two of those distances induce the same topology. The algebra is $\mathbb{R}^{8}$ as a topological space, the twelve operations are read in its one topology, and the eight forms of the table do not add a second one.

**Remark (the indefinite form gives a norm through its symmetry, not a second topology).** For the indefinite forms the symmetry does two things and only the first is a topological statement. It turns the form into a definite inner product, $\mathrm{Re}\,\Phi(\tilde P,J\tilde Q)$, and hence into a **norm**, $\lVert\tilde P\rVert_J^{2}=\mathrm{Re}\,\Phi(\tilde P,J\tilde P)$; and that norm is a norm **on the same real space**, so it induces the same topology as $\lVert\cdot\rVert_E$, by the equivalence of norms in finite dimension. The construction is therefore how an indefinite form still carries a norm, and it is never how it carries a second topology. In the Krein-space vocabulary the same fact reads: the **Krein norm** of an indefinite inner product is a definite norm, and a Krein space is a space **complete** in it. Completeness is a property that can differ between two norms only in infinite dimension; the algebra is $8$-dimensional, so the distinction cannot arise here and the Krein form gives no exception to the uniqueness of the topology.

**Remark (the two senses of *metric*).** The word is used here in two senses and they are not the same sense. A **metric tensor** is a non-degenerate form, definite or indefinite, symmetric or Hermitian; that is what the table lists, and of those there are several, the four forms of the region, of inertia $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$, plus the two alternating forms. A **metric**, in the sense of a distance function, is what a symmetry of the form returns; and of those there is exactly one, the Euclidean distance, because the symmetry of each of the four forms returns the general plain sesquilinear form, so the four distances coincide. So "several metrics" is true of the tensors and false of the distances, and the sentence "$\mathrm{GPA}$ carries an indefinite metric and no norm" means exactly this: it carries a metric tensor of inertia $(4,4)$, from which the diagonal route reads no norm, while the distance it induces through its symmetry is the Euclidean one, shared with the other eleven.

**Remark (one definite norm, reached by two routes).** The two routes give a definite norm under different conditions, and they end at the same norm. The **diagonal route**, reading the length from $\Phi(\tilde Q,\tilde Q)$ alone, gives a norm exactly when the form is positive definite; that is the case for the forms carried by $\mathrm{GPS}$ and $\mathrm{SPS}$, and the norm is $\lVert\cdot\rVert_E$. The **symmetry route**, reading the length from $\mathrm{Re}\,\Phi(\tilde Q,J\tilde Q)$, gives a norm for **every** non-degenerate form; and the norm it gives is again $\lVert\cdot\rVert_E$, because each symmetry returns the same definite form. So the twelve operations carry exactly one definite norm, $\lVert\cdot\rVert_E$, and the two routes differ only in how wide a class of forms reaches it: the diagonal route for the definite forms, the symmetry route for all of them. Alongside it the algebra carries its own norm, the complex-valued multiplicative biquaternion norm, which is a norm in the algebraic sense and not a definite one; the indefinite forms are not normless, they are normless **on the diagonal**. (On $\mathbb{R}^{8}$ in general there are many other norms; all are equivalent and give the one topology, and none of them is read from these forms.)

What the eight forms distinguish is not a topology but a **geometry**: an inertia, a level set, a group of isometries, and a definite or indefinite or alternating character. The one topological statement in which the forms genuinely differ is the one about their **isometry groups**, which are distinct closed subgroups of $GL_{8}(\mathbb{R})$ and hence distinct topological groups, and the one about their **level sets**, which are distinct subspaces read in the common topology by taking the subspace topology. Both are in the table.

## The Definite and the Indefinite, and the Groups of Motions

The article closes with the reading that separates the definite rows of the table from the indefinite ones, because the difference is not an accident of the coordinate signs.

On the **anti-Hermitian sector** $\mathbb{M}_{-}$, the real $4$-dimensional sector the antisymmetric part $\mathrm{APS}$ takes its values in, the four forms of the region restrict to four real forms, of inertia

$$
(3,1)\ \text{for the general quaternionic bilinear form},\qquad (1,3)\ \text{for the Krein form},
\qquad (4,0)\ \text{for the Hermitian form},\qquad (0,4)\ \text{for the general plain bilinear form}.
$$

The first two are indefinite and the last two are definite up to sign, and the difference shows in the groups that preserve them. Take the six-dimensional algebra of infinitesimal motions of the indefinite form of inertia $(3,1)$ on $\mathbb{M}_{-}$: the definite restrictions of the sector are preserved only by its three-dimensional compact part, while the indefinite restrictions are preserved by all six dimensions. And the space of symmetric forms on $\mathbb{M}_{-}$ that is preserved by the whole six-dimensional algebra is **one-dimensional**, spanned by the form of inertia $(3,1)$ itself.

The consequences are these, and they are the mathematical form of a familiar statement in the physics part of the corpus.

- An **indefinite form is a metric, and it carries no norm on its diagonal**. It has null vectors, its "unit sphere" is unbounded along them, and no norm comes from reading its diagonal; its distance comes from the symmetry route, and the metric it defines is the indefinite one. The norm it does carry is the common one, $\lVert\cdot\rVert_E$. This is the situation of rows 1, 2, 6 and 7 of the table.
- A **group of motions of the indefinite kind cannot preserve a positive definite form**. In the sector above, the forms invariant under the full six-dimensional algebra are a one-parameter family, all of them of inertia $(3,1)$, and every one of them is indefinite. So of the four restrictions, the two that are preserved by the whole algebra are exactly the two indefinite ones: the definite metric of the sector is preserved only by the rotations, and the indefinite metric is the one the full algebra of motions fixes.
- **The operation of the twelve that carries the definite metric** is $\mathrm{SPS}$, and it is also the operation of the plain sesquilinear row, whose antisymmetric companion $\mathrm{APS}$ takes its values in the sector just examined. The definite metric and the indefinite one are companions in one row of the table, which is why the same twelve operations support both readings.

The reading of the last two items in the rest of the corpus is *Biquaternion Automorphisms and Derivations*, where the group of the indefinite form appears as the automorphism group of the algebra, and *Biquaternion Lorentzian and Conformal Geometry*; the mathematics of the sector is *The Six Subspaces under the General Quaternionic Algebra of Biquaternions* and *The Six Subspaces under the General Plain Sesqualgebra of Biquaternions*.

## Summary

The twelve operations on the biquaternion space carry **one topology** and **ten scalar forms**. The topology is the single Hausdorff vector-space topology of $\mathbb{R}^{8}$, in which every operation and every one of its forms is read; the forms are the scalar parts of the operations, and they are what differs from operation to operation. Of the ten, two vanish, the two antisymmetric parts of the bilinear rows, whose products have a symmetric scalar part; two pairs of operations share one form each, the general plain bilinear form between $\mathrm{GPA}$ and $\mathrm{SPA}$ and the general quaternionic bilinear form between $\mathrm{GQA}$ and $\mathrm{SQA}$; and the four sesquilinear-row operations separate into the two Hermitian forms, carried by $\mathrm{GPS}$ and $\mathrm{GQS}$, and the two real and the two alternating forms they induce, carried by the symmetric halves $\mathrm{SPS}$ and $\mathrm{SQS}$ and the antisymmetric halves $\mathrm{APS}$ and $\mathrm{AQS}$. Exactly one of the eight is a positive definite symmetric real form, the real part of the Hermitian form carried by $\mathrm{SPS}$; the diagonal route therefore reaches a definite norm for $\mathrm{GPS}$ and $\mathrm{SPS}$ alone and stops for the other ten, while the symmetry route reaches the same norm, $\lVert\cdot\rVert_E$, for all twelve; the algebra's own norm, the multiplicative biquaternion norm $N$, is complex-valued and is not a definite norm, so a count of definite norms does not count it. The indefinite forms are not deficient: each is a metric, each gives the Euclidean distance through its symmetry, and each owns its level set and its isometry group, which are the objects the metric names of the region are true of. The two operations with no scalar part are $\mathrm{APA}$ and $\mathrm{AQA}$; $\mathrm{APA}$ owns a metric of its own through the Killing form of the Lie bracket it defines, of inertia $(3,3)$ with the centre as radical, and $\mathrm{AQA}$ owns none.

## Further Reading

- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the twelve names, their products, their laws and their images
- *Topology in the Space of Biquaternions* (`articles_maths/topology-in-the-space-of-biquaternions.md`), for the one topology that all twelve share
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms, their Gram matrices, their signatures, their isometry groups and their restrictions to the six subspaces, and for row 1 of the table
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the four general products whose scalar parts are the four forms
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`) and *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for rows 3 and 4, the sphere $S^{7}$ and the normed-algebra inequality
- *The Krein Gram Matrix and the Restrictions of the Form* (`articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.md`) and *The Krein Level Sets and the Hyperbolic Structure* (`articles_maths/the-krein-level-sets-and-the-hyperbolic-structure.md`), for rows 6 and 7 and the hyperboloids
- *The Fundamental Symmetry of the Biquaternion Algebra* (`articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.md`), for the symmetry of the Krein form and the fundamental decomposition
- *The Killing Form Operator* (`articles_maths/the-killing-form-operator.md`) and *The Unitary Lie Algebra* (`articles_maths/the-unitary-lie-algebra.md`), for the bracket of $\mathrm{APA}$ and its Killing form
- *The Six Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`) and *The Six Subspaces under the General Plain Sesqualgebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-plain-sesqualgebra-of-biquaternions.md`), for the restrictions of §*The Definite and the Indefinite*
- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the centre, the vector subspace and the two sectors named in the Conventions
- *Biquaternion Lorentzian and Conformal Geometry* (`articles_maths/biquaternion-lorentzian-and-conformal-geometry.md`) and *Biquaternion Automorphisms and Derivations* (`articles_maths/biquaternion-automorphisms-and-derivations.md`), for the reading of the indefinite metric of the sector and of the group that preserves it
