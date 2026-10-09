# __The Six Subspaces and the Four General Products__

## Introduction

The underlying $\mathbb{C}$-vector space of the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four general products, defined on the coordinates of a pair in *The Four General Products of the Biquaternion $\mathbb{C}$ Space*: the **general plain bilinear** $\tilde{P}\tilde{Q}$, the **general quaternionic bilinear** $\tilde{P}^{\natural}\tilde{Q}$, the **general plain sesquilinear** $\tilde{P}\tilde{Q}^{*}$ and the **general quaternionic sesquilinear** $\tilde{P}^{\natural}\tilde{Q}^{*}$. The first two are bilinear over $\mathbb{C}$ and the last two only over $\mathbb{R}$, and the first is associative while the other three are not.

This article reads the four general products against the six distinguished subspaces of *Introduction to the Six Subspaces* — the centre $\mathbb{C}_{\mathbb{B}}$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, the Hermitian subspace $\mathbb{M}_{+}$ and the anti-Hermitian subspace $\mathbb{M}_{-}$ — one subspace to a section. For every subspace it asks the same three questions, in the same order: **which of the four general products keep the subspace inside itself**, **which of their symmetrisations make it a Jordan algebra**, and **which of their brackets make it a Lie algebra**. Each of the six sections opens with the answer and then justifies it.

Each product $f$ splits into a symmetric and an antisymmetric half,
$$
\tilde{P}\bullet_{f}\tilde{Q}:=\tfrac12\bigl(f(\tilde{P},\tilde{Q})+f(\tilde{Q},\tilde{P})\bigr),\qquad
[\tilde{P},\tilde{Q}]_{f}:=f(\tilde{P},\tilde{Q})-f(\tilde{Q},\tilde{P}),
$$
so that $f(\tilde{P},\tilde{Q})=\tilde{P}\bullet_{f}\tilde{Q}+\tfrac12[\tilde{P},\tilde{Q}]_{f}$. For the general plain bilinear product, the only associative one, the subscripts are dropped: $\bullet$ is the **symmetrised product** and $[\tilde{P},\tilde{Q}]=\tilde{P}\tilde{Q}-\tilde{Q}\tilde{P}$ is the **commutator**. The two halves themselves are the subject of *The 12 Products of the Biquaternion Complex Space*; here they are used only as the two ways in which a subspace can be an algebra.

The criterion for each is the classical one. A subspace $U$ is a **Jordan algebra** for the symmetrisation $\bullet_{f}$ when $\tilde{P}\bullet_{f}\tilde{Q}$ lies in $U$ for all $\tilde{P},\tilde{Q}\in U$ and the Jordan identity holds on $U$; because $\mathbb{B}$ is associative, the symmetrisation of the general plain bilinear product inherits the identity, so for that product closure is the only test, while for the three non-associative products the identity must be checked as well. A subspace $U$ is a **Lie algebra** for the bracket $[\cdot,\cdot]_{f}$ when the bracket lies in $U$ and the Jacobi identity holds on $U$; the commutator of an associative algebra always satisfies Jacobi, so closure decides the Lie case for the general plain bilinear product, while for the other three products Jacobi must be tested, and on $\mathbb{B}$ it fails.

The scalar–vector form of the general plain bilinear product,
$$
\tilde{P}\tilde{Q}=\bigl(P_0Q_0-(\mathbf{P},\mathbf{Q})\bigr)+P_0\mathbf{Q}+Q_0\mathbf{P}+\mathbf{P}\times\mathbf{Q},
$$
with $\mathbf{P},\mathbf{Q}$ the vector parts and $(\mathbf{P},\mathbf{Q})$, $\mathbf{P}\times\mathbf{Q}$ the complex dot and cross products, is used throughout. The six subspaces, their defining conditions, their bases and their dimensions are not restated here; they belong to *Introduction to the Six Subspaces*, and the coordinate blocks $B_0=\mathbb{R}e_0$, $B_1=\operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ and $B_2=\operatorname{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$ come from *Comparison of the Six Subspaces*.

### The four general products have the same value set

**Proposition.** For each of the six subspaces the real span of $f(\tilde{P},\tilde{Q})$, as $\tilde{P}$ and $\tilde{Q}$ run over the subspace, is the same for all four general products $f$.

**Proof.** Each of the two conjugations $\natural$ and $*$ preserves each of the six subspaces, since each subspace is a fixed or anti-fixed space of one of the four conjugations of the group they generate (*The Group of Involutions*). Hence $\natural U=U$ and ${}^{*}U=U$ for every subspace $U$ of the list, and
$$
f_{2}(U,U)=U^{\natural}U=U\cdot U=f_{1}(U,U),
$$
and likewise $f_{3}(U,U)=U\,U^{*}=U\cdot U$ and $f_{4}(U,U)=U^{\natural}U^{*}=U\cdot U$. The four general products therefore take the same set of values on $U\times U$, and the common span is the span of the general plain bilinear product. $\square$

The common span is the subspace itself for the centre and for the quaternion subspace, the whole algebra for the vector subspace, the quaternion subspace for the anti-quaternion subspace, and $\mathbb{R}e_{0}\oplus\mathrm{Vect}(\mathbb{B})$, of real dimension seven, for the two Hermitian subspaces. The four general products thus differ not in where they send a pair but in the structure they leave on the value: the product keeps a subspace inside itself for exactly two of the six, the centre and the quaternion subspace, and in both cases for all four general products at once, while the vector, anti-quaternion, Hermitian and anti-Hermitian subspaces are closed under none of the four general products.

The symmetrisation and the bracket close on more of the six, and the pattern is the same for all four general products. The symmetrisation of every one of the four stays inside exactly the centre, the quaternion subspace and the Hermitian subspace; the bracket of every one of the four stays inside exactly the centre and the quaternion subspace, the two bilinear brackets also staying inside the vector subspace and the general plain sesquilinear bracket also inside the anti-Hermitian subspace. Whether the closed operation then satisfies the Jordan identity or the Jacobi identity decides the algebra, and the six sections below carry the answer subspace by subspace.

## The Centre Subspace

**The centre is both a Jordan algebra and a Lie algebra, and it is the only subspace of the six for which the Lie structure survives all four general products.** As a Jordan algebra it is the field $\mathbb{C}$, under $\bullet$ and $\bullet_{\natural}$; as a Lie algebra it is abelian under the two bilinear brackets and the **two-dimensional non-abelian Lie algebra** under the two sesquilinear ones.

A central element is $Ae_0$ with $A \in \mathbb{C}$. It is the fixed set of the natural conjugation $\natural$ and commutes with every element of $\mathbb{B}$, which makes the centre the simplest of the six subspaces. The three operations are taken in turn below, each tested first for closure and then for its identity.

**The four general products.** Because $Ae_0$ commutes with every element, the two products built on $\natural$ are the plain product of the scalars, and the two built on the Hermitian conjugation $*$ conjugate the second scalar:
$$
(Ae_0)(Be_0)=(Ae_0)^{\natural}(Be_0)=ABe_0,\qquad
(Ae_0)(Be_0)^{*}=(Ae_0)^{\natural}(Be_0)^{*}=A\bar{B}e_0 .
$$
The two bilinear products therefore coincide on the centre, as do the two sesquilinear ones, and **all four keep the centre inside itself**; the first pair is the multiplication of $\mathbb{C}$ read inside the algebra. The centre is, with the quaternion subspace, one of the two subspaces of the six that are closed under the product, and it is the only one of the six that is commutative.

**The symmetrisation.** The symmetrised general plain bilinear product is again the multiplication of $\mathbb{C}$, and the symmetrised general quaternionic bilinear product is the same function, because the two products agree on the centre:
$$
(Ae_0)\bullet(Be_0)=(Ae_0)\bullet_{\natural}(Be_0)=ABe_0 .
$$
The centre is therefore a **Jordan algebra** for those two products, namely the field $\mathbb{C}$ itself, and it is the smallest of the three Jordan subalgebras carried by the six. The two sesquilinear symmetrisations stay in the centre as well, but give **no Jordan algebra**: their common value,
$$
(Ae_0)\bullet_{*}(Be_0)=(Ae_0)\bullet_{\natural*}(Be_0)=\operatorname{Re}(A\bar{B})\,e_0,
$$
is commutative but only real-bilinear, and the Jordan identity fails. The failure is at $x=ie_0$, where $x\bullet_{*}x=e_0$, so that the two sides of the identity $(x\bullet_{*}x)\bullet_{*}(x\bullet_{*}x)=x\bullet_{*}\bigl(x\bullet_{*}(x\bullet_{*}x)\bigr)$ are $e_0$ and $0$.

**The bracket.** The two bilinear brackets vanish on the centre, which is therefore an **abelian Lie algebra** for both. The two sesquilinear brackets do not vanish, and they agree:
$$
[Ae_0,Be_0]_{*}=[Ae_0,Be_0]_{\natural*}=2i\,\operatorname{Im}(A\bar{B})\,e_0 .
$$
The bracket of any two central elements is a real multiple of the central imaginary unit $ie_0$, so the derived subalgebra is the line $\mathbb{R}(ie_0)$: one-dimensional, hence solvable. The algebra is not abelian, because $[e_0,ie_0]_{*}=[e_0,ie_0]_{\natural*}=-2ie_0$, and the Jacobi identity holds. The real span of $e_0$ and $ie_0$ under that bracket is the **two-dimensional non-abelian Lie algebra**, the smallest non-commutative Lie algebra and the only one of dimension two up to isomorphism. The centre is thus a **Lie algebra for all four general products** — the one-dimensional abelian algebra for the two bilinear ones and the two-dimensional non-abelian algebra for the two sesquilinear ones.

## The Vector Subspace

**The vector subspace is a Lie algebra but not a Jordan algebra.** Under the two bilinear brackets it is $(\mathrm{Vect}(\mathbb{B}),[\cdot,\cdot])\cong\mathfrak{sl}(2,\mathbb{C})$, the general quaternionic bilinear bracket being the negative of the commutator, and it is **no Jordan algebra** for any of the four symmetrisations.

A pure vector is $\mathbf{P}=P_1e_1+P_2e_2+P_3e_3$ with $P_1,P_2,P_3 \in \mathbb{C}$. Its scalar part vanishes and the natural conjugation reverses its sign, so the subspace, of real dimension six and complex dimension three, is the largest of the six and is the complex analogue of the imaginary quaternions. The three operations behave here as differently as anywhere in the article: the product leaves the subspace at once, the symmetrisation collapses to the centre, and only the bracket stays.

**The four general products.** The square of a single basis vector already leaves the subspace, and is a nonzero central scalar for each of the four general products:
$$
e_1e_1=-e_0,\qquad e_1^{\natural}e_1=e_0,\qquad e_1e_1^{*}=e_0,\qquad e_1^{\natural}e_1^{*}=-e_0 .
$$
In general the product of two pure vectors is the sum of a scalar and a vector: the scalar–vector form of the general plain bilinear product read on the vector subspace,
$$
\mathbf{P}\mathbf{Q}=-(\mathbf{P},\mathbf{Q})e_0+\mathbf{P}\times\mathbf{Q},
$$
with $(\mathbf{P},\mathbf{Q})$ the complex dot product and $\mathbf{P}\times\mathbf{Q}$ the complex cross product. The other three products are the same expression with the second factor replaced as the conjugation prescribes, and differ only in the signs of the two terms. Since the scalar part is a general complex number and the vector part a general vector, each of the four general products of a suitable pair **spans the whole algebra**, of real dimension eight. The vector subspace is therefore closed under **none of the four general products**.

**The symmetrisation.** No symmetrisation keeps the vector subspace inside itself either, and here the two bilinear and the two sesquilinear products part company. The two bilinear symmetrisations collapse to the centre, the cross-product terms cancelling in the symmetrised sum:
$$
\mathbf{P}\bullet\mathbf{Q}=-(\mathbf{P},\mathbf{Q})e_0,\qquad \mathbf{P}\bullet_{\natural}\mathbf{Q}=(\mathbf{P},\mathbf{Q})e_0,
$$
so that the pair $\mathbf{P}=\mathbf{Q}=e_1$ has symmetrised product $-e_0$, a central element outside the subspace. The contrast is sharp: the same two pure vectors whose plain product spans the whole algebra have their symmetrised product confined to the two-dimensional centre. The two sesquilinear symmetrisations instead fill the Hermitian subspace,
$$
\mathbf{P}\bullet_{*}\mathbf{Q}=\tfrac12\bigl(\mathbf{P}\mathbf{Q}^{*}+\mathbf{Q}\mathbf{P}^{*}\bigr)\in\mathbb{M}_{+},\qquad \mathbf{P}\bullet_{\natural*}\mathbf{Q}\in\mathbb{M}_{+},
$$
of real dimension four, again outside the vector subspace. The vector subspace is therefore a **Jordan algebra for none** of the four general products. The collapse $\mathbf{P}\bullet\mathbf{P}=-(\mathbf{P},\mathbf{P})e_0$ explains the square-zero elements of the vector subspace, which are its zero divisors (*Introduction to the Six Subspaces*).

**The bracket.** The commutator keeps the vector subspace inside itself, because the scalar part is symmetric and cancels in the antisymmetric half:
$$
[\mathbf{P},\mathbf{Q}]=2\,\mathbf{P}\times\mathbf{Q}\in\mathrm{Vect}(\mathbb{B}),\qquad
[\mathrm{Vect}(\mathbb{B}),\mathrm{Vect}(\mathbb{B})]=\mathrm{Vect}(\mathbb{B}) .
$$
The bracket of two pure vectors is twice their complex cross product, and the cross products of the complex vectors fill the whole subspace, so the algebra is equal to its own derived subalgebra and is perfect. It is the complex **Lie algebra $\mathfrak{sl}(2,\mathbb{C})$** of the traceless complex $2\times2$ matrices, of complex dimension three, read here in the coordinates $e_1,e_2,e_3$ against the Pauli matrices. The general quaternionic bilinear bracket is the negative of the commutator, since the natural conjugation negates a pure vector:
$$
[\mathbf{P},\mathbf{Q}]_{\natural}=\mathbf{P}^{\natural}\mathbf{Q}-\mathbf{Q}^{\natural}\mathbf{P}=(-\mathbf{P})\mathbf{Q}-(-\mathbf{Q})\mathbf{P}=-[\mathbf{P},\mathbf{Q}],
$$
so it is a **Lie algebra** too, the same one with the opposite sign. The two sesquilinear brackets leave the subspace: their values are anti-Hermitian, and they fill the anti-Hermitian subspace,
$$
[\mathrm{Vect}(\mathbb{B}),\mathrm{Vect}(\mathbb{B})]_{*}=[\mathrm{Vect}(\mathbb{B}),\mathrm{Vect}(\mathbb{B})]_{\natural*}=\mathbb{M}_{-},
$$
with the witness $[e_1,ie_1]_{*}=-2ie_0\notin\mathrm{Vect}(\mathbb{B})$. The vector subspace is therefore a **Lie algebra for exactly the two bilinear products** and a **Jordan algebra for none**; of the three operations only the antisymmetric half is carried by the subspace, and there it reproduces the classical Lie algebra of the whole algebra.

## The Quaternion Subspace

**The quaternion subspace is both a Jordan algebra and a Lie algebra.** Under $\bullet$ it is the symmetrised real quaternion algebra, and under $[\cdot,\cdot]$ and $[\cdot,\cdot]_{\natural*}$ it is $\mathbb{R}e_0\oplus\mathfrak{su}(2)$.

A quaternion element is $h=h_0e_0+h_1e_1+h_2e_2+h_3e_3$ with all four coefficients real. The subspace is the fixed set of the quaternionic conjugation, and it is the real quaternion algebra $\mathbb{H}$, of real dimension four. It is the larger of the two subspaces of the six that are closed under the product, and, with the centre, one of the two that carry all three structures at once. Unlike the centre it is non-commutative, and the three structures are spread over the four general products rather than shared between them.

**The four general products.** **All four keep the quaternion subspace inside itself**; on the real quaternions they read $hg$, $\bar{h}g$, $h\bar{g}$ and $\bar{h}\bar{g}=\overline{gh}$:
$$
\mathbb{H}_{\mathbb{B}}\mathbb{H}_{\mathbb{B}}=\mathbb{H}_{\mathbb{B}},\quad
\mathbb{H}_{\mathbb{B}}^{\natural}\mathbb{H}_{\mathbb{B}}=\mathbb{H}_{\mathbb{B}},\quad
\mathbb{H}_{\mathbb{B}}\mathbb{H}_{\mathbb{B}}^{*}=\mathbb{H}_{\mathbb{B}},\quad
\mathbb{H}_{\mathbb{B}}^{\natural}\mathbb{H}_{\mathbb{B}}^{*}=\mathbb{H}_{\mathbb{B}} .
$$
It is therefore closed under all four general products at once, and it is an associative subalgebra for exactly one of them, the general plain bilinear product; under that product it is the division algebra of the real quaternions, since the norm is a sum of four real squares and vanishes only at the origin. The other three products are not associative there: their counterexamples in *Comparison Between the Four General Products* §*The Failure of Associativity* are triples of the quaternion subspace, so each of them fails associativity inside the subspace already.

**The symmetrisation.** Only the general plain bilinear symmetrisation gives a **Jordan algebra**:
$$
\mathbb{H}_{\mathbb{B}}\bullet\mathbb{H}_{\mathbb{B}}=\mathbb{H}_{\mathbb{B}},
$$
the symmetrisation of the real quaternion algebra, a commutative Jordan algebra of real dimension four. The other three symmetrisations stay inside the subspace but **fail the Jordan identity**, so that the quaternion subspace, closed under all four general products, is a Jordan algebra for exactly one of them. The general quaternionic bilinear and the general plain sesquilinear symmetrisations coincide there and collapse to the centre:
$$
\tilde{P}\bullet_{\natural}\tilde{Q}=\tilde{P}\bullet_{*}\tilde{Q}=\bigl(P_0Q_0+(\mathbf{P},\mathbf{Q})\bigr)e_0,
$$
the trace form of the general quaternionic bilinear product; the general quaternionic sesquilinear one is the natural conjugate of the Jordan product, $\tilde{P}\bullet_{\natural*}\tilde{Q}=(\tilde{P}\bullet\tilde{Q})^{\natural}$. Each of the three fails the identity at $x=e_1$: for the general quaternionic bilinear and the general plain sesquilinear symmetrisations $x\bullet_{\natural}x=e_0$, so the two sides of $(x\bullet_{\natural}x)\bullet_{\natural}(x\bullet_{\natural}x)=x\bullet_{\natural}\bigl(x\bullet_{\natural}(x\bullet_{\natural}x)\bigr)$ are $e_0$ and $0$; for the general quaternionic sesquilinear one, where $x\bullet_{\natural*}x=-e_0$, they are $e_0$ and $-e_0$.

**The bracket.** The commutator stays inside the subspace and gives a **Lie algebra**:
$$
[\mathbb{H}_{\mathbb{B}},\mathbb{H}_{\mathbb{B}}]=B_1,\qquad
(\mathbb{H}_{\mathbb{B}},[\cdot,\cdot])\cong\mathbb{R}e_0\oplus\mathfrak{su}(2),
$$
the bracket of two real quaternions being twice the real cross product of their vector parts, a pure real quaternion, which is why the subspace closes. The derived subalgebra is the real vector triple $B_1=\operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$, the imaginary quaternions, which under the cross product is the Lie algebra $\mathfrak{su}(2)$ of the special unitary group $SU(2)$; the line $\mathbb{R}e_0$ is central, because $e_0$ is a central element of the algebra, so the Lie algebra of the subspace is the direct sum $\mathbb{R}e_0\oplus\mathfrak{su}(2)$. The general quaternionic sesquilinear bracket is the commutator itself, the two conjugations cancelling on the subspace,
$$
[\mathbb{H}_{\mathbb{B}},\mathbb{H}_{\mathbb{B}}]_{\natural*}=[\mathbb{H}_{\mathbb{B}},\mathbb{H}_{\mathbb{B}}],
$$
so the quaternion subspace is a Lie algebra for the general plain bilinear product and for the general quaternionic sesquilinear product. The general quaternionic bilinear and general plain sesquilinear brackets stay inside — their values are pure vectors — but **fail the Jacobi identity**, at the triple $(e_0,e_1,e_2)$, where the cyclic sum of *The 12 Products of the Biquaternion Complex Space* is $-4e_3$ for the general quaternionic bilinear bracket and $+4e_3$ for the general plain sesquilinear one. The quaternion subspace is thus, with the centre, one of the two subspaces that are at once closed under the product, a Jordan algebra and a Lie algebra; of the four general products the general plain bilinear one carries both structures, and the general quaternionic sesquilinear one the Lie structure alone.

## The Anti-Quaternion Subspace

**The anti-quaternion subspace carries no algebra at all.** It is neither a Jordan nor a Lie algebra, for any product, any symmetrisation or any bracket; its only structure is that of a two-sided module over the quaternion subspace.

An anti-quaternion element is $i\tilde{P}$ with $\tilde{P}$ a real quaternion. The subspace is the fixed set of the composition of the quaternionic and the natural conjugations, and it equals $i\mathbb{H}_{\mathbb{B}}$, so that $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$. It is the subspace on which nothing closes, since neither the product nor either of its two halves returns to it, and it is the odd part of the $\mathbb{Z}/2$-grading whose even part is the quaternion subspace.

**The four general products.** **None of the four keeps the anti-quaternion subspace inside itself.** Since the natural conjugation reverses the central imaginary unit and the quaternionic conjugation ignores it, the four general products of a pair fall back into the quaternion subspace:
$$
(i\tilde{P})(i\tilde{Q})=-\tilde{P}\tilde{Q},\quad
(i\tilde{P})^{\natural}(i\tilde{Q})=-\tilde{P}^{\natural}\tilde{Q},\quad
(i\tilde{P})(i\tilde{Q})^{*}=\tilde{P}\tilde{Q}^{\natural},\quad
(i\tilde{P})^{\natural}(i\tilde{Q})^{*}=\tilde{P}^{\natural}\tilde{Q}^{\natural}=(\tilde{Q}\tilde{P})^{\natural} .
$$
Each of the four **spans $\mathbb{H}_{\mathbb{B}}$**, so the anti-quaternion subspace is closed under none of the four general products. The product of two odd elements is even, which is exactly the statement that the split $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$ is a grading, and the anti-quaternion subspace is a two-sided module over the quaternion subspace — the module structure being the only structure it carries.

**The symmetrisation.** **No symmetrisation keeps the anti-quaternion subspace inside itself** either; every value is even:
$$
(i\tilde{P})\bullet(i\tilde{Q})=-\tilde{P}\bullet\tilde{Q},\qquad
(i\tilde{P})\bullet_{\natural}(i\tilde{Q})=-\tilde{P}\bullet_{\natural}\tilde{Q}\in\mathbb{R}e_0,\qquad
(i\tilde{P})\bullet_{*}(i\tilde{Q})=\tilde{P}\bullet_{*}\tilde{Q}\in\mathbb{R}e_0,\qquad
(i\tilde{P})\bullet_{\natural*}(i\tilde{Q})=\bigl(\tilde{P}\bullet\tilde{Q}\bigr)^{\natural}\in\mathbb{H}_{\mathbb{B}} ,
$$
the first and the fourth lying in the quaternion subspace, the second and the third in the centre $\mathbb{R}e_0$. The anti-quaternion subspace is therefore a **Jordan algebra for none** of the four general products.

**The bracket.** **No bracket keeps the anti-quaternion subspace inside itself** either; every value is again even:
$$
[i\tilde{P},i\tilde{Q}]=-[\tilde{P},\tilde{Q}],\qquad
[i\tilde{P},i\tilde{Q}]_{\natural}=-[\tilde{P},\tilde{Q}]_{\natural},\qquad
[i\tilde{P},i\tilde{Q}]_{*}=[\tilde{P},\tilde{Q}]_{*},\qquad
[i\tilde{P},i\tilde{Q}]_{\natural*}=[\tilde{P},\tilde{Q}] ,
$$
each lying in the real vector triple $B_1\subset\mathbb{H}_{\mathbb{B}}$. The anti-quaternion subspace has an imaginary scalar part and an imaginary vector part, and every value above is real, so nothing returns. It is a **Lie algebra for none** of the four general products and, with the symmetrisations, the subspace carries **no algebra at all**: not for the product and not for either of its two halves.

## The Hermitian Subspace

**The Hermitian subspace is a Jordan algebra but not a Lie algebra.** Under $\bullet$ and $\bullet_{*}$, which coincide there, it is $H_{2}(\mathbb{C})=J(\mathbb{B})$, and it is **no Lie algebra** for any of the four brackets.

A Hermitian element is $a_0e_0+i\mathbf{p}$ with $a_0 \in \mathbb{R}$ and $\mathbf{p}$ a real vector. The subspace is the fixed set of the Hermitian conjugation $*$ and has real dimension four. It is the mirror of the vector subspace — there the antisymmetric half is the richer, here it is the symmetric half — and it is the first subspace of the six that is a Jordan algebra but not a Lie algebra.

**The four general products.** **None of the four keeps the Hermitian subspace inside itself.** The product of two Hermitian elements,
$$
(a_0e_0+i\mathbf{p})(b_0e_0+i\mathbf{r})=\bigl(a_0b_0+(\mathbf{p},\mathbf{r})\bigr)e_0-\mathbf{p}\times\mathbf{r}+i(a_0\mathbf{r}+b_0\mathbf{p}),
$$
has a real scalar part and a vector part that runs over the whole complex vector subspace, and the middle term $-\mathbf{p}\times\mathbf{r}$ is a real pure vector, which no Hermitian element has: the witness is $(ie_1)(ie_2)=-e_3$. The other three products differ only in the signs of the terms, and each of the four **spans $\mathbb{R}e_0\oplus\mathrm{Vect}(\mathbb{B})$**, of real dimension seven. It is the failure of the interior term that does the work: the Hermitian subspace has no real vector part, and that is precisely what the product of two of its elements supplies.

**The symmetrisation.** This is the operation that stays. **All four symmetrisations keep the Hermitian subspace inside itself**, the special feature of this subspace: the cross-product term is antisymmetric and cancels, and the Hermitian conjugation $*$ fixes a Hermitian element, so that the general plain bilinear and the general plain sesquilinear symmetrisations agree:
$$
(a_0e_0+i\mathbf{p})\bullet(b_0e_0+i\mathbf{r})=(a_0e_0+i\mathbf{p})\bullet_{*}(b_0e_0+i\mathbf{r})=\bigl(a_0b_0+(\mathbf{p},\mathbf{r})\bigr)e_0+i(a_0\mathbf{r}+b_0\mathbf{p}).
$$
This is the **Jordan product**, and
$$
(\mathbb{M}_{+},\bullet)\cong H_{2}(\mathbb{C})=J(\mathbb{B})
$$
is the Hermitian Jordan algebra of degree two, with two orthogonal idempotents and Peirce dimensions $1+2+1$ (*The 12 Products of the Biquaternion Complex Space*). The two quaternionic symmetrisations also stay inside but are central,
$$
(a_0e_0+i\mathbf{p})\bullet_{\natural}(b_0e_0+i\mathbf{r})=(a_0e_0+i\mathbf{p})\bullet_{\natural*}(b_0e_0+i\mathbf{r})=\bigl(a_0b_0-(\mathbf{p},\mathbf{r})\bigr)e_0,
$$
and give **no Jordan algebra**, the identity failing at $x=ie_1$, where $x\bullet_{\natural}x=-e_0$ and the two sides of $(x\bullet_{\natural}x)\bullet_{\natural}(x\bullet_{\natural}x)=x\bullet_{\natural}\bigl(x\bullet_{\natural}(x\bullet_{\natural}x)\bigr)$ are $e_0$ and $0$. The Hermitian subspace is therefore a **Jordan algebra for the general plain bilinear product and for the general plain sesquilinear product**, which coincide there, and for neither of the two quaternionic products.

**The bracket.** **No bracket keeps the Hermitian subspace inside itself.** The bracket of two Hermitian elements has zero scalar part, because the scalar part of every product is symmetric and real on $\mathbb{M}_{+}$, so it is a pure vector; and the values are not all imaginary, so the subspace does not close. The commutator and the general plain sesquilinear bracket fill the real vector triple, and the two quaternionic brackets the whole complex vector subspace:
$$
[\mathbb{M}_{+},\mathbb{M}_{+}]=B_1,\qquad
[\mathbb{M}_{+},\mathbb{M}_{+}]_{\natural}=\mathrm{Vect}(\mathbb{B}),\qquad
[\mathbb{M}_{+},\mathbb{M}_{+}]_{*}=B_1,\qquad
[\mathbb{M}_{+},\mathbb{M}_{+}]_{\natural*}=\mathrm{Vect}(\mathbb{B}) .
$$
The commutator of two Hermitian elements is twice the cross product of their two imaginary vector parts, a real pure vector outside the subspace, so the Hermitian subspace is a **Lie algebra for none** of the four general products. It is the exact counterpart of the vector subspace: there the bracket is carried and the symmetrisation is not, here the symmetrisation is carried and the bracket is not, and the two are the subspaces of the six on which the two halves of the product each find their richest expression.

## The Anti-Hermitian Subspace

**The anti-Hermitian subspace is a Lie algebra but not a Jordan algebra.** Under $[\cdot,\cdot]$ and $[\cdot,\cdot]_{*}$, the latter the negative of the former, it is $\mathfrak{u}(2)\cong\mathbb{R}(ie_0)\oplus B_1$, and it is **no Jordan algebra** for any of the four symmetrisations.

An anti-Hermitian element is $ib'_0e_0+\mathbf{q}$ with $b'_0 \in \mathbb{R}$ and $\mathbf{q}$ a real vector. It is the anti-fixed set of the Hermitian conjugation $*$, has real dimension four, and is the image of the Hermitian subspace under multiplication by the central imaginary unit $ie_0$. It is the mirror of the Hermitian subspace — where the Hermitian subspace carries the symmetrisation, the anti-Hermitian one carries the bracket — and this reversal is the source of both its structures, the unitary Lie algebra $\mathfrak{u}(2)$ and the failure of the Jordan identity.

**The four general products.** **None of the four keeps the anti-Hermitian subspace inside itself.** The product of two anti-Hermitian elements,
$$
(ib'_0e_0+\mathbf{q})(ic'_0e_0+\mathbf{r})=\bigl(-b'_0c'_0-(\mathbf{q},\mathbf{r})\bigr)e_0+\mathbf{q}\times\mathbf{r}+i(b'_0\mathbf{r}+c'_0\mathbf{q}),
$$
has a real scalar part and a vector part that runs over the whole complex vector subspace, and it is the real scalar part that leaves the subspace: the witness is $(ie_0)(ie_0)=-e_0$, whereas an anti-Hermitian element has a purely imaginary scalar part. Each of the four **spans $\mathbb{R}e_0\oplus\mathrm{Vect}(\mathbb{B})$**, of real dimension seven, and the subspace is closed under no product.

**The symmetrisation.** **No symmetrisation keeps the anti-Hermitian subspace inside itself.** The general plain bilinear symmetrisation is Hermitian-valued,
$$
(ib'_0e_0+\mathbf{q})\bullet(ic'_0e_0+\mathbf{r})=\bigl(-b'_0c'_0-(\mathbf{q},\mathbf{r})\bigr)e_0+i(b'_0\mathbf{r}+c'_0\mathbf{q})\in\mathbb{M}_{+},
$$
with a real scalar part and an imaginary vector part, and the general plain sesquilinear symmetrisation is its negative, since $*$ negates an anti-Hermitian element. The two quaternionic symmetrisations are also central, and are the negative of each other:
$$
(ib'_0e_0+\mathbf{q})\bullet_{\natural}(ic'_0e_0+\mathbf{r})=\bigl(-b'_0c'_0+(\mathbf{q},\mathbf{r})\bigr)e_0,\qquad
(ib'_0e_0+\mathbf{q})\bullet_{\natural*}(ic'_0e_0+\mathbf{r})=\bigl(b'_0c'_0-(\mathbf{q},\mathbf{r})\bigr)e_0 .
$$
The anti-Hermitian subspace is therefore a **Jordan algebra for none** of the four general products, and the symmetrised product of two anti-Hermitian elements is never anti-Hermitian. This is the sign reversal that separates the two sectors: multiplication by the central imaginary unit exchanges $\mathbb{M}_{+}$ and $\mathbb{M}_{-}$, but it does not carry the symmetrisation of one to the symmetrisation of the other, and only $\mathbb{M}_{+}$ is closed under it.

**The bracket.** This is the operation that stays, and it is where the subspace is an algebra. **The commutator keeps the anti-Hermitian subspace inside itself**, and gives a Lie algebra:
$$
[\mathbb{M}_{-},\mathbb{M}_{-}]=B_1,\qquad
(\mathbb{M}_{-},[\cdot,\cdot])\cong\mathfrak{u}(2)\cong\mathbb{R}(ie_0)\oplus B_1,
$$
the bracket of two anti-Hermitian elements being twice the real cross product of their two real vector parts, a real pure vector. The derived subalgebra is the triple $B_1$, which under the cross product is $\mathfrak{su}(2)$, and the line $\mathbb{R}(ie_0)$ is central, because $ie_0$ is a central element of the algebra; the algebra of the subspace is therefore the direct sum of a central line and $\mathfrak{su}(2)$, which is the **Lie algebra $\mathfrak{u}(2)$** of the unitary group $U(2)$, the skew-Hermitian complex $2\times2$ matrices of real dimension four, with centre $\mathbb{R}(ie_0)$ and derived subalgebra $\mathfrak{su}(2)$. The general plain sesquilinear bracket is the negative of the commutator, since $*$ negates an anti-Hermitian element:
$$
[\mathbb{M}_{-},\mathbb{M}_{-}]_{*}=-[\mathbb{M}_{-},\mathbb{M}_{-}],
$$
so the anti-Hermitian subspace is a **Lie algebra for the general plain bilinear product and for the general plain sesquilinear product**. The two quaternionic brackets leave the subspace: their values are complex pure vectors, and they fill the whole complex vector subspace,
$$
[\mathbb{M}_{-},\mathbb{M}_{-}]_{\natural}=[\mathbb{M}_{-},\mathbb{M}_{-}]_{\natural*}=\mathrm{Vect}(\mathbb{B}),
$$
with the witness $[ie_0,e_1]_{\natural}=2ie_1\notin\mathbb{M}_{-}$. The anti-Hermitian subspace is therefore a **Lie algebra for exactly the two products** whose brackets reproduce the commutator up to sign, and a **Jordan algebra for none**.

## The Two Splits and the Two Readings

The six subspaces of this article are the homes of the parts of the four general products under the **plain** exchange of the two arguments. The two parts of a bilinear product are read there directly, the antisymmetric parts of the two bilinear products spanning the vector subspace and the symmetric part of the quaternionic one collapsing to the centre; and the two parts of the plain sesquilinear product are the Hermitian subspace $\mathbb{M}_{+}$ and the anti-Hermitian subspace $\mathbb{M}_{-}$.

The **exchange by the coefficientwise conjugation**, $f^{c}(\tilde{P},\tilde{Q})=\overline{f(\tilde{Q},\tilde{P})}$, keeps the class of the two sesquilinear products, and its two parts sit in two other subspaces of the same list. For $\tilde{P}\tilde{Q}^{*}$ they are the scalar part and the vector part of the value, so they lie in the **centre** $\mathbb{C}_{\mathbb{B}}$ and in the **vector subspace** $\mathrm{Vect}(\mathbb{B})$ — the two subspaces that carry the parts of the general quaternionic bilinear product under the plain exchange. For $\tilde{P}^{\natural}\tilde{Q}^{*}$ the skew half is the cross product $\mathbf{P}\times\overline{\mathbf{Q}}$ of the two vectors, so it lies in the **vector subspace**, while the conjugate-symmetric half carries the form $K(\tilde{P},\tilde{Q})=P_0\overline{Q_0}-(\mathbf{P},\overline{\mathbf{Q}})$ in its scalar part and is not central, so it lies in no subspace of the six.

So three of the passages of the adapted reading land in the list — the centre and the vector subspace for the plain sesquilinear product, the vector subspace again for the quaternionic one — against the Hermitian and the anti-Hermitian subspace, where the plain reading of the same two products lands. The two readings are of one pair of products each and neither is the other; the twelve names of *The 12 Products of the Biquaternion Complex Space* belong to the **adapted** reading and not to the plain one tabulated here, and the plain reading's own four halves are the operations of *The Sesquilinear Symmetrised Product* and *The Sesquilinear Commutator* (*The 12 Products of the Biquaternion Complex Space*, §*The Other Exchange, and the Class It Keeps*).

## Summary

**The four general products** carried by the underlying $\mathbb{C}$-vector space of $\mathbb{B}$ take the same set of values on each of the six distinguished subspaces, because the two conjugations $\natural$ and $*$ preserve every subspace of the list; the common span is the subspace itself for the centre and the quaternion subspace, the whole algebra for the vector subspace, the quaternion subspace for the anti-quaternion subspace, and $\mathbb{R}e_0\oplus\mathrm{Vect}(\mathbb{B})$ for the two Hermitian subspaces. The four general products differ only in the structure they leave on those values. The product keeps a subspace inside itself for exactly two of the six, the centre and the quaternion subspace, both for all four general products.

**Three of the six subspaces are Jordan algebras:** the centre, for the general plain bilinear product and for the general quaternionic bilinear product, which coincide there, and which give the field $\mathbb{C}$; the quaternion subspace, for the general plain bilinear product, giving the symmetrised real quaternion algebra; and the Hermitian subspace, for the general plain bilinear product and for the general plain sesquilinear product, which coincide there, giving $H_{2}(\mathbb{C})=J(\mathbb{B})$, of degree two. The symmetrisations of the two quaternionic products stay inside some subspaces but give a Jordan algebra nowhere: the general quaternionic bilinear symmetrisation is central on the centre, on the quaternion subspace and on the Hermitian subspace, and the general quaternionic sesquilinear symmetrisation is central on the centre and on the Hermitian subspace and is the conjugate of the Jordan product on the quaternion subspace, and the identity fails on all three.

**Four of the six subspaces are Lie algebras:** the centre, for all four general products, abelian for the two bilinear and the two-dimensional non-abelian algebra for the two sesquilinear; the vector subspace, for the two bilinear products, $(\mathrm{Vect}(\mathbb{B}),[\cdot,\cdot])\cong\mathfrak{sl}(2,\mathbb{C})$, the general quaternionic bilinear bracket being the negative of the commutator; the quaternion subspace, for the general plain bilinear product and for the general quaternionic sesquilinear product, which coincide there, giving $\mathbb{R}e_0\oplus\mathfrak{su}(2)$; and the anti-Hermitian subspace, for the general plain bilinear product and for the general plain sesquilinear product, the latter the negative of the former, giving $\mathfrak{u}(2)$. Each of the three products other than the general plain bilinear one reduces to the commutator, up to sign, on exactly one further subspace: the general quaternionic bilinear product on the vector subspace, the general plain sesquilinear product on the anti-Hermitian subspace, and the general quaternionic sesquilinear product on the quaternion subspace. **The anti-quaternion subspace carries no algebra under any product**, for the product, for its symmetrisations or for its brackets; it is the odd part of the $\mathbb{Z}/2$-grading whose even part is the quaternion subspace. Among the four four-dimensional subspaces the quaternion subspace is the one carrying both a Jordan and a Lie algebra, the anti-Hermitian subspace a Lie algebra alone, the Hermitian subspace a Jordan algebra alone, and the anti-quaternion subspace neither.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_{+}, \mathbb{M}_{-}$ | the Hermitian and anti-Hermitian subspaces |
| $B_0, B_1, B_2$ | the real scalar line, the real and the imaginary vector triples |
| $\tilde{P}\tilde{Q}, \tilde{P}^{\natural}\tilde{Q}, \tilde{P}\tilde{Q}^{*}, \tilde{P}^{\natural}\tilde{Q}^{*}$ | the four general products, from *The Four General Products of the Biquaternion $\mathbb{C}$ Space* |
| $\tilde{P}\bullet_{f}\tilde{Q}$ | the symmetrisation $\tfrac12(f(\tilde{P},\tilde{Q})+f(\tilde{Q},\tilde{P}))$ |
| $[\tilde{P},\tilde{Q}]_{f}$ | the bracket $f(\tilde{P},\tilde{Q})-f(\tilde{Q},\tilde{P})$ |
| $\bullet, [\cdot,\cdot]$ | the symmetrised product and the commutator of the general plain bilinear product |
| $(\mathbf{P},\mathbf{Q}), \mathbf{P}\times\mathbf{Q}$ | the complex dot and cross products of the vector parts |
| $\mathfrak{sl}(2,\mathbb{C}), \mathfrak{u}(2), \mathfrak{su}(2)$ | the classical Lie algebras of the vector, anti-Hermitian and quaternion subspaces |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section
- *Comparison of the Six Subspaces* (`articles_maths/comparison-of-the-six-subspaces.md`), for the coordinate blocks, the intersections and the sums of the six
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the definition of the four general products and their scalar–vector forms
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the symmetric and antisymmetric halves of each of the four general products, the Jordan algebra of the whole algebra, the Jordan identity, the trace form and the Peirce decomposition
- *Relations Between the Four General Products* (`articles_maths/relations-between-the-four-general-products.md`), for the identities that link the four general products
