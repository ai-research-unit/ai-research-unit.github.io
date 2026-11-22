# __Classification of the Real Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups in $M_2(\mathbb{C})$__

## Introduction

**The question.** The complex operator algebra is $\mathcal{E}_{\mathbb{C}}=\operatorname{End}_{\mathbb{C}}(M_2(\mathbb{C}))\cong M_4(\mathbb{C})$, with the two real forms $M_4(\mathbb{R})$ and $M_2(\mathbb{H})$. This article describes the two forms layer by layer: the associative subalgebras, the Lie subalgebras with their Killing forms, the Jordan layer, and the Lie groups attached to the Lie algebras.

**Why it is the same statement.** This is the in-depth matrix reading of [Classification of the Real Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups](classification-of-the-real-structures-of-the-operators-of-the-biquaternion-algebra.html). The source works in the abstract operator algebra; the display identifies it with $M_4(\mathbb{C})$ and writes every subalgebra as a set of explicit matrices. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The two real forms, with the trace-form inertia that separates them. The biquaternion base inside each form: the regular families $\mathrm I_2\otimes M_2(\mathbb{C})$ and $M_2(\mathbb{C})^{\mathsf T}\otimes\mathrm I_2$, and the quaternion copy $L(\mathbb{H})$. The module dictionary for the semisimple associative subalgebras of $M_4(\mathbb{R})$, $\sum_i m_in_id_i=4$, and the seventeen isomorphism types. The corresponding dictionary for $M_2(\mathbb{H})$, $\sum_in_i\le2$. The Lie layer: $\mathfrak{gl}(4,\mathbb{R})=\mathfrak{sl}(4,\mathbb{R})\oplus\mathbb{R}\mathrm I_4$, the Killing form $8\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$, the inertia table, and the maximal subalgebras. The quaternionic Lie layer, with $\mathfrak{sl}(2,\mathbb{H})\cong\mathfrak{su}^{*}(4)$. The Jordan layer. The Lie groups, with the simply connected covers and the fundamental groups.

**What the article does not do.** It does not reprove the classification of the real forms, which is [Classification of the Structures of the Operators of the Biquaternion Algebra in $M_2(\mathbb{C})$](classification-of-the-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html), and it does not treat the complex structures of the split extension, which is [Classification of the Complex Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups in $M_2(\mathbb{C})$](classification-of-the-complex-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html). It states the Lie correspondence and does not prove it.

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$. The operator frame is the basis $(E_t,E_x,E_y,E_z)$ with $E_t=\mathrm I_2$, $E_x=-i\sigma_1$, $E_y=-i\sigma_2$, $E_z=-i\sigma_3$, and operators are $4\times4$ matrices in that basis. The left and right actors are $\mathrm I_2\otimes A$ and $B^{\mathsf T}\otimes\mathrm I_2$. The inertia of a symmetric form is the pair (positive, negative) of eigenvalue counts, so a compact simple algebra reads $(0,\dim)$.

**Boundaries.** The cone of products is [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html). The polar decomposition of an operator is [The Adjoints and the Polar Decomposition of an Operator at $n=2$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-2.html). The spin groups are [The Spin Group via $4\times4$ Real Matrices](the-spin-group-via-4x4-real-matrices-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Symmetric and Antisymmetric Parts of the Operator Space at $n=2$](the-symmetric-and-antisymmetric-parts-of-the-operator-space-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $\mathcal{E}_{\mathbb{H}}$ is $M_2(\mathbb{H})$ in the block model. $\mathfrak{sl}_2$ is the traceless part of $M_2(\mathbb{C})$. $K$ is the Killing form. $\mathcal{E}(A_0)$ is the two-sided span of a real form $A_0$.

## The Two Real Forms

**The algebra and its forms.** $\mathcal{E}_{\mathbb{C}}=M_4(\mathbb{C})$ has complex dimension sixteen and real dimension thirty-two. Its two real forms are
$$
M_4(\mathbb{R})\quad(\text{split}),\qquad M_2(\mathbb{H})\quad(\text{quaternionic}),
$$
both of real dimension sixteen, both central simple over $\mathbb{R}$.

**The two real structures.** $\tau_{\mathbb{R}}(X)=\bar X$ has fixed set $M_4(\mathbb{R})$, and $\tau_{\mathbb{H}}(X)=J_0\bar XJ_0^{-1}$ has fixed set the block model
$$
\mathcal{E}_{\mathbb{H}}=\left\{\begin{pmatrix}A&B\\-\bar B&\bar A\end{pmatrix}:A,B\in M_2(\mathbb{C})\right\}.
$$

**The table.**

| form | $\dim_{\mathbb{R}}$ | centre | trace-form inertia | simple part | Lie algebra |
|---|---|---|---|---|---|
| $M_4(\mathbb{R})$ | $16$ | $\mathbb{R}\mathrm I_4$ | $(10,6)$ | $\mathfrak{sl}(4,\mathbb{R})$ | $\mathfrak{gl}(4,\mathbb{R})$ |
| $M_2(\mathbb{H})$ | $16$ | $\mathbb{R}\mathrm I_4$ | $(6,10)$ | $\mathfrak{sl}(2,\mathbb{H})=\mathfrak{su}^{*}(4)$ | $\mathfrak{gl}(2,\mathbb{H})$ |

**Why not compact.** The compact real form of $\mathfrak{gl}(4,\mathbb{C})$ is $\mathfrak{u}(4)$, and no real form of the associative algebra has that Lie algebra, since the product of two skew-Hermitian matrices is skew-Hermitian only when the two commute. The simple part of the quaternionic form has maximal compact subalgebra of dimension ten out of fifteen. The words are split and quaternionic.

## The Biquaternion Base Inside Each Form

**The two regular families.** $\mathrm I_2\otimes M_2(\mathbb{C})$ and $M_2(\mathbb{C})^{\mathsf T}\otimes\mathrm I_2$ are commuting copies of $M_2(\mathbb{C})$, meeting in $\mathbb{C}\mathrm I_4$. Both consist of complex matrices, so both lie in the complexification of either real form; their real points are described by the next rows.

**In the split form.** The real points of the left family are $\mathrm I_2\otimes M_2(\mathbb{R})$, of real dimension four, and those of the right family are $M_2(\mathbb{R})^{\mathsf T}\otimes\mathrm I_2$. The two-sided span of $M_2(\mathbb{R})$ is all of $M_4(\mathbb{R})$, by the tensor identity $M_2(\mathbb{R})\otimes_{\mathbb{R}}M_2(\mathbb{R})^{\mathrm{op}}\cong M_4(\mathbb{R})$.

**In the quaternionic form.** The real points of the left family are
$$
\mathrm I_2\otimes\mathbb{H}=\left\{\begin{pmatrix}A&0\\0&A\end{pmatrix}\right\}\subset M_2(\mathbb{H}),
$$
a copy of $\mathbb{H}$ inside the block model, of real dimension four. It is the image $L(\mathbb{B}_H)$ of the quaternion space, and its traceless part is $\mathfrak{su}(2)$.

**The three distinguished base objects.** $L(M_2(\mathbb{C}))\cong M_2(\mathbb{C})$ of complex dimension four, $L(\mathbb{H})\cong\mathbb{H}$ of real dimension four, and $L(\mathfrak{sl}_2)$ of complex dimension three. The first is a maximal semisimple subalgebra of $M_4(\mathbb{R})$ up to conjugacy; the second is the smallest non-commutative one; the third is a subspace and not a subalgebra.

## Associative Subalgebras of the Split Form

**The principle.** A unital subalgebra of $M_4(\mathbb{R})$ is the same thing as a faithful module structure on $\mathbb{R}^4$, so the classification is a classification of module structures.

**Theorem (module dictionary).** Let $A\cong\prod_{i=1}^{r}M_{n_i}(D_i)$ be semisimple with $D_i\in\{\mathbb{R},\mathbb{C},\mathbb{H}\}$ and $d_i=\dim_{\mathbb{R}}D_i$. Then $A$ embeds unitally in $M_4(\mathbb{R})$ if and only if there are integers $m_i\ge1$ with
$$
\sum_{i=1}^{r}m_in_id_i=4 .
$$

*Proof.* The simple module of $M_{n_i}(D_i)$ is $D_i^{n_i}$ of real dimension $n_id_i$, and faithfulness forces $m_i\ge1$ on each factor.

**The count.** Exactly seventeen isomorphism types, with weights $1$ for $\mathbb{R}$, $2$ for $M_2(\mathbb{R})$ and $\mathbb{C}$, $3$ for $M_3(\mathbb{R})$, and $4$ for $M_4(\mathbb{R})$, $M_2(\mathbb{C})$ and $\mathbb{H}$. The largest proper type is $M_3(\mathbb{R})\oplus\mathbb{R}$ of dimension ten; $M_3(\mathbb{R})$ alone does not embed, since $4$ is not a multiple of $3$.

**The maximal semisimple types.** $M_2(\mathbb{C})$ and $M_2(\mathbb{R})\oplus M_2(\mathbb{R})$, both of dimension eight. An irreducible semisimple subalgebra has one factor and $m=1$ with $nd=4$, giving $M_4(\mathbb{R})$, $M_2(\mathbb{C})$ and $\mathbb{H}$, and $\mathbb{H}$ sits inside $M_2(\mathbb{C})$.

**The parabolics and the Borel.** The stabilizer of a line in $\mathbb{R}^4$ has dimension $1+3+9=13$, of a $2$-plane $4+4+4=12$, of a hyperplane $13$. The stabilizer of a complete flag is the upper triangular algebra, of dimension $4+3+2+1=10$.

**The biquaternion entries.** $L(M_2(\mathbb{R}))$ of dimension four, $L(\mathbb{H})$ of dimension four, and $L(\mathfrak{sl}_2)$ of dimension three as a space. The first two are subalgebras; the third is not, since the product of two traceless matrices is not traceless. Witness: $E_x^{2}=-\mathrm I_2$.

## Associative Subalgebras of the Quaternionic Form

**The criterion.** An embedding $A\hookrightarrow\operatorname{End}_{\mathbb{H}}(\mathbb{H}^2)$ is a faithful module structure over $A\otimes_{\mathbb{R}}\mathbb{H}^{\mathrm{op}}$ on a real space of dimension eight.

**Theorem (module dictionary).** For semisimple $A=\prod_iM_{n_i}(D_i)$ the embedding into $M_2(\mathbb{H})$ exists if and only if
$$
\sum_{i=1}^{r}n_i\le2 .
$$

*Proof.* $M_n(\mathbb{R})\otimes\mathbb{H}\cong M_n(\mathbb{H})$, $M_n(\mathbb{C})\otimes\mathbb{H}\cong M_{2n}(\mathbb{C})$ and $M_n(\mathbb{H})\otimes\mathbb{H}\cong M_{4n}(\mathbb{R})$, so each factor needs $4n_i$ real dimensions and the total is $4\sum_in_i\le8$.

**The comparison.** The split form requires $\sum m_in_id_i=4$ with all $m_i\ge1$; the quaternionic form requires $\sum_in_i\le2$. Neither list contains the other.

**The consequences.** No copy of $M_2(\mathbb{R})$ or $M_3(\mathbb{R})$ embeds in $M_2(\mathbb{H})$; the largest semisimple subalgebras are $\mathbb{H}$, $\mathbb{C}$ and $M_2(\mathbb{R})$, of real dimension four, for $\sum n_i=1$, and $\mathbb{C}\oplus\mathbb{C}$ and $\mathbb{C}\oplus\mathbb{H}$ are excluded because $\sum n_i=3$.

## Lie Subalgebras of the Split Form

**The algebra.** The commutator turns $M_4(\mathbb{R})$ into $\mathfrak{gl}(4,\mathbb{R})$, of real dimension sixteen, with centre $\mathbb{R}\mathrm I_4$ and
$$
\mathfrak{gl}(4,\mathbb{R})=\mathfrak{sl}(4,\mathbb{R})\oplus\mathbb{R}\mathrm I_4,\qquad \dim\mathfrak{sl}(4,\mathbb{R})=15,
$$
and $\mathfrak{sl}(4,\mathbb{R})$ simple of type $A_3$.

**The Killing form.** Computed from the adjoint representation,
$$
K(X,Y)=8\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y),
$$
verified on random pairs to $4\cdot10^{-15}$. Its radical is the centre, and on the traceless part it is $8\operatorname{tr}(XY)$, of inertia $(9,6)$.

**The inertia table.** The pair is (positive, negative); a null direction from the centre is recorded separately.

| subalgebra | $\dim_{\mathbb{R}}$ | type | $K$ inertia |
|---|---|---|---|
| $\mathfrak{gl}(4,\mathbb{R})$ | $16$ | $A_3\oplus T_1$ | $(9,6)$ plus one null |
| $\mathfrak{sl}(4,\mathbb{R})$ | $15$ | $A_3$ split | $(9,6)$ |
| $\mathfrak{sp}(2,\mathbb{R})$ | $10$ | $C_2$ split | $(6,4)$ |
| $\mathfrak{sl}(3,\mathbb{R})\oplus\mathbb{R}$ | $9$ | Levi | $(5,3)$ plus one null |
| $\mathfrak{so}(4)$ | $6$ | $D_2$ compact | $(0,6)$ |
| $\mathfrak{so}(3,1)$ | $6$ | $D_2$ Lorentzian | $(3,3)$ |
| $\mathfrak{so}(2,2)$ | $6$ | $D_2$ split | $(4,2)$ |
| $\mathfrak{gl}(2,\mathbb{R})$ | $4$ | $A_1\oplus T_1$ | $(2,1)$ plus one null |
| $\mathfrak{u}(2)$ | $4$ | compact reductive | $(0,3)$ plus one null |
| $\mathfrak{sl}(2,\mathbb{R})$ | $3$ | $A_1$ split | $(2,1)$ |
| $\mathfrak{su}(2)$ | $3$ | $A_1$ compact | $(0,3)$ |

**The three six-dimensional algebras.** $\mathfrak{so}(4)$, $\mathfrak{so}(3,1)$ and $\mathfrak{so}(2,2)$ are real forms of the one complex algebra $\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$ and are pairwise non-isomorphic, separated by their inertias.

**The maximal subalgebras.** Up to conjugacy: the two parabolics of dimensions twelve and eleven, the symplectic $\mathfrak{sp}(2,\mathbb{R})$ of dimension ten, the two Levi factors of dimensions nine and seven, the three $\mathfrak{so}$ algebras of dimension six, and an $\mathfrak{sl}(2,\mathbb{R})$ of dimension three acting irreducibly on $\operatorname{Sym}^3$.

**The biquaternion subalgebras.** $\mathfrak{sl}(2,\mathbb{R})\oplus\mathfrak{sl}(2,\mathbb{R})$ of dimension six sits inside $\mathfrak{so}(2,2)$; the compact $\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ sits inside $\mathfrak{so}(4)$; and the copy $\mathfrak{u}(2)$ comes from $\mathbb{B}_{\Phi}$.

## Lie Subalgebras of the Quaternionic Form

**The algebra.** $\mathfrak{gl}(2,\mathbb{H})$ of real dimension sixteen, with centre $\mathbb{R}\mathrm I_4$ and simple part
$$
\mathfrak{sl}(2,\mathbb{H})=\mathfrak{su}^{*}(4),\qquad \dim_{\mathbb{R}}=15,
$$
whose maximal compact subalgebra is $\mathfrak{sp}(2)$ of dimension ten and whose complement has dimension five.

**The table.**

| subalgebra | $\dim_{\mathbb{R}}$ | type | compact part |
|---|---|---|---|
| $\mathfrak{gl}(2,\mathbb{H})$ | $16$ | $A_3$ quaternionic $+T_1$ | $\mathfrak{sp}(2)\oplus\mathbb{R}$ |
| $\mathfrak{sl}(2,\mathbb{H})=\mathfrak{su}^{*}(4)$ | $15$ | $A_3$ quaternionic | $\mathfrak{sp}(2)$, $\dim10$ |
| $\mathfrak{sp}(2)$ | $10$ | $C_2$ compact | itself |
| $\mathfrak{sp}(1,1)$ | $10$ | $C_2$ non-compact | $\mathfrak{sp}(1)\oplus\mathfrak{sp}(1)$ |
| $\mathfrak{sp}(1)\oplus\mathfrak{sp}(1)\oplus\mathbb{R}$ | $7$ | Levi | itself |

**The two algebras of dimension ten.** $\mathfrak{sp}(2)$ and $\mathfrak{sp}(1,1)$ are real forms of $\mathfrak{sp}(2,\mathbb{C})$; the first is compact with killing inertia $(0,10)$, the second has inertia $(5,5)$.

**The biquaternion copy.** $\mathfrak{su}(2)=\mathfrak{sp}(1)$ sits inside $\mathfrak{sl}(2,\mathbb{H})$ as the traceless part of $L(\mathbb{H})$, and the pair $\mathfrak{sp}(1)\oplus\mathfrak{sp}(1)$ is the image of $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ under the two regular families.

## The Jordan Layer

**The symmetrized product.** $X\circ Y=\tfrac12(XY+YX)$ makes $M_4(\mathbb{C})^{+}$ a Jordan algebra, with the three real forms
$$
M_4(\mathbb{R})^{+},\qquad M_2(\mathbb{H})^{+},\qquad H_4(\mathbb{C}),
$$
of real dimension sixteen and trace-form inertias $(10,6)$, $(6,10)$ and $(16,0)$.

**The Peirce layer.** The idempotents of $M_4(\mathbb{C})^{+}$ include the two diagonal blocks $P_1\oplus P_2$ and the four coordinate projectors, and the Peirce decomposition of a Jordan algebra with two orthogonal idempotents is the matrix form of the corner decomposition of [One-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$](one-sided-operators-on-the-n-regular-sector-in-m2c.html).

**The Hermitian subspace.** $H_4(\mathbb{C})$ is closed under $\circ$, is not closed under the associative product, and has no associative real form above it. Its Lie shadow is $\mathfrak{u}(4)$, the compact form that has no associative model.

## The Lie Groups Attached to the Lie Algebras

**The correspondence.** Each real Lie algebra has a simply connected group, unique up to isomorphism; every connected group with that algebra is a quotient by a discrete central subgroup, and the fundamental group of the quotient is that subgroup.

**The split form.**

| algebra | simply connected group | centre | noteworthy quotient |
|---|---|---|---|
| $\mathfrak{gl}(4,\mathbb{R})$ | $\widetilde{SL(4,\mathbb{R})}\times\mathbb{R}$ | $\mathbb{Z}_2^{2}\times\mathbb{R}$ | $GL^{+}(4,\mathbb{R})\cong SL(4,\mathbb{R})\times\mathbb{R}_{>0}$, $\pi_1=\mathbb{Z}_2$ |
| $\mathfrak{sl}(4,\mathbb{R})$ | $\widetilde{SL(4,\mathbb{R})}$ | $\mathbb{Z}_2^{2}$ | $SL(4,\mathbb{R})$, $\pi_1=\mathbb{Z}_2$; $PSL(4,\mathbb{R})$, $\pi_1=\mathbb{Z}_2^{2}$ |
| $\mathfrak{sp}(2,\mathbb{R})$ | $\widetilde{Sp(2,\mathbb{R})}$ | $\mathbb{Z}$ | $Sp(2,\mathbb{R})$, $\pi_1=\mathbb{Z}$ |
| $\mathfrak{so}(4)$ | $Spin(4)=SU(2)\times SU(2)$ | $\mathbb{Z}_2^{2}$ | $SO(4)$, $\pi_1=\mathbb{Z}_2$ |
| $\mathfrak{so}(3,1)$ | $SL(2,\mathbb{C})$ | $\mathbb{Z}_2$ | $SO^{+}(3,1)$, $\pi_1=\mathbb{Z}_2$ |
| $\mathfrak{so}(2,2)$ | $\widetilde{SL(2,\mathbb{R})}^{2}$ | $\mathbb{Z}^{2}$ | $SO^{+}(2,2)\cong(SL(2,\mathbb{R})\times SL(2,\mathbb{R}))/\{\pm(\mathrm I,\mathrm I)\}$ |
| $\mathfrak{su}(2)$ | $SU(2)$ | $\mathbb{Z}_2$ | $SO(3)$, $\pi_1=\mathbb{Z}_2$ |

**The quaternionic form.**

| algebra | simply connected group | centre | noteworthy quotient |
|---|---|---|---|
| $\mathfrak{gl}(2,\mathbb{H})$ | $SL(2,\mathbb{H})\times\mathbb{R}$ | $\mathbb{Z}_2\times\mathbb{R}$ | $GL(2,\mathbb{H})\cong SL(2,\mathbb{H})\times\mathbb{R}_{>0}$, $\pi_1=0$ |
| $\mathfrak{sl}(2,\mathbb{H})$ | $SL(2,\mathbb{H})$ | $\mathbb{Z}_2$ | $PSL(2,\mathbb{H})\cong SO^{+}(5,1)$, $\pi_1=\mathbb{Z}_2$ |
| $\mathfrak{sp}(2)$ | $Sp(2)$ | $\mathbb{Z}_2$ | $SO(5)$, $\pi_1=\mathbb{Z}_2$ |
| $\mathfrak{sp}(1,1)$ | $Spin(4,1)$ | $\mathbb{Z}_2$ | $SO^{+}(4,1)$, $\pi_1=\mathbb{Z}_2$ |

**The five groups of $\mathfrak{sl}(4,\mathbb{R})$.** The centre of the cover is $\mathbb{Z}_2^{2}$, whose five subgroups give five connected groups: the cover, $SL(4,\mathbb{R})$, $PSL(4,\mathbb{R})$ and two intermediate double covers. The element level has three groups for $\mathfrak{sl}(2,\mathbb{R})$, and the difference is the rank of the centre.

**The simply connected quaternionic groups.** $SL(2,\mathbb{H})$ and $GL(2,\mathbb{H})$ are simply connected, because their maximal compact subgroup is $Sp(2)$, which is simply connected. The real counterparts have double covers because $SO(4)$ does not.

**The three covers used in geometry.**
$$
SL(2,\mathbb{C})\to SO^{+}(3,1),\qquad Spin(4)=SU(2)\times SU(2)\to SO(4),\qquad SL(2,\mathbb{H})\to SO^{+}(5,1).
$$

**The algebra does not determine the group.** $\mathfrak{sl}(4,\mathbb{R})$ is the algebra of five connected groups and $\mathfrak{gl}(4,\mathbb{R})$ of infinitely many; the discrete central subgroup is extra data.

## Where $n=2$ Differs

**The real rank.** The simple part $\mathfrak{sl}(4,\mathbb{R})$ has real rank three against the real rank one of $\mathfrak{sl}(2,\mathbb{R})$ at the element level. The three commuting $\mathfrak{sl}(2,\mathbb{R})$'s of the split form are the origin of the three rotation planes of the biquaternion algebra, and at $n=2$ there is one.

**The dimension of the complement.** $\mathfrak{sl}_2\otimes\mathfrak{sl}_2$ is nine-dimensional at $n=2$, that is $3\times3$; the Cartan complement of the maximal compact is five-dimensional in the quaternionic form and nine-dimensional in the split one, against one at the element level.

**The group count.** $\mathfrak{sl}(4,\mathbb{R})$ has five connected groups and $\mathfrak{sl}(2,\mathbb{R})$ three; the counts differ because the centre of the cover is $\mathbb{Z}_2^{2}$ against $\mathbb{Z}$.

**Nothing else differs in kind.** The module dictionaries, the maximal subalgebras, the quaternionic simple part $\mathfrak{su}^{*}(4)$ and the Jordan triple hold at every order with the sizes changed.

## Summary

The operator algebra $M_4(\mathbb{C})$ has the two real forms $M_4(\mathbb{R})$ and $M_2(\mathbb{H})$, separated by the trace-form inertia $(10,6)$ against $(6,10)$. Inside each form sits the biquaternion base: the regular families $\mathrm I_2\otimes M_2(\mathbb{R})$ and $M_2(\mathbb{R})^{\mathsf T}\otimes\mathrm I_2$ in the split form, and the copies $\mathrm I_2\otimes\mathbb{H}$ and $\mathbb{H}\otimes\mathrm I_2$ in the quaternionic one.

The semisimple associative subalgebras are classified by the module dictionaries $\sum m_in_id_i=4$ for the split form, with seventeen isomorphism types and the maximal pair $M_2(\mathbb{C})$, $M_2(\mathbb{R})\oplus M_2(\mathbb{R})$, and $\sum_in_i\le2$ for the quaternionic form.

The Lie layer of the split form is $\mathfrak{gl}(4,\mathbb{R})=\mathfrak{sl}(4,\mathbb{R})\oplus\mathbb{R}\mathrm I_4$ with Killing form $8\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$, verified to $4\cdot10^{-15}$, and inertia $(9,6)$ on the traceless part. The quaternionic simple part is $\mathfrak{su}^{*}(4)$ with compact $\mathfrak{sp}(2)$ of dimension ten.

The Jordan layer has the three real forms $M_4(\mathbb{R})^{+}$, $M_2(\mathbb{H})^{+}$ and $H_4(\mathbb{C})$. The groups attached to the split algebra are quotients of $\widetilde{SL(4,\mathbb{R})}$ by the five subgroups of $\mathbb{Z}_2^{2}$, and the quaternionic groups $SL(2,\mathbb{H})$ and $GL(2,\mathbb{H})$ are simply connected, with $SL(2,\mathbb{H})\cong Spin(5,1)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{E}_{\mathbb{H}}$ | $M_2(\mathbb{H})$ in the block model |
| $m_i,n_i,d_i$ | multiplicity, matrix size and division-algebra dimension |
| $K$ | the Killing form |
| $\mathfrak{su}^{*}(4)$ | $\mathfrak{sl}(2,\mathbb{H})$ |
| $\mathfrak{sp}(2),\mathfrak{sp}(1,1)$ | the compact and the non-compact form of $C_2$ |
| $H_4(\mathbb{C})$ | the Hermitian matrices |

## Further Reading

- [Classification of the Real Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups](classification-of-the-real-structures-of-the-operators-of-the-biquaternion-algebra.html), for the source tables and the element-level comparison.
- [Classification of the Structures of the Operators of the Biquaternion Algebra in $M_2(\mathbb{C})$](classification-of-the-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html), for the two real forms and the double centralizer.
- [Classification of the Complex Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups in $M_2(\mathbb{C})$](classification-of-the-complex-structures-of-the-operators-of-the-biquaternion-algebra-in-m2c.html), for the split extension $M_4(\mathbb{C})\oplus M_4(\mathbb{C})$.
- [The Spin Group via $4\times4$ Real Matrices](the-spin-group-via-4x4-real-matrices-in-m2c.html), for the spin covers as real $4\times4$ matrices.
- [The Adjoints and the Polar Decomposition of an Operator at $n=2$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-2.html), for the Cartan decomposition of the operator group.
