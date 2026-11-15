# __The Four Forms and the Four Norms__

## Introduction

**This entry reads the seventh section of the mathematical category: what a product measures once it is reduced to a scalar, and what the four reductions are.**

**The question is what a product has to say about the pair it acts on.** The previous entry read the product as an operation and its two halves. A scalar part is different: it is a single number, and the number asks what the operation is *for*. The mathematics answers with four functions of two elements, and each becomes a function of one element on the diagonal.

**The rule is one line, read at two arities.**

$$
\boxed{\;\varphi(\tilde Q_1,\tilde Q_2)=\mathrm{Sc}\bigl(K_1(\tilde Q_1)\,K_2(\tilde Q_2)\bigr),\qquad \varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q)\;}
$$

**Two arguments give a form; one argument gives an algebraic norm.** The four settings of the previous entry give four forms, and each form read on the diagonal gives one norm:

$$
P(\tilde Q)=\sum_\mu\varepsilon_\mu Q_\mu^{2},\qquad \langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2},\qquad H(\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2},\qquad \mathrm{Kr}(\tilde Q)=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2},
$$

with $\varepsilon=(1,-1,-1,-1)$.

**The single idea is that two properties single out two of the four, and they are different properties.** The quaternionic norm is the one that is multiplicative. The Hermitian norm is the one that is definite. No function is both, and the reason is not an accident of this algebra: it is the zero divisors. Everything that follows — the mass shell, the Born weight, the indefinite constraint, the sign of the sector — is a consequence of that split.

**The four words are the corpus's shorthand, and they follow the algebra rather than the other way round.** The quaternionic form is **the interval**, because its level sets on the material sector are the mass shells. The Hermitian form is **the weight**, because it is the only one that can be normalised. The plain form is **the pairing**, because it is the invariant trace pairing of two elements and its values are complex. The Krein form is **the volume**, because it is the only real-valued form that is signed. A pairing may be complex; a measure must be real; and only one of the two real measures is indefinite.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| the four forms, their brackets, their Gram matrices, their signatures, their null sets, their isometry groups, the two slots, the four algebraic norms, multiplicativity and definiteness, the qualified regular and degenerate pairs | [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) |
| the twelve operations and their scalar parts, the symmetrisation that keeps a form and the antisymmetrisation that kills it, the distinction over $\mathbb{C}$ and the coincidence over $\mathbb{R}$ | [Symmetric and Antisymmetric Decomposition of the Four General Products](../articles_maths/symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html) |
| the four general products whose scalar parts the four forms are, the identities among the four scalar parts, the trace convention | [The Four General Products and Their Relations over the Biquaternion Algebra](../articles_maths/the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html) |
| the restriction of the four forms and the four norms to the six remarkable subspaces, the signatures, the definiteness on each | [Remarkable Subspaces and the Four General Products, Forms and Norms](../articles_maths/remarkable-subspaces-and-the-four-general-products-forms-and-norms.html) |
| the $\natural$-regular and $\natural$-degenerate partition, the unit group, the null cone, the criterion of invertibility | [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) |
| the Krein partition, the two sectors of the Krein norm, the indefinite geometry | [Kr-Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/kr-regularity-and-degeneracy-in-the-biquaternion-algebra.html) |
| the algebraic norm of a form and its distinction from the topological norm | [The Norm Defined by a Form](../articles_maths/the-norm-defined-by-a-form.html) |
| the one topological norm of the space and its square root | [The Euclidean Topology of the Biquaternion Algebra](../articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.html) |
| the unqualified *regular* and *degenerate*, which are spectral and not norm-theoretic | [The Spectrum](../articles_maths/the-spectrum.html) |

**The rows are the entry's order.** The four forms first, because they are the objects; then the count of the four, which is one lemma; then the signatures, which are what a restriction can change; then the groups, which are what a form preserves; then the four partitions, which are what a form cuts.

## The Results in Brief

### Two Arities of One Letter

**A form takes two elements and a norm takes one, and one letter serves both.**

$$
2P(\tilde Q_1,\tilde Q_2)=\mathrm{Tr}\bigl(\tilde Q_1\tilde Q_2\bigr),\qquad
2N(\tilde Q_1,\tilde Q_2)=\mathrm{Tr}\bigl(\tilde Q_1^{\natural}\tilde Q_2\bigr),
$$
$$
2H(\tilde Q_1,\tilde Q_2)=\mathrm{Tr}\bigl(\tilde Q_1\tilde Q_2^{*}\bigr),\qquad
2\mathrm{Kr}(\tilde Q_1,\tilde Q_2)=\mathrm{Tr}\bigl(\tilde Q_1^{\natural}\tilde Q_2^{*}\bigr),
$$

in the $2\times2$ image, where the trace of the central part is twice the scalar coefficient.

**The distinction is not cosmetic, and the two arities carry different laws.** A form of two elements is symmetric or conjugate-symmetric and bilinear or sesquilinear; a norm of one element is a quadratic function of the coordinates. Multiplicativity belongs to the second arity alone:

$$
N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)N(\tilde Q_2)\qquad\text{is a law about one element at a time.}
$$

**There is no law of the form of the same shape.** The candidate $N(\tilde Q_1\tilde Q_2,\tilde Q_3\tilde Q_4)=N(\tilde Q_1,\tilde Q_3)N(\tilde Q_2,\tilde Q_4)$ would need the middle product $\tilde Q_2\tilde Q_3$ to be central, and the algebra is not commutative; it fails on generic quadruples.

### The Four Forms

| form | letter | $\mathrm{Sc}$ of | coordinates | symmetry | Gram | signature over $\mathbb{R}$ | null set |
| --- | --- | --- | --- | --- | --- | --- | --- |
| the plain form | $P$ | $\tilde Q_1\tilde Q_2$ | $Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)$ | symmetric | $\mathrm E$ | $(4,4)$ | the complex cone |
| the quaternionic form | $N$ | $\tilde Q_1^{\natural}\tilde Q_2$ | $Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ | symmetric | $\mathrm I_4$ | $(4,4)$ | $\mathcal N$, the zero-divisor cone |
| the Hermitian form | $H$ | $\tilde Q_1\tilde Q_2^{*}$ | $Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ | conjugate-symmetric | $\mathrm I_4$ | $(8,0)$ | $\{0\}$ |
| the Krein form | $\mathrm{Kr}$ | $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | $Q_{1t}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ | conjugate-symmetric | $\mathrm E$ | $(2,6)$ | $\mathcal K$, the Krein cone |

**The four are distinct as functions of two elements, and one pair separates them.** At $\tilde Q_1=\vec e_x$ and $\tilde Q_2=\vec e_x+i\vec e_x$ the values are $-(1+i)$, $1+i$, $1-i$ and $-(1-i)$: four different complex numbers.

**The count of four is one lemma about the twelve operations.** The symmetrisation of a family keeps the scalar part of its general product, and the antisymmetrisation kills it. So the four general products and their four symmetric parts carry the four forms two by two, and the four antisymmetric parts carry the zero form. A bracket has no scalar part, and a measure cannot be obtained from one.

### What Each Slot Decides

**The second slot decides whether the value is complex or real.**

$$
K_2=\mathrm{id}\iff\text{bilinear}\iff\text{the norm lands in }\mathbb{C},\qquad
K_2={}^{*}\iff\text{sesquilinear}\iff\text{the norm lands in }\mathbb{R}.
$$

**The first slot decides the Gram matrix, and through it the signature and the definiteness on each subspace.**

$$
K_1=\mathrm{id}\iff\text{Gram }\mathrm E\iff\text{the vector part enters with a minus},\qquad
K_1={}^{\natural}\iff\text{Gram }\mathrm I_4\iff\text{the vector part enters with a plus}.
$$

**The two divisions are independent and their product is the four.** Two forms share a symmetry and two share a Gram matrix, and no two share both: $\{P,N\}$ and $\{H,\mathrm{Kr}\}$ are the two symmetries, $\{P,\mathrm{Kr}\}$ and $\{N,H\}$ the two Gram matrices, and each form is one intersection.

**One structural consequence is worth naming here.** Every one of the four forms is the plain form with a conjugation inserted in one or both slots:

$$
N(\tilde Q_1,\tilde Q_2)=P(\tilde Q_1^{\natural},\tilde Q_2),\qquad
H(\tilde Q_1,\tilde Q_2)=P(\tilde Q_1,\tilde Q_2^{*}),\qquad
\mathrm{Kr}(\tilde Q_1,\tilde Q_2)=P(\tilde Q_1^{\natural},\tilde Q_2^{*}).
$$

**So the four measures are one pairing with a conjugation inserted in one or both slots.** The two real ones are exactly those in which the *second* slot is an adjoint, and the reality of the value is the reality of that adjoint.

### The Four Norms

| algebraic norm | letter | value | multiplicative | definite | vanishing set | job |
| --- | --- | --- | --- | --- | --- | --- |
| $\sum_\mu\varepsilon_\mu Q_\mu^{2}$ | $P$ | $\mathbb{C}$ | no | — | the complex cone, dim $6$ | the pairing, read on the diagonal |
| $\sum_\mu Q_\mu^{2}$ | $N$ | $\mathbb{C}$ | **yes** | — | $\mathcal N$, dim $6$ | invertibility, the reduced norm, the interval |
| $\sum_\mu\lvert Q_\mu\rvert^{2}$ | $H$ | $\mathbb{R}$ | no | **yes** | $\{0\}$ | the topological norm, the weight |
| $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$ | $\mathrm{Kr}$ | $\mathbb{R}$ | no | no | $\mathcal K$, dim $7$ | the indefinite geometry, the constraint |

**Two of the four have a property the others lack, and the two properties are different.** The quaternionic norm is the determinant of the $2\times2$ image, hence multiplicative; the Hermitian norm is a sum of four non-negative terms, hence definite. Each fails the property of the other, and one substitution each settles it:

$$
N\bigl(\vec e_x+i\vec e_y\bigr)=0\quad\text{though}\quad\vec e_x+i\vec e_y\neq0,
$$
$$
H\bigl(\vec e_x+i\vec e_y\bigr)=2,\qquad \bigl(\vec e_x+i\vec e_y\bigr)^{2}=0,\qquad H\bigl(0\bigr)=0\neq2\cdot2 .
$$

**The second refutation is the sharper one, and it is not a violation.** $H$ is not multiplicative and cannot be: $H$ is a measure of an element, and the product of two elements is measured by the quaternionic norm. The two questions — *how large* and *is it invertible* — are answered by different functions.

### The Signatures at Three Levels

**A signature is a statement about one level, and the four forms have three levels.**

- the **complex form**: a Gram matrix and a complex rank;
- its **realification**: the form on the eight real coordinates, where a symmetric bilinear form of complex rank $n$ becomes the split $(n,n)$ and a Hermitian form of inertia $(p,q)$ doubles to $(2p,2q)$;
- its **restriction**: the form on a real subspace, which has a signature of its own and may be definite where the form is not.

**The three levels give three different answers for the same form.**

| form | complex Gram | realification | on $\mathbb{B}_{\Phi}$ | on $\mathbb{B}_{\Psi}$ |
| --- | --- | --- | --- | --- |
| $P$ | $\mathrm E$ | $(4,4)$ | $(0,4)$ | $(4,0)$ |
| $N$ | $\mathrm I_4$ | $(4,4)$ | $(3,1)$ | $(1,3)$ |
| $H$ | $\mathrm I_4$ | $(8,0)$ | $(4,0)$ | $(4,0)$ |
| $\mathrm{Kr}$ | $\mathrm E$ | $(2,6)$ | $(1,3)$ | $(1,3)$ |

**The two bilinear forms are neutral on the algebra and definite on a sector; the Hermitian one is definite everywhere; the Krein one is indefinite everywhere.** A reader who carries $(4,4)$ into a statement about spacetime has changed the object, and a reader who carries $(0,4)$ into a statement about the algebra has changed it in the other direction.

### The Restriction to the Sectors and the Subspaces

**On the two sectors the four forms coincide in pairs, with a sign.**

$$
P=-H,\qquad \mathrm{Kr}=-N\quad\text{on }\mathbb{B}_{\Phi};\qquad
P=H,\qquad \mathrm{Kr}=N\quad\text{on }\mathbb{B}_{\Psi}.
$$

**The sign is the sector, and the identity is a form-level statement.** It does not say that the four products agree there; the products are the subject of the previous entry and they do not.

**On the six subspaces the pairing of the four changes.** The Krein norm is positive definite of signature $(2,0)$ on the centre and negative definite of signature $(0,6)$ on the vector subspace; the plain and the quaternionic forms are $(1,1)$ on the centre and $(3,3)$ on the vector subspace; and the Hermitian form is definite on every one of the six.

**The imaginary part of a sesquilinear form is an alternating form, and the alternating companion is the area.** Write $\omega(\tilde X,\tilde Y)=\operatorname{Im}H(\tilde X,\tilde Y)$. Because $H$ is Hermitian, $\overline{H(\tilde X,\tilde Y)}=H(\tilde Y,\tilde X)$, so $\omega$ is real-valued and alternating, $\omega(\tilde X,\tilde X)=0$. Since $i$ is central and $(i\tilde Y)^{*}=-i\tilde Y$, both $H(\tilde X,i\tilde Y)=-iH(\tilde X,\tilde Y)$ and $H(i\tilde X,\tilde Y)=iH(\tilde X,\tilde Y)$ hold, and the identity that governs $\omega$ is one line,

$$
\omega(i\tilde X,\tilde Y)=\operatorname{Re}H(\tilde X,\tilde Y).
$$

The area is the metric with one argument turned by a quarter turn, and it is nothing else; the equivalent form $\omega(\tilde X,i\tilde Y)=-\operatorname{Re}H(\tilde X,\tilde Y)$ carries a minus that is only the bookkeeping of which argument is turned.

**Its rank on the six subspaces is $2$, $6$ and four zeros.**

| subspace | $\dim_{\mathbb{R}}$ | $\operatorname{rank}\omega$ |
| --- | --- | --- |
| $\mathbb{B}_{C}$, the centre | $2$ | $2$ |
| $\mathbb{B}_{V}$ | $6$ | $6$ |
| $\mathbb{B}_{H}$ | $4$ | $0$ |
| $\mathbb{B}_{iH}$ | $4$ | $0$ |
| $\mathbb{B}_{\Psi}$ | $4$ | $0$ |
| $\mathbb{B}_{\Phi}$ | $4$ | $0$ |

**Both halves of the table follow from the identity.** On a subspace stable under $J$ one has $iU=U$, so if $\omega(\tilde X,\cdot)$ vanishes on $U$ then $\operatorname{Re}H(\tilde X,\cdot)$ vanishes on $U$, and $\operatorname{Re}H$ is positive definite, hence $\tilde X=0$: the area is non-degenerate there. On a real-type subspace the Hermitian form is real-valued — each of them is the fixed space of an antilinear involution under which $H$ is conjugate-symmetric — so its imaginary part vanishes identically. The complex subspaces are exactly the $J$-stable ones, which is why the division falls where it does.

**The companion of the Krein form does the same.** Replacing $H$ by $\mathrm{Kr}$ in the definition gives an alternating form with the same ranks, $2$ and $6$ on the complex subspaces and zero on the four real-type ones; the two differ in value and not in where they live.

**The four-dimensional real-type subspaces carry the four signatures the corpus uses.**

| subspace | $P$ | $N$ | $H$ | $\mathrm{Kr}$ |
| --- | --- | --- | --- | --- |
| the real quaternions $\mathbb{R}^{4}$ | $(1,3)$ | $(4,0)$ | $(4,0)$ | $(1,3)$ |
| $i\mathbb{R}^{4}$ | $(3,1)$ | $(0,4)$ | $(4,0)$ | $(1,3)$ |
| $\mathbb{B}_{\Phi}$, the material sector | $(0,4)$ | $(3,1)$ | $(4,0)$ | $(1,3)$ |
| $\mathbb{B}_{\Psi}$, the informational sector | $(4,0)$ | $(1,3)$ | $(4,0)$ | $(1,3)$ |

**The table states the fact the entry turns on.** Each slice carries a form with one time direction and three space directions, and the letter that carries it changes: it is $P$ on the real quaternions, of signature $(1,3)$, and it is $N$ on the material sector, of signature $(3,1)$. The two are the same form with the overall sign reversed. The interval is a signature, and the letter records where the imaginary unit sits among the coordinates.

### The Four Collapse to Two on the Real Part

**For real coefficients the conjugation is the identity, so two pairs of forms coincide.**

$$
P=\mathrm{Kr},\qquad N=H\qquad(\tilde Q_1,\tilde Q_2\ \text{real}).
$$

**The collapse is exact and it is a loss.** A computation restricted to real coefficients sees two measures, one complex-valued and one real-valued, and it cannot separate the plain from the Krein or the quaternionic from the Hermitian. The complex structure is the carrier of the distinction, and the same phenomenon appears on the twelve operations and on the ten that survive.

**The consequence for a check is a caution.** An identity verified on real elements and claimed for the four forms is a claim about two, and a property that holds for $N$ and fails for $H$ — or the reverse — is invisible there.

### The Isometry Groups

**A form is known by the operators that preserve it, and the four groups are classical.**

$$
\mathrm{Isom}(P)=O_4(\mathbb{C}),\quad
\mathrm{Isom}(N)=O_4(\mathbb{C}),\quad
\mathrm{Isom}(H)=\mathrm{U}(4),\quad
\mathrm{Isom}(\mathrm{Kr})=\mathrm{U}(1,3),
$$

of real dimensions $12$, $12$, $16$ and $16$.

**The two bilinear groups carry the same name for a reason, and the two sesquilinear ones do not.** The sign matrix is congruent to the identity over $\mathbb{C}$,

$$
\mathrm E=S^{\mathsf T}S,\qquad S=\operatorname{diag}(1,i,i,i),
$$

so the two bilinear forms are conjugate copies and one group serves both. A Hermitian congruence preserves inertia, and $\mathrm E$ has inertia $(1,3)$ while $\mathrm I_4$ has $(4,0)$, so no invertible $S$ carries one to the other and $\mathrm U(1,3)$ is not a conjugate of $\mathrm U(4)$.

**The quaternion conjugation lies in all four groups.** It is the matrix $\mathrm E$ in the coordinate basis, $\mathrm E^{2}=\mathrm I_4$, and $\mathrm E$ preserves each of the four forms; the fundamental symmetry of the indefinite structure is therefore a symmetry of every measure, and not a property of the Krein form alone.

### The Qualified Regular and Degenerate Pairs

**Each letter cuts the algebra in two by the vanishing of its norm.**

| letter | degenerate set | $\dim_{\mathbb R}$ | contains a unit | equals the non-units |
| --- | --- | --- | --- | --- |
| $P$ | the complex cone $\{P=0\}$ | $6$ | yes | no |
| $N$ | $\mathcal N$, the origin together with the zero divisors | $6$ | no | **yes** |
| $H$ | $\{0\}$ | $0$ | no | no |
| $\mathrm{Kr}$ | $\mathcal K$, the Krein cone | $7$ | yes | no |

**Only the $N$ cut is the invertibility partition.** The witness is one element: $e_t+\vec e_x$ is a unit with $P=\mathrm{Kr}=0$ and $N=2$, so the plain and the Krein norms vanish on an invertible element; $H$ is a sum of four non-negative terms and vanishes only at the origin.

**The four degenerate sets are pairwise distinct, and four elements witness it.**

| element | $P$ | $N$ | $\mathrm{Kr}$ | what it is |
| --- | --- | --- | --- | --- |
| $e_t+\vec e_x$ | $0$ | $2$ | $0$ | a unit |
| $e_t+i\vec e_x$ | $2$ | $0$ | $0$ | a zero divisor |
| $\vec e_x+i\vec e_y$ | $0$ | $0$ | $-2$ | a zero divisor |
| $\sqrt2\,e_t+\vec e_x+i\vec e_y$ | $2$ | $2$ | $0$ | a unit |

**The words without a letter are different words.** *Regular* alone is **spectrally regular**, $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}\neq0$, and *degenerate* alone is **spectrally degenerate**, $B^{2}=0$. The letter is never omitted when the four norms are meant, because the spectral condition and the norm condition are independent: the entry before this one is about the first, and this one is about the second.

### The Four Are Not the Only Four

**Beside the four norms, the corpus reads one element four ways, and the two lists must not be confused.**

| reading | object | what it says | where it fails |
| --- | --- | --- | --- |
| norm | $N(\tilde R_\Phi)=\sum_\mu R_\mu^{2}$ | the value and its sign; the mass shell as a level set | detects no polarisation count and no label |
| rank | $\operatorname{rank}\mathsf M_2(\tilde R_\Phi\tilde R_\Phi^{*})$ | the count of polarisations, two massive and one massless | fixes only whether the mass vanishes |
| charge | the compact slice $\{\tilde U:\tilde U\tilde U^{*}=e_t\}\cong\mathrm U(2)$ | the discrete internal label | says nothing about the cone |
| scale | the polar modulus $r$ | the unit of length, the dilation potential | is a unit and not a level set |

**Only the first is the mass, and only $N$ belongs to both lists.** The rank agrees with the norm on the cone and is blind to the value of the mass; the charge is defined only off the cone; the scale is the unit the mass is measured in.

## The Interpretations

### I.7.a — A Form of Two Elements Is an Amplitude; Its Diagonal Is a Number

**Read:** the four forms take two elements and return a scalar, and the four norms are those forms at the two equal arguments.

**The two objects behave differently in a theory.** A function of two elements is what a theory evaluates on a pair — a transition, an overlap, an expectation. A function of one element is what a theory reads off a single object — a size, a mass, a normalisation. The algebra supplies both from one letter, and the passage between them is the diagonal.

**The diagonal is not a lossless restriction.** The form knows the pair and the norm knows one element; a form that vanishes on the diagonal can be non-zero off it, and a form that is non-zero on the diagonal can vanish on a pair. The $\mathrm{Kr}$ form is the clearest case: $\mathrm{Kr}(\tilde Q)=0$ on the whole Krein cone, while $\mathrm{Kr}(\tilde Q_1,\tilde Q_2)$ is non-zero for a generic pair of null elements.

**The physical reading is that a theory needs two arities and often confuses them.** The probability of a transition is a value of a form at two elements; the normalisation of a state is a value of a norm at one. A formalism that uses one word for both is using one symbol for two functions, and the four-letter notation is what keeps them apart.

**The boundary.** The reading is not a claim that every pairing is an amplitude. It is the claim that the arity is a real distinction, that the algebra carries it, and that a law proved at one arity does not transfer to the other.

### I.7.b — The Weight: the One Definite Measure and the One Distance

**Read:** the Hermitian norm is positive definite, $H(\tilde Q)>0$ for $\tilde Q\neq0$, of signature $(8,0)$ on the real algebra.

**One property follows at once and no other norm has it.** The square root is a norm in the topological sense:

$$
\lVert\tilde Q\rVert^{2}=H(\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2},
$$

and a norm gives distance, balls, convergence, bounded operators and a completion.

**The physical reading is that only this measure can be normalised.** A probability needs a positive number that can be divided by its total; a state needs a sphere to live on; a limit needs a topology. The three requirements are one requirement, and $H$ is the only one of the four that meets it.

**The measure is blind to the sector, and that blindness is exact.**

$$
H=\lVert\cdot\rVert^{2}\ \text{on both sectors};\qquad P=-H\ \text{on }\mathbb{B}_{\Phi},\quad P=H\ \text{on }\mathbb{B}_{\Psi}.
$$

**So the sign of the sector is not visible to the weight.** A material element and an informational element of the same coordinate moduli have the same weight, and the difference between them is a difference of a bilinear form and not of the measure. This is the precise content of the corpus's rule that the sesquilinear layer does not carry the sector.

**The form supplies the weight and not the state.** The pure states are the minimal Hermitian idempotents, $\tfrac12(e_t+i\vec u)$ with $\vec u$ a real unit vector; the weight pairs a state with an observable and returns a number. The state carries an axis and no phase, and the phase is not a value of $H$.

**The boundary.** That the definite Hermitian form is physical probability is the hypothesis of the informational sector and not a theorem of the algebra. The algebra proves that a definite pairing exists and that it is unique among the four.

### I.7.c — The Interval: the One Multiplicative Norm

**Read:** the quaternionic norm is multiplicative, $N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)N(\tilde Q_2)$, and it is the determinant of the $2\times2$ image.

**Multiplicativity is a law of composition, and it has one immediate consequence.** The causal type of a composite is the product of the causal types; the units, the zero divisors and the null set are each closed under multiplication; and the level set $N=1$ is a group.

**The physical reading is that this is the only measure that survives a product.** A theory that composes operations and asks for an invariant has exactly one candidate, and the candidate is the determinant. The other three measures are destroyed by composition: the weight of a product is not the product of the weights, and the plain norm of a product is not the product of the plain norms.

**The determinant reading makes the name precise.** $N(\tilde Q)=\det\mathsf M_2(\tilde Q)$, so the norm is the volume scale of the element as a linear map: the image of the unit cell has $N$ times the volume. A composite scales volumes by the product, which is multiplicativity read geometrically.

**On the material sector the same number is the interval.**

$$
N(\tilde R_\Phi)=-{r'_t}^{2}+x^{2}+y^{2}+z^{2},
$$

of signature $(3,1)$, with the light cone as its zero set and the hyperboloids $N=-m^{2}c^{2}$ as its level sets. One function, two readings: a volume scale on the algebra, an interval on the sector.

**The boundary.** The interval is real on the four-dimensional real-type subspaces and complex on the centre and the vector subspace. The mass shell is a level set on the sector, not a value of the form on the algebra, and the entry derives no mass spectrum from it.

### I.7.d — The Pairing: the Trace Form and the Sign of the Sector

**Read:** the plain form is the invariant pairing of the algebra, $2P(\tilde Q_1,\tilde Q_2)=\mathrm{Tr}(\tilde Q_1\tilde Q_2)$, and its value is complex in general.

**A pairing may be complex; a measure must be real, and this is where the alphabet divides.** The two forms with the star in the second slot have real values; the two without it have complex values. So the plain form is not a measure of size but a pairing of two elements, and the distinction is the second slot and not a convention.

**On the sectors the pairing is a signed square and the sign is the sector.**

$$
P(\tilde R_\Phi)=-\bigl({r'_t}^{2}+x^{2}+y^{2}+z^{2}\bigr)<0,\qquad
P(\tilde H_\Psi)={h_t}^{2}+s_x^{2}+s_y^{2}+s_z^{2}>0.
$$

**The physical reading is that the pairing is a flag and not a metric.** It says which half an element belongs to and measures neither half: it is minus the Euclidean square on the material side and plus it on the informational side, so its sign is the sector and its modulus is the weight.

**The pairing also crosses the split.** For one element of each sector the scalar part is purely imaginary,

$$
\mathrm{Sc}(\tilde R_\Phi\tilde H_\Psi)=i\bigl(r'_t h_t-(\vec v,\vec s)\bigr),
$$

the Minkowski pairing of the two four-vectors multiplied by $i$, with the relative sign of time and space inside the bracket. The same two elements paired by $N$ give the Euclidean pairing, $i(r'_t h_t+(\vec v,\vec s))$; the difference of the two is the sign of the spatial term, and that sign is the first slot.

**The sharpest warrant for the word *flag* is one comparison.** $P(e_t+\vec e_x)=0$ on a unit, and $P(e_t+i\vec e_x)=2$ on a zero divisor. A function that vanishes on an invertible element and does not vanish on a non-invertible one decides no invertibility, so it cannot be the metric of a theory of reversible operations.

**The boundary.** The complex cone $\{P=0\}$ is not the light cone and not the zero-divisor cone. It is a six-dimensional complex quadric that cuts across the units and the non-units alike, and no physical set is its image.

### I.7.e — The Volume: the Signed Content and the Krein Cone

**Read:** the Krein norm is real and indefinite, of signature $(2,6)$ on the algebra, and it is the difference of the two contents of the centre–vector split.

$$
\mathrm{Kr}(\tilde Q)=\lvert Q_t\rvert^{2}-\lvert\vec Q\rvert^{2}.
$$

**The reading is a signed content.** The Hermitian norm adds the squared moduli of the coordinates; the Krein one adds them with a minus on the three vector coordinates. The first counts the content of the element, the second counts the difference between its temporal content and its spatial content, and the surface where the two balance is the cone $\mathcal K=\{\lvert c\rvert=\lvert v\rvert\}$, of real dimension seven.

**Only one of the two real measures is signed, and that is the whole of the name.** A weight is a content and has no sign problem; a signed content is a volume with an orientation, and its sign says which side of the cone the element is on.

**The indefinite form normalises nothing, and the geometry shows it.** The level sets are not spheres but hyperboloids, and they split into two components of different topology:

$$
\{\mathrm{Kr}=1\}\cong S^{1}\times\mathbb{R}^{6},\qquad
\{\mathrm{Kr}=-1\}\cong\mathbb{R}^{2}\times S^{5}.
$$

**The physical reading is that a signed content fixes a constraint and not a state.** A gauge calibration distinguishes two kinds of direction and leaves the normalisation to a choice; it does not prepare a state, and its form is the form of that freedom. The signature is the difference: a definite form counts states, an indefinite one counts a constraint.

**The fundamental symmetry makes the reading consistent.** The quaternion conjugation is an isometry of $\mathrm{Kr}$ with $\mathrm{Kr}(\tilde Q^{\natural},\tilde Q^{\natural})=\mathrm{Kr}(\tilde Q,\tilde Q)$, and its eigenspaces are the centre and the vector subspace, of complex dimensions one and three, on which the sign is opposite. So $\mathrm{Kr}(\tilde Q_1,\tilde Q_2)=H(\tilde Q_1^{\natural},\tilde Q_2)$: the signed measure is the weight with the quaternion conjugate inserted in the first slot, and this is the exact sense in which an indefinite geometry is a definite one with a chosen conjugation. The map is ${}^{\natural}$ and not the mirror of §*I.1*, which is multiplication by the central $i$ and has order four.

**The boundary.** The form is a form. It derives no gauge group, no coupling and no field content; the indefinite structure at large belongs to the geometry block, and the cone $\mathcal K$ is not the zero-divisor cone.

### I.7.f — No Function Is Both a Mass and a Probability

**Read:** no function on the algebra with $\varphi(0)=0$ is both definite and multiplicative.

**The proof is one line and it is the whole entry.**

$$
(e_t+i\vec e_x)(e_t-i\vec e_x)=0,\qquad e_t\pm i\vec e_x\neq0,
$$

so a multiplicative $\varphi$ with $\varphi(0)=0$ gives $\varphi(e_t+i\vec e_x)\varphi(e_t-i\vec e_x)=0$; one factor vanishes on a non-zero element, and a definite function cannot vanish there.

**The physical reading is that a theory of one algebra needs two different norms.** The interval is the measure that survives composition, and it vanishes on the light cone. The weight is the measure that never vanishes, and it is destroyed by composition. A formalism that wants both a causal structure and a probability has to carry both, and it cannot identify them.

**This is also the precise reason the biquaternions are not a normed division algebra.** In $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and $\mathbb{O}$ the four normed division algebras of the Hurwitz theorem, the two senses coincide because there are no zero divisors. The complexification creates them, and the two senses separate.

**The obstruction is not non-commutativity, and the corpus's own examples say so.** The quaternions are non-commutative and $q\bar q$ is definite and multiplicative; the dual numbers are commutative and admit no definite multiplicative function, since $\varphi(\varepsilon)^{2}=\varphi(0)=0$ forces $\varphi(\varepsilon)=0$. The obstruction is the zero divisor, and the zero divisors come from the complexification.

**The boundary.** The proposition is about functions on the algebra, not about physical quantities. That the interval is the mass and the weight is the probability is the sector dictionary; the impossibility of one function being both is the algebra's.

### I.7.g — The Interval Is a Signature, Not a Letter

**Read:** the four-dimensional real-type subspaces carry the four signatures, and $P$ is $(1,3)$ on the real quaternions while $N$ is $(3,1)$ on the material sector.

**The letter that carries the interval is decided by the imaginary unit, and the arithmetic is one line.** A norm written $\sum_\mu Q_\mu^{2}$ gives a plus for a real coordinate and a minus for an imaginary one. In $\mathbb{B}_{\Phi}$ the scalar coordinate is imaginary and the three vector coordinates are real, so $N=-{r'_t}^{2}+x^{2}+y^{2}+z^{2}$: one time direction, three space directions. In $\mathbb{B}_{\Psi}$ the three vector coordinates are imaginary and the scalar one real, so $N={h_t}^{2}-s_x^{2}-s_y^{2}-s_z^{2}$: the same split with the other sign. On the real quaternions no coordinate is imaginary, $\sum_\mu Q_\mu^{2}$ is a sum of four squares, and the minus must be supplied by the sign matrix: the interval there is $P=t^{2}-x^{2}-y^{2}-z^{2}$.

**The physical reading is that the metric is a signature and the alphabet is a convention.** A theory that puts its spacetime in the material sector reads the interval off $N$; a theory that works on the real grade reads the same interval off $P$. The two are not two metrics. One is $\sum Q^{2}$ on a slice with an imaginary time coordinate, the other is the sign matrix on a slice with none.

**Central multiplication moves between the sectors and reverses the two bilinear measures.**

$$
i\mathbb{B}_{\Phi}=\mathbb{B}_{\Psi},\qquad
P(i\tilde Q)=-P(\tilde Q),\qquad
N(i\tilde Q)=-N(\tilde Q),\qquad
H(i\tilde Q)=H(\tilde Q),\qquad
\mathrm{Kr}(i\tilde Q)=\mathrm{Kr}(\tilde Q).
$$

**So the imaginary unit flips the two complex measures and is invisible to the two real ones.** The interval of the material sector and the interval of the informational sector are one form read with opposite values, and the two real measures cannot tell the sectors apart at all.

**The comparison also shows why the two are easy to exchange in print.** On the material sector $P=-H$ and $\mathrm{Kr}=-N$, so each measure is minus its partner there; a sign dropped in that double bookkeeping turns a metric into a weight without changing a symbol.

**The boundary.** The observation is about signatures on real subspaces. On the whole algebra over $\mathbb{C}$ both bilinear forms are neutral, $(4,4)$, and the interval of a sector is a restriction and not a global object.

### I.7.h — The Mass Shell Is a Level Set, Not a Spectrum

**Read:** on the material sector $N=-{r'_t}^{2}+x^{2}+y^{2}+z^{2}$, so the level set $N=-m^{2}c^{2}$ is the hyperboloid of four-vectors of mass $m$.

**The level set is the whole of what the norm says about the mass.** It fixes no value — the value is the label of the level set — it fixes no spin, no charge and no multiplicity.

**The physical reading is that the norm and the spectrum answer different questions.** The spectrum of the previous entry is the pair $\lambda_\pm=Q_t\pm iB$; the norm is the product $\lambda_+\lambda_-=Q_t^{2}+B^{2}=N$. The two invariants of an element are the trace and the norm, and the norm is the product of the two eigenvalues of the left multiplication.

**So the mass shell is one of the two symmetric functions of the spectrum and not a third object.** A level set of $N$ is a level set of the product of the two eigenvalues, and the mass is the value of that product on the sector.

**The reading also fixes what the other three measures cannot do.** The rank agrees with $N$ about the cone and says nothing about the value; the weight says nothing about the cone; the plain and Krein norms vanish on units and so say nothing about either.

**The boundary.** The mass shell is a level set of a form on a sector. The entry derives no mass spectrum, no mass ratio and no quantisation of the level sets.

### I.7.i — The Group Is the Measure

**Read:** the four isometry groups are $O_4(\mathbb{C})$, $O_4(\mathbb{C})$, $\mathrm U(4)$ and $\mathrm U(1,3)$, of real dimensions $12$, $12$, $16$ and $16$.

**A measure is known by what preserves it, and the two properties that matter physically are compactness and signature.** $\mathrm U(4)$ is compact; $\mathrm U(1,3)$ is not; $O_4(\mathbb{C})$ is complex and imposes no reality condition at all.

**The physical reading is that compactness is the difference between a probability theory and an indefinite one.** A compact group has a finite invariant volume and a discrete spectrum of representations; a non-compact one has neither, and keeps a distinguished time direction instead. The passage from $\mathrm U(4)$ to $\mathrm U(1,3)$ is the passage from a state space to a constrained one, and it is decided by the Gram matrix and nothing else.

**The two bilinear forms share their group, and that sharing is a fact about $\mathbb{C}$.** The sign matrix is congruent to the identity over the complex numbers, so the two bilinear measures are the same measure in two coordinate systems. Over $\mathbb{R}$ the congruence fails, and the two real specializations of the four are different groups: $O(1,3)$ and $O(4)$.

**On the material sector the isometry group of the interval is the Lorentz group.**

$$
\mathrm{Isom}\bigl(N|_{\mathbb{B}_{\Phi}}\bigr)=O(1,3).
$$

The statement is a restriction statement: it is the group of the interval on the sector, not of the quaternionic form on the algebra, and the two differ.

**The boundary.** A group of a form is not a gauge group of a theory. The entry does not claim that the gauge group of a physical model is one of the four; it claims that the measure determines its own isometries, and that the isometries are the group a theory must respect if it uses that measure.

### I.7.j — The Fundamental Symmetry Sits in All Four Groups

**Read:** the quaternion conjugation is the matrix $\mathrm E$ in the coordinate basis, and it preserves each of the four forms.

**No measure distinguishes an element from its quaternion conjugate.** Since $\mathrm E$ is an isometry of all four, every one of the four norms takes the same value on $\tilde Q$ and on $\tilde Q^{\natural}$:

$$
P(\tilde Q^{\natural})=P(\tilde Q),\qquad N(\tilde Q^{\natural})=N(\tilde Q),\qquad H(\tilde Q^{\natural})=H(\tilde Q),\qquad \mathrm{Kr}(\tilde Q^{\natural})=\mathrm{Kr}(\tilde Q).
$$

**The physical reading is that the discrete operation is invisible to every measure and visible in the pairing.** A norm is unchanged by ${}^{\natural}$; the *sign* of the vector part is what ${}^{\natural}$ reverses, and a norm squares it away. So a discrete symmetry of this kind cannot be detected by a mass or a weight, and it shows up only in a quantity that is odd in the vector part — a bracket, or the orientation of the frame.

**The same operator is what makes the indefinite form usable.** $\mathrm E$ is the fundamental symmetry of $\mathrm{Kr}$, the operator that turns it into the definite form $H$; so ${}^{\natural}$ is at once the symmetry of the four measures and the tool that converts the signed one into the positive one.

**The boundary.** That a measure is blind to ${}^{\natural}$ does not make ${}^{\natural}$ a physical symmetry. It states that the four measures cannot witness it, and it locates the witness elsewhere.

### I.7.k — Four Cones, and Only One Is the Wall

**Read:** the four norms have four different zero sets, of dimensions $6$, $6$, $0$ and $7$.

**Only the quaternionic one is the set of the non-units, and the others vanish on units.**

$$
\{N=0\}=\{0\}\cup\mathcal Z,\qquad
P(e_t+\vec e_x)=0,\qquad \mathrm{Kr}(e_t+\vec e_x)=0,\qquad \{H=0\}=\{0\}.
$$

**The physical reading is that reversibility has exactly one measure.** The wall of the reversible region is the zero set of the determinant, and no other norm draws it. A theory that wants a cone of reversibility — a horizon of invertibility, a massless boundary — must use $N$; a theory that uses $P$ or $\mathrm{Kr}$ draws a cone that contains units and therefore cuts through the reversible region.

**The light cone is a cut and not a null set.**

$$
\text{light cone}=\mathcal N\cap\mathbb{B}_{\Phi},
$$

and the two are different objects: the null set of $N$ on the algebra is six-dimensional and contains elements of both sectors, while the light cone is its trace on a four-dimensional slice.

**The two cones that are easy to confuse are the zero-divisor cone and the Krein cone.** They have dimensions six and seven, they are both real, and they are both invariant; but $\mathcal K$ contains units and $\mathcal N$ does not, so a statement about one is not a statement about the other.

**The boundary.** A zero set is a set. The entry does not claim that every element of the wall is a physical light ray, and it does not derive the signature from the cone; the direction is the other way.

### I.7.l — A Real Computation Sees Two Measures

**Read:** on real coefficients $P=\mathrm{Kr}$ and $N=H$.

**The collapse is a test of what a computation can conclude.** A numerical check on real elements cannot separate the plain pairing from the Krein volume, and cannot separate the quaternionic norm from the Hermitian one. Two of the four functions are invisible to it.

**The physical reading is that a real description loses the sector, and with it the shell.** On the real grade the quaternionic norm is $t^{2}+x^{2}+y^{2}+z^{2}$, a sum of four squares of real numbers, so it is positive definite there and no level set of it is a mass shell. The shell exists on $\mathbb{B}_{\Phi}$, where one coordinate is imaginary; it is a property of the complex structure and not of the algebra read over $\mathbb{R}$.

**The same lesson was stated for the operations, and the count is the same count.** Ten operations and two measures from twelve and four: the complex structure contributes one distinction to each list, and a real description loses both.

**The boundary.** A real computation is not a cheaper route to the same answers; it is a computation about a different object, and the entry states which object it is about whenever a signature is quoted.

### I.7.m — The Area Belongs to the Complex Subspaces and the Metric to the Sectors

**Read:** the alternating companion $\omega=\operatorname{Im}H$ is non-degenerate on the centre and on the complex space sector, of ranks $2$ and $6$, and it vanishes on the four real-type subspaces.

**The division of labour is between two questions.** The complex sectors carry the area: $\omega$ pairs the two times on $\mathbb{B}_{C}$ and each material direction with its informational partner on $\mathbb{B}_{V}$. The four real-type subspaces carry the metric and the probability, which are symmetric, and no area. *How much* and *how much turns* are two questions, and they are asked on two different subspaces.

**The reason is the identity and not the naming.** $\omega(i\tilde X,\tilde Y)=\operatorname{Re}H(\tilde X,\tilde Y)$ says that the area is the metric with one argument turned by a quarter turn. Where $J$ stays inside the subspace the turn stays inside too, so no direction of the subspace is invisible to $\omega$; on a real-type subspace the Hermitian form is real-valued, and a real form has no imaginary part to give. The complex subspaces are exactly the $J$-stable ones, so the division falls where it does and could not fall elsewhere.

**The boundary.** A subspace without an area pairing is not a subspace without an antisymmetric structure: the commutator is antisymmetric and does not vanish on a sector. The vanishing stated here concerns the scalar-valued alternating part of the two sesquilinear forms, and nothing else. The area also adds no dynamics; it is a property of the restriction of a form, and it supplies neither a Hamiltonian nor a quantisation.

## The Limits

**The four words are a naming and not a theorem.** The algebra proves that four forms exist, that they are distinct, that their Gram matrices and signatures are $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$, that one of them is multiplicative and another definite, and that no function is both. It does not prove that these are the four quantities a physical theory evaluates.

**Three levels of signature are kept apart throughout.** A complex Gram matrix, a realified signature and a restricted signature are three statements about the same form, and the entry names the level whenever a signature is quoted. The interval of a physical sector is a restriction.

**Two senses of norm are kept apart.** The algebraic norm is a map into the ring, complex for the two bilinear forms and real for the two Hermitian ones; the topological norm is the one positive square root, $\lVert\tilde Q\rVert^{2}=H(\tilde Q)$. A norm is not a distance until a positivity is declared.

**The coincidences on the sectors are form-level statements.** $P=\pm H$ and $\mathrm{Kr}=\pm N$ on a sector do not make the four products agree there, and they do not make the Krein form a probability or the plain form an interval.

**The entry states no dynamics, no mass value, no gauge group and no state space.** The mass shell is a level set; the charge is a label of a compact group; the interval is a metric and not an equation of motion; the volume is a signed content and not a field.

**The four partitions are four cuts and not one.** A degenerate biquaternion is not the same object as a zero divisor for any letter; only $N$'s cut coincides with the non-units, and only off the origin.

## Summary

- A form is the scalar part of a product and an algebraic norm is that form at two equal arguments; one letter serves the two arities, and the two arities obey different laws.
- The twelve operations carry four forms and no more: the symmetrisation keeps the scalar part of its family, the antisymmetrisation kills it, so the four general products and their symmetric parts carry the four forms two by two and the four brackets carry the zero form.
- The second slot decides whether the value is complex or real, and with it whether the form can supply a measure of size; the first slot decides the Gram matrix, the signature and the definiteness on each subspace.
- The four forms are $P=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, $N=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$, $H=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ and $\mathrm{Kr}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$, with Gram matrices $\mathrm E$, $\mathrm I_4$, $\mathrm I_4$ and $\mathrm E$ and realified signatures $(4,4)$, $(4,4)$, $(8,0)$ and $(2,6)$.
- Every one of the four is the plain form with a conjugation inserted in one or both slots; the two real forms are those whose second slot is an adjoint.
- The quaternionic norm is the one multiplicative norm, the determinant of the $2\times2$ image; the Hermitian norm is the one definite norm, and its square root is the only topological norm.
- No function is both definite and multiplicative, and the zero divisors are the reason; the split is the failure of the biquaternions to be a normed division algebra.
- On the material sector the four restrictions are $(0,4)$, $(3,1)$, $(4,0)$ and $(1,3)$; on the informational sector they are $(4,0)$, $(1,3)$, $(4,0)$ and $(1,3)$; on the sectors $P=-H$ and $\mathrm{Kr}=-N$ on the first and $P=H$, $\mathrm{Kr}=N$ on the second.
- The interval is a signature and not a letter: it is $P$, of signature $(1,3)$, on the real quaternions and $N$, of signature $(3,1)$, on the material sector, because $\sum_\mu Q_\mu^{2}$ takes a minus from an imaginary coordinate while $P$ takes it from the sign matrix.
- Central multiplication exchanges the two sectors and reverses both bilinear norms, $P(i\tilde Q)=-P(\tilde Q)$ and $N(i\tilde Q)=-N(\tilde Q)$, while leaving both real measures unchanged.
- The isometry groups are $O_4(\mathbb{C})$, $O_4(\mathbb{C})$, $\mathrm U(4)$ and $\mathrm U(1,3)$, of real dimensions $12$, $12$, $16$ and $16$; the quaternion conjugation lies in all four.
- Only the quaternionic cut is the invertibility partition; the plain and Krein norms vanish on units, the Hermitian norm only at the origin, and the four degenerate sets are pairwise distinct.
- On real coefficients the four collapse to two, $P=\mathrm{Kr}$ and $N=H$, so a real computation cannot tell the plain pairing from the Krein volume, nor the quaternionic norm from the Hermitian one.
- The four norms are the measures of one element; they are not the four readings of one element — norm, rank, charge and scale — and only the norm is the mass.
- The imaginary part of a sesquilinear form is an alternating form: it is non-degenerate on the two complex subspaces, of ranks $2$ and $6$, and it vanishes on the four real-type ones, because there the Hermitian form is real-valued.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $P(\tilde Q_1,\tilde Q_2)$, $\langle\cdot,\cdot\rangle$ | the plain form, $\mathrm{Sc}(\tilde Q_1\tilde Q_2)$, symmetric, Gram $\mathrm E$ |
| $N(\tilde Q_1,\tilde Q_2)$, $\langle\cdot,\cdot\rangle_{\natural}$ | the quaternionic form, the interval, $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$, Gram $\mathrm I_4$ |
| $H(\tilde Q_1,\tilde Q_2)$, $\langle\cdot,\cdot\rangle_{*}$ | the Hermitian form, the weight, $\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, Gram $\mathrm I_4$ |
| $\mathrm{Kr}(\tilde Q_1,\tilde Q_2)$, $\langle\cdot,\cdot\rangle_{\natural*}$ | the Krein form, the volume, $\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})$, Gram $\mathrm E$ |
| $\varphi(\tilde Q)=\varphi(\tilde Q,\tilde Q)$ | one letter, two arities: the form at two arguments, the algebraic norm at one |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector of the quaternion conjugation, which the first slot applies |
| $\mathrm E$, $\mathrm I_4$ | the two Gram matrices; $\mathrm E$ is also the matrix of the quaternion conjugation |
| $(4,4)$, $(4,4)$, $(8,0)$, $(2,6)$ | the realified signatures of $P$, $N$, $H$, $\mathrm{Kr}$ |
| $O_4(\mathbb{C})$, $\mathrm U(4)$, $\mathrm U(1,3)$ | the isometry groups, of real dimensions $12$, $16$ and $16$ |
| $\omega(\tilde X,\tilde Y)$ | the alternating companion, $\operatorname{Im}H$, of ranks $2$ and $6$ on the complex subspaces and $0$ on the four real-type ones |
| the complex cone, $\mathcal N$, $\mathcal K$ | the null sets of $P$, of $N$ and of $\mathrm{Kr}$; that of $H$ is $\{0\}$ |
| $P$-regular, $N$-regular, $H$-regular, $\mathrm{Kr}$-regular | $\Phi(\tilde Q)\neq0$ for the four letters; only $N$-regular is the unit group |
| $\Phi$-degenerate | $\Phi(\tilde Q)=0$; only the $N$ set is the non-unit set |
| $\lVert\tilde Q\rVert$ | the topological norm, $\bigl(H(\tilde Q)\bigr)^{1/2}$ |
| $\mathcal Z$ | the zero divisors; $\{N=0\}=\{0\}\cup\mathcal Z$ |

## Further Reading

**In the mathematics corpus.** The nine articles of the source table, and inside the first of them the sections *The Four Forms*, which owns the brackets and the isometry groups; *The Four Algebraic Norms*, which owns the multiplicativity and the definiteness; *What the Four Algebraic Norms Separate*, which owns the proposition that no function is both and the refutation of each of the other three; and *Commutativity, Multiplicativity and Definiteness*, which owns the correction of the common paraphrase — the obstruction is the zero divisors and not the non-commutativity.

**In this category.** *The Four Products: Composition, Probability, Causality and Gauge* supplies the products whose scalar parts the four forms are, and the two dials that index them. *The Spectrum and the Two Modes* supplies the two invariants of an element, the trace and the norm, and the pair whose product is the interval. *The Two Sectors: Split and the Four Bridges* supplies the cross-sector pairing and the restriction table.

**In the archive, until they are rewritten.** [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_physics/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) is the earlier treatment of the same four labels, with the change of scalars and the four readings of one element. [The Krein Form and the Indefinite Structure](../articles_physics/the-krein-form-and-the-indefinite-structure.html) is the indefinite geometry at large. [The Born Rule from the Hermitian Form: Derivation and Comparison](../articles_physics/the-born-rule-from-the-hermitian-form-derivation-and-comparison.html) is the weight read as a probability. [The Meaning of N-Regularity and Degeneracy](../articles_physics/the-meaning-of-n-regularity-and-degeneracy.html) is the invertibility cut. [The Zero-Divisor Cone and the Massless Spectrum](../articles_physics/the-zero-divisor-cone-and-the-massless-spectrum.html) is the cone as a physical boundary.
