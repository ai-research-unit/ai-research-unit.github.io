# __Operator and Calculus Conventions__

## Introduction

These are the conventions of the operators and of the calculus. An operator acting by multiplication is the element it multiplies by, and its glyph is the glyph of that element; the article fixes the named operators, the dagger, the Kraus operator and the Fock exception. The calculus follows: the derivative marks, the gradient and the d'Alembertian, and the four product-form-norm readings of the gradient that the field equations use.

The article assumes the base of *Algebra and Element Conventions*, the products and forms of *Product and Form Conventions*, and the norms of *Norm and Pairing Conventions*. The matrix models are in *Matrix Representations Conventions*; the superscripts on operators are in *Unit, Index and Notation Conventions*.

## The Operators

**An operator acting by multiplication is the element it multiplies by.** Every element acts on the algebra, on the left $L_{\tilde Q}$ or on the right $R_{\tilde Q}$, and an operator whose letter is the letter of an element **is** that element. The glyph of the operator is therefore the glyph of its element, and the marks are read on it as on the element: the tilde marks the quaternionic element read with its scalar part, the arrow the pure element read on its vector part alone. Neither mark says that a glyph is an operator, and no mark is added to say it.

**The named operators.** The structural operators take an upright capital letter and carry the element in the subscript, where it keeps its own mark:

| Operator | Glyph |
|---|---|
| left multiplication | $L_{\tilde Q_1}(\tilde Q_2)=\tilde Q_1\tilde Q_2$ |
| right multiplication | $R_{\tilde Q_1}(\tilde Q_2)=\tilde Q_2\tilde Q_1$ |
| two-sided | $L_{\tilde Q_4}R_{\tilde Q_1}(\tilde Q_2)=\tilde Q_4\tilde Q_2\tilde Q_1$ |
| sandwich | $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}=\operatorname{H}_{\tilde Q}$ |
| inner derivation | $\operatorname{ad}_{\tilde Q_4}(\tilde Q_1)=[\tilde Q_4,\tilde Q_1]$ |
| automorphism | $\operatorname{Ad}_{\tilde Q_4}$ |

The tilde sits in the subscript because it belongs to the element, not to the operator: $L_{\tilde Q}$ is an operator, $\tilde Q$ is the element that generates it.

**The basis operators.** The four units are written in the subscript, $L_{e_\mu}^{\mathrm{axf}}$ and $R_{e_\mu}^{\mathrm{axf}}$, and nowhere else: the short form $L_\mu$ is not used in this corpus. The right family is read from the left one by transposition in the coefficient basis, $R_{e_\nu}^{\mathrm{axf}}=D(L_{e_\nu}^{\mathrm{axf}})^{\mathsf T}D$ with $D=\operatorname{diag}(1,-1,-1,-1)$, and in the Peirce display of §*The Legacy Pauli Gamma Formulation* by the exchange $\mathsf S$ of the two mixed Peirce units, $R=\mathsf S L^{\mathsf T}\mathsf S^{-1}$, and the sixteen two-sided operators $L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}}$ are the matrix basis and the cell table of *Matrix Representations Conventions*, §*The Clifford Structure and the Frame*; five of the sixteen are the frame cells up to the factor $i$: $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$, $iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$.

**The spin operator and the words built on it.** The generator of the rotations is $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$, an operator whose glyph is the glyph of its element, like every operator of this section. The three words built on it — the **spin**, the **elementary spinor** and the **Dirac spinor** — are fixed in *Special Element Conventions*, §*The Spin Convention* and §*The Spinor Convention*, and are not restated here.

**The two marks on a glyph that is also an operator.** An operator read through its element follows the element rule in full.

- A glyph read with its scalar part, four components: the tilde. The canonical momentum $\tilde p=p_te_t+\vec p$, the Legendre conjugate of $\tilde q$; the biquaternionic gradient $\tilde\nabla$ of §*The Gradient*; the gauge-covariant gradient $\tilde\nabla^{\mathrm{gco}}$ of §*The Gauge-Covariant Gradient*.
- A pure glyph, three components: the arrow. The momentum operator $\vec p=-i\hbar\nabla=\sum_k\vec e_kp_k$.

The gradient decides the case cleanly: $\tilde\nabla$ is not pure, because its $e_t$ term carries $\partial/\partial Q_t$, while $\nabla=\sum_k\,\vec e_k\,\partial/\partial Q_k$ is pure and keeps the fixed glyph of §*The Gradient*, which carries no second mark.

**The case follows the layer.** The arrow does not change the case: a pure operator of the quaternion layer stays lower case, $\vec p$, and one of the biquaternion layer takes the upper case, $\vec P$. Where the letter already names another object of the layer, the operator is written in its explicit form, $-i\hbar\vec\nabla$, because no subscript marks an operator: the two-letter form $\mathrm{op}$ is not a token of the corpus, and *Algebra and Element Conventions* states the rule (§*The Algebra and Its Basis*). The three-momentum and the momentum operator share $\vec p$, as an eigenvalue and its operator do.

**The mark of a part, and the side carried by position.** The only arrow on a glyph is the short one, and it marks the **pure part**: $\vec e_x$, $\vec p$. The long arrow that sits over an operator is a different mark and not a second arrow of the same kind: it is the mark of the transposed reading, fixed in §*The Transposition of the Gradient*. The side of an action is not marked at all. It is carried by position, $b\psi$ against $\psi b$, the actor written on the side from which it acts, and position is unambiguous because the operand is itself a glyph.

**What names a side where position is not enough.** Three signs, each of which the corpus needs for a purpose of its own.

- $\natural$ marks the conjugation of an element, $a^{\natural}=(a_0,-a_1,-a_2,-a_3)$, and it is what carries a change of side, because it is an anti-automorphism: $(ab)^{\natural}=b^{\natural}a^{\natural}$, hence $(\psi D)^{\natural}=D^{\natural}\psi^{\natural}$, and a right action on $\psi$ is a left action on $\psi^{\natural}$. The theorem is below, §*The Two Sides and the Renaming Theorem*.
- $L_a$ and $R_a$ name a side outright when a statement is about operators rather than about fields, and the cell $L_{a}R_{b}$ prints both sides at once. The label of the side of a cell is the **operator chirality** — the left slot, the right slot, or both — fixed in *Special Element Conventions*, §*The Chirality Convention*, and proved in *Operator Chirality on the Biquaternion Algebra*, of the mathematical corpus.
- The superscript $R$ marks the one case that position alone leaves genuinely ambiguous: a derivative that differentiates the factor written to its left, $F\nabla^{R}=\sum_\mu(\partial F/\partial q_\mu)e_\mu$. It is used only inside a product of two distinct factors, which is where the theorem below does not reach.

**The dagger.** The dagger is the general adjoint of an operator, never of an element: $(L_a)^{\dagger}=L_{a^{*}}$. Several adjoints arise at once — one for each form, and one for each of the sandwiches — and the dagger is the mark that covers them all, of which the others are the instances. It is not a fifth conjugation: it belongs to the operators and not to the algebra. Where a dagger is written on an element the writing is an abuse: the mark that was meant is the star for the Hermitian conjugation, or the natural sign for the quaternion conjugation, according to the conjugation in view. The dagger is added to the glyph and does not replace the element's mark: the arrow states purity, which the adjoint preserves, so $\vec p^{\dagger}$ is again a pure operator; the tilde states a glyph read with its scalar part, which the adjoint also preserves, so $\tilde\nabla$ keeps its tilde. Where the adjoint in view is the one of the definite form and the operator carries no derivative, the two marks are written together, dagger first: $(L_a)^{\dagger}=(L_a)^{*}=L_{a^{*}}$. A derivative separates them: its dagger is the adjoint and carries the integration by parts, its star conjugates the units alone (§*The Gradient*); the series writes $\tilde\nabla^{*}=\tilde\nabla^{\natural}$ for the star.

**A Kraus operator is an element, not an array.** The Kraus operators of a channel or an instrument multiply the state on both sides, $\Phi(\tilde{Ϛ})=\sum_l\tilde K_l\tilde{Ϛ}\tilde K_l^{*}$, so each $\tilde K_l$ is an element of $\mathbb{B}$ and carries the tilde of the element. It is not a matrix, and the ban on a tilde on an array does not apply to it. Where the same operator is read as an array, that array is its image $\mathsf{M}_2(\tilde K_l)$, which carries no tilde, and its adjoint is the dagger, $\mathsf{M}_2(\tilde K_l)^{\dagger}=\mathsf{M}_2(\tilde K_l^{*})$; the corpus does not use that reading, and the star on the element is not a matrix adjoint.

**The Fock exception.** A Fock operator is not an element of the algebra; its superscript $\mathrm{fop}$ and the order of the two marks are fixed in *Unit, Index and Notation Conventions*, §*The Superscripts*.

## The Two Sides and the Renaming Theorem

**The statement.** Write $L_D\psi := D\psi$ and $R_D\psi := \psi D$ for the two one-sided actions on a field $\psi\in\mathbb{B}$. Then

$$
R_D=\natural\circ L_{D^{\natural}}\circ\natural,
\qquad
L_D=\natural\circ R_{D^{\natural}}\circ\natural,
$$

and on a field

$$
\boxed{\;(\psi D)^{\natural}=D^{\natural}\,\psi^{\natural}\;}
$$

**A right action on $\psi$ is a left action on $\psi^{\natural}$.** The side is not a property of the equation. It is a property of the field the equation is written on.

**The three properties.** Everything rests on them, and only the third is non-trivial.

| property | statement | residual |
|---|---|---|
| involutive | $\natural\circ\natural=\mathrm{id}$ | $0$ |
| $\mathbb{C}$-linear | $\natural(i\psi)=i\,\natural(\psi)$ | $0$ |
| anti-automorphism | $(ab)^{\natural}=b^{\natural}a^{\natural}$ | $2.6\times10^{-15}$ over $400$ random complex pairs |

The first makes $\natural$ invertible with $\natural^{-1}=\natural$. The third makes it **reverse the order of a product**. The second lets the mass, which is central, pass through untouched. An involution that preserved the order would identify the two sides; one that reverses the order exchanges them. $\natural$ reverses, so it exchanges.

**The proof is three symbols.** Applied to the two factors $\psi$ and $D$,

$$
(\psi D)^{\natural}=D^{\natural}\,\psi^{\natural}.
$$

Read forwards, conjugating a right action gives a left action of the conjugated operator. Read backwards, using $\natural^{2}=\mathrm{id}$, a right action is the conjugate of a left action — the two lines of the statement above.

**In matrix form it is one congruence.** With $N=\operatorname{diag}(1,-1,-1,-1)$ the matrix of $\natural$ on a coordinate column,

$$
N\,R_D\,N=L_{D^{\natural}},
\qquad
N\,L_D\,N=R_{D^{\natural}},
\qquad\text{both at residual }0 .
$$

$N$ is the change of basis that exchanges the two families, and $N^{\mathsf T}N=I$, $\det N=-1$.

**On an equation.** Take $\psi D=m\chi$ with $m$ central, so $m^{\natural}=m$, and conjugate both sides:

$$
D^{\natural}\,\psi^{\natural}=m\,\chi^{\natural}.
$$

The map $\Phi:(\psi,\chi)\mapsto(\psi^{\natural},\chi^{\natural})$ is $\mathbb{C}$-linear, involutive and invertible, so it is a **bijection of solution sets** and not an inclusion:

$$
\{\psi:\ \psi D=m\chi\}\ \xrightarrow{\ \Phi\ }\ \{u:\ D^{\natural}u=m\,\chi^{\natural}\},
\qquad \Phi^{-1}=\Phi .
$$

Verified: a pair solved on the right at residual $2.0\times10^{-15}$ maps to a pair solved on the left at residual $1.1\times10^{-15}$, on all four basis solutions. Same solutions, relabelled.

**What the theorem does not say.** It does not say the two operators are equal. On $D=-5e_t+3i\vec e_x$,

$$
\bigl\lVert R_D-L_{D^{\natural}}\bigr\rVert_{\mathrm F}=8.4853\neq0 ,
$$

so the two arrays differ and neither may be substituted for the other at sight. What is equal is the pair of solution sets after renaming, not the operators.

**Where the theorem does not reach.** Three cases, and each is stated where it is used.

1. **More than one field.** The anti-automorphism reverses the whole order, $(\psi D\chi)^{\natural}=\chi^{\natural}D^{\natural}\psi^{\natural}$, residual $1.3\times10^{-14}$ over $200$ random triples. The two fields exchange places, so renaming alone does not suffice, and where the two fields are not the same object the reordering changes the statement. The bilinear identities of the integration articles stand in this case, and it is why they carry the superscript $R$ on the derivative.
2. **A carrier without $\natural$.** On a column $\psi\in\mathbb{C}^{4}$ there is no natural conjugation, only the antilinear Dirac adjoint; on a space of functions of two variables, as in a star product, $\natural$ is not the involution in play. The theorem is a theorem about fields valued in $\mathbb{B}$.
3. **The side itself on display.** For the two-sided action $a\psi b$, the mirror coupling, or the exchange of the two slots of a cell, conjugating the field destroys what is being displayed. There both factors stay in place and the side is named by position, or by $L_a$ and $R_a$.

**The consequence for the corpus.** Every equation that acts on a single biquaternion field is written on the left. The ones that would read as acting on the right are the same equations on the conjugate field, and the chiral pair is the instance: with $\Phi=\tilde\Psi^{\natural}$, the pair $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$ and $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$ is complete as written, both equations acting from the left, and $\natural$ is what separates them. Across the $404$ files and $10\,196$ display equations of the physics corpus no glyph names a side: the side is position, the conjugation is $\natural$, and the exchange is $N$.

## Conventions for Derivation

In this work, subscripts denote vector components, not partial derivatives as in the PDE convention; every partial derivative is written explicitly with $\partial$ followed by its variable, and no subscript is ever attached to the $\partial$ of a derivative. A subscript is therefore a component index, as in $v_x$ for the component of a velocity along an axis, or a label, as in $\tilde U_{\mathrm r}$; it never denotes a derivative. The derivative with respect to a coordinate is written $\partial/\partial Q_\mu$, and in a fixed direction $\partial/\partial Q_t$, $\partial/\partial Q_x$, $\partial/\partial Q_y$ or $\partial/\partial Q_z$; a coordinate is never left under the $\partial$, so none of the abbreviated spellings occurs, and the rule admits no exception for a derivative, neither on a free index nor on any other.

**A subscript on an operator names its degree, its place or its bundle.** The rule governs the derivative of a field, which names its variable after the $\partial$. It does not forbid a label on an operator that differentiates nothing: the chain boundary is $\partial_n:C_n\to C_{n-1}$ and the face maps are $\partial_i$, with the degree in the subscript; the distinguished boundary of a polydisc is $\partial_0D$; the tame symbol is $\partial_v$, with the place; the twisted Dolbeault operator is $\bar\partial_E$, with the bundle. These are operator labels, in the sense of *Unit, Index and Notation Conventions*, §*The Subscripts*, and they stand as written.

**The coordinate derivative is unhalved.** It is defined by

$$
\frac{\partial}{\partial Q_\mu}:=\frac{\partial}{\partial q_\mu}+\frac{\partial}{\partial(iq'_\mu)},\qquad Q_\mu=q_\mu+iq'_\mu,
$$

the $i$ being glued to the primed coordinate: the derivative is taken with respect to the product $iq'_\mu$, not with respect to $q'_\mu$ with the $i$ pulled out in front. It is the formal derivative on the complex coordinate; with $Q_\mu$ and $\bar Q_\mu$ read as independent, its unhalved normalization gives $\partial Q_\mu/\partial Q_\mu=2$ and $\partial Q_\mu/\partial\bar Q_\mu=0$. On a real sector, where the fields depend on the tangential coordinate alone, the normal derivative is absent; on the material sector, with $Q_t=ict'$, the symbol is read with the tangential derivative alone, $\partial/\partial Q_t=-(i/c)\,\partial/\partial t'$, the reading that reproduces the kinetic term of §*The Hermitian Product, Its Form and Its Norm*; a derivative carrying a numerical factor would rescale that term. The conjugate derivative is

$$
\frac{\partial}{\partial\bar Q_\mu}:=\frac{\partial}{\partial q_\mu}-\frac{\partial}{\partial(iq'_\mu)},
$$

with $\partial\bar Q_\mu/\partial\bar Q_\mu=2$.

A derivative with respect to a variable that is not a coordinate is written the same way, its variable named in full: the Lagrangian derivative puts the function in the numerator, $\partial L/\partial u$, so that where a PDE text writes $L_u$ and $L_p$ the corpus writes $\partial L/\partial u$ and $\partial L/\partial p$; the second derivative has the same shape, $\partial^2 L/\partial u^2$. The function is named in the numerator whenever it is a letter of its own, as for a Lagrangian, a Hamiltonian or a generating function; the slashed form $\partial/\partial u$ is kept where the symbol is an operator or where the operand is a compound expression rather than a single letter. The time derivative $\partial/\partial Q_t$ is the imaginary-time derivative, and the material time derivative is written out as $\partial/\partial t'$. The rule holds on every object of the series, whether the letter names an element of the algebra, an element-valued field, a kernel or an operator.

**These studies do not use the covariant index conventions: subscripts are not coordinate indices or derivatives, partial derivatives are written with explicit operators, and structural information is carried by the algebra of the objects themselves.** A caret marks a power or a name, never a frame slot: $e^\lambda$, $2^k$ and $(-1)^k$ are powers, and $\mathrm{Cl}^i$, $K^0$, $M_4^\sigma$ and $\mathbb{B}^\sigma$ are names; a coordinate, a field component, a basis vector, a frame cell and a sign symbol are written with a low index — $x_\mu$, $A_\mu$, $\vec e_i$, $L_{e_\mu}^{\mathrm{axf}}R_{e_\nu}^{\mathrm{axf}}$, $\varepsilon_{ijk}$ — and a contraction is written as an explicit sum that names the summed index — $\sum_\mu e_\mu\partial/\partial Q_\mu$, $\sum_k\vec e_k A_k$, $\sum_{i,j}\varepsilon_{ijk}A_iB_j$ — never as a repeated index left to the summation convention. No index is summed by convention: an index that appears twice is summed only when a $\sum$ names it, and the shorthand with no sum is not used. A spatial matrix written with a raised index, whether a Pauli matrix or a stress component, is the same error as a raised coordinate: it hides which basis is contracted, and the index goes low.

### The Derivative Marks

**No dot.** No derivative is written with a dot. The total derivative with respect to a parameter is written with a fraction and the parameter named: $\frac{d}{dt'}$ for time, $\frac{d}{d\tau}$ for proper time, $\frac{d}{dt'_r}$ for retarded time; inline, the same derivative is written $dq/dt'$. The partial derivative is written $\frac{\partial}{\partial t'}$ or, inline, $\partial/\partial t'$. A higher derivative is written $\frac{d^2}{d{t'}^2}$, $\frac{\partial^2}{\partial {t'}^2}$. The derivative binds to its whole argument, so a power is written outside a bracket, $\left(\frac{dx}{dt'}\right)^2$, never as $\frac{dx^2}{dt'}$.

**The prime marks the imaginary part, and nothing else.** The prime belongs to a coefficient: it marks the imaginary part of a complex number, $q'_\mu$ of $Q_\mu = q_\mu + iq'_\mu$, the part that carries the $i$. It is not a derivative mark, and it is not a label of an element, a field or a coupling. A derivative is written with $d$ or $\partial$ and its variable named: a function of one variable is differentiated as $df/dx$, never as $f'$, and a second derivative as $d^2f/dx^2$ or $\partial^2f/\partial x^2$, never with a repeated prime or a repeated subscript. The complex time is $Q_t = ct+ict'$: its real part $ct$ is the informational time and its imaginary part $ct'$ the material time, with $q_t = ct$ and $q'_t = ct'$. The prime on $t'$ marks the coefficient that carries the $i$, exactly as the primes on $x',y',z'$ mark the imaginary spatial coefficients. Carried by an element glyph, the same prime names the element assembled from the primed coefficients, $\tilde q' = q'_t\,e_t+q'_x\vec e_x+q'_y\vec e_y+q'_z\vec e_z$ in $\tilde Q = \tilde q+i\tilde q'$, the antiquaternion part; it is the coefficient prime read on the whole glyph, not a label of a transformed or distinguished element.

**The prime is not a frame, source or field label.** The primed spatial coordinates $x',y',z'$ are the imaginary parts of the spatial coefficients, $Q_x=x+ix'$, $Q_y=y+iy'$, $Q_z=z+iz'$, with $(q'_x,q'_y,q'_z)=(x',y',z')$; the prime names the coordinate that carries the $i$. The primed time $t'$ is the imaginary part of $Q_t=ct+ict'$, with $q'_t=ct'$; the unprimed time $t$ is its real part, with $q_t=ct$. Outside these uses the prime is not written. A transformed frame is named by a subscript, never by $x'$ or $t'$; a source point, a second point and an integration variable take a numeric or role subscript, never a prime; an element, field, connection, curvature, current, state, coupling, group or map that is transformed or distinguished takes a numeric or role subscript, never a prime; and a derivative is written $df/dx$, never $f'$. The glyph $x'$ cannot be both the imaginary coordinate and a source or boosted coordinate: where both are needed, the source point or the frame takes the subscript.

**Labels that are not derivatives.** The second Lorentz label is written $\bar l$, and a spinor index of the conjugate representation is written $\bar\alpha$; the bar on an index marks the conjugate spinor. The conjugate matrix is $\bar\Pi$. These are labels, not derivatives.

**The scope mark.** In geometric calculus the factor differentiated is marked with an underline, $\underline{\partial}(AB)=\underline{\partial}A\,B+\underline{A}\,\underline{\partial}B$, not with a dot.

**The two derivative operators of the series** are the **biquaternionic gradient** $\tilde\nabla$ and the **d'Alembertian** $\Box$; every other partial derivative is written with $\partial$.

### The Gradient

The coordinate derivative is written $\partial/\partial Q_\mu$ and is defined by $\partial/\partial Q_\mu:=\partial/\partial q_\mu+\partial/\partial(iq'_\mu)$, with $Q_\mu=q_\mu+iq'_\mu$, as fixed in §*Conventions for Derivation*. The **biquaternionic gradient** is the element-valued operator

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial Q_\mu}=e_t\frac{\partial}{\partial Q_t}+\vec e_x\frac{\partial}{\partial Q_x}+\vec e_y\frac{\partial}{\partial Q_y}+\vec e_z\frac{\partial}{\partial Q_z},
$$

whose tilde marks its scalar part beside its vector part, with its **quaternion conjugate**, the involution of the norm,

$$
\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial Q_\mu}
=e_t\frac{\partial}{\partial Q_t}-\vec e_x\frac{\partial}{\partial Q_x}-\vec e_y\frac{\partial}{\partial Q_y}-\vec e_z\frac{\partial}{\partial Q_z},
\qquad \varepsilon=(1,-1,-1,-1).
$$

It is this conjugate and no other that the series composes with (*Biquaternion Analysis*, §*The Biquaternionic Gradient*, §*The Quaternion Conjugate of the Gradient*). Write $\nabla=\sum_k\vec e_k\,\partial/\partial Q_k$ for the spatial gradient, with divergence $\nabla\cdot\vec Q_{\mathrm f}$ and curl $\nabla\times\vec Q_{\mathrm f}$, and $\Delta_Q=\partial^2/\partial Q_x^2+\partial^2/\partial Q_y^2+\partial^2/\partial Q_z^2$ for the Laplacian in the three vector coordinates.

**The sum is written.** The gradient is a sum, and the sum is always spelled out. The shorthand $\vec e_k\partial/\partial Q_k$ is not used, because it repeats the index without summing it; the same holds for every contraction of a basis vector, a frame cell or a field component with a derivative. An index that appears twice is summed only where a $\sum$ names it.

**The conjugates of the gradient.** The gradient is an operator, and the marks are read on its units at fixed coordinate: the derivative symbols are held fixed and only the units are conjugated. This fixes the scope of the star, and it is not a claim that $\partial/\partial Q_\mu$ is real; the unhalved derivative of §*Conventions for Derivation* is complex, and on an element-valued field the star is coefficientwise, carried through the derivative by $\partial/\partial\bar Q_\mu$ rather than by $\partial/\partial Q_\mu$. Read on the units, the quaternion conjugation reverses the three spatial units, and so does the Hermitian conjugation, so the two act on the gradient alike,

$$
\tilde\nabla^{*}=\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial Q_\mu},
\qquad \overline{\tilde\nabla}=\tilde\nabla .
$$

**The forms stay four, the norms are two.** The four forms of *Product and Form Conventions*, §*The Involutions and the Four Forms* remain four distinct conventions here, because each conjugates its own slot: the quaternionic form conjugates the first argument and the Hermitian form the second, so on a general second argument they are not the same statement. But read at the two equal arguments they give two operators, the Hermitian norm coinciding with the quaternionic bilinear norm, $\langle\tilde\nabla\rangle_{*}=\langle\tilde\nabla\rangle_{\natural}$, and the Krein norm with the plain bilinear norm, $\langle\tilde\nabla\rangle_{\natural*}=\langle\tilde\nabla\rangle$. The four subsections below carry the four forms, and their norms are the two operators $\Box$ and $\partial^2/\partial Q_t^2-\Delta_Q$.

**On the material sector $\mathbb{M}_-$**, where $Q_t=ict'$ and $Q_k=q_k$, the time derivative reads $\partial/\partial Q_t=-\frac{i}{c}\,\partial/\partial t'$, the Laplacian is the physical $\Delta$, and the gradient is

$$
\tilde\nabla\big|_{\mathbb{M}_-}=-\frac{i}{c}\,e_t\frac{\partial}{\partial t'}+\sum_k\vec e_k\frac{\partial}{\partial Q_k}.
$$

**The dynamics.** The first-order dynamics of the series is the chiral pair $\tilde\nabla\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\tilde\nabla^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R$, with massless limit $\tilde\nabla\tilde{\Psi}=0$. Every component equation in the series is a **coordinate form** of that pair and not a second dynamics.

**The pair operator.** The two equations are one operator on $\mathbb{B}\oplus\mathbb{B}$. Write $\Psi=(\Psi_L,\Psi_R)$ and
$$
\mathbb{D}\Psi=\bigl(\tilde\nabla\Psi_R,\ \tilde\nabla^{\natural}\Psi_L\bigr).
$$
Then $\mathbb{D}^2=\Box I$, and the massive equation is $(\mathbb{D}-m)\Psi=0$. Its Green matrix is $\mathcal{S}=(\mathbb{D}+m)G$ with $(\Box-m^2)G=\delta$, so $(\mathbb{D}-m)\mathcal{S}=\delta I$. The operator is the pair written once; it is not a new object, and it contains no matrix generator.

**Plain $\mathbb{D}$ is $\mathbb{D}_{\tilde\nabla}$.** The glyph carries a subscript when the factor is not the material gradient, and it drops the subscript when it is: $\mathbb{D}_{p}$ for the constant momentum covector, so the symbol, $\mathbb{D}_{\mathrm E}$ for the gradient read at $t'=-i\tau$, and an element in parentheses, $\mathbb{D}(\tilde K)$, because a subscript on this glyph already means a factor while a letter on its right, $\mathbb{D}\Psi$, means the field acted on. The same rule governs the gradient itself, which is written $\tilde\nabla$ bare and takes $\mathrm E$, $\natural$ or a sector label only where a second one is in play.

### The Plain Bilinear Product, Its Form and Its Norm

**The product.** The general plain bilinear product is one of the four of *Product and Form Conventions*, §*The Twelve Products and Their Names*. On the gradient, with an element-valued field $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$, it is read with $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and $\vec e_j \vec e_k=-\delta_{jk}e_t+\epsilon_{jkl}\vec e_l$, so that the three spatial units carry the field back onto the scalar unit,

$$
\tilde\nabla\tilde Q_{\mathrm f}=\Bigl(\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}+\nabla Q_{\mathrm{f}t}+\nabla\times\vec Q_{\mathrm f} .
$$

A **product** is algebra-valued, and this one holds the divergence, the gradient and the curl of the field in a single object; for the field strength $\tilde F$ the equation $\tilde\nabla\tilde F=-\sqrt{\mu}\,\tilde J$, with $\tilde J=ic\rho\,e_t+\vec J$, is the series' Maxwell equation. **On the material sector** the same product is read with $\partial/\partial Q_t=-\frac{i}{c}\,\partial/\partial t'$, the space part being unchanged.

**The symmetric and antisymmetric parts.** Read with two arguments, the product splits as in *Product and Form Conventions*, §*The Twelve Products and Their Names*. The half-sum keeps the form as its scalar part,

$$
\tilde\nabla\bullet\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla\tilde Q_{\mathrm f}+\tilde Q_{\mathrm f}\tilde\nabla\bigr)=\Bigl[\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}-(\nabla,\vec Q_{\mathrm f})\Bigr]e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}+Q_{\mathrm{f}t}\nabla=\Bigl[\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f}\Bigr]e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}+\nabla Q_{\mathrm{f}t} ,
$$

and the half-difference is the curl,

$$
\tilde\nabla\wedge\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla\tilde Q_{\mathrm f}-\tilde Q_{\mathrm f}\tilde\nabla\bigr)=\tfrac12\bigl(\nabla\times\vec Q_{\mathrm f}+\nabla\times\vec Q_{\mathrm f}\bigr)=\nabla\times\vec Q_{\mathrm f} ,
$$

a pure vector, so the plain form carries the whole scalar content of the product. Throughout these four subsections the pair $(\nabla,\vec X)$ is read as the divergence $\nabla\cdot\vec X$ and $X\nabla$ as the gradient $\nabla X$, the derivative acting on the coefficient it multiplies, and the coordinate formulas substituted are those of *Product and Form Conventions*, §*The Twelve Products and Their Names*.

**The form.** The **plain form** is the scalar part of the product read in two arguments,

$$
\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle=\mathrm{Sc}(\tilde\nabla\tilde Q_{\mathrm f})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial}{\partial Q_\mu}Q_{\mathrm{f}\mu}=\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f} ,
$$

a scalar, the **contraction** of the derivative with the field in the sign vector $\varepsilon$. **On the material sector** it is $-\frac{i}{c}\frac{\partial Q_{\mathrm{f}t}}{\partial t'}-\nabla\cdot\vec Q_{\mathrm f}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments:

$$
\langle\tilde\nabla\rangle=\langle\tilde\nabla,\tilde\nabla\rangle=\mathrm{Sc}(\tilde\nabla\tilde\nabla)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}-\Delta_Q ,
$$

the cross terms cancelling. **On the material sector** it is $-c^{-2}\frac{\partial^2}{\partial {t'}^2}-\Delta$, which is neither the wave operator $\partial^2/\partial {t'}^2-c^2\Delta$ nor the series' d'Alembertian; on this sector the d'Alembertian is $\Delta-c^{-2}\partial^2/\partial {t'}^2$ (§*The Quaternionic Bilinear Product, Its Form and Its Norm*).

### The Quaternionic Bilinear Product, Its Form and Its Norm

**The product.** The general quaternionic bilinear product is the second of the four of *Product and Form Conventions*, §*The Twelve Products and Their Names*; on the gradient it is $\tilde\nabla^{\natural}\tilde Q_{\mathrm f}$, the conjugate derivative, read with the same rules, the three spatial units now carrying the field back onto the scalar unit with the opposite sign,

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}=\Bigl(\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}+\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}-\nabla Q_{\mathrm{f}t}-\nabla\times\vec Q_{\mathrm f} .
$$

**On the material sector** the same substitution $\partial/\partial Q_t=-\frac{i}{c}\,\partial/\partial t'$ applies.

**The symmetric and antisymmetric parts.** The half-sum is central and is the quaternionic form itself,

$$
\tilde\nabla\bullet_{\natural}\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde Q_{\mathrm f}+\tilde Q_{\mathrm f}^{\natural}\tilde\nabla\bigr)=\Bigl[\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}+(\nabla,\vec Q_{\mathrm f})\Bigr]e_t=\Bigl(\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}+\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t ,
$$

and the half-difference is the vector part of the product,

$$
\tilde\nabla\wedge_{\natural}\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde Q_{\mathrm f}-\tilde Q_{\mathrm f}^{\natural}\tilde\nabla\bigr)=\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}-Q_{\mathrm{f}t}\nabla-\nabla\times\vec Q_{\mathrm f}=\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}-\nabla Q_{\mathrm{f}t}-\nabla\times\vec Q_{\mathrm f} .
$$

**The form.** The **quaternionic form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde Q_{\mathrm f})=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial}{\partial Q_\mu}Q_{\mathrm{f}\mu}=\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}+\nabla\cdot\vec Q_{\mathrm f} ,
$$

a scalar, the **contraction** of the derivative with the field, all four signs plus because the conjugate derivative already carries $\varepsilon$; it differs from the plain form by the three signs of $\varepsilon$, which are **computed from the product** $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and not assumed. **On the material sector** it is $-\frac{i}{c}\frac{\partial Q_{\mathrm{f}t}}{\partial t'}+\nabla\cdot\vec Q_{\mathrm f}$.

**The norm, and the definition of the d'Alembertian.** The norm is defined with the form, as that form at its two equal arguments, and the two orders of the product agree:

$$
\Box=\langle\tilde\nabla\rangle_{\natural}=\langle\tilde\nabla,\tilde\nabla\rangle_{\natural}
=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{\natural})
=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q .
$$

**This is the definition of the d'Alembertian**: the quaternionic norm of the gradient, an operator on the whole algebra, one and the same before any sector is named (*The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*). The coordinates $Q_\mu$ are those of the algebra and are complex in general; the operator is $\partial^2/\partial Q_t^2+\Delta_Q$ whatever the sector, and it is **scalar**: it multiplies by $e_t$ and acts coefficient by coefficient, $\Box\tilde Q_{\mathrm f}=\sum_\mu(\Box Q_{\mathrm{f}\mu})e_\mu$. It is the identity above, and not the $ict'$ substitution, that fixes it, and **no article of the series defines a second d'Alembertian**; no mass-term sign is left to a local convention.

**The special case of the material sector.** On $\mathbb{M}_-$ the coordinates are the material ones, $Q_t=ict'$ and $Q_k=q_k$, and the $ict'$ substitution flips the sign of the time second derivative, $\partial^2/\partial Q_t^2=-c^{-2}\,\partial^2/\partial {t'}^2$, so the same operator reads

$$
\Box\big|_{\mathbb{M}_-}=\frac{\partial^2}{\partial Q_t^2}+\Delta=\Delta-c^{-2}\,\frac{\partial^2}{\partial {t'}^2},
$$

a plus on the spatial part and a minus on the time part. On $\mathbb{M}_-$, where the series does its work, this reading is the **series convention**, used by the Klein–Gordon article, the Dirac article, the dedicated article *The Biquaternion D'Alembertian and Its Green's Functions*, and the great majority of the series. **The $ict'$ substitution is a statement about the material sector, not about the operator**, which in every case is $\partial^2/\partial Q_t^2+\Delta_Q$; its signature is not a property of the operator but of the **slice** it is read on, since on a named subspace some of the $Q_\mu$ are purely imaginary. The operator is one, and every article writes it the same way.

### The Hermitian Product, Its Form and Its Norm

**The product.** The general plain sesquilinear product is the third of the four of *Product and Form Conventions*, §*The Twelve Products and Their Names*; it is the plain product applied to the **conjugated** field $\tilde Q_{\mathrm f}^{*}=\bar Q_{\mathrm{f}t}e_t-\overline{\vec Q_{\mathrm f}}$, so that on the gradient it is $\tilde\nabla\tilde Q_{\mathrm f}^{*}$, conjugate-linear in the field while the first slot stays $\mathbb{C}$-linear,

$$
\tilde\nabla\tilde Q_{\mathrm f}^{*}=\Bigl(\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}+\nabla\bar Q_{\mathrm{f}t}-\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**The symmetric and antisymmetric parts.** Under the conjugate transpose the half-sum is central and is the Hermitian form itself,

$$
\tilde\nabla\bullet_{*}\tilde Q_{\mathrm f}=\mathrm{Sc}(\tilde\nabla\tilde Q_{\mathrm f}^{*})=\Bigl[\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+(\nabla,\overline{\vec Q_{\mathrm f}})\Bigr]e_t=\Bigl(\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t ,
$$

and the half-difference is the vector part,

$$
\tilde\nabla\wedge_{*}\tilde Q_{\mathrm f}=\mathrm{Vect}(\tilde\nabla\tilde Q_{\mathrm f}^{*})=-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}+\bar Q_{\mathrm{f}t}\nabla-\nabla\times\overline{\vec Q_{\mathrm f}}=-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}+\nabla\bar Q_{\mathrm{f}t}-\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**The form.** The **Hermitian form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{*}=\mathrm{Sc}(\tilde\nabla\tilde Q_{\mathrm f}^{*})=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial}{\partial Q_\mu}\bar Q_{\mathrm{f}\mu}=\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}} ,
$$

a scalar, the **contraction** of the derivative with the **conjugated** field, all four signs plus because the conjugation and the derivative together supply the sign vector. Taken on the scalar field it gives the **kinetic density**, the scalar part of the product of the two conjugated gradients,

$$
\mathrm{Sc}\bigl[(\tilde\nabla^{\natural}\tilde\Phi^{*})(\tilde\nabla\tilde\Phi)\bigr]=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial\Phi^{*}}{\partial Q_\mu}\frac{\partial\Phi}{\partial Q_\mu} ,
$$

in which the conjugate stands on the first factor and no absolute value is taken; the two time derivatives are imaginary on the material sector, so that scalar part is $-c^{-2}\lvert\partial\phi/\partial t'\rvert^2+\lvert\nabla\phi\rvert^2$, and the kinetic term the series writes is

$$
\mathcal L^{\mathrm{kin}}=-\mathrm{Sc}\bigl[(\tilde\nabla^{\natural}\tilde\Phi^{*})(\tilde\nabla\tilde\Phi)\bigr]=\frac{1}{c^2}\Bigl|\frac{\partial\phi}{\partial t'}\Bigr|^2-\lvert\nabla\phi\rvert^2 ,
$$

the kinetic density of the Klein–Gordon article (*Hamiltonian Field Theory in Biquaternionic Form*). **On the material sector** the form itself is $-\frac{i}{c}\frac{\partial\bar Q_{\mathrm{f}t}}{\partial t'}+\nabla\cdot\overline{\vec Q_{\mathrm f}}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments. By §*The Gradient*, $\tilde\nabla^{*}=\tilde\nabla^{\natural}$, and

$$
\langle\tilde\nabla,\tilde\nabla\rangle_{*}=\langle\tilde\nabla\rangle_{*}=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{*})=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{\natural})=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q=\Box ,
$$

so the Hermitian norm of the gradient is the d'Alembertian, the same operator as its quaternionic bilinear norm. The **Hermitian form is the one positive-definite form of the four**, $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^2$ on the elements, and its square root is the topological norm $\lVert\tilde Q\rVert_E$; positivity is a property of the elements, the norm of this subsection being the operator $\Box$. **On the material sector** it is the same operator, $\Box|_{\mathbb{M}_-}=\Delta-c^{-2}\,\partial^2/\partial {t'}^2$.

### The Krein Product, Its Form and Its Norm

**The product.** The general quaternionic sesquilinear product is the fourth of the four of *Product and Form Conventions*, §*The Twelve Products and Their Names*; it is the conjugate derivative applied to the conjugated field, $\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}$, the companion of the quaternionic bilinear product in the second slot,

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}=\Bigl(\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}-\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}-\nabla\bar Q_{\mathrm{f}t}+\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**The symmetric and antisymmetric parts.** Under the conjugate transpose the half-sum is

$$
\tilde\nabla\bullet_{\natural*}\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}+\tilde Q_{\mathrm f}^{*}\tilde\nabla^{\natural}\bigr)=\Bigl[\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}-(\nabla,\overline{\vec Q_{\mathrm f}})\Bigr]e_t-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}-\bar Q_{\mathrm{f}t}\nabla=\Bigl[\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}-\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr]e_t-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}-\nabla\bar Q_{\mathrm{f}t} ,
$$

whose scalar part is the Krein form, and the half-difference is the curl of the conjugated field,

$$
\tilde\nabla\wedge_{\natural*}\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}-\tilde Q_{\mathrm f}^{*}\tilde\nabla^{\natural}\bigr)=\tfrac12\bigl(\nabla\times\overline{\vec Q_{\mathrm f}}+\nabla\times\overline{\vec Q_{\mathrm f}}\bigr)=\nabla\times\overline{\vec Q_{\mathrm f}} ,
$$

a pure vector.

**The form.** The **Krein form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural*}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial}{\partial Q_\mu}\bar Q_{\mathrm{f}\mu}=\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}-\nabla\cdot\overline{\vec Q_{\mathrm f}} ,
$$

a scalar, the **contraction** of the conjugate derivative with the conjugated field in the $ict'$ metric. **On the material sector** it is $-\frac{i}{c}\frac{\partial\bar Q_{\mathrm{f}t}}{\partial t'}-\nabla\cdot\overline{\vec Q_{\mathrm f}}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments; on the gradient, since $\tilde\nabla^{*}=\tilde\nabla^{\natural}$ (§*The Gradient*),

$$
\langle\tilde\nabla,\tilde\nabla\rangle_{\natural*}=\langle\tilde\nabla\rangle_{\natural*}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla^{*})=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla^{\natural})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}-\Delta_Q ,
$$

so the Krein norm of the gradient **coincides with the plain bilinear norm**. It is the indefinite partner of the Hermitian form, and on the elements it is the form of signature $(1,3)$ whose diagonal is $\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2$: Hermitian, and negative on a nonzero element, so it carries no positivity. It is the form of the indefinite theory — the Krein space — and not of the contractions of these subsections. **On the material sector** it is $-c^{-2}\frac{\partial^2}{\partial {t'}^2}-\Delta$.

**A contraction is a form, never an index.** The metric of the series is the sign vector $\varepsilon$ inside the product, so no index is raised and none is lowered. Where a text with covariant indices contracts a derivative with a field through a raised and a lowered index, the series writes the quaternionic form $\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural}$; where it contracts two derivatives, the series writes the quaternionic norm $\langle\tilde\nabla\rangle_{\natural}=\Box$; and where it moves an index through a metric, the series writes the element $\tilde Q_{\mathrm f}$ itself, the metric being the sign vector inside the product. The four-index alternating symbol is not an index carrier: it is the orientation density, written all-low, $\epsilon_{0123}=+1$, and its height carries no sign. Its rank distinguishes it from the sign vector of the same letter.

### The Gauge-Covariant Gradient

A derivative that differentiates a field charged under a connection is the gradient with a connection added. It carries the gradient's letter and **a label, not a letter of its own**:

$$
\tilde\nabla^{\mathrm{gco}}=\tilde\nabla+\frac{iϙ}{\hbar}\tilde A=\sum_{\mu\in\{t,x,y,z\}}e_\mu\,\tilde\nabla^{\mathrm{gco}}_\mu,
\qquad
\tilde\nabla^{\mathrm{gco}}_\mu=\frac{\partial}{\partial Q_\mu}+\frac{iϙ}{\hbar}A_\mu,
$$

with $\tilde A=\sum_\mu A_\mu e_\mu\in\mathbb{M}_-$ the connection and $ϙ$ the charge of the field the operator acts on. The superscript $\mathrm{gco}$ names the family once and is read on every member of it.

**The decomposition is the gradient's, direction by direction.** One index, one basis element, one coefficient, exactly as in $\tilde\nabla=\sum_\mu e_\mu\,\partial/\partial Q_\mu$. The only change is the coefficient: the partial derivative of the free gradient is replaced by the covariant one, $\partial/\partial Q_\mu\mapsto\tilde\nabla^{\mathrm{gco}}_\mu$, and the basis $e_\mu$ is untouched. The sum is spelled out here as everywhere. The coefficient is a **central scalar** — it commutes with $e_\nu$ and with every element of $\mathbb{B}$ — and that is what lets the involution act on the basis and leave the coefficients in place:

$$
\tilde\nabla^{\mathrm{gco},\natural}=\sum_{\mu\in\{t,x,y,z\}}e_\mu^{\natural}\,\tilde\nabla^{\mathrm{gco}}_\mu=\tilde\nabla^{\natural}+\frac{iϙ}{\hbar}\tilde A^{\natural}.
$$

The label is written **before** the conjugation, in the order the operator is built: the family first, the involution second. The conjugate is not a second operator; it is the same sum with $\natural$ read on the units, and its coefficients are the same scalars.

**The side.** Both members act from the left. The position of the operator names the side, as it does for every field of the series, and no glyph names it: a right action on $\psi$ is the left action of $\tilde\nabla^{\mathrm{gco},\natural}$ on $\psi^{\natural}$, by the exchange of §*The Two Sides and the Renaming Theorem*.

**The curvature and the square.** The components do not commute, and their commutator carries no derivative:

$$
[\tilde\nabla^{\mathrm{gco}}_\mu,\tilde\nabla^{\mathrm{gco}}_\nu]=\frac{iϙ}{\hbar}F_{\mu\nu},
\qquad
\tilde\nabla^{\mathrm{gco},\natural}\tilde\nabla^{\mathrm{gco}}=\sum_{\mu\in\{t,x,y,z\}}\bigl(\tilde\nabla^{\mathrm{gco}}_\mu\bigr)^{2}+\frac{iϙ}{\hbar}\tilde F,
$$

with $\tilde F=\mathrm{Vect}(\tilde\nabla^{\natural}\tilde A)$ the curvature. The scalar part of the square is the covariant d'Alembertian and the vector part is the curvature; both are read in *The Covariant Derivative and Gauge Connection in Biquaternionic Form*.

**The coupling, and the letter $\kappa$.** A few articles write the same operator as $\tilde\nabla+i\kappa\mathcal A$, with $\kappa$ the coupling and $\mathcal A$ the connection. That is one object under two spellings, $\kappa=ϙ/\hbar$ and $\mathcal A=\tilde A$. The series writes $\frac{iϙ}{\hbar}\tilde A$, so that $\kappa$ stays free for the retarded denominator $\kappa=1-\vec u_R\cdot\vec\beta$ of *Algebra and Element Conventions*, which is not a coupling.

## The Transposition of the Gradient

**The transposed reading.** A gradient acts on the factor written to its right, $\tilde\nabla\tilde Q_1$. The long arrow over the glyph marks the other reading: the operator acts on the factor written to its left, and the arrow points at that factor, $\tilde Q_1\overleftarrow{\tilde\nabla}$. The mark belongs to the operator and not to the field, and it is not the short arrow of the pure part, which sits on an element and marks its vector part alone. Read this way, the gradient has its derivative to the right of the element it differentiates,

$$
\tilde Q_1\overleftarrow{\tilde\nabla}:=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial\tilde Q_1}{\partial Q_\mu}\,e_\mu ,
$$

the same four coefficients in the same four directions, with the unit written after each. The integration articles write this object $\nabla^{R}$ and use it wherever a derivative has to be moved off a product. It is not a second operator: it is the gradient with its two factors exchanged, and the exchange is what the identity below computes.

**The identity.** For every element-valued field $\tilde Q_1$,

$$
\boxed{\;\bigl(\tilde Q_1\overleftarrow{\tilde\nabla}\bigr)^{\natural}=\tilde\nabla^{\natural}\tilde Q_1^{\natural}\;}
\qquad\Longrightarrow\qquad
\tilde Q_1\overleftarrow{\tilde\nabla}=\bigl(\tilde\nabla^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}.
$$

**The proof is one term.** The involution is $\mathbb{C}$-linear, it acts on the units at fixed coordinate, and it commutes with $\partial/\partial Q_\mu$; and $e_\mu^{\natural}=\varepsilon_\mu e_\mu$. The $\mu$-th term on the left, $(\partial\tilde Q_1/\partial Q_\mu)^{\natural}(e_\mu)^{\natural}$, is therefore $\varepsilon_\mu e_\mu\,\partial\tilde Q_1^{\natural}/\partial Q_\mu$, which is the $\mu$-th term of $\tilde\nabla^{\natural}\tilde Q_1^{\natural}$. Summing over $\mu$ gives the boxed line, and $\natural^{2}=\mathrm{id}$ gives the arrow back.

**What it says.** A right action is the conjugation of a left action: conjugate the field, apply the conjugate gradient from the left, conjugate the result. In the notation of §*The Two Sides and the Renaming Theorem*, $R_{\tilde\nabla}=\natural\circ L_{\tilde\nabla^{\natural}}\circ\natural$, read on a differential operator rather than on a multiplication. The statement needs no equation, no mass, no chirality and no pair of fields. It is an identity between operators, true of any $\tilde Q_1$: a solution, a non-solution, a product, a constant.

**With a connection nothing changes.** The components of $\tilde\nabla^{\mathrm{gco}}$ are central scalars, so the same term-by-term computation gives $\bigl(\tilde Q_1\overleftarrow{\tilde\nabla^{\mathrm{gco}}}\bigr)^{\natural}=\tilde\nabla^{\mathrm{gco},\natural}\tilde Q_1^{\natural}$, at the same residual, with $\natural$ again fixing the coefficients and reading the units alone.

**The instance that hides the generality.** The chiral pair is the case usually quoted. From $\tilde\nabla^{\natural}\Psi_L=m\Psi_R$, transposing with $\tilde Q_1=\Psi_L^{\natural}$ and using $m^{\natural}=m$,

$$
\tilde\nabla^{\natural}\Psi_L=m\,\Psi_R
\qquad\Longrightarrow\qquad
\Psi_L^{\natural}\overleftarrow{\tilde\nabla}=m\,\Psi_R^{\natural},
$$

one line, with the derivative now written to the right of $\Psi_L^{\natural}$ and the same mass in place. Read alone, the pair suggests that the right action is a property of the Dirac equation. It is not: the two lines hold of $\tilde\nabla\Psi_R=m\Psi_L$ as well, of a massless field, and of any equation in which one field stands to the right of a derivative. The equation supplies the right-hand side; the identity does not depend on it.

**Why the superscript $R$ is nevertheless written.** The identity holds for a field, and a product of fields is a field. What it does not do is move the derivative off one factor of a product while the other stays. On $\tilde Q_1\tilde Q_2$ the Leibniz rule gives

$$
(\tilde Q_1\tilde Q_2)\overleftarrow{\tilde\nabla}=\sum_{\mu\in\{t,x,y,z\}}\Bigl(\frac{\partial\tilde Q_1}{\partial Q_\mu}\tilde Q_2+\tilde Q_1\frac{\partial\tilde Q_2}{\partial Q_\mu}\Bigr)e_\mu ,
$$

with the unit after the bracket. It does not pass to the left of $\tilde Q_2$: that is a commutation with the units, allowed only when $\tilde Q_2$ is central. Nor is the rule $\sum_\mu(\partial\tilde Q_1/\partial Q_\mu)e_\mu\tilde Q_2$, which differs from the first term by the defect $\sum_\mu(\partial\tilde Q_1/\partial Q_\mu)[\tilde Q_2,e_\mu]$. That is the case §*The Two Sides and the Renaming Theorem* excludes, and the case the integration articles meet. There the derivative is named $\nabla^{R}$ after the factor it differentiates, and the name is a position, not a second operator.

**The slots.** The transposition is the exchange of the two slots of a cell, read on a differential operator. In the language of *Operator Chirality on the Biquaternion Algebra*, §*Conjugation Exchanges the Sides*, the map that carries a left multiplier to a right multiplier is $\mathsf C$, the conjugation written as a congruence, $\mathsf C L(a^{\natural})\mathsf C=R(a)$, which in the axis-free frame is the switch $\mathsf D=\operatorname{diag}(1,-1,-1,-1)$ and is the $N$ of the matrix form above. A left action of the gradient and a right action of the same gradient therefore have arrays that agree up to that sign and that order, which is where the phases of the two sides come from.

**What it is not.** Not a transpose without conjugation: $N$ is not the identity, and $N^{\mathsf T}N=I$ with $\det N=-1$ make the congruence a congruence and not a similarity. Not the adjoint either: the dagger carries the integration by parts and the boundary term, while $\natural$ carries the units alone at fixed coordinate; the two agree on the gradient, $\tilde\nabla^{*}=\tilde\nabla^{\natural}$, and part on a general element.

**Verified.** On random polynomial fields in the four coordinates the boxed line holds at residual $0.0$, the reconstruction from the conjugate at $0.0$, the chiral instance at $0.0$, and the product rule above at $0.0$; on $\tilde Q_1=x\vec e_x$ and $\tilde Q_2=\vec e_y$ the naive rule returns $-\vec e_y$ where the product rule returns $+\vec e_y$. The anti-automorphism it uses holds at residual $1.0\times10^{-15}$ over $200$ random pairs; the automorphism that would be needed if the units were not reversed fails at $2.7\times10^{1}$.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate and on the metric, $g[\mathbb{B}]$ or $g[\mathbb{M}_-]$.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

An operator whose letter is the letter of an element is that element: the tilde and the arrow are read on it as on the element, and no mark says operator. The named operators are left and right multiplication, the two-sided operator, the sandwich and the inner derivation. The side of an action is position, $D\psi$ against $\psi D$; the two are exchanged by the natural conjugation, $(\psi D)^{\natural}=D^{\natural}\psi^{\natural}$, so a right action on a field is a left action on the conjugate field, and no glyph marks a side. The superscript $R$ marks the right derivative, the one case the exchange does not reach, and on the gradient even that case is a conjugation: $\tilde Q_1\overleftarrow{\tilde\nabla}=\bigl(\tilde\nabla^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}$, so a right action is the left action of the conjugate gradient on the conjugate field, and the identity needs no equation. The dagger is the general adjoint of an operator and not a fifth conjugation, and it adds to the element's mark rather than replacing it. A Kraus operator is an element, not an array. The Fock operator is the one operator that is not an element, and its superscript is fixed with the other tokens.

A subscript is a component or a label, never a derivative; every partial derivative is written with $\partial$ and its variable. A caret is a power or a name, never a frame slot: every coordinate, component, basis vector, frame cell and sign symbol is written low, and a contraction is a form with the sign vector. The coordinate derivative is unhalved, $\partial/\partial Q_\mu=\partial/\partial q_\mu+\partial/\partial(iq'_\mu)$. The gradient is $\tilde\nabla$, not pure. The d'Alembertian is $\Box=\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\partial^2/\partial Q_t^2+\Delta_Q$, read on the material sector as $\Delta-c^{-2}\partial^2/\partial t'^2$, and every article uses this one operator with the mass equation $(\Box-m^2c^2/\hbar^2)\psi=0$. The gauge-covariant gradient is the same sum with the coefficient replaced, $\tilde\nabla^{\mathrm{gco}}=\sum_\mu e_\mu\tilde\nabla^{\mathrm{gco}}_\mu=\tilde\nabla+\frac{iϙ}{\hbar}\tilde A$, and it carries a label rather than a letter of its own.

The four forms remain four distinct conventions and the norms two, because each form conjugates its own slot. The four closing subsections read the same gradient through the plain, quaternionic, Hermitian and Krein products, each with its form and its norm, and the signs follow from the algebra rather than from a choice of metric.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q}, R_{\tilde Q}$ | Left and right multiplication by the element; the glyph of the operator is the glyph of the element |
| $L_{\tilde Q_4}R_{\tilde Q_1}$ | The two-sided operator, $\tilde Q_2\mapsto\tilde Q_4\tilde Q_2\tilde Q_1$ |
| $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ | The sandwich, the congruence by the element |
| $\operatorname{ad}_{\tilde Q}$ | The inner derivation, $[\tilde Q,\cdot]$ |
| $^{\dagger}$ | The general adjoint of an operator; $(L_a)^{\dagger}=L_{a^{*}}$ |
| $\partial/\partial Q_\mu$ | The unhalved coordinate derivative, $\partial/\partial q_\mu+\partial/\partial(iq'_\mu)$ |
| $\tilde\nabla$ | The biquaternionic gradient, four components, not pure |
| $\tilde\nabla^{\mathrm{gco}}$ | The gauge-covariant gradient, $\tilde\nabla+\frac{iϙ}{\hbar}\tilde A$; its component $\tilde\nabla^{\mathrm{gco}}_\mu=\partial/\partial Q_\mu+\frac{iϙ}{\hbar}A_\mu$, its conjugate $\tilde\nabla^{\mathrm{gco},\natural}$ |
| $\Box$ | The d'Alembertian, $\tilde\nabla\tilde\nabla^{\natural}=\partial^2/\partial Q_t^2+\Delta_Q$ |
| $^{\natural}$ | The natural conjugation, $a^{\natural}=(a_0,-a_1,-a_2,-a_3)$; an anti-automorphism, $(ab)^{\natural}=b^{\natural}a^{\natural}$ |
| $(\psi D)^{\natural}=D^{\natural}\psi^{\natural}$ | The exchange of the two sides: a right action on $\psi$ is a left action on $\psi^{\natural}$ |
| $\nabla^{R}$ | The right gradient, $F\nabla^{R}=\sum_\mu(\partial F/\partial q_\mu)e_\mu$; used only where a derivative meets two distinct factors |
| $\overleftarrow{\ }$ | The long arrow over an operator: it acts on the factor written to its left, and the arrow points at that factor; it is not the short arrow of the pure part |
| $\tilde Q_1\overleftarrow{\tilde\nabla}$ | The same gradient transposed, $\sum_\mu(\partial\tilde Q_1/\partial Q_\mu)e_\mu$; the right action, equal to $\bigl(\tilde\nabla^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html), for the algebra and the element glyphs.
- [Conventions of the Products and the Forms](product-and-form-conventions.html), for the four products read on the gradient.
- [Conventions of the Norms and the Pairings](norm-and-pairing-conventions.html), for the norms of those products.
- [Conventions of the Units, the Indices and the Notation](unit-index-and-notation-conventions.html), for the Fock superscript and the subscript rules.
- [The Element and Operator Representations](element-and-operator-representations-the-three-actions.html), companion article, for the three actions and their matrices.
