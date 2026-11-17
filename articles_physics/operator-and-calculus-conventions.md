# __Operator and Calculus Conventions__

## Introduction

These are the conventions of the operators and of the calculus. An operator acting by multiplication is the element it multiplies by, and its glyph is the glyph of that element; the article fixes the named operators, the dagger, the Kraus operator and the Fock exception. The calculus follows: the derivative marks, the gradient and the d'Alembertian, and the four product-form-norm readings of the gradient that the field equations use.

The article assumes the base of *Algebra and Element Conventions*, the products and forms of *Product and Form Conventions*, and the norms of *Norm and Pairing Conventions*. The matrix models are in *Matrix Representations Conventions*; the superscripts on operators are in *Index and Notation Conventions*.

## The Operators

**An operator acting by multiplication is the element it multiplies by.** Every element acts on the algebra, on the left $L_{\tilde Q}$ or on the right $R_{\tilde Q}$, and an operator whose letter is the letter of an element **is** that element. The glyph of the operator is therefore the glyph of its element, and the marks are read on it as on the element: the tilde marks the quaternionic element read with its scalar part, the arrow the pure element read on its vector part alone. Neither mark says that a glyph is an operator, and no mark is added to say it.

**The named operators.** The structural operators take an upright capital letter and carry the element in the subscript, where it keeps its own mark:

| Operator | Glyph |
| --- | --- |
| left multiplication | $L_{\tilde Q_1}(\tilde Q_2)=\tilde Q_1\tilde Q_2$ |
| right multiplication | $R_{\tilde Q_1}(\tilde Q_2)=\tilde Q_2\tilde Q_1$ |
| two-sided | $L_{\tilde Q_4}R_{\tilde Q_1}(\tilde Q_2)=\tilde Q_4\tilde Q_2\tilde Q_1$ |
| two-sided operator | $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}=\operatorname{H}_{\tilde Q}$ |
| inner derivation | $\operatorname{ad}_{\tilde Q_4}(\tilde Q_1)=[\tilde Q_4,\tilde Q_1]$ |
| automorphism | $\operatorname{Ad}_{\tilde Q_4}$ |

The tilde sits in the subscript because it belongs to the element, not to the operator: $L_{\tilde Q}$ is an operator, $\tilde Q$ is the element that generates it.

**The basis operators.** The four units are written in the subscript, $L_{\mathrm{axf},e_\mu}$ and $R_{\mathrm{axf},e_\mu}$, and nowhere else: the short form $L_\mu$ is not used in this corpus. The right family is read from the left one by transposition in the coefficient basis, $R_{\mathrm{axf},e_\nu}=D(L_{\mathrm{axf},e_\nu})^{\mathsf T}D$ with $D=\operatorname{diag}(1,-1,-1,-1)$, and in the Peirce display of §*The Legacy Pauli Gamma Formulation* by the exchange $\mathsf S$ of the two mixed Peirce units, $R=\mathsf S L^{\mathsf T}\mathsf S^{-1}$, and the sixteen two-sided operators $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ are the matrix basis and the basis operator table of *Matrix Representations Conventions*, §*The Clifford Structure and the Frame*; five of the sixteen are the frame basis operators up to the factor $i$: $iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}$, $iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}$, $iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}$, $iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}$, $-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}$.

**The spin operator and the words built on it.** The generator of the rotations is $\tilde S_{\Psi,\eta}=\frac{\hbar}{2}i\vec e_\eta$, an operator whose glyph is the glyph of its element, like every operator of this section. The three words built on it — the **spin**, the **elementary spinor** and the **Dirac spinor** — are fixed in *Special Element Conventions*, §*The Spin Convention* and §*The Spinor Convention*, and are not restated here.

**The two marks on a glyph that is also an operator.** An operator read through its element follows the element rule in full.

- A glyph read with its scalar part, four components: the tilde. The canonical momentum $\tilde p=p_te_t+\vec p$, the Legendre conjugate of $\tilde q$; the biquaternionic gradient $\tilde\nabla_\Phi$ of §*The Gradient*; the gauge-covariant gradient $\tilde\nabla_{\mathrm{gco},\Phi}$ of §*The Gauge-Covariant Gradient*.
- A pure glyph, three components: the arrow. The momentum operator $\vec p=-i\,\hbar\,\vec\nabla_\Phi=\sum_{\eta\in\{x,y,z\}}\vec e_\eta p_\eta$.

The gradient decides the case cleanly: $\tilde\nabla_\Phi$ is not pure, because its $e_t$ term carries $-i\,\partial/\partial r'_t$, while $\vec\nabla_\Phi=\sum_{\eta\in\{x,y,z\}}\,\vec e_\eta\,\partial/\partial r_\eta$ is pure: it is the vector part of $\tilde\nabla_\Phi$, $\tilde\nabla_\Phi=-i\,e_t\partial/\partial r'_t+\vec\nabla_\Phi$, and the fixed glyph $\vec\nabla_\Phi$ of §*The Gradient* and the arrowed $\vec\nabla_\Phi$ name the one operator, the arrow being written where its purity is what the sentence names.

**The case follows the layer.** The arrow does not change the case: a pure operator of the quaternion layer stays lower case, $\vec p$, and one of the biquaternion layer takes the upper case, $\vec P$. Where the letter already names another object of the layer, the operator is written in its explicit form, $-i\,\hbar\,\vec\nabla_\Phi$, because no subscript marks an operator: the two-letter form $\mathrm{op}$ is not a token of the corpus, and *Algebra and Element Conventions* states the rule (§*The Algebra and Its Basis*). The three-momentum and the momentum operator share $\vec p$, as an eigenvalue and its operator do.

**The mark of a part, and the side carried by position.** The only arrow on a glyph is the short one, and it marks the **pure part**: $\vec e_x$, $\vec p$. The long arrow that sits over an operator is a different mark and not a second arrow of the same kind: it is the mark of the transposed reading, fixed in §*The Transposition of the Gradient*. The side of an action is not marked at all. It is carried by position, $b\tilde{Ξ}$ against $\tilde{Ξ} b$, the actor written on the side from which it acts, and position is unambiguous because the operand is itself a glyph.

**What names a side where position is not enough.** Three signs, each of which the corpus needs for a purpose of its own.

- $\natural$ marks the conjugation of an element, $a^{\natural}=(a_0,-a_1,-a_2,-a_3)$, and it is what carries a change of side, because it is an anti-automorphism: $(ab)^{\natural}=b^{\natural}a^{\natural}$, hence $(\tilde{Ξ} D)^{\natural}=D^{\natural}\tilde{Ξ}^{\natural}$, and a right action on $\tilde{Ξ}$ is a left action on $\tilde{Ξ}^{\natural}$. The theorem is below, §*The Two Sides and the Renaming Theorem*.
- $L_a$ and $R_a$ name a side outright when a statement is about operators rather than about fields, and the basis operator $L_{a}R_{b}$ prints both sides at once. The label of the side of a basis operator is the **operator chirality** — the left slot, the right slot, or both — fixed in *Special Element Conventions*, §*The Chirality Convention*, and proved in *Operator Chirality on the Biquaternion Algebra*, of the mathematical corpus.
- The superscript $R$ marks the one case that position alone leaves genuinely ambiguous: a derivative that differentiates the factor written to its left, $F\vec\nabla_\Phi^{R}=-i(\partial F/\partial r'_t)e_t+\sum_{\eta\in\{x,y,z\}}(\partial F/\partial r_\eta)\vec e_\eta$. It is used only inside a product of two distinct factors, which is where the theorem below does not reach.

**The dagger.** The dagger is the general adjoint of an operator, never of an element: $(L_a)^{\dagger}=L_{a^{*}}$. Several adjoints arise at once — one for each form, and one for each of the two-sided operators — and the dagger is the mark that covers them all, of which the others are the instances. It is not a fifth conjugation: it belongs to the operators and not to the algebra. Where a dagger is written on an element the writing is an abuse: the mark that was meant is the star for the Hermitian conjugation, or the sign ${}^{\natural}$ for the quaternion conjugation, according to the conjugation in view. The dagger is added to the glyph and does not replace the element's mark: the arrow states purity, which the adjoint preserves, so $\vec p^{\dagger}$ is again a pure operator; the tilde states a glyph read with its scalar part, which the adjoint also preserves, so $\tilde\nabla_\Phi$ keeps its tilde. Where the adjoint in view is the one of the definite form and the operator carries no derivative, the two marks are written together, dagger first: $(L_a)^{\dagger}=(L_a)^{*}=L_{a^{*}}$. A derivative separates them: its dagger is the adjoint and carries the integration by parts, its star conjugates the invertibles alone (§*The Gradient*); the series writes $\tilde\nabla_\Phi^{*}=(\tilde\nabla_\Phi)^{\natural}$ for the star.

**A Kraus operator is an element, not an array.** The Kraus operators of a channel or an instrument multiply the state on both sides, $Ξ(\tilde{Ϛ}_{\Psi})=\sum_{l\in\mathrm{Kraus}}\tilde M_{\mathrm{kraus},l}\tilde{Ϛ}_{\Psi}\tilde M_{\mathrm{kraus},l}^{*}$, so each $\tilde M_{\mathrm{kraus},l}$ is an element of $\mathbb{B}$ and carries the tilde of the element. It is not a matrix, and the ban on a tilde on an array does not apply to it. Where the same operator is read as an array, that array is its image $\mathsf{M}_2(\tilde M_{\mathrm{kraus},l})$, which carries no tilde, and its adjoint is the dagger, $\mathsf{M}_2(\tilde M_{\mathrm{kraus},l})^{\dagger}=\mathsf{M}_2(\tilde M_{\mathrm{kraus},l}^{*})$; the corpus does not use that reading, and the star on the element is not a matrix adjoint.

**The Fock exception.** A Fock operator is not an element of the algebra; its superscript $\mathrm{fop}$ and the order of the two marks are fixed in *Index and Notation Conventions*, §*The Labels*.

## The Two Sides and the Renaming Theorem

**The statement.** Write $L_D\tilde{Ξ} := D\tilde{Ξ}$ and $R_D\tilde{Ξ} := \tilde{Ξ} D$ for the two one-sided actions on a field $\tilde{Ξ}\in\mathbb{B}$. Then

$$
R_D=\natural\circ L_{D^{\natural}}\circ\natural,
\qquad
L_D=\natural\circ R_{D^{\natural}}\circ\natural,
$$

and on a field

$$
\boxed{\;(\tilde{Ξ} D)^{\natural}=D^{\natural}\,\tilde{Ξ}^{\natural}\;}
$$

**A right action on $\tilde{Ξ}$ is a left action on $\tilde{Ξ}^{\natural}$.** The side is not a property of the equation. It is a property of the field the equation is written on.

**The three properties.** Everything rests on them, and only the third is non-trivial.

| property | statement | residual |
| --- | --- | --- |
| involutive | $\natural\circ\natural=\mathrm{id}$ | $0$ |
| $\mathbb{C}$-linear | $\natural(i\tilde{Ξ})=i\,\natural(\tilde{Ξ})$ | $0$ |
| anti-automorphism | $(ab)^{\natural}=b^{\natural}a^{\natural}$ | $2.6\times10^{-15}$ over $400$ random complex pairs |

The first makes $\natural$ invertible with $\natural^{-1}=\natural$. The third makes it **reverse the order of a product**. The second lets the mass, which is central, pass through untouched. An involution that preserved the order would identify the two sides; one that reverses the order exchanges them. $\natural$ reverses, so it exchanges.

**The proof is three symbols.** Applied to the two factors $\tilde{Ξ}$ and $D$,

$$
(\tilde{Ξ} D)^{\natural}=D^{\natural}\,\tilde{Ξ}^{\natural}.
$$

Read forwards, conjugating a right action gives a left action of the conjugated operator. Read backwards, using $\natural^{2}=\mathrm{id}$, a right action is the conjugate of a left action — the two lines of the statement above.

**In matrix form it is one congruence.** With $\mathsf C=\operatorname{diag}(1,-1,-1,-1)$ the matrix of $\natural$ on a coordinate column,

$$
\mathsf C\,R_D\,\mathsf C=L_{D^{\natural}},
\qquad
\mathsf C\,L_D\,\mathsf C=R_{D^{\natural}},
\qquad\text{both at residual }0 .
$$

$\mathsf C$ is the change of basis that exchanges the two families, and $\mathsf C^{\mathsf T}\mathsf C=I$, $\det\mathsf C=-1$.

**On an equation.** Take $\tilde{Ξ} D=m\xi$ with $m$ central, so $m^{\natural}=m$, and conjugate both sides:

$$
D^{\natural}\,\tilde{Ξ}^{\natural}=m\,\xi^{\natural}.
$$

The map $Ξ:(\tilde{Ξ},\xi)\mapsto(\tilde{Ξ}^{\natural},\xi^{\natural})$ is $\mathbb{C}$-linear, involutive and invertible, so it is a **bijection of solution sets** and not an inclusion:

$$
\{\tilde{Ξ}:\ \tilde{Ξ} D=m\xi\}\ \xrightarrow{\ Ξ\ }\ \{u:\ D^{\natural}u=m\,\xi^{\natural}\},
\qquad Ξ^{-1}=Ξ .
$$

Verified: a pair solved on the right at residual $2.0\times10^{-15}$ maps to a pair solved on the left at residual $1.1\times10^{-15}$, on all four basis solutions. Same solutions, relabelled.

**What the theorem does not say.** It does not say the two operators are equal. On $D=-5e_t+3i\vec e_x$,

$$
\bigl\langle R_D-L_{D^{\natural}}\bigr\rangle_*^{1/2}=8.4853\neq0 ,
$$

so the two arrays differ and neither may be substituted for the other at sight. What is equal is the pair of solution sets after renaming, not the operators.

**Where the theorem does not reach.** Three cases, and each is stated where it is used.

1. **More than one field.** The anti-automorphism reverses the whole order, $(\tilde{Ξ} D\xi)^{\natural}=\xi^{\natural}D^{\natural}\tilde{Ξ}^{\natural}$, residual $1.3\times10^{-14}$ over $200$ random triples. The two fields exchange places, so renaming alone does not suffice, and where the two fields are not the same object the reordering changes the statement. The bilinear identities of the integration articles stand in this case, and it is why they carry the superscript $R$ on the derivative.
2. **A carrier without $\natural$.** On a column $\tilde{Ξ}\in\mathbb{C}^{4}$ there is no quaternion conjugation, only the antilinear Dirac adjoint; on a space of functions of two variables, as in a star product, $\natural$ is not the involution in play. The theorem is a theorem about fields valued in $\mathbb{B}$.
3. **The side itself on display.** For the two-sided action $a\tilde{Ξ} b$, the mirror coupling, or the exchange of the two slots of a basis operator, conjugating the field destroys what is being displayed. There both factors stay in place and the side is named by position, or by $L_a$ and $R_a$.

**The consequence for the corpus.** Every equation that acts on a single biquaternion field is written on the left. The ones that would read as acting on the right are the same equations on the conjugate field, and the chiral pair is the instance: with $Ξ=\tilde{Ξ}^{\natural}$, the pair $\tilde\nabla_\Phi\tilde{Ξ}_{R}=k_m\tilde{Ξ}_{L}$ and $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=k_m\tilde{Ξ}_{R}$ is complete as written, both equations acting from the left, and $\natural$ is what separates them. Across the $404$ files and $10\,196$ display equations of the physics corpus no glyph names a side: the side is position, the conjugation is $\natural$, and the exchange is $N$.

## Conventions for Derivation

In this work, subscripts denote vector components, not partial derivatives as in the PDE convention; every partial derivative is written explicitly with $\partial$ followed by its variable, and no subscript is ever attached to the $\partial$ of a derivative. A subscript is therefore a component index, as in $v_x$ for the component of a velocity along an axis, or a label, as in $\tilde U_{\mathrm r}$; it never denotes a derivative. The derivative with respect to a coordinate is written with its parameter named, $\partial/\partial r'_t$ for the fourth slot and $\partial/\partial r_x$, $\partial/\partial r_y$ or $\partial/\partial r_z$ for the three space slots; a parameter is never left under the $\partial$, so none of the abbreviated spellings occurs, and the rule admits no exception for a derivative, neither on a free index nor on any other.

**A subscript on an operator names its degree, its place, its argument or its sector.** The rule governs the derivative of a field, which names its variable after the $\partial$. It does not forbid a low mark on an operator that differentiates nothing: the chain boundary is $\partial_n:C_n\to C_{n-1}$, with the degree in the subscript. These are operator labels, in the sense of *Index and Notation Conventions*, §*The Subscripts*, and they stand as written. The gradient is not one of them: it differentiates a field, its variable is fixed by the sector, and the directional derivative along a vector is written $\vec\nabla_\Phi\cdot\vec X$ and never with the vector in the low slot.

**A variant of an operator is a label, and a chart is not a variant.** The gradient carries $\natural$ in the caret or a label low, $(\tilde\nabla_\Phi)^{\natural}$ and $\tilde\nabla_{\mathrm{gco},\Phi}$, and it never takes a letter in the low slot for the coordinates it is read in. Where both marks stand on one glyph the sector goes low on the operator and $\natural$ goes outside, $(\tilde\nabla_\Phi)^{\natural}$: the conjugate of the material gradient is the material gradient of the conjugate, because $\natural$ negates the vector part and leaves the scalar imaginary alone. The sector so named is $\Phi$ and no other, and $\Psi$ never stands in the low slot of an operator. A sector is not a coordinate: $\tilde\nabla_{\Phi}$ names the four material parameters the derivative is taken in, and no coordinate is ever written in its low slot. A chart is not a slice either: a chart re-reads the parameters themselves, and the operator is not marked for it. The Wick rotation is written on the parameter, $r'_t\mapsto-i\tau$; the four terms of the sum are unchanged, only the sign of $\partial^2/\partial {r'_t}^2$ moves, and the article that continues the coordinates says which chart it reads them in rather than marking the operator.

**The low slot spells the operator, or names its component, and nothing else.** A label in the low slot names a distinct operator by spelling what makes it that operator. The label is roman and is read as written, $\tilde\nabla_{\mathrm{gco},\Phi}$ with its companion $\Box_{\mathrm{gco},\Phi}$. A single component index may follow, $\tilde\nabla_{\mathrm{gco},\Phi,\mu}$, and nothing may follow that. Nothing else enters the slot, and the list of what may not is the list of everything that distinguishes one instance of an operator from another rather than one operator from another.

Never a number. A shift is written out, $\tilde\nabla_\Phi+\kappa$, and the glyph keeps its name while the number varies; a glyph such as $\tilde\nabla_{\kappa,\Phi}$ would make the operator a function of a parameter and would have to be read as a different operator at every value of it.

Never a sign or a factor. The operators $-\Box_\Phi$ and $i\tilde\nabla_\Phi$ are written as they stand, and no glyph is reserved for a signed or scaled copy of another: the source's mutual bigradients are $\vec\nabla_{+} = i\tilde\nabla_\Phi$ and $\vec\nabla_{-} = i(\tilde\nabla_\Phi)^{\natural}$, and its wave operator is $-\Box_\Phi$.

Never a subspace or a carrier. On a subspace the gradient is $\tilde\nabla_\Phi$ in the coordinates of that subspace, the coordinates being named in the display and not in the glyph; on $\mathbb{B}_{iH}$ it is $-i$ times the gradient of $\mathbb{B}_{H}$, which is a statement about a coefficient and not a new operator.

Never a coordinate, a chart, a representation, or the variable the operator differentiates. The d'Alembertian is $\Box_\Phi$ and not $\Box_{\Phi,x}$, the covariant gradient is $\tilde\nabla_{\mathrm{gco},\Phi}$ for every field because the representation is a property of the field and is written on it, $\tilde\Xi_\psi$, and a Green's function says in words which of its arguments the operator acts on, $\Box_\Phi G(\tilde R_\Phi,\tilde R_{\Phi,2})$, rather than writing the argument in the slot, $\Box_{\tilde R_\Phi}$.

**A pair of mutual operators is two glyphs, never one glyph with a plus-or-minus.** A pair is written out, one operator at a time, and a formula that holds for both members is written twice: the source's bigradients are $\vec\nabla_{+} = i\tilde\nabla_\Phi$ and $\vec\nabla_{-} = i(\tilde\nabla_\Phi)^{\natural}$, and her wave operator is $\Box_A = \partial^2/\partial\tau^2-\Delta_\Phi$, in her letters and never wearing a $\Phi$ of its own. The rule governs the parameter shifts in the same way: $\tilde\nabla_\Phi+\kappa$ and $\tilde\nabla_\Phi-\kappa$ are two operators and both are written, and $\kappa$ itself is never a subscript.

The reason for the whole rule is one. A coefficient belongs to the element and an argument belongs to the field, so neither may enter the name of the operator, which is one operator for every value, every argument and every chart.

**The Levi-Civita derivative is not this operator.** A curved background carries a metric connection, and the articles on curved spacetime write its covariant derivative as $\nabla_\mu$, with the index it differentiates. It is a differential-geometric object of the manifold, it acts on tensors and not on the algebra, and it is never the gradient of this series. The two never meet in one computation: where a curved background meets a field of this series, the article says which of the two it has written, and the biquaternionic gradient keeps its $\Phi$.

**The derivative is written against the material parameter, and it is unhalved.** The four parameters this series differentiates are the imaginary time $r'_t$ and the three real space numbers $r_\eta$. They are real, so the derivative is taken against the parameter itself: no factor of two stands in front of it, and no factor of $i$ stands in it either, because the $i$ belongs to the coefficient of the gradient, where the fourth slot carries $-i$. The derivative against a coordinate is written $\partial/\partial r'_t$ for the fourth slot and $\partial/\partial r_\eta$ for a space slot; no derivative of the corpus is written against $R_\mu$, against $\bar R_\mu$, against the real time $h_t$ or against a primed space number $h'_\eta$.

**One derivative, and it is the material one.** The two halves of a coefficient are not two derivatives. The gradient is four terms, one per material parameter, and it is written down once, in §*The Gradient*:

$$
\tilde\nabla_\Phi=-i\,e_t\frac{\partial}{\partial r'_t}+\sum_{\eta\in\{x,y,z\}}\vec e_\eta\frac{\partial}{\partial r_\eta}.
$$

A derivative with respect to a variable that is not a coordinate is written the same way, its variable named in full: the Lagrangian derivative puts the function in the numerator, $\partial L/\partial u$, so that where a PDE text writes $L_u$ and $L_p$ the corpus writes $\partial L/\partial u$ and $\partial L/\partial p$; the second derivative has the same shape, $\partial^2 L/\partial u^2$. The function is named in the numerator whenever it is a letter of its own, as for a Lagrangian, a Hamiltonian or a generating function; the slashed form $\partial/\partial u$ is kept where the symbol is an operator or where the operand is a compound expression rather than a single letter. The time derivative is the material one, $\partial/\partial r'_t$, and it is the imaginary-time derivative because the coefficient of the fourth slot of the gradient is $-i$. The rule holds on every object of the series, whether the letter names an element of the algebra, an element-valued field, a kernel or an operator.

**These studies do not use the covariant index conventions, and they print no contravariant index at all: a raised index is not allowed anywhere in the series, because the one metric is the identity. Subscripts are not coordinate indices or derivatives, partial derivatives are written with explicit operators, and structural information is carried by the algebra of the objects themselves.** A caret marks a power or a name, never a frame slot: $e^\lambda$, $2^k$ and $(-1)^k$ are powers, and $\mathrm{Cl}^i$, $K^0$, $M_4^\sigma$ and $\mathbb{B}^\sigma$ are names; a coordinate, a field component, a basis vector, a frame basis operator and a sign symbol are written with a low index — $x_\mu$, $A_\mu$, $\vec e_i$, $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$, $\varepsilon_{ij\eta}$ — and a contraction is written as an explicit sum that names the summed index and the set it runs over — $\sum_{\eta\in\{x,y,z\}}\vec e_\eta\partial/\partial r_\eta$, $\sum_{\eta\in\{x,y,z\}}\vec e_\eta A_\eta$, $\sum_{i,j\in\{x,y,z\}}\varepsilon_{ij\eta}A_iB_j$ — never as a repeated index left to the summation convention. No index is summed by convention: an index that appears twice is summed only when a $\sum$ names it, and the shorthand with no sum is not used. A spatial matrix written with a raised index, whether a Pauli matrix or a stress component, is the same error as a raised coordinate: it hides which basis is contracted, and the index goes low.

### The Derivative Marks

**No dot.** No derivative is written with a dot. The total derivative with respect to a parameter is written with a fraction and the parameter named: $\frac{d}{dt'}$ for the clock of the material coordinate, $\frac{d}{dh_t}$ for informational time, $\frac{d}{d\tau}$ for proper time, $\frac{d}{dt'_{\mathrm{ret}}}$ for the retarded clock; inline, the same derivative is written $d\xi/dt'$. A derivative against the material coordinate itself keeps its $c$ and is written $c\,d\xi/dr'_t$, since $r'_t=c\,t'$; a bare $d\xi/dr'_t$ that is meant as a rate has set $c=1$. The partial derivative is written $\frac{\partial}{\partial r'_t}$ or, inline, $\partial/\partial r'_t$. A higher derivative is written $\frac{d^2}{d{r'_{t}}^2}$, $\frac{\partial^2}{\partial {r'_{t}}^2}$. The derivative binds to its whole argument, so a power is written outside a bracket, $\left(\frac{d\xi}{dr'_t}\right)^2$, never as $\frac{d\xi^2}{dr'_t}$.

**The prime marks the imaginary part, and nothing else.** The prime belongs to a coefficient: it marks the imaginary part of a complex number, $r'_\mu$ of $R_\mu = r_\mu + ir'_\mu$, the part that carries the $i$. It is not a derivative mark, and it is not a label of an element, a field or a coupling. A derivative is written with $d$ or $\partial$ and its variable named: a function of one variable is differentiated as $df/dx$, never as $f'$, and a second derivative as $d^2f/dx^2$ or $\partial^2f/\partial x^2$, never with a repeated prime or a repeated subscript. The complex time is $Q_t = q_t+i q'_t$: its real part $q_t$ is the informational coordinate and its imaginary part $q'_{t}$ the material one, with $q_t = h_t$ and $q'_t = r'_{t}$. The prime on $r'_t$ marks the coefficient that carries the $i$, exactly as the primes on $h'_{x},h'_{y},h'_{z}$ mark the imaginary spatial coefficients. Carried by an element glyph, the same prime names the element assembled from the primed coefficients, $\tilde q' = q'_t\,e_t+q'_x\vec e_x+q'_y\vec e_y+q'_z\vec e_z$ in $\tilde Q = \tilde q+i\tilde q'$, the antiquaternion part; it is the coefficient prime read on the whole glyph, not a label of a transformed or distinguished element.

**The prime is not a frame, source or field label.** The primed spatial coordinates $h'_{x},h'_{y},h'_{z}$ are the imaginary parts of the spatial coefficients, $R_x=r_x+i h'_{x}$, $R_y=r_y+i h'_{y}$, $R_z=r_z+i h'_{z}$; the prime names the coordinate that carries the $i$. The primed time $r'_t$ is the imaginary part of $R_t=h_t+i r'_t$, and the unprimed $h_t$ its real part; both halves are lengths, the primed temporal coordinate as much as the unprimed one. Outside these uses the prime is not written. A transformed frame is named by a subscript, never by $h'_{x}$ or $r'_t$; a source point, a second point and an integration variable take a numeric or role subscript, never a prime; an element, field, connection, curvature, current, state, coupling, group or map that is transformed or distinguished takes a numeric or role subscript, never a prime; and a derivative is written $df/dx$, never $f'$. The glyph $h'_{x}$ cannot be both the imaginary coordinate and a source or boosted coordinate: where both are needed, the source point or the frame takes the subscript.

**Labels that are not derivatives.** The second Lorentz label is written $\bar l$, and a spinor index of the conjugate representation is written $\bar\alpha$; the bar on an index marks the conjugate spinor. The conjugate matrix is $\bar\Pi$. These are labels, not derivatives.

**The scope mark.** In geometric calculus the factor differentiated is marked with an underline, $\underline{\partial}(AB)=\underline{\partial}A\,B+\underline{A}\,\underline{\partial}B$, not with a dot.

**The two derivative operators of the series** are the **biquaternionic gradient** $\tilde\nabla_\Phi$ and the **d'Alembertian** $\Box_\Phi$; every other partial derivative is written with $\partial$.

### The Gradient

**One operator of each order, and every glyph of them carries $\Phi$.** The calculus of this series has a first-order derivative and a second-order one, and both carry the subscript $\Phi$: the **biquaternionic gradient** $\tilde\nabla_\Phi$ and the **d'Alembertian** $\Box_\Phi$, with the **spatial gradient** $\vec\nabla_\Phi$ and the **Laplacian** $\Delta_\Phi$ as the parts they carry. The rule holds in every article of the physics catalogue and in every article of the mathematics catalogue: no gradient, no Laplacian and no d'Alembertian is written without that subscript, and a derivative glyph standing alone does not occur. A derivative mark met in a derivation that lacks the subscript belongs to another subject and not to this series.

**The element, written once.** The coordinate biquaternion is

$$
\tilde R=\sum_{\mu\in\{t,x,y,z\}}R_\mu e_\mu,\qquad R_\mu=r_\mu+i r'_\mu,
$$

four complex coefficients on the four units and eight real parameters. The capital is written here and in the table of §*Index and Notation Conventions*, and nowhere in the calculus: every derivative below is written against a lowercase parameter.

**The derivatives are operators on the material parameters, and on nothing else.** Four of the eight real parameters are differentiated in this series: the imaginary time $r'_t$ and the three real space numbers $r_\eta$. They are the material ones, and $\Phi$ is their name. The other four, the real time $h_t$ and the three imaginary space numbers $h'_\eta$, are never written under a $\partial$: they are read on elements, and no article of the series differentiates against them. So a derivative has one of two shapes, $\partial/\partial r'_t$ or $\partial/\partial r_\eta$, and no derivative of the corpus is written against $R_\mu$, against $\bar R_\mu$ or against any other parameter.

**The gradient.** The first-order operator is the sum of the four unit-weighted derivatives on the four material parameters,

$$
\tilde\nabla_\Phi=-i\,e_t\frac{\partial}{\partial r'_t}+\sum_{\eta\in\{x,y,z\}}\vec e_\eta\frac{\partial}{\partial r_\eta},
$$

whose tilde marks its scalar part beside its vector part, with its **quaternion conjugate**, the involution of the norm,

$$
(\tilde\nabla_\Phi)^{\natural}=-i\,e_t\frac{\partial}{\partial r'_t}-\sum_{\eta\in\{x,y,z\}}\vec e_\eta\frac{\partial}{\partial r_\eta}.
$$

The coefficient of the fourth slot is $-i$ and the coefficient of each space slot is $1$; the vector part of the glyph is the three space slots together, which is why the glyph carries the tilde and not the arrow. It is this conjugate, and no other, that the series composes with (*Biquaternion Analysis*, §*The Biquaternionic Gradient*, §*The Quaternion Conjugate of the Gradient*).

**The spatial gradient and the Laplacian.** The three space slots are the pure spatial gradient, whose divergence $\vec\nabla_\Phi\cdot\vec Q_{\mathrm f}$ and curl $\vec\nabla_\Phi\times\vec Q_{\mathrm f}$ are the ordinary ones of the vector part, and its second-order companion is the Laplacian of the corpus:

$$
\vec\nabla_\Phi=\sum_{\eta\in\{x,y,z\}}\vec e_\eta\frac{\partial}{\partial r_\eta},
\qquad
\Delta_\Phi=\sum_{\eta\in\{x,y,z\}}\frac{\partial^2}{\partial r_\eta^2}.
$$

**The two products of the spatial gradient.** Read with the dot, the spatial gradient composed with itself returns the Laplacian, and read with the circle it returns minus the Laplacian, the sign carried by $e_t$, the identity of the algebra:

$$
\vec\nabla_\Phi\cdot\vec\nabla_\Phi=\Delta_\Phi,
\qquad
\vec\nabla_\Phi\circ\vec\nabla_\Phi=-e_t\,\Delta_\Phi .
$$

The dot reads the three spatial units as an orthonormal frame, where each unit pairs with itself to $1$; the circle reads them as elements of the algebra, where each squares to $-e_t$. The sign belongs to the reading and the operator is one. Where an article writes the second line as $-\Delta_\Phi$, the temporal unit is understood on both sides.

**The d'Alembertian.** The second-order operator is the norm of the gradient. Write $T=-i\,e_t\partial/\partial r'_t$ and $S=\sum_{\eta\in\{x,y,z\}}\vec e_\eta\partial/\partial r_\eta$ for the two halves of the sum. They commute, $T^{2}=(-i)^2\partial^2/\partial {r'_t}^2=-\partial^2/\partial {r'_t}^2$ and $S^{2}=-\Delta_\Phi$, so

$$
\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=(T+S)(T-S)=T^{2}-S^{2}=-\frac{\partial^{2}}{\partial {r'_{t}}^{2}}+\Delta_\Phi=\Box_\Phi=\Delta_\Phi-\frac{\partial^{2}}{\partial {r'_{t}}^2},
$$

the square of the temporal half entering with the minus and the squares of the three spatial ones with the plus. That sign is the sign pattern read on the two halves instead of on the four second derivatives: $(-,+,+,+)$ on the material parameters, which is the signature the series works in throughout.

**The operator at work.** Because it is scalar, the d'Alembertian passes through the units and differentiates the coefficients, and written on an element it is

$$
\Box_\Phi\tilde\Xi=\left(\Delta_\Phi-\frac{\partial^{2}}{\partial {r'_{t}}^{2}}\right)\tilde\Xi
=\sum_{\eta\in\{x,y,z\}}\frac{\partial^{2}\tilde\Xi}{\partial r_\eta^{2}}-\frac{\partial^{2}\tilde\Xi}{\partial {r'_{t}}^{2}}.
$$

The two equations the corpus writes with it are the harmonic one and the massive one,

$$
\Box_\Phi\tilde\Xi=0,
\qquad
\left(\Box_\Phi-k_m^{2}\right)\tilde\Xi=0,
$$

the first on a regular field, which is the harmonic equation of the corpus (*The Derivative, the Field and the Transform*), the second with the mass as a central shift (§*The Two First-Order Equations and Their Symbol*). Two limiting readings of the same display follow, and both are used. A field that does not depend on $r'_t$ loses the temporal term and the d'Alembertian is the Laplacian,

$$
\Box_\Phi\tilde\Xi=\Delta_\Phi\tilde\Xi,
$$

the wave equation passing to the Laplace equation of a static field. A field that does not depend on the three space parameters loses the Laplacian instead and keeps one term, $-\partial^2\tilde\Xi/\partial {r'_{t}}^2$.

**Why the subscript stands on every glyph.** The derivative is written on the material parameters and on no others, and $\Phi$ is their name: the glyph carries the name of the four parameters it differentiates. An article that writes the informational part writes an element, and no derivative of the corpus is taken against it.

**The conjugates of the gradient.** The marks are read on the invertibles at fixed parameter: the derivative symbols are held fixed and only the units are conjugated. This fixes the scope of the star, and it is not a claim that $\partial/\partial r'_t$ is real. Read on the units, the quaternion conjugation reverses the three spatial units and fixes the temporal one, and the Hermitian conjugation does the same, so the two marks agree on the gradient term by term:

$$
\tilde\nabla_\Phi^{*}=(\tilde\nabla_\Phi)^{\natural}.
$$

**The sum is written, and the sum carries its scope.** The gradient is a sum, and the sum is always spelled out. The shorthand $\vec e_\eta\partial/\partial r_\eta$ is not used, because it repeats the index without summing it; the same holds for every contraction of a basis vector, a gamma or a field component with a derivative. The index is named under the $\sum$, and so is the set it runs over: the space index runs over the three space letters, $\sum_{\eta\in\{x,y,z\}}$, and the coordinate index over the four, $\sum_{\mu\in\{t,x,y,z\}}$. A glyph such as $\sum_\eta$ is not written, because the reader would have to supply the range.

**What the material reading gives.** The time derivative is imaginary, $\partial/\partial r'_t$ in the coefficient $-i$, the three space derivatives are the physical ones, the spatial gradient is the physical $\vec\nabla_\Phi=\sum_{\eta\in\{x,y,z\}}\vec e_\eta\,\partial/\partial r_\eta$, its divergence and its curl are the ordinary divergence $\vec\nabla_\Phi\cdot\vec Q_{\mathrm f}$ and curl $\vec\nabla_\Phi\times\vec Q_{\mathrm f}$ of the field, and the Laplacian is the physical $\Delta_\Phi=\sum_{\eta\in\{x,y,z\}}\partial^2/\partial r_\eta^2$. So a real field has a purely imaginary time derivative and real space derivatives, and that one fact is what turns the gradient into the Maxwell pair and the chiral pair below.

**A continuation is a change of coordinate, not of operator.** The Wick rotation $r'_t\mapsto-i\tau$ reads the material clock in another chart, and the four terms of $\tilde\nabla_\Phi$ are untouched, each being the derivative in its own parameter; only the sign of $\partial^2/\partial {r'_t}^2$ in $\Box_\Phi$ moves. The operator keeps its subscript $\Phi$ in both charts, and the article that continues the coordinates says which chart it reads them in rather than marking the operator.

The operators, in one table:

| symbol | definition | the parameters it differentiates |
| --- | --- | --- |
| $\tilde R$ | $\sum_{\mu\in\{t,x,y,z\}}R_\mu e_\mu$ with $R_\mu=r_\mu+i r'_\mu$ | the element; the capital is written here and nowhere in the calculus |
| $\tilde\nabla_\Phi$ | $-i\,e_t\partial_{r'_t}+\sum_{\eta\in\{x,y,z\}}\vec e_\eta\partial_{r_\eta}$ | $r'_t,\ r_x,\ r_y,\ r_z$ |
| $(\tilde\nabla_\Phi)^{\natural}$ | $-i\,e_t\partial_{r'_t}-\sum_{\eta\in\{x,y,z\}}\vec e_\eta\partial_{r_\eta}$ | $r'_t,\ r_x,\ r_y,\ r_z$ |
| $\vec\nabla_\Phi$ | $\sum_{\eta\in\{x,y,z\}}\vec e_\eta\partial_{r_\eta}$ | $r_x,\ r_y,\ r_z$ |
| $\Delta_\Phi$ | $\sum_{\eta\in\{x,y,z\}}\partial^2_{r_\eta}$ | $r_x,\ r_y,\ r_z$ |
| $\Box_\Phi$ | $\Delta_\Phi-\partial^2_{r'_t}$ | $r'_t,\ r_x,\ r_y,\ r_z$ |

### The Plain Bilinear Product, Its Form and Its Norm

**The product.** The general plain bilinear product is one of the four of *Product and Form Conventions*, §*The Twelve Products and Their Names*. On the gradient, with an element-valued field $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$, it is read with $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and $\vec e_j \vec e_\eta=-\delta_{j\eta}e_t+\epsilon_{j\eta l}\vec e_l$, so that the three spatial units carry the field back onto the scalar unit.


A **product** is algebra-valued, and this one holds the divergence, the gradient and the curl of the field in a single object; for the field strength $\tilde F$ the equation $\tilde\nabla_\Phi\tilde F=-\sqrt{\mu}\,\tilde J_{\Phi}$, with $\tilde J_{\Phi}=ic\rho\,e_t+\vec J$, is the series' Maxwell equation. **Read on the material parameters**, $\vec\nabla_\Phi$ is the physical spatial gradient, so the space part is the ordinary one and the time part carries the factor $-i$:

$$
\tilde\nabla_\Phi\tilde Q_{\mathrm f}=\Bigl(-i\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}-\vec\nabla_\Phi\cdot\vec Q_{\mathrm f}\Bigr)e_t-i\frac{\partial\vec Q_{\mathrm f}}{\partial r'_t}+\vec\nabla_\Phi Q_{\mathrm{f}t}+\vec\nabla_\Phi\times\vec Q_{\mathrm f} .
$$

The display is the general product with the material coefficients substituted: the divergence and the curl appear with their own sign on $\mathbb{B}_{\Phi}$, because the three spatial derivatives there are the physical ones. Nothing is redefined and no second product is introduced: a reader who substitutes the coefficients into the general display above obtains the line, and a reader who does not substitute keeps the general display, which is the operator's own form and the one the definition fixes.

**The symmetric and antisymmetric parts.** Read with two arguments, the product splits as in *Product and Form Conventions*, §*The Twelve Products and Their Names*. The half-sum keeps the form as its scalar part,

$$
\tilde\nabla_\Phi\bullet\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla_\Phi\tilde Q_{\mathrm f}+\tilde Q_{\mathrm f}\tilde\nabla_\Phi\bigr)=\Bigl[-i\frac{\partial}{\partial r'_t}Q_{\mathrm{f}t}-(\vec\nabla_\Phi,\vec Q_{\mathrm f})\Bigr]e_t-i\frac{\partial}{\partial r'_t}\vec Q_{\mathrm f}+Q_{\mathrm{f}t}\vec\nabla_\Phi=\Bigl[-i\frac{\partial}{\partial r'_t}Q_{\mathrm{f}t}-\vec\nabla_\Phi\cdot\vec Q_{\mathrm f}\Bigr]e_t-i\frac{\partial}{\partial r'_t}\vec Q_{\mathrm f}+\vec\nabla_\Phi Q_{\mathrm{f}t},
$$


and the half-difference is the curl,

$$
\tilde\nabla_\Phi\wedge\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla_\Phi\tilde Q_{\mathrm f}-\tilde Q_{\mathrm f}\tilde\nabla_\Phi\bigr)=\tfrac12\bigl(\vec\nabla_\Phi\times\vec Q_{\mathrm f}+\vec\nabla_\Phi\times\vec Q_{\mathrm f}\bigr)=\vec\nabla_\Phi\times\vec Q_{\mathrm f} ,
$$

a pure vector, so the plain form carries the whole scalar content of the product. Throughout these four subsections the pair $(\vec\nabla_\Phi,\vec X)$ is read as the divergence $\vec\nabla_\Phi\cdot\vec X$ and $X\vec\nabla_\Phi$ as the gradient $\vec\nabla_\Phi X$, the derivative acting on the coefficient it multiplies, and the coordinate formulas substituted are those of *Product and Form Conventions*, §*The Twelve Products and Their Names*.

**The form.** The **plain form** is the scalar part of the product read in two arguments,

$$
\langle\tilde\nabla_\Phi,\tilde Q_{\mathrm f}\rangle=\mathrm{Sc}(\tilde\nabla_\Phi\tilde Q_{\mathrm f})=-i\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}-\vec\nabla_\Phi\cdot\vec Q_{\mathrm f}
$$

a scalar, the **contraction** of the derivative with the field in the sign vector $\varepsilon$. **On the gradient** it is $-i\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}-\vec\nabla_\Phi\cdot\vec Q_{\mathrm f}$, the time slot imaginary and the divergence real. 

The plain form is the **contraction** in the sense of §*A contraction is a form, never an index*: the derivative meets the field component of its own name, the time with the time and each space with its space, and the sign it carries is $\varepsilon_\mu$, which is why the time term enters with a plus and the three space terms with a minus. The sign vector is also the sign pattern, because the three space coefficients are real and the time coefficient imaginary.

**The norm.** The norm is defined with the form, as that form at its two equal arguments:

$$
\langle\tilde\nabla_\Phi\rangle=\langle\tilde\nabla_\Phi,\tilde\nabla_\Phi\rangle=\mathrm{Sc}(\tilde\nabla_\Phi\tilde\nabla_\Phi)=-\frac{\partial^2}{\partial {r'_{t}}^2}-\Delta_\Phi ,
$$


the cross terms cancelling. **On the gradient** it is $-\frac{\partial^2}{\partial {r'_{t}}^2}-\Delta_\Phi$, which is neither the wave operator $\partial^2/\partial {r'_{t}}^2-\Delta_\Phi$ nor the series' d'Alembertian $\Delta_\Phi-\partial^2/\partial {r'_{t}}^2$: it differs from the d'Alembertian by one overall sign (§*The Quaternionic Bilinear Product, Its Form and Its Norm*). 

### The Quaternionic Bilinear Product, Its Form and Its Norm

**The product.** The general quaternionic bilinear product is the second of the four of *Product and Form Conventions*, §*The Twelve Products and Their Names*; on the gradient it is $(\tilde\nabla_\Phi)^{\natural}\tilde Q_{\mathrm f}$, the conjugate derivative, read with the same rules, the three spatial units now carrying the field back onto the scalar unit with the opposite sign,

$$
(\tilde\nabla_\Phi)^{\natural}\tilde Q_{\mathrm f}=\Bigl(-i\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}+\vec\nabla_\Phi\cdot\vec Q_{\mathrm f}\Bigr)e_t-i\frac{\partial\vec Q_{\mathrm f}}{\partial r'_t}-\vec\nabla_\Phi Q_{\mathrm{f}t}-\vec\nabla_\Phi\times\vec Q_{\mathrm f} .
$$

**The symmetric and antisymmetric parts.** The half-sum is central and is the quaternionic form itself,

$$
\tilde\nabla_\Phi\bullet_{\natural}\tilde Q_{\mathrm f}=\tfrac12\bigl((\tilde\nabla_\Phi)^{\natural}\tilde Q_{\mathrm f}+\tilde Q_{\mathrm f}^{\natural}\tilde\nabla_\Phi\bigr)=\Bigl(-i\frac{\partial}{\partial r'_t}Q_{\mathrm{f}t}+\vec\nabla_\Phi\cdot\vec Q_{\mathrm f}\Bigr)e_t
$$

and the half-difference is the vector part of the product,

$$
\tilde\nabla_\Phi\wedge_{\natural}\tilde Q_{\mathrm f}=\tfrac12\bigl((\tilde\nabla_\Phi)^{\natural}\tilde Q_{\mathrm f}-\tilde Q_{\mathrm f}^{\natural}\tilde\nabla_\Phi\bigr)=-i\frac{\partial}{\partial r'_t}\vec Q_{\mathrm f}-\vec\nabla_\Phi Q_{\mathrm{f}t}-\vec\nabla_\Phi\times\vec Q_{\mathrm f}
$$

**The form.** The **quaternionic form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla_\Phi,\tilde Q_{\mathrm f}\rangle_{\natural}=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde Q_{\mathrm f})=-i\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}+\vec\nabla_\Phi\cdot\vec Q_{\mathrm f} ,
$$


a scalar, the **contraction** of the derivative with the field, all four signs plus because the conjugate derivative already carries $\varepsilon$; it differs from the plain form by the three signs of $\varepsilon$, which are **computed from the product** $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and not assumed. **On the gradient** it is $-i\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}+\vec\nabla_\Phi\cdot\vec Q_{\mathrm f}$, the divergence entering with a plus where the plain form carries a minus.

**The norm, and the definition of the d'Alembertian.** The norm is defined with the form, as that form at its two equal arguments, and the two orders of the product agree:

$$
\Box_\Phi=\langle\tilde\nabla_\Phi\rangle_{\natural}=\langle\tilde\nabla_\Phi,\tilde\nabla_\Phi\rangle_{\natural}
=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi)=\mathrm{Sc}(\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural})
=-\frac{\partial^{2}}{\partial {r'_{t}}^{2}}+\Delta_\Phi .
$$

**This is the definition of the d'Alembertian**: the quaternionic norm of the gradient, one operator and one only (*The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*). It carries the subscript $\Phi$ like every derivative of the corpus, and it is **scalar**: it multiplies by $e_t$ and acts coefficient by coefficient, $\Box_\Phi\tilde Q_{\mathrm f}=\sum_{\mu\in\{t,x,y,z\}}(\Box_\Phi Q_{\mathrm{f}\mu})e_\mu$. The last equality is the material substitution and nothing more, **no article of the series defines a second d'Alembertian**, and no mass-term sign is left to a local convention.

**There is no second reading.** The operator is $\Box_\Phi=\Delta_\Phi-\partial^2/\partial {r'_t}^2$ everywhere in the corpus: the temporal coefficient of the gradient is $-i$, so the fourth second derivative enters with a minus and the three space ones with a plus. The sign is the algebra's, not a slice's, and no article chooses between two conventions of the operator. The reading is the one used by the Klein–Gordon article, the Dirac article and the dedicated article *The Biquaternion D'Alembertian and Its Green's Functions*.

### The Laplacian Is the Only Delta

**One letter, one operator, one subscript.** $\Delta_\Phi$ is the spatial Laplacian and nothing else: $\Delta_\Phi=\sum_{\eta\in\{x,y,z\}}\partial^2/\partial r_\eta^2$, on the three material space parameters. It is written with its subscript wherever it appears, and there is no other Laplacian in the catalogue: no chart Laplacian, no subspace Laplacian and no unmarked Laplacian in a derivative sense. The mathematics catalogue uses the same capital for the Hodge Laplacian of a complex and for the exterior-algebra differential, objects of its own, and the physics catalogue uses none of them. **No other operator of the physics catalogue wears the letter.** A symbol that has two readings has no reading, because the eye cannot separate an operator from an increment, and the subscript $\Phi$ is what separates them.

**A bare capital is an increment, and the operator never goes bare.** A difference of two values of a variable is written with the capital and the variable it belongs to, $\Delta t$, $\Delta r'_t$, $\Delta k$, $\Delta S$: it carries no subscript, so it cannot be read as $\Delta_\Phi$. A variation of a field, of an action or of a trajectory carries the stroke, $\delta\xi$, $\delta u$, $\delta S$, as do the Dirac delta $\delta^{(4)}$ and the Kronecker $\delta_{ij}$. The operator carries $\Phi$ and only $\Phi$, and the subscript is the whole of the difference between an operator and a difference of two values.

**A named object takes a calligraphic letter and a subscript that spells it.** $\mathcal{W}_{\mathrm{dim}}$ for a conformal weight, $\mathcal{S}_{\mathrm{rep}}$ for the spinor module, $\mathcal{G}_{\mathrm{gap}}$ for a gap, a detuning or a pairing term, $\mathcal{E}_{\mathrm{shift}}$ for a level shift, $\mathcal{J}_{\mathrm{FP}}$ for a Faddeev–Popov determinant or a Jacobian, $\mathcal{M}_{\mathrm{mod}}$ for the Tomita modular operator, $\mathcal{P}_{\mathrm{PJ}}$ for a Pauli–Jordan function, $\mathcal{V}_{\mathrm{var}}$ for a variance, $\mathcal{T}_{\mathrm{tune}}$ for a tuning fraction, $\mathcal{K}_{\mathrm{con}}$ for a constraint matrix, $\mathcal{D}_{\mathrm{disc}}$ for a discriminant, $\mathcal{L}_{\mathrm{sep}}$ for a separation, $\mathcal{A}_{\mathrm{adv}}$ for an advance per revolution, $\mathcal{P}_{\mathrm{jet}}$ for a jet fraction, $\mathcal{B}_{\mathrm{dec}}$ for the decuplet baryon, $\mathcal{N}_{\mathrm{NP}}$ for the Newman–Penrose directional derivative.

**A subscript never redeems the letter.** A Laplacian does not become a modular operator, a gauge determinant or a Newman–Penrose derivative by acquiring a subscript. A name that needs one takes a calligraphic letter, so the operator and the object stay in different alphabets and no glyph has to be disambiguated by its context. The one subscript the letter carries is $\Phi$, and it names the coordinates the derivatives are taken in, never a chart or a subspace.

### The Hermitian Product, Its Form and Its Norm

**The product.** The general plain sesquilinear product is the third of the four of *Product and Form Conventions*, §*The Twelve Products and Their Names*; it is the plain product applied to the **conjugated** field $\tilde Q_{\mathrm f}^{*}=\bar Q_{\mathrm{f}t}e_t-\overline{\vec Q_{\mathrm f}}$, so that on the gradient it is $\tilde\nabla_\Phi\tilde Q_{\mathrm f}^{*}$, conjugate-linear in the field while the first slot stays $\mathbb{C}$-linear,

$$
\tilde\nabla_\Phi\tilde Q_{\mathrm f}^{*}=\Bigl(-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}+\vec\nabla_\Phi\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t+i\frac{\partial\overline{\vec Q_{\mathrm f}}}{\partial r'_t}+\vec\nabla_\Phi\bar Q_{\mathrm{f}t}-\vec\nabla_\Phi\times\overline{\vec Q_{\mathrm f}} .
$$

Two signs have moved relative to the plain product, and both for one reason: the conjugation reversed the sign of the vector part of the field before any derivative met it, so the vector term of the scalar slot carries a plus, and the time derivative of the vector slot carries a plus as well. The display is what makes the Hermitian product usable, because its scalar slot is the one that survives the conjugate transpose: the material reading carries an imaginary time derivative and a real divergence.

**The symmetric and antisymmetric parts.** Under the conjugate transpose the half-sum is central and is the Hermitian form itself,

$$
\tilde\nabla_\Phi\bullet_{*}\tilde Q_{\mathrm f}=\mathrm{Sc}(\tilde\nabla_\Phi\tilde Q_{\mathrm f}^{*})\,e_t=\Bigl(-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}+\vec\nabla_\Phi\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t
$$

and the half-difference is the vector part,

$$
\tilde\nabla_\Phi\wedge_{*}\tilde Q_{\mathrm f}=\mathrm{Vect}(\tilde\nabla_\Phi\tilde Q_{\mathrm f}^{*})=i\frac{\partial\overline{\vec Q_{\mathrm f}}}{\partial r'_t}+\vec\nabla_\Phi\bar Q_{\mathrm{f}t}-\vec\nabla_\Phi\times\overline{\vec Q_{\mathrm f}}
$$

**The form.** The **Hermitian form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla_\Phi,\tilde Q_{\mathrm f}\rangle_{*}=\mathrm{Sc}(\tilde\nabla_\Phi\tilde Q_{\mathrm f}^{*})=-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}+\vec\nabla_\Phi\cdot\overline{\vec Q_{\mathrm f}}
$$

a scalar, the **contraction** of the derivative with the **conjugated** field, all four signs plus because the conjugation and the derivative together supply the sign vector. Taken on the scalar field it gives the **kinetic density**, the scalar part of the product of the two conjugated gradients,

$$
\mathrm{Sc}\bigl[((\tilde\nabla_\Phi)^{\natural}\tilde\Phi^{*})(\tilde\nabla_\Phi\tilde\Phi)\bigr]=-\frac{\partial\Phi^{*}}{\partial r'_t}\frac{\partial\Phi}{\partial r'_t}+\sum_{\eta\in\{x,y,z\}}\frac{\partial\Phi^{*}}{\partial r_\eta}\frac{\partial\Phi}{\partial r_\eta}
$$

in which the conjugate stands on the first factor and no absolute value is taken; the two time derivatives are imaginary on the material part, so that scalar part is $-\lvert\partial\xi_{\mathrm{scl}}/\partial r'_t\rvert^2+\lvert\vec\nabla_\Phi\xi_{\mathrm{scl}}\rvert^2$, and the kinetic term the series writes is

$$
\mathcal L_{\mathrm{kin}}=-\mathrm{Sc}\bigl[((\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}^{*})(\tilde\nabla_\Phi\tilde{Ξ})\bigr]=\Bigl|\frac{\partial\xi_{\mathrm{scl}}}{\partial r'_t}\Bigr|^2-\lvert\vec\nabla_\Phi\xi_{\mathrm{scl}}\rvert^2 ,
$$

the kinetic density of the Klein–Gordon article (*Hamiltonian Field Theory in Biquaternionic Form*). **On the gradient** the form itself is $-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}+\vec\nabla_\Phi\cdot\overline{\vec Q_{\mathrm f}}$, a real divergence beside an imaginary time derivative. The Hermitian form and the plain form agree on $\mathbb{B}_{\Phi}$ up to the sign of the divergence, which is the sign that separates the two products.

**The norm.** The norm is defined with the form, as that form at its two equal arguments. By §*The Gradient*, $\tilde\nabla_\Phi^{*}=(\tilde\nabla_\Phi)^{\natural}$, and


so the Hermitian norm of the gradient is the d'Alembertian, the same operator as its quaternionic bilinear norm. The **Hermitian form is the one positive-definite form of the four**, $\langle\tilde Q\rangle_{*}=\sum_{\mu\in\{t,x,y,z\}}\lvert Q_\mu\rvert^2$ on the elements, and its square root is the topological norm $\lVert\tilde Q\rVert$; positivity is a property of the elements, the norm of this subsection being the operator $\Box_\Phi$. **On the gradient** it is the same operator, $\Box_\Phi=\Delta_\Phi-\partial^2/\partial {r'_{t}}^2$, with the spatial Laplacian positive and the time term negative. Positivity is untouched by the sign pattern: the form is positive on the elements, and what changes is the operator's own sign and not the form's.

### The Krein Product, Its Form and Its Norm

**The product.** The general quaternionic sesquilinear product is the fourth of the four of *Product and Form Conventions*, §*The Twelve Products and Their Names*; it is the conjugate derivative applied to the conjugated field, $(\tilde\nabla_\Phi)^{\natural}\tilde Q_{\mathrm f}^{*}$, the companion of the quaternionic bilinear product in the second slot,

$$
(\tilde\nabla_\Phi)^{\natural}\tilde Q_{\mathrm f}^{*}=\Bigl(-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}-\vec\nabla_\Phi\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t+i\frac{\partial\overline{\vec Q_{\mathrm f}}}{\partial r'_t}-\vec\nabla_\Phi\bar Q_{\mathrm{f}t}+\vec\nabla_\Phi\times\overline{\vec Q_{\mathrm f}} ,
$$

with the divergence and the gradient carrying a minus where the Hermitian product carries a plus, the signs of the three space terms turning over once more, since the conjugate already carries $\varepsilon$ and the coefficient carries $-i$. The pair is the exact companion of the quaternionic pair of §*The Quaternionic Bilinear Product, Its Form and Its Norm*: the two bilinear products have companions with the conjugated field, the four lines are the four products on the two slices, and no line requires a convention beyond the four factors of §*The Gradient*.

**The symmetric and antisymmetric parts.** Under the conjugate transpose the half-sum is


whose scalar part is the Krein form, and the half-difference is the curl of the conjugated field,

$$
\tilde\nabla_\Phi\wedge_{\natural*}\tilde Q_{\mathrm f}=\tfrac12\bigl((\tilde\nabla_\Phi)^{\natural}\tilde Q_{\mathrm f}^{*}-\tilde Q_{\mathrm f}^{*}(\tilde\nabla_\Phi)^{\natural}\bigr)=\tfrac12\bigl(\vec\nabla_\Phi\times\overline{\vec Q_{\mathrm f}}+\vec\nabla_\Phi\times\overline{\vec Q_{\mathrm f}}\bigr)=\vec\nabla_\Phi\times\overline{\vec Q_{\mathrm f}} ,
$$

a pure vector.

**The form.** The **Krein form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla_\Phi,\tilde Q_{\mathrm f}\rangle_{\natural*}=\mathrm{Sc}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde Q_{\mathrm f}^{*}\bigr)=-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}-\vec\nabla_\Phi\cdot\overline{\vec Q_{\mathrm f}}
$$

a scalar, the **contraction** of the conjugate derivative with the conjugated field in the $i r'_t$ coordinate. **On the gradient** it is $-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}-\vec\nabla_\Phi\cdot\overline{\vec Q_{\mathrm f}}$, the divergence with a minus as in the plain form. That double application is the whole difference between the Krein form and the Hermitian form, and it is why the two coincide on the elements only once the signs are taken into account.

**The norm.** The norm is defined with the form, as that form at its two equal arguments; on the gradient, since $\tilde\nabla_\Phi^{*}=(\tilde\nabla_\Phi)^{\natural}$ (§*The Gradient*),

$$
\langle\tilde\nabla_\Phi,\tilde\nabla_\Phi\rangle_{\natural*}=\langle\tilde\nabla_\Phi\rangle_{\natural*}=\mathrm{Sc}\bigl((\tilde\nabla_\Phi)^{\natural}(\tilde\nabla_\Phi)^{\natural}\bigr)=-\frac{\partial^2}{\partial {r'_t}^2}-\Delta_\Phi
$$

so the Krein norm of the gradient **coincides with the plain bilinear norm**. It is the indefinite partner of the Hermitian form, and on the elements it is the form of inertia $(1,3)$ whose diagonal is $\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2$: Hermitian, and negative on a nonzero element, so it carries no positivity. It is the form of the indefinite theory — the Krein space — and not of the contractions of these subsections. **On the gradient** it is $-\frac{\partial^2}{\partial {r'_{t}}^2}-\Delta_\Phi$, both terms negative. The two norms agree with each other, and both differ from $\Box_\Phi$ by one overall sign, which is the sign separating the indefinite pair from the definite one.

**A contraction is a form, never an index.** The series has one metric, the unit metric $\delta_{\mu\nu}=(1,1,1,1)$, and it is the identity, so no index is raised and none is lowered: a raised index would be the same index. What the product carries is the plain weight $\varepsilon$, and the weight is not a metric. Where a text with covariant indices contracts a derivative with a field through a raised and a lowered index, the series writes the quaternionic form $\langle\tilde\nabla_\Phi,\tilde Q_{\mathrm f}\rangle_{\natural}$; where it contracts two derivatives, the series writes the quaternionic norm $\langle\tilde\nabla_\Phi\rangle_{\natural}=\Box_\Phi$; and where it moves an index through a metric, the series writes the element $\tilde Q_{\mathrm f}$ itself, the weight being the sign vector inside the product. The four-index alternating symbol is not an index carrier: it is the orientation density, written all-low, $\epsilon_{0123}=+1$, and its height carries no sign. Its rank distinguishes it from the sign vector of the same letter.

**The rule is one rule on both parts.** A contraction never raises an index and never lowers one, on $\mathbb{B}_{\Phi}$ or on $\mathbb{B}_{\Psi}$, because the metric is the identity on both and a raised index would be the same index. What changes between the slices is only the coefficient the contraction carries: on $\mathbb{B}_{\Phi}$ the time component is multiplied by $-i$ and the three space components by $1$, while on $\mathbb{B}_{\Psi}$ the time component is multiplied by $1$ and the three space components by $-i$. A reader who checks a component formula written on either slice checks those four numbers and nothing else, and the check is complete, because the weight $\varepsilon$ belongs to the product, the coefficients belong to the slice, and the two never merge into a single symbol.

### The Gauge-Covariant Gradient

A derivative that differentiates a field charged under a connection is the gradient with a connection added. It carries the gradient's letter and **a label, not a letter of its own**:

$$
\tilde\nabla_{\mathrm{gco},\Phi}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}
=e_t\Bigl(-i\frac{\partial}{\partial r'_t}+\frac{i\,ϙ}{\hbar}A_t\Bigr)+\sum_{\eta\in\{x,y,z\}}\vec e_\eta\Bigl(\frac{\partial}{\partial r_\eta}+\frac{i\,ϙ}{\hbar}A_\eta\Bigr),
$$

with $\tilde A_{\Phi}=\sum_{\mu\in\{t,x,y,z\}} A_\mu e_\mu\in\mathbb{B}_{\Phi}$ the connection and $ϙ$ the charge of the field the operator acts on. The superscript $\mathrm{gco}$ names the family once and is read on every member of it.

**The decomposition is the gradient's, slot by slot.** One coefficient per slot, one basis element, exactly as in $\tilde\nabla_\Phi=-i\,e_t\partial/\partial r'_t+\sum_{\eta\in\{x,y,z\}}\vec e_\eta\partial/\partial r_\eta$. The only change is the coefficient: the derivative of the free gradient is joined by the connection, slot for slot, and the basis is untouched. The sum is spelled out here as everywhere. The coefficient is a **central scalar** — it commutes with $e_\nu$ and with every element of $\mathbb{B}$ — and that is what lets the involution act on the basis and leave the coefficients in place:

$$
(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}=(\tilde\nabla_\Phi)^{\natural}+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}^{\natural}
=-i\,e_t\frac{\partial}{\partial r'_t}-\sum_{\eta\in\{x,y,z\}}\vec e_\eta\frac{\partial}{\partial r_\eta}+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}^{\natural}.
$$

The label is written **before** the conjugation, in the order the operator is built: the family first, the involution second. The conjugate is not a second operator; it is the same sum with $\natural$ read on the invertibles, and its coefficients are the same scalars.

**The operator is written on the material parameters.** Its four coefficients are read in the letters $r'_t$ and $r_\eta$, and $A_\mu$ stands beside each as it stands, with no derivative on it:

$$
\tilde\nabla_{\mathrm{gco},\Phi}=e_t\Bigl(-i\frac{\partial}{\partial r'_t}+\frac{i\,ϙ}{\hbar}A_t\Bigr)+\sum_{\eta\in\{x,y,z\}}\vec e_\eta\Bigl(\frac{\partial}{\partial r_\eta}+\frac{i\,ϙ}{\hbar}A_\eta\Bigr),
$$

and the connection enters with a plus on every slot.

**The connection is a value and the derivative is the factor.** The substitution of §*The Gradient* replaces the derivative term of each coefficient and leaves $A_\mu$ exactly as it stands, because $A_\mu$ is a component of a field and carries no derivative: the substitution acts on the $\partial$ and never on the $A$. That is the check to apply to any covariant formula of the series: the substitution acts on the $\partial$ and never on the $A$.

**The side.** Both members act from the left. The position of the operator names the side, as it does for every field of the series, and no glyph names it: a right action on $\tilde{Ξ}$ is the left action of $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}$ on $\tilde{Ξ}^{\natural}$, by the exchange of §*The Two Sides and the Renaming Theorem*.

**The curvature and the square.** The components do not commute, and their commutator carries no derivative:

$$
[\tilde\nabla_{\mathrm{gco},\Phi,\mu},\tilde\nabla_{\mathrm{gco},\Phi,\nu}]=\frac{i\,ϙ}{\hbar}F_{\mu\nu},
\qquad
(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}\tilde\nabla_{\mathrm{gco},\Phi}=\sum_{\mu\in\{t,x,y,z\}}\bigl(\tilde\nabla_{\mathrm{gco},\Phi,\mu}\bigr)^{2}+\frac{i\,ϙ}{\hbar}\tilde F,
$$

with $\tilde F=\mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde A_{\Phi})$ the curvature. The scalar part of the square is the covariant d'Alembertian and the vector part is the curvature; both are read in *The Covariant Derivative and Gauge Connection in Biquaternionic Form*.

**The coupling, and the letter $\kappa$.** A few articles write the same operator as $\tilde\nabla_\Phi+i\kappa\mathcal A$, with $\kappa$ the coupling and $\mathcal A$ the connection. That is one object under two spellings, $\kappa=\frac{ϙ}{\hbar}$ and $\mathcal A=\tilde A_{\Phi}$. The series writes $\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}$, so that $\kappa$ stays free for the retarded denominator $\kappa=1-\vec u_R\cdot\vec\beta$ of *Algebra and Element Conventions*, which is not a coupling.

**The letter $\kappa$ carries two meanings, separated by article, and both are scalars.** In the kinematics articles it is the retarded denominator $1-\vec u_R\cdot\vec\beta$. In the articles on the generalized Maxwell–Dirac operator it is the complex shift added to the gradient, $\tilde\nabla_\Phi+\kappa$ with $\kappa\in\mathbb{C}$, and it is written in the expression and never in the subscript of a glyph. The two uses do not meet in one computation, and an article that uses $\kappa$ says which of the two it means.

## The Two First-Order Equations and Their Symbol

**The pair operator is not allowed.** The two chiral equations are two equations, and the series writes two equations. No letter gathers them into one object on $\mathbb{B}\oplus\mathbb{B}$: no $\mathbb{D}$, no two-by-two array and no subscripted glyph. The gathered letter hides the four statements that carry the physics. Its adjoint is a single sign, so it cannot hold a derivative term that is anti-Hermitian and a mass term that is Hermitian, and $\mathbb{D}^{\dagger}=-\mathbb{D}$ covers the massless operator only. Its metric is chosen silently, diagonal on the two slots and never written. Its signs are invisible, because the square reports one scalar for the two members. And its carrier is ambiguous, eight complex dimensions or four, with no mark to say which. The two equations state all four, one after the other.

**The two equations.** The dynamics of a field of mass $m$ is

$$
\tilde\nabla_\Phi\tilde{Ξ}_{R}=k_m\,\tilde{Ξ}_{L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=k_m\,\tilde{Ξ}_{R},
$$

with $k_m=mc/\hbar$ the mass wave number, the inverse of the mass length. Every component equation of the series is a **coordinate form** of these two and not a second dynamics.

**The mass is the coupling.** Each line multiplies one chiral part and returns a multiple of the other. $k_m$ is real and central, it commutes with both gradients, and it is the only term of either line that names the other part. The massless limit is the same two lines at $k_m=0$, and each line then involves one part alone.

**Neither gradient squares to the d'Alembertian, and their composition does.** Written as a product of elements, $\tilde\nabla_\Phi^{2}$ is not $\Box_\Phi$: $e_t$ commutes with the three spatial units, so the mixed derivatives survive and the square is not scalar. Only the composition with the conjugate is scalar, $(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Box_\Phi$, and this is why the massive dynamics needs two lines and not one: one gradient on one field is first order and cannot equal a second-order operator, so no one-field first-order massive equation exists in this algebra. The free equation stays first order on one field, and the mass is what needs the second field.

**The square, line by line.** Composing each line with the conjugate of the other gives

$$
(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\tilde{Ξ}_{R}=k_m^{2}\tilde{Ξ}_{R},
\qquad
\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=k_m^{2}\tilde{Ξ}_{L},
$$

that is $(\Box_\Phi-k_m^{2})\tilde{Ξ}_{R}=0$ and $(\Box_\Phi-k_m^{2})\tilde{Ξ}_{L}=0$. Each part obeys the Klein–Gordon equation on its own, with the same second-order operator.

**The symbol.** On a plane wave the gradient acts as left multiplication by the wave element, $\tilde\nabla_\Phi\mapsto i\tilde K_{\Phi}$ with $\hbar\tilde K_{\Phi}=\tilde P_{\Phi}=i(E/c)e_t+\vec p$, so that $-\hbar^{2}\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=E^{2}/c^{2}-\lvert\vec p\rvert^{2}=-N$, the four-momentum being $p_0=E/c$. The symbol of the two equations is the two lines with each gradient read at its plane-wave value,

$$
i\tilde K_{\Phi}\,w_R=k_m\,w_L,
\qquad
i\tilde K_{\Phi}^{\natural}\,w_L=k_m\,w_R,
$$

and the two lines share one condition. Composing them returns $-\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}w=k_m^{2}w$, that is $E^{2}/c^{2}-\lvert\vec p\rvert^{2}=m^{2}c^{2}$, so the symbol is singular exactly on $N=-m^{2}c^{2}$ and nowhere else.

**The inverse is one scalar and two kernels.** With $G$ the Green's function of the d'Alembertian, $(\Box_\Phi-k_m^{2})G=\delta$, the solution of the two lines with a source is the pair of kernels

$$
S_L=i\bigl(\tilde\nabla_\Phi+k_m\bigr)G,
\qquad
S_R=i\bigl((\tilde\nabla_\Phi)^{\natural}+k_m\bigr)G,
$$

and substitution returns $i\delta$ in each line, because the cross terms cancel and $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi=\Box_\Phi$ with $k_m$ central. The inverse introduces no new object.

**Marks.** There is no glyph for the two equations and no subscript for a sector or a chart. A subscript on a kernel names the part it carries, $S_L$ and $S_R$. The gradient has one spelling with one subscript, $\tilde\nabla_\Phi$, and $\natural$ for its conjugate; there is no unsubscripted form of it, and no derivative of the corpus carries $\Psi$.

**The equations are material.** The two lines are written in the letters $r'_t$ and $r_\eta$, and the corpus writes no informational twin of them: there is no second gradient, and no derivative on $h_t$ or on $h'_\eta$ anywhere in the series. The second-order operator is the d'Alembertian of §*The Quaternionic Bilinear Product, Its Form and Its Norm*, $\Box_\Phi=\Delta_\Phi-\partial^2/\partial {r'_{t}}^2$.

## The Transposition of the Gradient

**The transposed reading.** A gradient acts on the factor written to its right, $\tilde\nabla_\Phi\tilde Q_1$. The long arrow over the glyph marks the other reading: the operator acts on the factor written to its left, and the arrow points at that factor, $\tilde Q_1\overleftarrow{\tilde\nabla_\Phi}$. The mark belongs to the operator and not to the field, and it is not the short arrow of the pure part, which sits on an element and marks its vector part alone. Read this way, the gradient has its derivative to the right of the element it differentiates,

$$
\tilde Q_1\overleftarrow{\tilde\nabla_\Phi}:=-i\frac{\partial\tilde Q_1}{\partial r'_t}\,e_t+\sum_{\eta\in\{x,y,z\}}\frac{\partial\tilde Q_1}{\partial r_\eta}\,\vec e_\eta ,
$$


the same four coefficients in the same four directions, with the unit written after each. The integration articles write this object $\vec\nabla_\Phi^{R}$ and use it wherever a derivative has to be moved off a product. It is not a second operator: it is the gradient with its two factors exchanged, and the exchange is what the identity below computes.

**The identity.** For every element-valued field $\tilde Q_1$,

$$
\boxed{\;\bigl(\tilde Q_1\overleftarrow{\tilde\nabla_\Phi}\bigr)^{\natural}=(\tilde\nabla_\Phi)^{\natural}\tilde Q_1^{\natural}\;}
\qquad\Longrightarrow\qquad
\tilde Q_1\overleftarrow{\tilde\nabla_\Phi}=\bigl((\tilde\nabla_\Phi)^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}.
$$

**The proof is one term.** The involution is $\mathbb{C}$-linear, it acts on the units at fixed parameter, and it commutes with the derivative, because a derivative holds its parameter fixed. Written out, the gradient is $-i\,e_t\,\partial/\partial r'_t+\sum_{\eta\in\{x,y,z\}}\vec e_\eta\,\partial/\partial r_\eta$, so every term is a scalar coefficient, a unit and a derivative, and the involution reads only the unit: $e_t^{\natural}=e_t$ and $\vec e_\eta^{\natural}=-\vec e_\eta$. The temporal term on the left is therefore $(\partial\tilde Q_1/\partial r'_t)^{\natural}(-i\,e_t)=-i\,e_t\,\partial\tilde Q_1^{\natural}/\partial r'_t$, which is the temporal term of $(\tilde\nabla_\Phi)^{\natural}\tilde Q_1^{\natural}$, and each space term is $(\partial\tilde Q_1/\partial r_\eta)^{\natural}(-\vec e_\eta)=-\vec e_\eta\,\partial\tilde Q_1^{\natural}/\partial r_\eta$, which is the corresponding space term. Adding the four gives the boxed line, and $\natural^{2}=\mathrm{id}$ gives the arrow back.

**What it says.** A right action is the conjugation of a left action: conjugate the field, apply the conjugate gradient from the left, conjugate the result. In the notation of §*The Two Sides and the Renaming Theorem*, $R_{\tilde\nabla_\Phi}=\natural\circ L_{(\tilde\nabla_\Phi)^{\natural}}\circ\natural$, read on a differential operator rather than on a multiplication. The statement needs no equation, no mass, no chirality and no pair of fields. It is an identity between operators, true of any $\tilde Q_1$: a solution, a non-solution, a product, a constant.

**With a connection nothing changes.** The components of $\tilde\nabla_{\mathrm{gco},\Phi}$ are central scalars, so the same term-by-term computation gives $\bigl(\tilde Q_1\overleftarrow{\tilde\nabla_{\mathrm{gco},\Phi}}\bigr)^{\natural}=(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}\tilde Q_1^{\natural}$, at the same residual, with $\natural$ again fixing the coefficients and reading the invertibles alone.

**The instance that hides the generality.** The chiral pair is the case usually quoted. From $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=k_m\tilde{Ξ}_{R}$, transposing with $\tilde Q_1=\tilde{Ξ}_{L}^{\natural}$ and using $m^{\natural}=m$,

$$
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=k_m\,\tilde{Ξ}_{R}
\qquad\Longrightarrow\qquad
\tilde{Ξ}_{L}^{\natural}\overleftarrow{\tilde\nabla_\Phi}=k_m\,\tilde{Ξ}_{R}^{\natural},
$$

one line, with the derivative now written to the right of $\tilde{Ξ}_{L}^{\natural}$ and the same mass in place. Read alone, the pair suggests that the right action is a property of the Dirac equation. It is not: the two lines hold of $\tilde\nabla_\Phi\tilde{Ξ}_{R}=k_m\tilde{Ξ}_{L}$ as well, of a massless field, and of any equation in which one field stands to the right of a derivative. The equation supplies the right-hand side; the identity does not depend on it.

**Why the superscript $R$ is nevertheless written.** The identity holds for a field, and a product of fields is a field. What it does not do is move the derivative off one factor of a product while the other stays. On $\tilde Q_1\tilde Q_2$ the Leibniz rule gives


with the unit after the bracket. It does not pass to the left of $\tilde Q_2$: that is a commutation with the units, allowed only when $\tilde Q_2$ is central. Nor is the rule $-i(\partial\tilde Q_1/\partial r'_t)e_t\tilde Q_2+\sum_{\eta\in\{x,y,z\}}(\partial\tilde Q_1/\partial r_\eta)\vec e_\eta\tilde Q_2$, which differs from the first term by the defect $-i(\partial\tilde Q_1/\partial r'_t)[\tilde Q_2,e_t]+\sum_{\eta\in\{x,y,z\}}(\partial\tilde Q_1/\partial r_\eta)[\tilde Q_2,\vec e_\eta]$. That is the case §*The Two Sides and the Renaming Theorem* excludes, and the case the integration articles meet. There the derivative is named $\vec\nabla_\Phi^{R}$ after the factor it differentiates, and the name is a position, not a second operator.

**The slots.** The transposition is the exchange of the two slots of a basis operator, read on a differential operator. In the language of *Operator Chirality on the Biquaternion Algebra*, §*Conjugation Exchanges the Sides*, the map that carries a left multiplier to a right multiplier is $\mathsf C$, the conjugation written as a congruence, $\mathsf C L(a^{\natural})\mathsf C=R(a)$, which in the axis-free frame is the switch $\mathsf D=\operatorname{diag}(1,-1,-1,-1)$ and is the $N$ of the matrix form above. A left action of the gradient and a right action of the same gradient therefore have arrays that agree up to that sign and that order, which is where the phases of the two sides come from.

**What it is not.** Not a transpose without conjugation: $\mathsf C$ is not the identity, and $\mathsf C^{\mathsf T}\mathsf C=I$ with $\det\mathsf C=-1$ make the congruence a congruence and not a similarity. Not the adjoint either: the dagger carries the integration by parts and the boundary term, while $\natural$ carries the invertibles alone at fixed coordinate; the two agree on the gradient, $\tilde\nabla_\Phi^{*}=(\tilde\nabla_\Phi)^{\natural}$, and part on a general element.

**Verified.** On random polynomial fields in the four coordinates the boxed line holds at residual $0.0$, the reconstruction from the conjugate at $0.0$, the chiral instance at $0.0$, and the product rule above at $0.0$; on $\tilde Q_1=r_x\vec e_x$ and $\tilde Q_2=\vec e_y$ the naive rule returns $-\vec e_y$ where the product rule returns $+\vec e_y$. The anti-automorphism it uses holds at residual $1.0\times10^{-15}$ over $200$ random pairs; the automorphism that would be needed if the units were not reversed fails at $2.7\times10^{1}$.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate, $Q_\mu$ or $x_\mu$. There is one metric, $\delta_{\mu\nu}=(1,1,1,1)$, and a display never names it.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}=a\tilde{Ξ}$ and $R_b\tilde{Ξ}=\tilde{Ξ} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame basis operator of the chirality $\Gamma$; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the basis operators span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a basis operator named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

An operator whose letter is the letter of an element is that element: the tilde and the arrow are read on it as on the element, and no mark says operator. The named operators are left and right multiplication, the two-sided operator and the inner derivation. The side of an action is position, $D\tilde{Ξ}$ against $\tilde{Ξ} D$; the two are exchanged by the quaternion conjugation, $(\tilde{Ξ} D)^{\natural}=D^{\natural}\tilde{Ξ}^{\natural}$, so a right action on a field is a left action on the conjugate field, and no glyph marks a side. The superscript $R$ marks the right derivative, the one case the exchange does not reach, and on the gradient even that case is a conjugation: $\tilde Q_1\overleftarrow{\tilde\nabla_\Phi}=\bigl((\tilde\nabla_\Phi)^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}$, so a right action is the left action of the conjugate gradient on the conjugate field, and the identity needs no equation. The dagger is the general adjoint of an operator and not a fifth conjugation, and it adds to the element's mark rather than replacing it. A Kraus operator is an element, not an array. The Fock operator is the one operator that is not an element, and its superscript is fixed with the other tokens.

A subscript is a component or a label, never a derivative; every partial derivative is written with $\partial$ and its variable. A caret is a power and never a label: every label, coordinate, component, basis vector, frame basis operator and sign symbol is written low, and a contraction is a form with the sign vector. Every derivative is written against a material parameter, $\partial/\partial r'_t$ or $\partial/\partial r_\eta$, with no factor of two and no dilation in front. Every derivative operator carries the subscript $\Phi$: the gradient $\tilde\nabla_\Phi$, its conjugate $(\tilde\nabla_\Phi)^{\natural}$, the spatial gradient $\vec\nabla_\Phi$, the Laplacian $\Delta_\Phi$ and the d'Alembertian $\Box_\Phi$. None of the five is ever written without it, and no glyph of the corpus names a gradient, a Laplacian or a d'Alembertian of the informational part. The gradient is $\tilde\nabla_\Phi$, not pure: by slot it splits into a Hermitian temporal term and an anti-Hermitian spatial sum. The four parameters it differentiates are the material ones, $\tilde\nabla_\Phi=-i\,e_t\partial_{r'_t}+\sum_{\eta\in\{x,y,z\}}\vec e_\eta\partial_{r_\eta}$, and the subscript is the only mark it carries. No glyph of the corpus carries a derivative on any other set of coordinates. The d'Alembertian is $\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi=\Delta_\Phi-\partial^2/\partial {r'_{t}}^2$, and every article uses this one operator with the mass equation $(\Box_\Phi-k_m^{2})\tilde{Ξ}=0$, where $k_m^{2}$ is written $k_m^{2}$ with $k_m=mc/\hbar$. The gauge-covariant gradient is the same sum with the coefficient replaced, $\tilde\nabla_{\mathrm{gco},\Phi}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}$, and it carries a label rather than a letter of its own.

The gradient and its conjugate act on two chiral parts, and the series writes the dynamics as two equations, $\tilde\nabla_\Phi\tilde{Ξ}_{R}=k_m\tilde{Ξ}_{L}$ and $(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=k_m\tilde{Ξ}_{R}$, of §*The Two First-Order Equations and Their Symbol*. The pair operator $\mathbb{D}$ is not allowed: it hides the adjoint, the metric and the signs, and its square is $\Box_\Phi$ on each part only after composing the two lines. A subscript names a part and not a slice: $\tilde\nabla_\Phi$ is the anti-Hermitian part, which keeps the imaginary time and the real space numbers (*The Gradient*).

One letter is reserved: $\Delta_\Phi$ is the spatial Laplacian in every article, the subscript is $\Phi$ and nothing else, a bare capital is a difference of two values, and a named object takes a calligraphic letter with a subscript that spells it. The rule is stated in §*The Laplacian Is the Only Delta*.

The four forms remain four distinct conventions and the norms two, because each form conjugates its own slot. The four product subsections read the same gradient through the plain, quaternionic, Hermitian and Krein products, each with its form and its norm, and the signs follow from the algebra rather than from a choice of metric.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $L_{\tilde Q}, R_{\tilde Q}$ | Left and right multiplication by the element; the glyph of the operator is the glyph of the element |
| $L_{\tilde Q_4}R_{\tilde Q_1}$ | The two-sided operator, $\tilde Q_2\mapsto\tilde Q_4\tilde Q_2\tilde Q_1$ |
| $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ | The two-sided operator, the congruence by the element |
| $\operatorname{ad}_{\tilde Q}$ | The inner derivation, $[\tilde Q,\cdot]$ |
| $^{\dagger}$ | The general adjoint of an operator; $(L_a)^{\dagger}=L_{a^{*}}$ |
| $\partial/\partial r'_t$, $\partial/\partial r_\eta$ | The two shapes a derivative takes: the material time and a material space coordinate; real parameters, so no dilation stands in front |
| $\tilde\nabla_\Phi$ | The biquaternionic gradient, $-i\,e_t\partial_{r'_t}+\sum_{\eta\in\{x,y,z\}}\vec e_\eta\partial_{r_\eta}$, four components and not pure |
| $\tfrac12\bigl(\tilde\nabla_\Phi-\tilde\nabla_\Phi^{*}\bigr)$ | The projection $X\mapsto\tfrac12(X-X^{*})$ with the star read on the units at fixed coordinate; on the gradient it gives the operator itself, $-i\,e_t\partial_{r'_t}+\sum_{\eta\in\{x,y,z\}}\vec e_\eta\partial_{r_\eta}$ on $r'_t,r_\eta$ |
| $\tilde\nabla_{\mathrm{gco},\Phi}$ | The gauge-covariant gradient, $\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_{\Phi}$; its four coefficients $-i\partial/\partial r'_t+\frac{i\,ϙ}{\hbar}A_t$ and $\partial/\partial r_\eta+\frac{i\,ϙ}{\hbar}A_\eta$, its conjugate $(\tilde\nabla_{\mathrm{gco},\Phi})^{\natural}$ |
| $\Box_\Phi$ | The d'Alembertian, $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Delta_\Phi-\partial^2/\partial {r'_t}^2$ |
| $\Delta_\Phi$ | The spatial Laplacian, $\sum_{\eta\in\{x,y,z\}}\partial^2/\partial r_\eta^2$, and nothing else; a bare $\Delta$ is an increment, and a named object takes a calligraphic letter, as in §*The Laplacian Is the Only Delta* |
| $\tilde R$ | The variable, $\sum_{\mu\in\{t,x,y,z\}} R_\mu e_\mu$ with $R_\mu=r_\mu+i r'_\mu$; the capital is written once, at the definition of the gradient, and every derivative after it is written on a lowercase parameter |
| $\tilde\nabla_{\Phi}$, $(\tilde\nabla_\Phi)^{\natural}$ | The gradient and its conjugate, $\tilde\nabla_{\Phi}=-i\,e_t\partial_{r'_t}+\sum_{\eta\in\{x,y,z\}}\vec e_\eta\partial_{r_\eta}$ and $(\tilde\nabla_\Phi)^{\natural}=-i\,e_t\partial_{r'_t}-\sum_{\eta\in\{x,y,z\}}\vec e_\eta\partial_{r_\eta}$, with the tuples $(-i,1,1,1)$ and $(-i,-1,-1,-1)$ on $r'_t$ and $r_\eta$; both anti-Hermitian |
| $\vec\nabla_{\Phi}$, $\Delta_{\Phi}$, $\Box_\Phi$ | The spatial gradient, the spatial Laplacian and the d'Alembertian, $\vec\nabla_{\Phi}=\sum_{\eta\in\{x,y,z\}}\vec e_\eta\partial_{r_\eta}$, $\Delta_\Phi=\sum_{\eta\in\{x,y,z\}}\partial^2/\partial r_\eta^2$ and $\Box_\Phi=\Delta_{\Phi}-\partial^2/\partial {r'_t}^2$ |
| $1/k_m$ | The mass length, $\hbar/(mc)$; a quotient pairing $\hbar$ with a mass, in either order, is $1/k_m$ or its reciprocal $k_m$, so the mass equation reads $(\Box_\Phi-k_m^{2})\tilde{Ξ}=0$ |
| $^{\natural}$ | The quaternion conjugation, $a^{\natural}=(a_0,-a_1,-a_2,-a_3)$; an anti-automorphism, $(ab)^{\natural}=b^{\natural}a^{\natural}$ |
| $(\tilde{Ξ} D)^{\natural}=D^{\natural}\tilde{Ξ}^{\natural}$ | The exchange of the two sides: a right action on $\tilde{Ξ}$ is a left action on $\tilde{Ξ}^{\natural}$ |
| $\vec\nabla_\Phi^{R}$ | The right gradient, $F\vec\nabla_\Phi^{R}=-i(\partial F/\partial r'_t)e_t+\sum_{\eta\in\{x,y,z\}}(\partial F/\partial r_\eta)\vec e_\eta$; used only where a derivative meets two distinct factors |
| $\overleftarrow{\ }$ | The long arrow over an operator: it acts on the factor written to its left, and the arrow points at that factor; it is not the short arrow of the pure part |
| $\tilde Q_1\overleftarrow{\tilde\nabla_\Phi}$ | The same gradient transposed, $-i(\partial\tilde Q_1/\partial r'_t)e_t+\sum_{\eta\in\{x,y,z\}}(\partial\tilde Q_1/\partial r_\eta)\vec e_\eta$; the right action, equal to $\bigl((\tilde\nabla_\Phi)^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html), for the algebra and the element glyphs.
- [Conventions of the Products and the Forms](product-and-form-conventions.html), for the four products read on the gradient.
- [Conventions of the Norms and the Pairings](norm-and-pairing-conventions.html), for the norms of those products.
- [Index and Notation Conventions](index-and-notation-conventions.html), for the Fock superscript and the subscript rules.
- [The Operators of the Algebra](the-operators-of-the-algebra.html), companion article, for the three actions and their matrices.
