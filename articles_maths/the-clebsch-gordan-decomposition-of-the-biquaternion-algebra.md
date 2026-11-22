# __The Clebsch–Gordan Decomposition of the Biquaternion Algebra__

## Introduction

**The question.** What does the biquaternion algebra hold, read as a carrier of the rotor group? The question is not about a list of subspaces found by inspection. It is about one decomposition, forced by one rule, from which every other count in this subsection follows.

**The answer.** The algebra is the endomorphism algebra of one slot, so it is the tensor product of that slot with its dual. The slot is the defining carrier $V_{1/2}$ of the rotor group, the dual is the same carrier, and the Clebsch–Gordan series for the pair of them is

$$
V_{1/2}\otimes V_{1/2}=V_{1}\oplus V_{0},\qquad 3+1=4 .
$$

The two summands are the vector part and the centre, and the split is realized by two operators,

$$
P_{1}=\tfrac12\bigl(\mathrm{id}-\natural\bigr),\qquad P_{0}=\tfrac12\bigl(\mathrm{id}+\natural\bigr),
$$

built from the conjugation $\natural$ and from nothing else.

**The route.** *The Two Slots* identifies the algebra with the square of the slot and says why the second slot is the dual. *The Clebsch–Gordan Series* states the addition rule and applies it. *The Two Projectors* turns the abstract split into two operators and proves that they are the Clebsch–Gordan projectors of the diagonal action. *The Two Summands and Their Spins* identifies the summands, by subspace, by weights and by dimension. *The Range and What Falls Outside It* reads the range of the label off the series. *The Casimir Is the Projector* shows that the quadratic Casimir is one of the two projectors up to a factor, so the labels and the split are the same statement. *Where the Coefficients Are* says what the series does not need and what it does. *The Slot and the Algebra* separates the two kinds of carrier, the factor and the summand, which is where the three-carrier list of this subsection comes from.

**What is not used.** No basis, no coefficient table, no array display. The two projectors are canonical, the conjugation that builds them is canonical, and every identity below is written at a general axis or with no axis at all. The Clebsch–Gordan coefficients appear only in *Where the Coefficients Are*, and only as the price of a secondary refinement.

**The one number to carry away.** The algebra holds integer spins $0$ and $1$, and no other, because it is a square of a single half-integer slot. Each further factor raises the maximum by $\tfrac12$ and adds one summand; at $n$ the slot itself is $V_{(n-1)/2}$ and the chain is longer, which is *The Spin Decomposition of $M_n(\mathbb{C})$*, quoted and not reproved here.

Nothing below is a statement of physics. The elements are written $\tilde X,\tilde Q$; the units are $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t$ the identity and $\vec e_k^{2}=-e_t$; a general element splits as $\tilde X=a\,e_t+\vec v$ with $a\in\mathbb{C}$ and $\vec v$ in the complexified vector part $\mathbb{C}\mathfrak{k}$, where $\mathfrak{k}=\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z$ is the real vector part; $\natural$ is the quaternion conjugation and $*$ is the Hermitian adjoint, $*=\bar{\cdot}\circ\natural$.

## The Two Slots

**Two multiplications.** The algebra acts on itself on the left and on the right,

$$
L_{\tilde Q}(\tilde X)=\tilde Q\tilde X,\qquad R_{\tilde Q}(\tilde X)=\tilde X\tilde Q .
$$

The first is a homomorphism, $L_{\tilde Q}L_{\tilde P}=L_{\tilde Q\tilde P}$. The second is an anti-homomorphism, $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$, because $(\tilde X\tilde P)\tilde Q=\tilde X(\tilde P\tilde Q)$.

**Why the second slot is the dual.** A slot on which an algebra acts by left multiplication is a module. A slot on which it acts on the right, with the order reversed, is the transpose action on the dual. Writing the same map as an action on the dual repairs the order, because the transpose of a composite reverses the factors. So the right slot is not a second copy of the first: it is its dual. The algebra is therefore the tensor product of the slot with the dual slot,

$$
\mathbb{B}\cong S\otimes S^{*},\qquad \dim_{\mathbb{C}}S=2,\qquad 2\cdot 2=4 .
$$

**Why the two-sided product is compulsory.** One-sided multiplication is not an action of a group on the algebra by algebra maps: $L_{\tilde Q}(\tilde X\tilde Y)$ carries one factor $\tilde Q$ and $L_{\tilde Q}(\tilde X)L_{\tilde Q}(\tilde Y)$ carries two, and no normalization repairs the count. Conjugation $\tilde X\mapsto\tilde Q\tilde X\tilde Q^{-1}$ is an algebra map for every invertible $\tilde Q$. So the group that acts on the algebra by algebra maps is the pair $S^{3}_{L}\times S^{3}_{R}$ with the single diagonal copy selected by $\tilde Q=\tilde P$, and the algebra is a module for that pair through the two slots.

**The diagonal copy.** The rotation is the diagonal subgroup,

$$
X\longmapsto\tilde u\,X\,\tilde u^{-1},\qquad \tilde u\tilde u^{-1}=e_t,
$$

and its generators are $J_{k}-J'_{k}$, where $J_{k}=\tfrac12L_{\vec e_{k}}$ and $J'_{k}=\tfrac12R_{\vec e_{k}}$. The minus sign is the anti-homomorphism read at the level of the Lie algebra: the right generators obey $[J'_{x},J'_{y}]=-J'_{z}$ while the left ones obey $[J_{x},J_{y}]=+J_{z}$, and the two minus signs cancel. The decomposition below is a decomposition under this diagonal copy, which is the group $S^{3}=\mathrm{Spin}(3)$ of the rotations.

**The slot is self-dual.** The rotor group preserves a nondegenerate antisymmetric form on $S$, the volume form, and an antisymmetric form is an isomorphism $S\to S^{*}$. Hence $S^{*}\cong S$ as carriers, and the algebra is a square,

$$
\mathbb{B}\cong S\otimes S .
$$

The isomorphism is not an equality and not canonical in form: it is the place where a sign may enter, and it is the same place where the conjugation $\natural$ enters below. The square is the object the addition rule applies to.

## The Clebsch–Gordan Series

**Theorem (the addition rule).** The irreducible unitary carriers of the rotor group are labelled by $j\in\tfrac12\mathbb{Z}_{\ge0}$, the carrier of label $j$ has dimension $2j+1$ and Casimir $j(j+1)$, and for two labels

$$
j_{1}\otimes j_{2}=\bigoplus_{j=\lvert j_{1}-j_{2}\rvert}^{j_{1}+j_{2}} j,
$$

each summand occurring once. This is a theorem about the labels of a compact group; it is not a formula about coefficients, and it is proved without any here.

**The case of the algebra.** With $j_{1}=j_{2}=\tfrac12$,

$$
\tfrac12\otimes\tfrac12=0\oplus 1,
$$

and since the algebra is the square of the slot,

$$
\mathbb{B}\cong V_{1}\oplus V_{0},\qquad \dim_{\mathbb{C}}V_{1}=3,\qquad \dim_{\mathbb{C}}V_{0}=1,\qquad 3+1=4 .
$$

**What the theorem asserts and what it leaves open.** It asserts the two labels, that each occurs once, and that no other label occurs. It does not say which subspace of the algebra is which summand; that needs the projectors of the next section, and it is there that the abstract series becomes a statement about $\mathbb{B}$.

**Multiplicity one, and what that buys.** Each label occurs once, so each summand is the whole isotypic piece of its label. There is no room for a second copy and no ambiguity in an identification: once a subspace is known to be invariant and of the right dimension, it *is* the summand. The whole identification below is a dimension count and an invariance check, and nothing more.

## The Two Projectors

**Definition.** The **Clebsch–Gordan projectors** are

$$
P_{0}=\tfrac12\bigl(\mathrm{id}+\natural\bigr),\qquad P_{1}=\tfrac12\bigl(\mathrm{id}-\natural\bigr).
$$

**Proposition (they are the split).** The conjugation $\natural$ is complex-linear and involutive, $\natural^{2}=\mathrm{id}$, and

$$
P_{0}^{2}=P_{0},\qquad P_{1}^{2}=P_{1},\qquad P_{0}P_{1}=P_{1}P_{0}=0,\qquad P_{0}+P_{1}=\mathrm{id}.
$$

*Proof.* Complex-linearity: $\natural$ reverses the three vector units and fixes $e_t$, and it does not touch the complex coefficients, so $\natural(i\tilde X)=i\natural(\tilde X)$. Involution is the definition of a conjugation. The four identities are the algebra of $\pm1$ eigenspaces of an involution. ∎

**Proposition (their images).** For $\tilde X=a\,e_t+\vec v$,

$$
P_{0}\tilde X=a\,e_t,\qquad P_{1}\tilde X=\vec v,
$$

so $P_{0}\mathbb{B}=\mathbb{C}e_t$ is the centre and $P_{1}\mathbb{B}=\mathbb{C}\mathfrak{k}$ is the vector part.

*Proof.* $\natural(a\,e_t+\vec v)=a\,e_t-\vec v$, and the two combinations give the two halves. ∎

**Why the conjugation and not the other mark.** The Hermitian adjoint is $*=\bar{\cdot}\circ\natural$, and it is conjugate-linear. A conjugate-linear involution does not split a complex vector space: its $\pm1$ "eigenspaces" are real subspaces and their sum is the real space, not the complex one. The split needs a complex-linear involution, and among the two marks of the corpus $\natural$ is the one. This is also why the two-sided operator of this subsection carries the $\natural$ mark and not the $*$ mark: the exponential articles use the $*$ form for the Hermitian pairing, and the decomposition uses the $\natural$ form for the split.

**Proposition (equivariance).** For a unit element $\tilde u$, meaning $\natural\tilde u=\tilde u^{-1}$,

$$
P_{0}\bigl(\tilde u\,\tilde X\,\tilde u^{-1}\bigr)=\tilde u\,P_{0}\bigl(\tilde X\bigr)\tilde u^{-1},
\qquad
P_{1}\bigl(\tilde u\,\tilde X\,\tilde u^{-1}\bigr)=\tilde u\,P_{1}\bigl(\tilde X\bigr)\tilde u^{-1}.
$$

*Proof.* $\natural$ is an anti-automorphism, $\natural(\tilde A\tilde B\tilde C)=\natural\tilde C\,\natural\tilde B\,\natural\tilde A$. On the conjugate element, $\natural(\tilde u\tilde X\tilde u^{-1})=\natural(\tilde u^{-1})\natural(\tilde X)\natural(\tilde u)=\tilde u\,\natural(\tilde X)\,\tilde u^{-1}$, using $\natural\tilde u=\tilde u^{-1}$, and then $P_{0}$ acts on the middle factor alone. ∎

**Corollary (the split is two-sided, and only two-sided).** The two projectors commute with the total generators $J_{k}-J'_{k}$ and do not commute with the one-sided generators $J_{k}$. The split therefore belongs to the pair and not to either factor, and the reason is structural: a projector built from the slot swap belongs to the diagonal action by construction. The observation that the projection onto the scalar part commutes with the total generators and not with one factor is the same fact, and this is its proof.

**Remark (no axis).** Neither projector mentions $\vec e_x$, $\vec e_y$, $\vec e_z$ individually, and neither needs a positive-definite form. They are polynomial in $\natural$, which is a datum of the algebra, so the split is canonical. This is the precise sense in which the decomposition costs nothing: it is the two-element group $\{\mathrm{id},\natural\}$ acting on the algebra, and the two projectors are its averaging operators.

## The Two Summands and Their Spins

**The summand $V_{0}$.** $P_{0}\mathbb{B}=\mathbb{C}e_t$ is the centre. The diagonal action fixes it, the generator acts as $0$ there, and the weight set is $\{0\}$. Dimension $1=2\cdot0+1$, Casimir value $0=0\cdot1$. The label is $0$.

**The summand $V_{1}$.** $P_{1}\mathbb{B}=\mathbb{C}\mathfrak{k}$ is the vector part. It is three-dimensional and invariant: the diagonal action sends $\vec v$ to $\tilde u\vec v\tilde u^{-1}$, which is again a vector. The operator $H^{\mathrm{tot}}_{z}=i\tfrac12\,\mathrm{ad}_{\vec e_{z}}$ has, on the complex basis $\vec e_{x}+i\vec e_{y}$, $\vec e_{x}-i\vec e_{y}$ and $\vec e_{z}$, the eigenvalues $+1$, $-1$ and $0$. The weight set is $\{-1,0,+1\}$, the highest weight is $1$, the dimension is $3=2\cdot1+1$, and the Casimir value is $2=1\cdot2$. The label is $1$.

**Proposition (the weights add up).** On the whole algebra the multiset of weights of $H^{\mathrm{tot}}_{z}$ is $\{-1,0,+1,0\}$, the union of the two summands, and the multiplicities are those of the two dimensions.

*Proof.* On $\vec e_{x}+i\vec e_{y}$: $\mathrm{ad}_{\vec e_{z}}(\vec e_{x}+i\vec e_{y})=2\vec e_{y}-2i\vec e_{x}=-2i(\vec e_{x}+i\vec e_{y})$, and the factor $i\tfrac12$ gives $+1$. On the conjugate vector the sign is opposite. On $\vec e_{z}$ and on $e_t$ the adjoint of $\vec e_{z}$ kills the vector, so the weight is $0$ twice. ∎

**The real forms.** The two summands are complex subspaces of complex dimension $1$ and $3$. Their real forms are the fixed line $\mathbb{R}e_t$ and the real vector part $\mathfrak{k}$, of real dimensions $1$ and $3$, and those are the carriers of real dimension $2s+1$ used in the carriers and closures articles. The passage from the complex summand to the real carrier is restriction to the real form, and it changes no label: $2s+1$ is read on the complex summand, and the real form has the same dimension for integer $s$. Nothing in the decomposition depends on that reading; it is recorded because the three carrier articles of this subsection are written over the reals.

**A full turn is the identity.** The exponential of $2\pi H^{\mathrm{tot}}_{z}$ acts as $e^{2\pi i}$ on the weight $+1$ part, $e^{-2\pi i}$ on the weight $-1$ part and as $1$ on the weight $0$ part, so it is the identity on the algebra. A half turn is not: it acts as $-1$ on the two weight-$\pm1$ directions and as $+1$ on the weight-$0$ directions. The diagonal action is therefore an action of the rotation group and not merely of its double cover, and the statement is the integer-valuedness of the two labels read as a statement about a turn.

## The Range and What Falls Outside It

**The range.** The summands of $\tfrac12\otimes\tfrac12$ are $j=0$ and $j=1$. The range is the pair of integers between $0$ and $1$, and no half-integer occurs, because the lower end is $0$ and the upper end is the sum $1$.

**A third slot.** Three factors give $\tfrac12\otimes\tfrac12\otimes\tfrac12=(\tfrac12\otimes\tfrac12)\otimes\tfrac12=(0\oplus1)\otimes\tfrac12=\tfrac12\oplus\bigl(\tfrac12\oplus\tfrac32\bigr)$, so the first appearance of $j=\tfrac32$ costs a third factor. Four factors reach $j=2$ and no further, and in general $m$ factors of the half-integer slot reach the maximum $\tfrac m2$ and every label below it. At $n$ the slot of $M_{n}(\mathbb{C})$ is $V_{(n-1)/2}$ and the algebra is its square, so its labels run over $0,\dots,n-1$; that is the table of *The Spin Decomposition of $M_n(\mathbb{C})$*, and the biquaternion algebra is the case $n=2$, the case with the shortest chain.

**Two consequences to state plainly.** The algebra holds no spin $\tfrac32$ and no spin $2$, so nothing in it transforms as a third-rank or fourth-rank object under the rotation. And the algebra holds no half-integral label at all: every summand has an integer label, which is the same statement as the full turn acting as the identity.

## The Casimir Is the Projector

**The identity.** With $H_{k}=iJ_{k}$ and $\mathbf{H}^{2}_{\mathrm{tot}}=\sum_{k}\bigl(H_{k}-H'_{k}\bigr)^{2}$,

$$
\mathbf{H}^{2}_{\mathrm{tot}}=2P_{1}=\mathrm{id}-\natural .
$$

**Proof (operator level).** Since $L_{\vec e_{k}}-R_{\vec e_{k}}=\mathrm{ad}_{\vec e_{k}}$, the total generator is $\tfrac12\mathrm{ad}_{\vec e_{k}}$ and

$$
\mathbf{H}^{2}_{\mathrm{tot}}=\sum_{k}\Bigl(i\tfrac12\mathrm{ad}_{\vec e_{k}}\Bigr)^{2}=-\tfrac14\sum_{k}\mathrm{ad}^{2}_{\vec e_{k}} .
$$

On the centre the adjoint of every $\vec e_{k}$ kills, so the sum is $0$. On the vector part, for $k\ne j$,

$$
\mathrm{ad}^{2}_{\vec e_{k}}\vec e_{j}=\bigl[\vec e_{k},[\vec e_{k},\vec e_{j}]\bigr]=\bigl[\vec e_{k},\pm2\vec e_{l}\bigr]=-4\vec e_{j},
$$

using $[\vec e_{x},\vec e_{y}]=2\vec e_{z}$ and $[\vec e_{x},\vec e_{z}]=-2\vec e_{y}$, and $\mathrm{ad}^{2}_{\vec e_{k}}\vec e_{k}=0$. So each of the three vector directions receives $-4$ from the two values of $k$ different from its own, the sum is $-8$ on $\mathfrak{k}$ and $0$ on the centre, that is

$$
\sum_{k}\mathrm{ad}^{2}_{\vec e_{k}}=-8P_{1},
$$

and $\mathbf{H}^{2}_{\mathrm{tot}}=\tfrac14\cdot 8P_{1}=2P_{1}$. ∎

**What the identity says.** The quadratic Casimir of the diagonal action *is* the Clebsch–Gordan projector, up to the factor $2$. Its two values are $0$ and $2$, those are $j(j+1)$ at $j=0$ and $j=1$, and its $\pm1$ structure is the split itself. The label is not an external bookkeeping imposed on the algebra: it is a polynomial in the generators, and the polynomial is the projector.

**The slot value.** The same computation with a single slot, $L$ alone, gives $\sum_{k}H_{k}^{2}=-\sum_{k}J_{k}^{2}=\tfrac34\mathrm{id}$, because $L^{2}_{\vec e_{k}}=L_{\vec e_{k}^{2}}=-\mathrm{id}$ and each $J_{k}^{2}=-\tfrac14\mathrm{id}$. The value $\tfrac34$ is $j(j+1)$ at $j=\tfrac12$, so the single slot carries $V_{1/2}$. The two numbers $\tfrac34$ and $2$ are the Casimir read on a factor and on a summand, and the difference between them is the difference between the two kinds of carrier.

**The factorization.** Write the total Casimir as the sum of the two one-sided Casimirs minus the cross term,

$$
\mathbf{H}^{2}_{\mathrm{tot}}=\sum_{k}\bigl(H_{k}^{2}+H_{k}^{\prime 2}-2H_{k}H'_{k}\bigr)=\tfrac32\,\mathrm{id}-2\sum_{k}H_{k}H'_{k}.
$$

Comparing with $\mathbf{H}^{2}_{\mathrm{tot}}=2P_{1}$ gives

$$
\sum_{k}H_{k}H'_{k}=\tfrac34\,\mathrm{id}-P_{1},
$$

so the cross term takes the value $\tfrac34$ on the vector part and $-\tfrac14$ on the centre. It is the only place where the two factors meet, and the identity says that the meeting is an affine function of the projector: the difference of the two values is the split, and the average is the slot Casimir $\tfrac34$.

## Where the Coefficients Are

**The series is used whole.** The split $V_{1}\oplus V_{0}$ is the series, and it needs no coefficient: the two projectors are built from $\natural$ and the summands are their images.

**The coefficients are the refinement of a summand.** The Clebsch–Gordan coefficients appear when the carrier $V_{1}$ is resolved into weight vectors, or when the two slots are resolved into weight vectors and the summands are written as combinations of products. Both resolutions need an axis: the weight vectors of $H^{\mathrm{tot}}_{z}$ are $\vec e_{x}\pm i\vec e_{y}$ and $\vec e_{z}$, and the axis $\vec u_{\mathrm{r}}$ replaces $\vec e_{z}$. A coefficient table is a table of weights, and a table of weights is a choice of axis.

**The rule of the subsection, read correctly.** The statement that no array and no preferred axis is used does not forbid the Clebsch–Gordan series. It forbids the resolution. The series is canonical, the resolution is not, and the two are separated by exactly the two projectors: everything above the projectors is coefficient-free, everything below them carries the axis. This is the precise sense in which the section's no-axis rule and the Clebsch–Gordan logic are the same rule.

## The Slot and the Algebra

**The apparent conflict.** The series gives two summands and this subsection lists three carriers: $0$, $\tfrac12$ and $1$. Both counts are right, and they count different things.

**The resolution.** A summand is a subspace of the algebra; a factor is not. The algebra holds $V_{1}$ and $V_{0}$ as subspaces, canonically, by the two projectors. The spin-$\tfrac12$ carrier is the slot $S$, and $S$ is not a subspace of $S\otimes S^{*}$: it is one of the two things being multiplied. To see a spinor inside the algebra one must choose a minimal left ideal, that is an idempotent $\tilde\Pi_{+}=\tfrac12(e_t+i\vec u_{\mathrm{r}})$, and then $\mathbb{C}\tilde\Pi_{+}$ carries $V_{1/2}$ under left multiplication. The ideal is a realization, not a summand, and the axis in it is a choice.

**The three carries, stated exactly.** $V_{0}$ is canonical and one-dimensional, and it is the centre. $V_{1}$ is canonical and three-dimensional, and it is the vector part. $V_{1/2}$ is canonical as a factor and not as a subspace: it is realized by any minimal left ideal, and the family of realizations is a family of axes. So the two integer carriers are data of the algebra and the half-integer carrier is data of the algebra plus a choice.

**Why the three are not a direct sum.** Their dimensions are $1$, $2$ and $3$ over $\mathbb{R}$, they sum to $6$, and the algebra has real dimension $8$. The two summands account for $1+3=4$ real dimensions as real forms, or $2+6=8$ as complex subspaces, and the slot accounts for none of them: it is a factor, of complex dimension $2$ and real dimension $4$, and it is not a subspace at all except through a choice. The arithmetic $1+2+3=6\neq8$ is not an accident of counting; it is the statement that the list mixes the two kinds of carrier.

**The hierarchy this gives the subsection.** The canonical objects are the two summands and their projectors; the choice-dependent object is the spinor plane; and the closures of the carriers are the places where a chosen carrier sits inside a canonical subspace. That is the order in which *From the Spin to the Carriers and the Closures* is now written, and it is the reason its three carriers are read after the series and not before.

## What Must Not Be Written

**Four sentences that are false, with their repairs.**

1. **"The biquaternion algebra contains spin $\tfrac32$."** The range of $\tfrac12\otimes\tfrac12$ is $0$ and $1$. A third slot is needed, and at $n$ slots the top label is $\tfrac{n-1}{2}$.
2. **"The algebra is $S\otimes S$."** It is $S\otimes S^{*}$. The second slot is the dual, because right multiplication is an anti-homomorphism; the two slots are isomorphic as carriers, and the isomorphism is a form, not an identity.
3. **"The Clebsch–Gordan coefficients are needed to split the algebra."** The split is $P_{0}$ and $P_{1}$, built from $\natural$. The coefficients are needed to resolve a summand into weight vectors, which is a further and optional step.
4. **"The decomposition is a grading of the algebra."** It is not: $\vec e_{x}\vec e_{x}=-e_{t}$ puts a scalar in the product of two vector elements, so $V_{1}\cdot V_{1}$ meets $V_{0}$ and the product does not respect the split. The split is a decomposition of the module, and the algebra product does not preserve it.

**A fifth, about the mark.** "The split is built from the Hermitian adjoint." It is built from $\natural$. The adjoint is conjugate-linear, so it splits the real space and not the complex one.

## Verification

Every row was recomputed on the algebra over $\mathbb{C}$ with a multiplication table built from the units and no library quaternion type. The operators were applied to arbitrary elements and the residual is the largest absolute value of an entry.

| claim | what was computed | value |
| --- | --- | --- |
| $\natural$ is complex-linear and involutive | $\natural(i\tilde X)-i\natural\tilde X$, $\natural^{2}\tilde X-\tilde X$ | $0$ |
| the two projectors | $P_{0}^{2}-P_{0}$, $P_{1}^{2}-P_{1}$, $P_{0}P_{1}$, $P_{0}+P_{1}-\mathrm{id}$ | $0$ |
| the images | $\vec e_{t}$, $\vec e_{x}$, $\vec e_{y}$, $\vec e_{z}$ components of $P_{0}\tilde X$ and $P_{1}\tilde X$ | scalar part and vector part exactly |
| the traces | $\operatorname{tr}P_{0}$, $\operatorname{tr}P_{1}$ on the four complex dimensions | $1$, $3$ |
| the half bracket | $[J_{x},J_{y}]-J_{z}$ | $0$ |
| the slot Casimir | $\sum_{k}H_{k}^{2}-\tfrac34\mathrm{id}$ | $0$ |
| the doubled commutator | $\sum_{k}\mathrm{ad}^{2}_{\vec e_{k}}+8P_{1}$ | $0$ |
| the total Casimir | $\mathbf{H}^{2}_{\mathrm{tot}}-2P_{1}$ | $0$ |
| the equivariance | $P_{0}(\tilde u\tilde X\tilde u^{-1})-\tilde uP_{0}(\tilde X)\tilde u^{-1}$ over unit rotors | $8.9\cdot10^{-16}$ |
| the split is two-sided | $[P_{0},J_{k}-J'_{k}]$ | $0$ |
| the split is not one-sided | $[P_{0},J_{k}]$ | $0.5$ in the largest entry |
| the weights of the total generator | eigenvalues of $H^{\mathrm{tot}}_{z}$ | $\{+1,-1,0,0\}$ |
| the Casimir spectrum | eigenvalues of $\mathbf{H}^{2}_{\mathrm{tot}}$ | $0$ once, $2$ thrice |
| the cross term | $\sum_{k}H_{k}H'_{k}-\bigl(\tfrac34\mathrm{id}-P_{1}\bigr)$ | $0$ |
| a full turn | $\exp\bigl(2\pi H^{\mathrm{tot}}_{z}\bigr)$ | $\mathrm{id}$ |

**The two rows that carry the article.** $\mathbf{H}^{2}_{\mathrm{tot}}=2P_{1}$ and $\sum_{k}\mathrm{ad}^{2}_{\vec e_{k}}=-8P_{1}$ are the identity between the Casimir and the projector, one at the level of the generators and one at the level of the adjoint. Everything else in the table is a consistency check on them.

**One check that is not numerical.** The addition rule is a theorem about all labels and no sample confirms it. What the numbers confirm is its instance $\tfrac12\otimes\tfrac12$: two labels, dimensions $1$ and $3$, and the two Casimir values.

## Summary

The algebra is the square of one slot, $\mathbb{B}\cong S\otimes S^{*}\cong V_{1/2}\otimes V_{1/2}$, because left multiplication is a homomorphism and right multiplication an anti-homomorphism, and the right slot is the dual for that reason. The slot is self-dual through an antisymmetric form, so the square is a square of one carrier.

The Clebsch–Gordan series for two half-integer labels is $0\oplus1$, so the algebra is $V_{1}\oplus V_{0}$, of complex dimensions $3$ and $1$. The split is realized by the two projectors $P_{0}=\tfrac12(\mathrm{id}+\natural)$ and $P_{1}=\tfrac12(\mathrm{id}-\natural)$, which are complementary, canonical, complex-linear, and equivariant for the diagonal action. Their images are the centre and the vector part, with labels $0$ and $1$ read from the weights $\{0\}$ and $\{-1,0,+1\}$.

The quadratic Casimir of the diagonal action is $2P_{1}$ exactly, so the label is a polynomial in the generators and the projector is the label. On a single slot the same computation gives $\tfrac34$, the value at $j=\tfrac12$.

The range of the series is the range of the labels: no spin $\tfrac32$ and no spin $2$ inside the algebra, and no half-integer label at all, which is the same statement as a full turn acting as the identity. The Clebsch–Gordan coefficients are not needed for the split; they are needed to resolve a summand into weight vectors, and that resolution is the choice of an axis.

The two summands are subspaces of the algebra and the half-integer carrier is a factor of it. That is why the subsection lists three carriers while the series gives two summands, and it is why the spinor plane of the carriers article is realized by a minimal left ideal and carries a choice of axis.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $S$, $S^{*}$ | the slot and its dual; $\mathbb{B}\cong S\otimes S^{*}$ |
| $V_{j}$ | the irreducible carrier of label $j$, of dimension $2j+1$ and Casimir $j(j+1)$ |
| $L_{\tilde Q}$, $R_{\tilde Q}$ | left and right multiplication by $\tilde Q$ |
| $J_{k}=\tfrac12L_{\vec e_{k}}$, $J'_{k}=\tfrac12R_{\vec e_{k}}$ | the halved one-sided generators |
| $J_{k}-J'_{k}=\tfrac12\mathrm{ad}_{\vec e_{k}}$ | the generators of the diagonal action |
| $H_{k}=iJ_{k}$, $\mathbf{H}^{2}_{\mathrm{tot}}$ | the Hermitian normalization and the total Casimir |
| $\natural$, $*$ | quaternion conjugation and the Hermitian adjoint $*=\bar{\cdot}\circ\natural$ |
| $\natural\tilde X=a\,e_t-\vec v$ | the conjugation on $\tilde X=a\,e_t+\vec v$ |
| $P_{0}=\tfrac12(\mathrm{id}+\natural)$, $P_{1}=\tfrac12(\mathrm{id}-\natural)$ | the Clebsch–Gordan projectors |
| $\mathfrak{k}$, $\mathbb{C}\mathfrak{k}$ | the real vector part $\mathbb{R}\vec e_{x}\oplus\mathbb{R}\vec e_{y}\oplus\mathbb{R}\vec e_{z}$, and its complexification |
| $\tilde\Pi_{+}=\tfrac12(e_t+i\vec u_{\mathrm{r}})$ | the idempotent that realizes the slot as a minimal left ideal |

## Further Reading

- [The Tensor Square of $\mathbb{C}^2$](the-tensor-square-of-c2.html), for the same four-dimensional square split as $3+1$, computed with a chosen form and the symmetric and alternating squares.
- [The Spin Decomposition of $M_n(\mathbb{C})$](the-spin-decomposition-of-mnc.html), for the general $n$: the module of label $\tfrac{n-1}{2}$ and the labels $0,\dots,n-1$ of the algebra, of which this article is the case $n=2$.
- [From the Spin to the Carriers and the Closures](the-carriers-the-representation-the-spin-and-the-closure.html), for the three carriers, the spinor plane as a minimal left ideal, the closure of each carrier and the spin table.
- [From the Spin Group to the Spin of a Single Rotor](from-the-spin-group-to-the-spin-of-a-single-rotor.html), for the single slot: the spin group as $S^{3}$, the one-sided generators and the Casimir value $\tfrac34$.
- [The Spin Group via $4\times4$ Real Matrices](the-spin-group-via-4x4-real-matrices.html), for the faithful real form of the slot and the two isoclinic copies of $S^{3}$ in $SO(4)$.
- [One-Sided Operators on the N-Regular Sector](one-sided-operators-on-the-n-regular-sector.html) and [Two-Sided Operators on the N-Regular Sector](two-sided-operators-on-the-n-regular-sector.html), for the two actions read factor by factor, with the multiplicativity laws and the exponentials.
- [From the Spin of a Pair of Operators to the Spin of $M_n(\mathbb{C})$](from-the-spin-of-a-pair-of-operators-to-the-spin-of-mnc.html), for the passage from the pair to the algebra at general $n$.
- W. Fulton and J. Harris, *Representation Theory*, lecture 11, for the Clebsch–Gordan rule and its proof by highest weights.
- J.-P. Serre, *Linear Representations of Finite Groups*, part I, for the averaging operators and the isotypic decomposition.
