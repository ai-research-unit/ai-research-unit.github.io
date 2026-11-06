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
| sandwich | $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}=\operatorname{H}_{\tilde Q}$ |
| inner derivation | $\operatorname{ad}_{\tilde Q_4}(\tilde Q_1)=[\tilde Q_4,\tilde Q_1]$ |
| automorphism | $\operatorname{Ad}_{\tilde Q_4}$ |

The tilde sits in the subscript because it belongs to the element, not to the operator: $L_{\tilde Q}$ is an operator, $\tilde Q$ is the element that generates it.

**The basis operators.** The four units are written in the subscript, $L_{\mathrm{axf},e_\mu}$ and $R_{\mathrm{axf},e_\mu}$, and nowhere else: the short form $L_\mu$ is not used in this corpus. The right family is read from the left one by transposition in the coefficient basis, $R_{\mathrm{axf},e_\nu}=D(L_{\mathrm{axf},e_\nu})^{\mathsf T}D$ with $D=\operatorname{diag}(1,-1,-1,-1)$, and in the Peirce display of §*The Legacy Pauli Gamma Formulation* by the exchange $\mathsf S$ of the two mixed Peirce units, $R=\mathsf S L^{\mathsf T}\mathsf S^{-1}$, and the sixteen two-sided operators $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$ are the matrix basis and the cell table of *Matrix Representations Conventions*, §*The Clifford Structure and the Frame*; five of the sixteen are the frame cells up to the factor $i$: $iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}$, $iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y}$, $iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}$, $iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y}$, $-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}$.

**The spin operator and the words built on it.** The generator of the rotations is $\tilde S_k=\tfrac{\hbar}{2}i\vec e_k$, an operator whose glyph is the glyph of its element, like every operator of this section. The three words built on it — the **spin**, the **elementary spinor** and the **Dirac spinor** — are fixed in *Special Element Conventions*, §*The Spin Convention* and §*The Spinor Convention*, and are not restated here.

**The two marks on a glyph that is also an operator.** An operator read through its element follows the element rule in full.

- A glyph read with its scalar part, four components: the tilde. The canonical momentum $\tilde p=p_te_t+\vec p$, the Legendre conjugate of $\tilde q$; the biquaternionic gradient $\tilde\nabla$ of §*The Gradient*; the gauge-covariant gradient $\tilde\nabla_{\mathrm{gco}}$ of §*The Gauge-Covariant Gradient*.
- A pure glyph, three components: the arrow. The momentum operator $\vec p=-i\hbar\nabla=\sum_k\vec e_kp_k$.

The gradient decides the case cleanly: $\tilde\nabla$ is not pure, because its $e_t$ term carries $\partial/\partial R_t$, while $\nabla=\sum_k\,\vec e_k\,\partial/\partial R_k$ is pure and keeps the fixed glyph of §*The Gradient*, which carries no second mark.

**The case follows the layer.** The arrow does not change the case: a pure operator of the quaternion layer stays lower case, $\vec p$, and one of the biquaternion layer takes the upper case, $\vec P$. Where the letter already names another object of the layer, the operator is written in its explicit form, $-i\hbar\vec\nabla$, because no subscript marks an operator: the two-letter form $\mathrm{op}$ is not a token of the corpus, and *Algebra and Element Conventions* states the rule (§*The Algebra and Its Basis*). The three-momentum and the momentum operator share $\vec p$, as an eigenvalue and its operator do.

**The mark of a part, and the side carried by position.** The only arrow on a glyph is the short one, and it marks the **pure part**: $\vec e_x$, $\vec p$. The long arrow that sits over an operator is a different mark and not a second arrow of the same kind: it is the mark of the transposed reading, fixed in §*The Transposition of the Gradient*. The side of an action is not marked at all. It is carried by position, $b\tilde{Ξ}_{\mathrm{sp}}$ against $\tilde{Ξ}_{\mathrm{sp}} b$, the actor written on the side from which it acts, and position is unambiguous because the operand is itself a glyph.

**What names a side where position is not enough.** Three signs, each of which the corpus needs for a purpose of its own.

- $\natural$ marks the conjugation of an element, $a^{\natural}=(a_0,-a_1,-a_2,-a_3)$, and it is what carries a change of side, because it is an anti-automorphism: $(ab)^{\natural}=b^{\natural}a^{\natural}$, hence $(\tilde{Ξ}_{\mathrm{sp}} D)^{\natural}=D^{\natural}\tilde{Ξ}_{\mathrm{sp}}^{\natural}$, and a right action on $\tilde{Ξ}_{\mathrm{sp}}$ is a left action on $\tilde{Ξ}_{\mathrm{sp}}^{\natural}$. The theorem is below, §*The Two Sides and the Renaming Theorem*.
- $L_a$ and $R_a$ name a side outright when a statement is about operators rather than about fields, and the cell $L_{a}R_{b}$ prints both sides at once. The label of the side of a cell is the **operator chirality** — the left slot, the right slot, or both — fixed in *Special Element Conventions*, §*The Chirality Convention*, and proved in *Operator Chirality on the Biquaternion Algebra*, of the mathematical corpus.
- The superscript $R$ marks the one case that position alone leaves genuinely ambiguous: a derivative that differentiates the factor written to its left, $F\nabla^{R}=\sum_\mu(\partial F/\partial R_\mu)e_\mu$. It is used only inside a product of two distinct factors, which is where the theorem below does not reach.

**The dagger.** The dagger is the general adjoint of an operator, never of an element: $(L_a)^{\dagger}=L_{a^{*}}$. Several adjoints arise at once — one for each form, and one for each of the sandwiches — and the dagger is the mark that covers them all, of which the others are the instances. It is not a fifth conjugation: it belongs to the operators and not to the algebra. Where a dagger is written on an element the writing is an abuse: the mark that was meant is the star for the Hermitian conjugation, or the natural sign for the quaternion conjugation, according to the conjugation in view. The dagger is added to the glyph and does not replace the element's mark: the arrow states purity, which the adjoint preserves, so $\vec p^{\dagger}$ is again a pure operator; the tilde states a glyph read with its scalar part, which the adjoint also preserves, so $\tilde\nabla$ keeps its tilde. Where the adjoint in view is the one of the definite form and the operator carries no derivative, the two marks are written together, dagger first: $(L_a)^{\dagger}=(L_a)^{*}=L_{a^{*}}$. A derivative separates them: its dagger is the adjoint and carries the integration by parts, its star conjugates the units alone (§*The Gradient*); the series writes $\tilde\nabla^{*}=\tilde\nabla^{\natural}$ for the star.

**A Kraus operator is an element, not an array.** The Kraus operators of a channel or an instrument multiply the state on both sides, $Ξ(\tilde{Ϛ})=\sum_l\tilde K_l\tilde{Ϛ}\tilde K_l^{*}$, so each $\tilde K_l$ is an element of $\mathbb{B}$ and carries the tilde of the element. It is not a matrix, and the ban on a tilde on an array does not apply to it. Where the same operator is read as an array, that array is its image $\mathsf{M}_2(\tilde K_l)$, which carries no tilde, and its adjoint is the dagger, $\mathsf{M}_2(\tilde K_l)^{\dagger}=\mathsf{M}_2(\tilde K_l^{*})$; the corpus does not use that reading, and the star on the element is not a matrix adjoint.

**The Fock exception.** A Fock operator is not an element of the algebra; its superscript $\mathrm{fop}$ and the order of the two marks are fixed in *Unit, Index and Notation Conventions*, §*The Superscripts*.

## The Two Sides and the Renaming Theorem

**The statement.** Write $L_D\tilde{Ξ}_{\mathrm{sp}} := D\tilde{Ξ}_{\mathrm{sp}}$ and $R_D\tilde{Ξ}_{\mathrm{sp}} := \tilde{Ξ}_{\mathrm{sp}} D$ for the two one-sided actions on a field $\tilde{Ξ}_{\mathrm{sp}}\in\mathbb{B}$. Then

$$
R_D=\natural\circ L_{D^{\natural}}\circ\natural,
\qquad
L_D=\natural\circ R_{D^{\natural}}\circ\natural,
$$

and on a field

$$
\boxed{\;(\tilde{Ξ}_{\mathrm{sp}} D)^{\natural}=D^{\natural}\,\tilde{Ξ}_{\mathrm{sp}}^{\natural}\;}
$$

**A right action on $\tilde{Ξ}_{\mathrm{sp}}$ is a left action on $\tilde{Ξ}_{\mathrm{sp}}^{\natural}$.** The side is not a property of the equation. It is a property of the field the equation is written on.

**The three properties.** Everything rests on them, and only the third is non-trivial.

| property | statement | residual |
|---|---|---|
| involutive | $\natural\circ\natural=\mathrm{id}$ | $0$ |
| $\mathbb{C}$-linear | $\natural(i\tilde{Ξ}_{\mathrm{sp}})=i\,\natural(\tilde{Ξ}_{\mathrm{sp}})$ | $0$ |
| anti-automorphism | $(ab)^{\natural}=b^{\natural}a^{\natural}$ | $2.6\times10^{-15}$ over $400$ random complex pairs |

The first makes $\natural$ invertible with $\natural^{-1}=\natural$. The third makes it **reverse the order of a product**. The second lets the mass, which is central, pass through untouched. An involution that preserved the order would identify the two sides; one that reverses the order exchanges them. $\natural$ reverses, so it exchanges.

**The proof is three symbols.** Applied to the two factors $\tilde{Ξ}_{\mathrm{sp}}$ and $D$,

$$
(\tilde{Ξ}_{\mathrm{sp}} D)^{\natural}=D^{\natural}\,\tilde{Ξ}_{\mathrm{sp}}^{\natural}.
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

**On an equation.** Take $\tilde{Ξ}_{\mathrm{sp}} D=m\xi$ with $m$ central, so $m^{\natural}=m$, and conjugate both sides:

$$
D^{\natural}\,\tilde{Ξ}_{\mathrm{sp}}^{\natural}=m\,\xi^{\natural}.
$$

The map $Ξ:(\tilde{Ξ}_{\mathrm{sp}},\xi)\mapsto(\tilde{Ξ}_{\mathrm{sp}}^{\natural},\xi^{\natural})$ is $\mathbb{C}$-linear, involutive and invertible, so it is a **bijection of solution sets** and not an inclusion:

$$
\{\tilde{Ξ}_{\mathrm{sp}}:\ \tilde{Ξ}_{\mathrm{sp}} D=m\xi\}\ \xrightarrow{\ Ξ\ }\ \{u:\ D^{\natural}u=m\,\xi^{\natural}\},
\qquad Ξ^{-1}=Ξ .
$$

Verified: a pair solved on the right at residual $2.0\times10^{-15}$ maps to a pair solved on the left at residual $1.1\times10^{-15}$, on all four basis solutions. Same solutions, relabelled.

**What the theorem does not say.** It does not say the two operators are equal. On $D=-5e_t+3i\vec e_x$,

$$
\bigl\lVert R_D-L_{D^{\natural}}\bigr\rVert_{\mathrm F}=8.4853\neq0 ,
$$

so the two arrays differ and neither may be substituted for the other at sight. What is equal is the pair of solution sets after renaming, not the operators.

**Where the theorem does not reach.** Three cases, and each is stated where it is used.

1. **More than one field.** The anti-automorphism reverses the whole order, $(\tilde{Ξ}_{\mathrm{sp}} D\xi)^{\natural}=\xi^{\natural}D^{\natural}\tilde{Ξ}_{\mathrm{sp}}^{\natural}$, residual $1.3\times10^{-14}$ over $200$ random triples. The two fields exchange places, so renaming alone does not suffice, and where the two fields are not the same object the reordering changes the statement. The bilinear identities of the integration articles stand in this case, and it is why they carry the superscript $R$ on the derivative.
2. **A carrier without $\natural$.** On a column $\tilde{Ξ}_{\mathrm{sp}}\in\mathbb{C}^{4}$ there is no natural conjugation, only the antilinear Dirac adjoint; on a space of functions of two variables, as in a star product, $\natural$ is not the involution in play. The theorem is a theorem about fields valued in $\mathbb{B}$.
3. **The side itself on display.** For the two-sided action $a\tilde{Ξ}_{\mathrm{sp}} b$, the mirror coupling, or the exchange of the two slots of a cell, conjugating the field destroys what is being displayed. There both factors stay in place and the side is named by position, or by $L_a$ and $R_a$.

**The consequence for the corpus.** Every equation that acts on a single biquaternion field is written on the left. The ones that would read as acting on the right are the same equations on the conjugate field, and the chiral pair is the instance: with $Ξ=\tilde{Ξ}_{\mathrm{sp}}^{\natural}$, the pair $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=m\tilde{Ξ}_{\mathrm{sp},R}$ is complete as written, both equations acting from the left, and $\natural$ is what separates them. Across the $404$ files and $10\,196$ display equations of the physics corpus no glyph names a side: the side is position, the conjugation is $\natural$, and the exchange is $N$.

## Conventions for Derivation

In this work, subscripts denote vector components, not partial derivatives as in the PDE convention; every partial derivative is written explicitly with $\partial$ followed by its variable, and no subscript is ever attached to the $\partial$ of a derivative. A subscript is therefore a component index, as in $v_x$ for the component of a velocity along an axis, or a label, as in $\tilde U_{\mathrm r}$; it never denotes a derivative. The derivative with respect to a coordinate is written $\partial/\partial R_\mu$, and in a fixed direction $\partial/\partial R_t$, $\partial/\partial R_x$, $\partial/\partial R_y$ or $\partial/\partial R_z$; a coordinate is never left under the $\partial$, so none of the abbreviated spellings occurs, and the rule admits no exception for a derivative, neither on a free index nor on any other.

**A subscript on an operator names its degree, its place or its argument.** The rule governs the derivative of a field, which names its variable after the $\partial$. It does not forbid a low mark on an operator that differentiates nothing: the chain boundary is $\partial_n:C_n\to C_{n-1}$, with the degree in the subscript, and a derivative taken along a vector is $\nabla_X$, with the vector. These are operator labels, in the sense of *Unit, Index and Notation Conventions*, §*The Subscripts*, and they stand as written.

**A variant of an operator is a label, and a chart is not a variant.** The gradient carries $\natural$ in the caret or a label low, $\tilde\nabla^{\natural}$ and $\tilde\nabla_{\mathrm{gco}}$, and it never takes a letter in the low slot for the coordinates it is read in. The Wick rotation is written on the coordinate, $r'_t\mapsto-i\tau$, which sends $R_t=i c r'_t$ to $R_t=c\tau$; the four terms of the sum are unchanged, only the sign of $\partial^2/\partial R_t^2$ moves, and the article that continues the coordinates says which chart it reads them in rather than marking the operator.

**The coordinate derivative is unhalved.** It is taken at the point, so it is written in the position letters, and it is defined by

$$
\frac{\partial}{\partial R_\mu}:=\frac{1}{c_\mu}\Bigl(\frac{\partial}{\partial r_\mu}-i\frac{\partial}{\partial r'_\mu}\Bigr),\qquad R_\mu=c_\mu\,(r_\mu+ir'_\mu),\quad c_t=c,\ \ c_k=1 .
$$

The $i$ is glued to the primed parameter: the derivative is taken with respect to the product $i r'_\mu$, not with respect to $r'_\mu$ with the $i$ pulled out in front, so the second term carries a minus and no reciprocal. The factor $c_\mu$ is the speed of light, the $c$ of the time coefficient and nothing else, and it is a dilation of that coefficient and not a dynamical quantity, so that $R_t$, $r_t$ and $r'_t$ are lengths in the same sense as $R_k$, $r_k$ and $r'_k$; it divides the whole derivative and not one of its two terms. It is the formal derivative on the complex coordinate; with $R_\mu$ and $\bar R_\mu$ read as independent, its unhalved normalization gives $\partial R_\mu/\partial R_\mu=2$ and $\partial R_\mu/\partial\bar R_\mu=0$. The conjugate derivative reverses the sign of the $i$ and nothing else,

$$
\frac{\partial}{\partial\bar R_\mu}:=\frac{1}{c_\mu}\Bigl(\frac{\partial}{\partial r_\mu}+i\frac{\partial}{\partial r'_\mu}\Bigr),
$$

with $\partial\bar R_\mu/\partial\bar R_\mu=2$.

**One derivative, two halves, and a sector keeps one half.** The two terms of the definition are the two halves of the coefficient, the unprimed term and the primed term. A sector sets one of them to zero, because the parameter it names is then not a coordinate of that slice, and what is left is the tangential derivative alone.

**On the material sector $\mathbb{M}_-$** the slice keeps $r'_t$ and $r_k$, so $\partial/\partial r_t=0$ and $\partial/\partial r'_k=0$, and the definition reads

$$
\frac{\partial}{\partial R_t}\Big|_{\mathbb{M}_-}=-\frac{i}{c}\frac{\partial}{\partial r'_t},
\qquad
\frac{\partial}{\partial R_k}\Big|_{\mathbb{M}_-}=\frac{\partial}{\partial r_k};
$$

**On the informational sector $\mathbb{M}_+$** the slice keeps $r_t$ and $r'_k$, so $\partial/\partial r'_t=0$ and $\partial/\partial r_k=0$, and the definition reads

$$
\frac{\partial}{\partial R_t}\Big|_{\mathbb{M}_+}=\frac{1}{c}\frac{\partial}{\partial r_t},
\qquad
\frac{\partial}{\partial R_k}\Big|_{\mathbb{M}_+}=-i\frac{\partial}{\partial r'_k}.
$$

**The two lines are the parent formula read twice, and the whole sector arithmetic is visible in them.** The $i$ sits on the time slot on the material sector and on the three space slots on the informational one; the $1/c$ never leaves the time slot on either; and the unprimed half and the primed half are never both present, because no sector keeps both parameters of one slot. A reader who substitutes a sector line for the parent formula gains no new object: the parent formula is the definition, and the sector lines are its restrictions. The material reading reproduces the kinetic term of §*The Hermitian Product, Its Form and Its Norm*, and a derivative carrying a numerical factor would rescale that term.

**The general element keeps the letter $Q$, and the mark is the same mark.** A generic element of the algebra is $\tilde Q$, and a display that names the coordinate slot of that element writes $\partial/\partial Q_\mu$ where this article writes $\partial/\partial R_\mu$; the slot is the same slot and the derivative the same derivative, the letter being the general element's instead of the point's. The gradient is taken at the point, so this article writes $R$; no second derivative is defined by the difference, and no factor of $c$ or of $i$ hangs on the choice of letter.

A derivative with respect to a variable that is not a coordinate is written the same way, its variable named in full: the Lagrangian derivative puts the function in the numerator, $\partial L/\partial u$, so that where a PDE text writes $L_u$ and $L_p$ the corpus writes $\partial L/\partial u$ and $\partial L/\partial p$; the second derivative has the same shape, $\partial^2 L/\partial u^2$. The function is named in the numerator whenever it is a letter of its own, as for a Lagrangian, a Hamiltonian or a generating function; the slashed form $\partial/\partial u$ is kept where the symbol is an operator or where the operand is a compound expression rather than a single letter. The time derivative $\partial/\partial R_t$ is the imaginary-time derivative, and the material time derivative is written out as $\partial/\partial r'_t$. The rule holds on every object of the series, whether the letter names an element of the algebra, an element-valued field, a kernel or an operator.

**These studies do not use the covariant index conventions: subscripts are not coordinate indices or derivatives, partial derivatives are written with explicit operators, and structural information is carried by the algebra of the objects themselves.** A caret marks a power or a name, never a frame slot: $e^\lambda$, $2^k$ and $(-1)^k$ are powers, and $\mathrm{Cl}^i$, $K^0$, $M_4^\sigma$ and $\mathbb{B}^\sigma$ are names; a coordinate, a field component, a basis vector, a frame cell and a sign symbol are written with a low index — $x_\mu$, $A_\mu$, $\vec e_i$, $L_{\mathrm{axf},e_\mu}R_{\mathrm{axf},e_\nu}$, $\varepsilon_{ijk}$ — and a contraction is written as an explicit sum that names the summed index — $\sum_\mu e_\mu\partial/\partial R_\mu$, $\sum_k\vec e_k A_k$, $\sum_{i,j}\varepsilon_{ijk}A_iB_j$ — never as a repeated index left to the summation convention. No index is summed by convention: an index that appears twice is summed only when a $\sum$ names it, and the shorthand with no sum is not used. A spatial matrix written with a raised index, whether a Pauli matrix or a stress component, is the same error as a raised coordinate: it hides which basis is contracted, and the index goes low.

### The Derivative Marks

**No dot.** No derivative is written with a dot. The total derivative with respect to a parameter is written with a fraction and the parameter named: $\frac{d}{dr'_t}$ for material time, $\frac{d}{dr_t}$ for informational time, $\frac{d}{d\tau}$ for proper time, $\frac{d}{dr'_{\mathrm{ret},t}}$ for retarded time; inline, the same derivative is written $d\xi/dr'_t$. The partial derivative is written $\frac{\partial}{\partial r'_t}$ or, inline, $\partial/\partial r'_t$. A higher derivative is written $\frac{d^2}{d{r'_{t}}^2}$, $\frac{\partial^2}{\partial {r'_{t}}^2}$. The derivative binds to its whole argument, so a power is written outside a bracket, $\left(\frac{d\xi}{dr'_t}\right)^2$, never as $\frac{d\xi^2}{dr'_t}$.

**The prime marks the imaginary part, and nothing else.** The prime belongs to a coefficient: it marks the imaginary part of a complex number, $r'_\mu$ of $R_\mu = c_\mu(r_\mu + ir'_\mu)$, the part that carries the $i$. It is not a derivative mark, and it is not a label of an element, a field or a coupling. A derivative is written with $d$ or $\partial$ and its variable named: a function of one variable is differentiated as $df/dx$, never as $f'$, and a second derivative as $d^2f/dx^2$ or $\partial^2f/\partial x^2$, never with a repeated prime or a repeated subscript. The complex time is $Q_t = c r_t+i c r'_t$: its real part $c r_t$ is the informational time and its imaginary part $c r'_{t}$ the material time, with $q_t = c r_t$ and $q'_t = c r'_{t}$. The prime on $r'_t$ marks the coefficient that carries the $i$, exactly as the primes on $r'_{x},r'_{y},r'_{z}$ mark the imaginary spatial coefficients. Carried by an element glyph, the same prime names the element assembled from the primed coefficients, $\tilde q' = q'_t\,e_t+q'_x\vec e_x+q'_y\vec e_y+q'_z\vec e_z$ in $\tilde Q = \tilde q+i\tilde q'$, the antiquaternion part; it is the coefficient prime read on the whole glyph, not a label of a transformed or distinguished element.

**The prime is not a frame, source or field label.** The primed spatial coordinates $r'_{x},r'_{y},r'_{z}$ are the imaginary parts of the spatial coefficients, $R_x=r_x+i r'_{x}$, $R_y=r_y+i r'_{y}$, $R_z=r_z+i r'_{z}$; the prime names the coordinate that carries the $i$. The primed time $r'_t$ is the imaginary part of $R_t=c r_t+i c r'_t$, and the unprimed $r_t$ its real part; the factor $c$ carries both halves onto the same footing, so the primed time is a time and not a length. Outside these uses the prime is not written. A transformed frame is named by a subscript, never by $r'_{x}$ or $r'_t$; a source point, a second point and an integration variable take a numeric or role subscript, never a prime; an element, field, connection, curvature, current, state, coupling, group or map that is transformed or distinguished takes a numeric or role subscript, never a prime; and a derivative is written $df/dx$, never $f'$. The glyph $r'_{x}$ cannot be both the imaginary coordinate and a source or boosted coordinate: where both are needed, the source point or the frame takes the subscript.

**Labels that are not derivatives.** The second Lorentz label is written $\bar l$, and a spinor index of the conjugate representation is written $\bar\alpha$; the bar on an index marks the conjugate spinor. The conjugate matrix is $\bar\Pi$. These are labels, not derivatives.

**The scope mark.** In geometric calculus the factor differentiated is marked with an underline, $\underline{\partial}(AB)=\underline{\partial}A\,B+\underline{A}\,\underline{\partial}B$, not with a dot.

**The two derivative operators of the series** are the **biquaternionic gradient** $\tilde\nabla$ and the **d'Alembertian** $\Box$; every other partial derivative is written with $\partial$.

### The Gradient

The coordinate derivative is written $\partial/\partial R_\mu$ and is defined by $\partial/\partial R_\mu:=\frac{1}{c_\mu}\bigl(\partial/\partial r_\mu-i\,\partial/\partial r'_\mu\bigr)$, with $R_\mu=c_\mu(r_\mu+ir'_\mu)$, as fixed in §*Conventions for Derivation*. The **biquaternionic gradient** is the element-valued operator

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial R_\mu}=e_t\frac{\partial}{\partial R_t}+\vec e_x\frac{\partial}{\partial R_x}+\vec e_y\frac{\partial}{\partial R_y}+\vec e_z\frac{\partial}{\partial R_z},
$$

whose tilde marks its scalar part beside its vector part, with its **quaternion conjugate**, the involution of the norm,

$$
\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial R_\mu}
=e_t\frac{\partial}{\partial R_t}-\vec e_x\frac{\partial}{\partial R_x}-\vec e_y\frac{\partial}{\partial R_y}-\vec e_z\frac{\partial}{\partial R_z},
\qquad \varepsilon=(1,-1,-1,-1).
$$

It is this conjugate and no other that the series composes with (*Biquaternion Analysis*, §*The Biquaternionic Gradient*, §*The Quaternion Conjugate of the Gradient*). Write $\nabla=\sum_k\vec e_k\,\partial/\partial R_k$ for the spatial gradient, with divergence $\nabla\cdot\vec Q_{\mathrm f}$ and curl $\nabla\times\vec Q_{\mathrm f}$, and $\Delta_Q=\partial^2/\partial R_x^2+\partial^2/\partial R_y^2+\partial^2/\partial R_z^2$ for the Laplacian in the three vector coordinates.

**One operator, two readings, and no third.** The eight real parameters of the algebra are the four $r_\mu$ and the four $r'_\mu$, and a sector is the setting of four of them to zero. The material sector $\mathbb{M}_-$ keeps the imaginary time $c r'_t$ together with the three real space parameters $r_k$; the informational sector $\mathbb{M}_+$ keeps the real time $c r_t$ together with the three imaginary space parameters $r'_k$. The two keep complementary halves, and neither keeps a part of the other's half. The gradient is one sum in both readings, and what a sector fixes is the **value of the coefficients**, not the shape of the operator: on $\mathbb{M}_-$ the coordinates are $R_t=i c r'_t$ and $R_k=r_k$, so $\partial/\partial R_t=-\frac{i}{c}\,\partial/\partial r'_t$ and $\partial/\partial R_k=\partial/\partial r_k$; on $\mathbb{M}_+$ they are $R_t=c r_t$ and $R_k=i r'_k$, so $\partial/\partial R_t=\frac{1}{c}\,\partial/\partial r_t$ and $\partial/\partial R_k=\frac{1}{i}\,\partial/\partial r'_k=-i\,\partial/\partial r'_k$. The basis $e_\mu$, the four terms of the sum, the tilde and the $\natural$ belong to the operator and are untouched by either substitution. A sector is a slice and not a variant, and no article of the series defines a second gradient.

**What the sector substitution moves, and what it leaves.** The substitution moves one thing only: the factor that stands between a derivative symbol and its coordinate. On $\mathbb{M}_-$ that factor is $-i/c$ on the time slot and $1$ on the three space slots; on $\mathbb{M}_+$ it is $1/c$ on the time slot and $-i$ on the three space slots. Every sign below follows from those four numbers and from nothing else, so a reader who has them can reconstruct any formula in this article without consulting a table.

**The sum is written.** The gradient is a sum, and the sum is always spelled out. The shorthand $\vec e_k\partial/\partial R_k$ is not used, because it repeats the index without summing it; the same holds for every contraction of a basis vector, a frame cell or a field component with a derivative. An index that appears twice is summed only where a $\sum$ names it.

**The conjugates of the gradient.** The gradient is an operator, and the marks are read on its units at fixed coordinate: the derivative symbols are held fixed and only the units are conjugated. This fixes the scope of the star, and it is not a claim that $\partial/\partial R_\mu$ is real; the unhalved derivative of §*Conventions for Derivation* is complex, and on an element-valued field the star is coefficientwise, carried through the derivative by $\partial/\partial\bar R_\mu$ rather than by $\partial/\partial R_\mu$. Read on the units, the quaternion conjugation reverses the three spatial units, and so does the Hermitian conjugation, so the two act on the gradient alike,

$$
\tilde\nabla^{*}=\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial R_\mu},
\qquad \overline{\tilde\nabla}=\tilde\nabla .
$$

**The forms stay four, the norms are two.** The four forms of *Product and Form Conventions*, §*The Involutions and the Four Forms* remain four distinct conventions here, because each conjugates its own slot: the quaternionic form conjugates the first argument and the Hermitian form the second, so on a general second argument they are not the same statement. But read at the two equal arguments they give two operators, the Hermitian norm coinciding with the quaternionic bilinear norm, $\langle\tilde\nabla\rangle_{*}=\langle\tilde\nabla\rangle_{\natural}$, and the Krein norm with the plain bilinear norm, $\langle\tilde\nabla\rangle_{\natural*}=\langle\tilde\nabla\rangle$. The four subsections below carry the four forms, and their norms are the two operators $\Box$ and $\partial^2/\partial R_t^2-\Delta_Q$.

**On the material sector $\mathbb{M}_-$**, where $R_t=i c r'_t$ and $R_k=r_k$, the time derivative reads $\partial/\partial R_t=-\frac{i}{c}\,\partial/\partial r'_t$, the three space derivatives are the physical ones, $\partial/\partial R_k=\partial/\partial r_k$, the spatial gradient is the physical $\nabla=\sum_k\vec e_k\,\partial/\partial r_k$, its divergence and its curl are the ordinary divergence $\nabla\cdot\vec Q_{\mathrm f}$ and curl $\nabla\times\vec Q_{\mathrm f}$ of the field, the Laplacian in the vector coordinates collapses to the physical $\Delta_Q=\sum_k\partial^2/\partial r_k^2=\Delta$, and the gradient is

$$
\tilde\nabla\big|_{\mathbb{M}_-}=-\frac{i}{c}\,e_t\frac{\partial}{\partial r'_t}+\sum_k\vec e_k\frac{\partial}{\partial r_k},
\qquad
\tilde\nabla^{\natural}\big|_{\mathbb{M}_-}=-\frac{i}{c}\,e_t\frac{\partial}{\partial r'_t}-\sum_k\vec e_k\frac{\partial}{\partial r_k},
$$

the conjugate carrying the three minus signs on the space slots and none on the time slot, because $\varepsilon=(1,-1,-1,-1)$ and the substitution touches the coefficients only. This is the reading in which the series does its work: the time term is imaginary and the space terms are real, so a real field has a purely imaginary time derivative and real space derivatives, and that one fact is what turns the gradient into the Maxwell pair and the chiral pair below.

**On the informational sector $\mathbb{M}_+$**, where $R_t=c r_t$ and $R_k=i r'_k$, the time derivative is real, $\partial/\partial R_t=\frac{1}{c}\,\partial/\partial r_t$, the three space derivatives carry $\frac{1}{i}=-i$, so $\partial/\partial R_k=-i\,\partial/\partial r'_k$, and the roles are exchanged: the time slot is now the real one and the three space slots are now the imaginary ones. The three spatial operations are those of the general definitions, read on the sector and marked with the sector and with nothing else: $\nabla|_{\mathbb{M}_+}=\sum_k\vec e_k\,\partial/\partial r'_k$ and $\Delta|_{\mathbb{M}_+}=\sum_k\partial^2/\partial {r'_k}^2$, the sum spelled out as everywhere and the mark naming the slice and not a chart. With $\partial/\partial R_k=-i\,\partial/\partial r'_k$ the two carry one factor $-i$ and one factor $(-i)^2=-1$ respectively, so $\Delta_Q|_{\mathbb{M}_+}=-\Delta|_{\mathbb{M}_+}$, and the gradient is

$$
\tilde\nabla\big|_{\mathbb{M}_+}=\frac{1}{c}\,e_t\frac{\partial}{\partial r_t}-i\sum_k\vec e_k\frac{\partial}{\partial r'_k},
\qquad
\tilde\nabla^{\natural}\big|_{\mathbb{M}_+}=\frac{1}{c}\,e_t\frac{\partial}{\partial r_t}+i\sum_k\vec e_k\frac{\partial}{\partial r'_k},
$$

the conjugate again moving the three minus signs onto the space slots and leaving the time slot alone. The two displays are the same operator, and the difference between them is the position of the $i$: on $\mathbb{M}_-$ it sits on the time coefficient, where it squares to $(i c)^2=-c^2$; on $\mathbb{M}_+$ it sits on the three space coefficients, where it squares to $i^2=-1$ three times. Reading the two lines term by term, the time slot loses its $-i/c$ and gains a $1/c$, the space slots lose their $1$ and gain a $-i$, and no other difference exists.

**The two readings differ in the sign of the second derivatives, and the difference is the signature.** Because $(i c)^2=-c^2$ on $\mathbb{M}_-$ and $i^2=-1$ on $\mathbb{M}_+$, the time second derivative is negative on $\mathbb{M}_-$ and positive on $\mathbb{M}_+$, while the three space second derivatives are positive on $\mathbb{M}_-$ and negative on $\mathbb{M}_+$. The material reading is therefore the sign pattern $(-,+,+,+)$ on the quadruple of second derivatives and the informational reading the pattern $(+,-,-,-)$, and the two are negatives of each other. That overall sign is not a convention to be chosen: it is the signature of the slice, read on the operator, and it is why the d'Alembertian of §*The Quaternionic Bilinear Product, Its Form and Its Norm* carries the time term first and the spatial Laplacian second on the material sector and the opposite overall sign on the informational one. A series that used one reading for the equations of motion and the other for the Lagrangian would carry a spurious minus through every action; the corpus does not, and the rule is that the sector is fixed once per article and the operator follows it.

**A continuation is a change of coordinate, not of operator.** The Wick rotation $r'_t\mapsto-i\tau$ sends $R_t=i c r'_t$ to $R_t=c\tau$, and the four terms of $\tilde\nabla=\sum_\mu e_\mu\partial/\partial R_\mu$ are untouched, each being the derivative with respect to the same coordinate under the same name; the list of coordinates is now $(c\tau,r_x,r_y,r_z)$, all real. What the continuation changes is one sign, $\partial^2/\partial R_t^2|_{\mathbb{M}_-}=-c^{-2}\partial^2/\partial {r'_{t}}^2$ on the material sector against $+\partial^2/\partial x_4^2$ on the real-quaternion slice, and that sign is the whole of the difference between the hyperbolic $\Box$ and the elliptic operator. So the gradient read on the continued slice is $\tilde\nabla$, and the d'Alembertian read there is $\Box$; the substitution is written on the *coordinate*, $r'_t\mapsto-i\tau$, and never on the operator.

### The Plain Bilinear Product, Its Form and Its Norm

**The product.** The general plain bilinear product is one of the four of *Product and Form Conventions*, §*The Twelve Products and Their Names*. On the gradient, with an element-valued field $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$, it is read with $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and $\vec e_j \vec e_k=-\delta_{jk}e_t+\epsilon_{jkl}\vec e_l$, so that the three spatial units carry the field back onto the scalar unit,

$$
\tilde\nabla\tilde Q_{\mathrm f}=\Bigl(\frac{\partial}{\partial R_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial}{\partial R_t}\vec Q_{\mathrm f}+\nabla Q_{\mathrm{f}t}+\nabla\times\vec Q_{\mathrm f} .
$$

A **product** is algebra-valued, and this one holds the divergence, the gradient and the curl of the field in a single object; for the field strength $\tilde F$ the equation $\tilde\nabla\tilde F=-\sqrt{\mu}\,\tilde J$, with $\tilde J=ic\rho\,e_t+\vec J$, is the series' Maxwell equation. **On the material sector** the same product is read with $\partial/\partial R_t=-\frac{i}{c}\,\partial/\partial r'_t$ and $\nabla$ the physical spatial gradient, so the space part is unchanged and the time part gains the factor $-i/c$:

$$
\tilde\nabla\tilde Q_{\mathrm f}\big|_{\mathbb{M}_-}=\Bigl(-\frac{i}{c}\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}-\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t-\frac{i}{c}\frac{\partial\vec Q_{\mathrm f}}{\partial r'_t}+\nabla Q_{\mathrm{f}t}+\nabla\times\vec Q_{\mathrm f} .
$$

**On the informational sector** the same product is read with $\partial/\partial R_t=\frac{1}{c}\,\partial/\partial r_t$ and with the three spatial derivatives carrying $-i$, so the whole spatial part is multiplied by $-i$ and the time part is real:

$$
\tilde\nabla\tilde Q_{\mathrm f}\big|_{\mathbb{M}_+}=\Bigl(\frac{1}{c}\frac{\partial Q_{\mathrm{f}t}}{\partial r_t}+i\,\nabla|_{\mathbb{M}_+}\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{1}{c}\frac{\partial\vec Q_{\mathrm f}}{\partial r_t}-i\,\nabla|_{\mathbb{M}_+}Q_{\mathrm{f}t}-i\,\nabla|_{\mathbb{M}_+}\times\vec Q_{\mathrm f} .
$$

The two displays are one product read on two slices, and they differ in the way the gradient differs: the divergence and the curl appear with their own sign on $\mathbb{M}_-$ and with an $i$ and a change of sign on $\mathbb{M}_+$, because $-i$ factors out of three spatial derivatives and multiplies each of them once. Nothing is redefined and no second product is introduced: a reader who substitutes the coefficients into the general display above obtains each line, and a reader who does not substitute keeps the general display, which is the operator's own form and the one the definition fixes.

**The symmetric and antisymmetric parts.** Read with two arguments, the product splits as in *Product and Form Conventions*, §*The Twelve Products and Their Names*. The half-sum keeps the form as its scalar part,

$$
\tilde\nabla\bullet\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla\tilde Q_{\mathrm f}+\tilde Q_{\mathrm f}\tilde\nabla\bigr)=\Bigl[\frac{\partial}{\partial R_t}Q_{\mathrm{f}t}-(\nabla,\vec Q_{\mathrm f})\Bigr]e_t+\frac{\partial}{\partial R_t}\vec Q_{\mathrm f}+Q_{\mathrm{f}t}\nabla=\Bigl[\frac{\partial}{\partial R_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f}\Bigr]e_t+\frac{\partial}{\partial R_t}\vec Q_{\mathrm f}+\nabla Q_{\mathrm{f}t} ,
$$

and the half-difference is the curl,

$$
\tilde\nabla\wedge\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla\tilde Q_{\mathrm f}-\tilde Q_{\mathrm f}\tilde\nabla\bigr)=\tfrac12\bigl(\nabla\times\vec Q_{\mathrm f}+\nabla\times\vec Q_{\mathrm f}\bigr)=\nabla\times\vec Q_{\mathrm f} ,
$$

a pure vector, so the plain form carries the whole scalar content of the product. Throughout these four subsections the pair $(\nabla,\vec X)$ is read as the divergence $\nabla\cdot\vec X$ and $X\nabla$ as the gradient $\nabla X$, the derivative acting on the coefficient it multiplies, and the coordinate formulas substituted are those of *Product and Form Conventions*, §*The Twelve Products and Their Names*.

**The form.** The **plain form** is the scalar part of the product read in two arguments,

$$
\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle=\mathrm{Sc}(\tilde\nabla\tilde Q_{\mathrm f})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial}{\partial R_\mu}Q_{\mathrm{f}\mu}=\frac{\partial}{\partial R_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f} ,
$$

a scalar, the **contraction** of the derivative with the field in the sign vector $\varepsilon$. **On the material sector** it is $-\frac{i}{c}\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}-\nabla\cdot\vec Q_{\mathrm f}$, the time slot imaginary and the divergence real. **On the informational sector** it is $\frac{1}{c}\frac{\partial Q_{\mathrm{f}t}}{\partial r_t}+i\,\nabla|_{\mathbb{M}_+}\cdot\vec Q_{\mathrm f}$, the time slot real and the divergence imaginary, the divergence entering with the sign opposite to the quaternionic form's below — the same exchange of signs as between the two products, read on the scalar part alone.

The plain form is the **contraction** in the sense of §*A contraction is a form, never an index*: the derivative meets the field component of its own name, the time with the time and each space with its space, and the sign it carries is $\varepsilon_\mu$, which is why the time term enters with a plus and the three space terms with a minus. On the material sector that sign vector is also the signature, because there the three space coefficients are real and the time coefficient imaginary; on the informational sector it is not, and the reader who wants the signature takes it from the operator and not from the form.

**The norm.** The norm is defined with the form, as that form at its two equal arguments:

$$
\langle\tilde\nabla\rangle=\langle\tilde\nabla,\tilde\nabla\rangle=\mathrm{Sc}(\tilde\nabla\tilde\nabla)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial^2}{\partial R_\mu^2}=\frac{\partial^2}{\partial R_t^2}-\Delta_Q ,
$$

the cross terms cancelling. **On the material sector** it is $-c^{-2}\frac{\partial^2}{\partial {r'_{t}}^2}-\Delta$, which is neither the wave operator $\partial^2/\partial {r'_{t}}^2-c^2\Delta$ nor the series' d'Alembertian; on this sector the d'Alembertian is $\Delta-c^{-2}\partial^2/\partial {r'_{t}}^2$ (§*The Quaternionic Bilinear Product, Its Form and Its Norm*). **On the informational sector** the same norm is $c^{-2}\frac{\partial^2}{\partial r_t^2}+\Delta|_{\mathbb{M}_+}$, with the time term positive and the primed Laplacian positive as well, because $\partial^2/\partial R_t^2$ gains $+c^{-2}$ and $-\Delta_Q$ gains $+\Delta|_{\mathbb{M}_+}$; it is the negative of the material reading, as the sign pattern of §*The Gradient* requires, and it is neither the wave operator nor the d'Alembertian either.

### The Quaternionic Bilinear Product, Its Form and Its Norm

**The product.** The general quaternionic bilinear product is the second of the four of *Product and Form Conventions*, §*The Twelve Products and Their Names*; on the gradient it is $\tilde\nabla^{\natural}\tilde Q_{\mathrm f}$, the conjugate derivative, read with the same rules, the three spatial units now carrying the field back onto the scalar unit with the opposite sign,

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}=\Bigl(\frac{\partial}{\partial R_t}Q_{\mathrm{f}t}+\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial}{\partial R_t}\vec Q_{\mathrm f}-\nabla Q_{\mathrm{f}t}-\nabla\times\vec Q_{\mathrm f} .
$$

**On the material sector** the same substitution $\partial/\partial R_t=-\frac{i}{c}\,\partial/\partial r'_t$ applies with $\nabla$ the physical gradient, the space part unchanged and the time part gaining $-i/c$:

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}\big|_{\mathbb{M}_-}=\Bigl(-\frac{i}{c}\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}+\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t-\frac{i}{c}\frac{\partial\vec Q_{\mathrm f}}{\partial r'_t}-\nabla Q_{\mathrm{f}t}-\nabla\times\vec Q_{\mathrm f} .
$$

**On the informational sector** the substitution is $\partial/\partial R_t=\frac{1}{c}\,\partial/\partial r_t$ with $-i$ on the three space derivatives, and the space signs turn over once more, because the conjugate already carries them and the coefficient carries an $i$:

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}\big|_{\mathbb{M}_+}=\Bigl(\frac{1}{c}\frac{\partial Q_{\mathrm{f}t}}{\partial r_t}-i\,\nabla|_{\mathbb{M}_+}\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{1}{c}\frac{\partial\vec Q_{\mathrm f}}{\partial r_t}+i\,\nabla|_{\mathbb{M}_+}Q_{\mathrm{f}t}+i\,\nabla|_{\mathbb{M}_+}\times\vec Q_{\mathrm f} .
$$

Compared with the plain product on the same slice, the two lines differ exactly as the general displays do, in the sign of the divergence and in the sign of the gradient and the curl, which is the statement that the conjugate derivative is not a second operator but the same operator with $\varepsilon$ applied to its units.

**The symmetric and antisymmetric parts.** The half-sum is central and is the quaternionic form itself,

$$
\tilde\nabla\bullet_{\natural}\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde Q_{\mathrm f}+\tilde Q_{\mathrm f}^{\natural}\tilde\nabla\bigr)=\Bigl[\frac{\partial}{\partial R_t}Q_{\mathrm{f}t}+(\nabla,\vec Q_{\mathrm f})\Bigr]e_t=\Bigl(\frac{\partial}{\partial R_t}Q_{\mathrm{f}t}+\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t ,
$$

and the half-difference is the vector part of the product,

$$
\tilde\nabla\wedge_{\natural}\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde Q_{\mathrm f}-\tilde Q_{\mathrm f}^{\natural}\tilde\nabla\bigr)=\frac{\partial}{\partial R_t}\vec Q_{\mathrm f}-Q_{\mathrm{f}t}\nabla-\nabla\times\vec Q_{\mathrm f}=\frac{\partial}{\partial R_t}\vec Q_{\mathrm f}-\nabla Q_{\mathrm{f}t}-\nabla\times\vec Q_{\mathrm f} .
$$

**The form.** The **quaternionic form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde Q_{\mathrm f})=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial}{\partial R_\mu}Q_{\mathrm{f}\mu}=\frac{\partial}{\partial R_t}Q_{\mathrm{f}t}+\nabla\cdot\vec Q_{\mathrm f} ,
$$

a scalar, the **contraction** of the derivative with the field, all four signs plus because the conjugate derivative already carries $\varepsilon$; it differs from the plain form by the three signs of $\varepsilon$, which are **computed from the product** $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and not assumed. **On the material sector** it is $-\frac{i}{c}\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}+\nabla\cdot\vec Q_{\mathrm f}$, the divergence entering with a plus where the plain form carries a minus. **On the informational sector** it is $\frac{1}{c}\frac{\partial Q_{\mathrm{f}t}}{\partial r_t}-i\,\nabla|_{\mathbb{M}_+}\cdot\vec Q_{\mathrm f}$, and the two sector readings differ from each other as the two forms differ from each other: the time slot changes its factor, the divergence changes its sign and its coefficient, and no term of the contraction is left unaccounted for.

**The norm, and the definition of the d'Alembertian.** The norm is defined with the form, as that form at its two equal arguments, and the two orders of the product agree:

$$
\Box=\langle\tilde\nabla\rangle_{\natural}=\langle\tilde\nabla,\tilde\nabla\rangle_{\natural}
=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{\natural})
=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial R_\mu^2}=\frac{\partial^2}{\partial R_t^2}+\Delta_Q .
$$

**This is the definition of the d'Alembertian**: the quaternionic norm of the gradient, an operator on the whole algebra, one and the same before any sector is named (*The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*). The coordinates $R_\mu$ are those of the algebra and are complex in general; the operator is $\partial^2/\partial R_t^2+\Delta_Q$ whatever the sector, and it is **scalar**: it multiplies by $e_t$ and acts coefficient by coefficient, $\Box\tilde Q_{\mathrm f}=\sum_\mu(\Box Q_{\mathrm{f}\mu})e_\mu$. It is the identity above, and not the $i c r'_t$ substitution, that fixes it, and **no article of the series defines a second d'Alembertian**; no mass-term sign is left to a local convention.

**The special case of the material sector.** On $\mathbb{M}_-$ the coordinates are the material ones, $R_t=i c r'_t$ and $R_k=r_k$, and the $i c r'_t$ substitution flips the sign of the time second derivative, $\partial^2/\partial R_t^2=-c^{-2}\,\partial^2/\partial {r'_{t}}^2$, so the same operator reads

$$
\Box\big|_{\mathbb{M}_-}=\frac{\partial^2}{\partial R_t^2}+\Delta=\Delta-c^{-2}\,\frac{\partial^2}{\partial {r'_{t}}^2},
$$

a plus on the spatial part and a minus on the time part. On $\mathbb{M}_-$, where the series does its work, this reading is the **series convention**, used by the Klein–Gordon article, the Dirac article, the dedicated article *The Biquaternion D'Alembertian and Its Green's Functions*, and the great majority of the series. **The $i c r'_t$ substitution is a statement about the material sector, not about the operator**, which in every case is $\partial^2/\partial R_t^2+\Delta_Q$; its signature is not a property of the operator but of the **slice** it is read on, since on a named subspace some of the $Q_\mu$ are purely imaginary. The operator is one, and every article writes it the same way.

**The special case of the informational sector.** On $\mathbb{M}_+$ the coordinates are the informational ones, $R_t=c r_t$ and $R_k=i r'_k$, and the substitution works the other way round: the time second derivative gains a plus, $\partial^2/\partial R_t^2=c^{-2}\,\partial^2/\partial r_t^2$, while each of the three space second derivatives gains a minus, $\partial^2/\partial Q_k^2=-\partial^2/\partial {r'_k}^2$, so the same operator reads

$$
\Box\big|_{\mathbb{M}_+}=\frac{\partial^2}{\partial R_t^2}+\Delta_Q=\frac{1}{c^2}\frac{\partial^2}{\partial r_t^2}-\Delta|_{\mathbb{M}_+},
$$

a plus on the time part and a minus on the spatial part, the sign pattern $(+,-,-,-)$ and the negative of the material line above. The two sector lines are one operator and the two signatures are one signature read twice: the material sector keeps the four parameters $r'_t$ and $r_k$, the informational sector keeps the four complementary ones $r_t$ and $r'_k$, and a slice that keeps a coordinate carrying an $i$ turns one sign while a slice that keeps the same coordinate without one does not. The informational reading is the one the state space $\mathbb{M}_+$ is written in, and the operator it carries is $\Box$ with the time term positive; a reader who moves an equation from one sector to the other moves one overall sign and nothing else.

### The Hermitian Product, Its Form and Its Norm

**The product.** The general plain sesquilinear product is the third of the four of *Product and Form Conventions*, §*The Twelve Products and Their Names*; it is the plain product applied to the **conjugated** field $\tilde Q_{\mathrm f}^{*}=\bar Q_{\mathrm{f}t}e_t-\overline{\vec Q_{\mathrm f}}$, so that on the gradient it is $\tilde\nabla\tilde Q_{\mathrm f}^{*}$, conjugate-linear in the field while the first slot stays $\mathbb{C}$-linear,

$$
\tilde\nabla\tilde Q_{\mathrm f}^{*}=\Bigl(\frac{\partial}{\partial R_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{\partial}{\partial R_t}\overline{\vec Q_{\mathrm f}}+\nabla\bar Q_{\mathrm{f}t}-\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**On the material sector** the product is read with $\partial/\partial R_t=-\frac{i}{c}\,\partial/\partial r'_t$ and the physical gradient, so the conjugated field keeps its coefficients and only the factors of the derivatives change:

$$
\tilde\nabla\tilde Q_{\mathrm f}^{*}\big|_{\mathbb{M}_-}=\Bigl(-\frac{i}{c}\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t+\frac{i}{c}\frac{\partial\overline{\vec Q_{\mathrm f}}}{\partial r'_t}+\nabla\bar Q_{\mathrm{f}t}-\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

Two signs have moved relative to the plain product, and both for one reason: the conjugation reversed the sign of the vector part of the field before any derivative met it, so the vector term of the scalar slot carries a plus, and the time derivative of the vector slot carries a plus as well. **On the informational sector** the same product is read with $\partial/\partial R_t=\frac{1}{c}\,\partial/\partial r_t$ and $-i$ on the three space derivatives:

$$
\tilde\nabla\tilde Q_{\mathrm f}^{*}\big|_{\mathbb{M}_+}=\Bigl(\frac{1}{c}\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r_t}-i\,\nabla|_{\mathbb{M}_+}\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{1}{c}\frac{\partial\overline{\vec Q_{\mathrm f}}}{\partial r_t}-i\,\nabla|_{\mathbb{M}_+}\bar Q_{\mathrm{f}t}+i\,\nabla|_{\mathbb{M}_+}\times\overline{\vec Q_{\mathrm f}} .
$$

The pair of sector lines is what makes the Hermitian product usable, because its scalar slot is the one that survives the conjugate transpose: the two readings are two ways of writing one density, the material one with an imaginary time derivative and a real divergence, the informational one with a real time derivative and an imaginary divergence.

**The symmetric and antisymmetric parts.** Under the conjugate transpose the half-sum is central and is the Hermitian form itself,

$$
\tilde\nabla\bullet_{*}\tilde Q_{\mathrm f}=\mathrm{Sc}(\tilde\nabla\tilde Q_{\mathrm f}^{*})=\Bigl[\frac{\partial}{\partial R_t}\bar Q_{\mathrm{f}t}+(\nabla,\overline{\vec Q_{\mathrm f}})\Bigr]e_t=\Bigl(\frac{\partial}{\partial R_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t ,
$$

and the half-difference is the vector part,

$$
\tilde\nabla\wedge_{*}\tilde Q_{\mathrm f}=\mathrm{Vect}(\tilde\nabla\tilde Q_{\mathrm f}^{*})=-\frac{\partial}{\partial R_t}\overline{\vec Q_{\mathrm f}}+\bar Q_{\mathrm{f}t}\nabla-\nabla\times\overline{\vec Q_{\mathrm f}}=-\frac{\partial}{\partial R_t}\overline{\vec Q_{\mathrm f}}+\nabla\bar Q_{\mathrm{f}t}-\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**The form.** The **Hermitian form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{*}=\mathrm{Sc}(\tilde\nabla\tilde Q_{\mathrm f}^{*})=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial}{\partial R_\mu}\bar Q_{\mathrm{f}\mu}=\frac{\partial}{\partial R_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}} ,
$$

a scalar, the **contraction** of the derivative with the **conjugated** field, all four signs plus because the conjugation and the derivative together supply the sign vector. Taken on the scalar field it gives the **kinetic density**, the scalar part of the product of the two conjugated gradients,

$$
\mathrm{Sc}\bigl[(\tilde\nabla^{\natural}\tilde{Ξ}^{*})(\tilde\nabla\tilde{Ξ})\bigr]=\sum_{\mu\in\{t,x,y,z\}}\frac{\partialΞ^{*}}{\partial R_\mu}\frac{\partialΞ}{\partial R_\mu} ,
$$

in which the conjugate stands on the first factor and no absolute value is taken; the two time derivatives are imaginary on the material sector, so that scalar part is $-c^{-2}\lvert\partial\xi_{\mathrm{scl}}/\partial r'_t\rvert^2+\lvert\nabla\xi_{\mathrm{scl}}\rvert^2$, and the kinetic term the series writes is

$$
\mathcal L_{\mathrm{kin}}=-\mathrm{Sc}\bigl[(\tilde\nabla^{\natural}\tilde{Ξ}^{*})(\tilde\nabla\tilde{Ξ})\bigr]=\frac{1}{c^2}\Bigl|\frac{\partial\xi_{\mathrm{scl}}}{\partial r'_t}\Bigr|^2-\lvert\nabla\xi_{\mathrm{scl}}\rvert^2 ,
$$

**On the informational sector** the sum runs over the same four terms with the other factors, and since the time factor is real and each of the three space factors is $-i$, the time slot contributes $+c^{-2}$ and the three space slots $-1$; the scalar part is then $c^{-2}\lvert\partial\xi_{\mathrm{scl}}/\partial r_t\rvert^2-\lvert\nabla|_{\mathbb{M}_+}\xi_{\mathrm{scl}}\rvert^2$ and the kinetic term is its negative, $-c^{-2}\lvert\partial\xi_{\mathrm{scl}}/\partial r_t\rvert^2+\lvert\nabla|_{\mathbb{M}_+}\xi_{\mathrm{scl}}\rvert^2$. The overall sign belongs to the operator and not to the density, and an article that writes a Lagrangian on $\mathbb{M}_+$ fixes the sign of its own action there, exactly as the Klein–Gordon article fixes it on $\mathbb{M}_-$; what no article may do is take the density from one sector and the operator from the other.

the kinetic density of the Klein–Gordon article (*Hamiltonian Field Theory in Biquaternionic Form*). **On the material sector** the form itself is $-\frac{i}{c}\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}$, a real divergence beside an imaginary time derivative. **On the informational sector** it is $\frac{1}{c}\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r_t}-i\,\nabla|_{\mathbb{M}_+}\cdot\overline{\vec Q_{\mathrm f}}$, an imaginary divergence beside a real time derivative. The Hermitian form and the plain form agree on $\mathbb{M}_-$ up to the sign of the divergence, which is the sign that separates the two products; on $\mathbb{M}_+$ they agree up to that same sign, and a reader who has the two sector lines of §*The Gradient* passes between them without a further convention.

**The norm.** The norm is defined with the form, as that form at its two equal arguments. By §*The Gradient*, $\tilde\nabla^{*}=\tilde\nabla^{\natural}$, and

$$
\langle\tilde\nabla,\tilde\nabla\rangle_{*}=\langle\tilde\nabla\rangle_{*}=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{*})=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{\natural})=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial R_\mu^2}=\frac{\partial^2}{\partial R_t^2}+\Delta_Q=\Box ,
$$

so the Hermitian norm of the gradient is the d'Alembertian, the same operator as its quaternionic bilinear norm. The **Hermitian form is the one positive-definite form of the four**, $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^2$ on the elements, and its square root is the topological norm $\lVert\tilde Q\rVert_E$; positivity is a property of the elements, the norm of this subsection being the operator $\Box$. **On the material sector** it is the same operator, $\Box|_{\mathbb{M}_-}=\Delta-c^{-2}\,\partial^2/\partial {r'_{t}}^2$, with the spatial Laplacian positive and the time term negative. **On the informational sector** it is the same operator again, $\Box|_{\mathbb{M}_+}=c^{-2}\,\partial^2/\partial r_t^2-\Delta|_{\mathbb{M}_+}$, with the time term positive and the primed Laplacian negative, and the two lines are negatives of each other because the two sectors keep complementary halves of the eight parameters. Positivity is untouched by that sign: the form is positive on the elements in either reading, and what changes is the operator's own sign and not the form's.

### The Krein Product, Its Form and Its Norm

**The product.** The general quaternionic sesquilinear product is the fourth of the four of *Product and Form Conventions*, §*The Twelve Products and Their Names*; it is the conjugate derivative applied to the conjugated field, $\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}$, the companion of the quaternionic bilinear product in the second slot,

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}=\Bigl(\frac{\partial}{\partial R_t}\bar Q_{\mathrm{f}t}-\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{\partial}{\partial R_t}\overline{\vec Q_{\mathrm f}}-\nabla\bar Q_{\mathrm{f}t}+\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**On the material sector** the product is read with $\partial/\partial R_t=-\frac{i}{c}\,\partial/\partial r'_t$ and the physical gradient, so that

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}\big|_{\mathbb{M}_-}=\Bigl(-\frac{i}{c}\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}-\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t+\frac{i}{c}\frac{\partial\overline{\vec Q_{\mathrm f}}}{\partial r'_t}-\nabla\bar Q_{\mathrm{f}t}+\nabla\times\overline{\vec Q_{\mathrm f}} ,
$$

with the divergence and the gradient carrying a minus where the Hermitian product carries a plus. **On the informational sector** the same product is read with $\partial/\partial R_t=\frac{1}{c}\,\partial/\partial r_t$ and $-i$ on the three space derivatives:

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}\big|_{\mathbb{M}_+}=\Bigl(\frac{1}{c}\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r_t}+i\,\nabla|_{\mathbb{M}_+}\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{1}{c}\frac{\partial\overline{\vec Q_{\mathrm f}}}{\partial r_t}+i\,\nabla|_{\mathbb{M}_+}\bar Q_{\mathrm{f}t}-i\,\nabla|_{\mathbb{M}_+}\times\overline{\vec Q_{\mathrm f}} ,
$$

the signs of the three space terms turning over once more, since the conjugate already carries $\varepsilon$ and the coefficient carries $-i$. The pair is the exact companion of the quaternionic pair of §*The Quaternionic Bilinear Product, Its Form and Its Norm*: the two bilinear products have companions with the conjugated field, the four lines are the four products on the two slices, and no line requires a convention beyond the four factors of §*The Gradient*.

**The symmetric and antisymmetric parts.** Under the conjugate transpose the half-sum is

$$
\tilde\nabla\bullet_{\natural*}\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}+\tilde Q_{\mathrm f}^{*}\tilde\nabla^{\natural}\bigr)=\Bigl[\frac{\partial}{\partial R_t}\bar Q_{\mathrm{f}t}-(\nabla,\overline{\vec Q_{\mathrm f}})\Bigr]e_t-\frac{\partial}{\partial R_t}\overline{\vec Q_{\mathrm f}}-\bar Q_{\mathrm{f}t}\nabla=\Bigl[\frac{\partial}{\partial R_t}\bar Q_{\mathrm{f}t}-\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr]e_t-\frac{\partial}{\partial R_t}\overline{\vec Q_{\mathrm f}}-\nabla\bar Q_{\mathrm{f}t} ,
$$

whose scalar part is the Krein form, and the half-difference is the curl of the conjugated field,

$$
\tilde\nabla\wedge_{\natural*}\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}-\tilde Q_{\mathrm f}^{*}\tilde\nabla^{\natural}\bigr)=\tfrac12\bigl(\nabla\times\overline{\vec Q_{\mathrm f}}+\nabla\times\overline{\vec Q_{\mathrm f}}\bigr)=\nabla\times\overline{\vec Q_{\mathrm f}} ,
$$

a pure vector.

**The form.** The **Krein form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural*}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial}{\partial R_\mu}\bar Q_{\mathrm{f}\mu}=\frac{\partial}{\partial R_t}\bar Q_{\mathrm{f}t}-\nabla\cdot\overline{\vec Q_{\mathrm f}} ,
$$

a scalar, the **contraction** of the conjugate derivative with the conjugated field in the $i c r'_t$ coordinate. **On the material sector** it is $-\frac{i}{c}\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}-\nabla\cdot\overline{\vec Q_{\mathrm f}}$, the divergence with a minus as in the plain form. **On the informational sector** it is $\frac{1}{c}\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r_t}+i\,\nabla|_{\mathbb{M}_+}\cdot\overline{\vec Q_{\mathrm f}}$, the divergence back with a plus, because the conjugate derivative has already applied $\varepsilon$ and the substitution has applied $-i$ three times; that double application is the whole difference between the Krein form and the Hermitian form on either slice, and it is why the two coincide on the elements only once the signature is taken into account.

**The norm.** The norm is defined with the form, as that form at its two equal arguments; on the gradient, since $\tilde\nabla^{*}=\tilde\nabla^{\natural}$ (§*The Gradient*),

$$
\langle\tilde\nabla,\tilde\nabla\rangle_{\natural*}=\langle\tilde\nabla\rangle_{\natural*}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla^{*})=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla^{\natural})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial^2}{\partial R_\mu^2}=\frac{\partial^2}{\partial R_t^2}-\Delta_Q ,
$$

so the Krein norm of the gradient **coincides with the plain bilinear norm**. It is the indefinite partner of the Hermitian form, and on the elements it is the form of signature $(1,3)$ whose diagonal is $\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2$: Hermitian, and negative on a nonzero element, so it carries no positivity. It is the form of the indefinite theory — the Krein space — and not of the contractions of these subsections. **On the material sector** it is $-c^{-2}\frac{\partial^2}{\partial {r'_{t}}^2}-\Delta$, both terms negative. **On the informational sector** it is $c^{-2}\frac{\partial^2}{\partial r_t^2}+\Delta|_{\mathbb{M}_+}$, both terms positive, and the Krein norm there is again the plain bilinear norm and not the d'Alembertian: the two norms agree with each other on both slices, and both differ from $\Box$ by one overall sign, which is the sign separating the indefinite pair from the definite one.

**A contraction is a form, never an index.** The series has one metric, the unit metric $\delta_{\mu\nu}=(1,1,1,1)$, and it is the identity, so no index is raised and none is lowered: a raised index would be the same index. What the product carries is the plain weight $\varepsilon$, and the weight is not a metric. Where a text with covariant indices contracts a derivative with a field through a raised and a lowered index, the series writes the quaternionic form $\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural}$; where it contracts two derivatives, the series writes the quaternionic norm $\langle\tilde\nabla\rangle_{\natural}=\Box$; and where it moves an index through a metric, the series writes the element $\tilde Q_{\mathrm f}$ itself, the weight being the sign vector inside the product. The four-index alternating symbol is not an index carrier: it is the orientation density, written all-low, $\epsilon_{0123}=+1$, and its height carries no sign. Its rank distinguishes it from the sign vector of the same letter.

**The rule is one rule on both slices.** A contraction never raises an index and never lowers one, on $\mathbb{M}_-$ or on $\mathbb{M}_+$, because the metric is the identity on both and a raised index would be the same index. What changes between the slices is only the coefficient the contraction carries: on $\mathbb{M}_-$ the time component is multiplied by $-i/c$ and the three space components by $1$, while on $\mathbb{M}_+$ the time component is multiplied by $1/c$ and the three space components by $-i$. A reader who checks a component formula written on either slice checks those four numbers and nothing else, and the check is complete, because the weight $\varepsilon$ belongs to the product, the coefficients belong to the slice, and the two never merge into a single symbol.

### The Gauge-Covariant Gradient

A derivative that differentiates a field charged under a connection is the gradient with a connection added. It carries the gradient's letter and **a label, not a letter of its own**:

$$
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla+\frac{iϙ}{\hbar}\tilde A=\sum_{\mu\in\{t,x,y,z\}}e_\mu\,\tilde\nabla_{\mathrm{gco},\mu},
\qquad
\tilde\nabla_{\mathrm{gco},\mu}=\frac{\partial}{\partial R_\mu}+\frac{iϙ}{\hbar}A_\mu,
$$

with $\tilde A=\sum_\mu A_\mu e_\mu\in\mathbb{M}_-$ the connection and $ϙ$ the charge of the field the operator acts on. The superscript $\mathrm{gco}$ names the family once and is read on every member of it.

**The decomposition is the gradient's, direction by direction.** One index, one basis element, one coefficient, exactly as in $\tilde\nabla=\sum_\mu e_\mu\,\partial/\partial R_\mu$. The only change is the coefficient: the partial derivative of the free gradient is replaced by the covariant one, $\partial/\partial R_\mu\mapsto\tilde\nabla_{\mathrm{gco},\mu}$, and the basis $e_\mu$ is untouched. The sum is spelled out here as everywhere. The coefficient is a **central scalar** — it commutes with $e_\nu$ and with every element of $\mathbb{B}$ — and that is what lets the involution act on the basis and leave the coefficients in place:

$$
\tilde\nabla_{\mathrm{gco}}^{\natural}=\sum_{\mu\in\{t,x,y,z\}}e_\mu^{\natural}\,\tilde\nabla_{\mathrm{gco},\mu}=\tilde\nabla^{\natural}+\frac{iϙ}{\hbar}\tilde A^{\natural}.
$$

The label is written **before** the conjugation, in the order the operator is built: the family first, the involution second. The conjugate is not a second operator; it is the same sum with $\natural$ read on the units, and its coefficients are the same scalars.

**On the material sector** the covariant coefficients are read with $\partial/\partial R_t=-\frac{i}{c}\,\partial/\partial r'_t$ and $\partial/\partial R_k=\partial/\partial r_k$, so the gradient is

$$
\tilde\nabla_{\mathrm{gco}}\big|_{\mathbb{M}_-}=e_t\Bigl(-\frac{i}{c}\frac{\partial}{\partial r'_t}+\frac{iϙ}{\hbar}A_t\Bigr)+\sum_k\vec e_k\Bigl(\frac{\partial}{\partial r_k}+\frac{iϙ}{\hbar}A_k\Bigr),
$$

and the connection enters with a plus on every slot. **On the informational sector** the same coefficients are read with $\partial/\partial R_t=\frac{1}{c}\,\partial/\partial r_t$ and $\partial/\partial R_k=-i\,\partial/\partial r'_k$, so

$$
\tilde\nabla_{\mathrm{gco}}\big|_{\mathbb{M}_+}=e_t\Bigl(\frac{1}{c}\frac{\partial}{\partial r_t}+\frac{iϙ}{\hbar}A_t\Bigr)+\sum_k\vec e_k\Bigl(-i\frac{\partial}{\partial r'_k}+\frac{iϙ}{\hbar}A_k\Bigr).
$$

**The connection is a value and the derivative is the factor.** The substitution of §*The Gradient* replaces the derivative term of each coefficient and leaves $A_\mu$ exactly as it stands, because $A_\mu$ is a component of a field and carries no derivative; a slice is a statement about the coordinates, and the connection does not know which slice the derivative beside it is read on. That is why the two displays differ in their derivative terms and agree in their connection terms, and it is the check to apply to any covariant formula of the series: the substitution acts on the $\partial$ and never on the $A$.

**The side.** Both members act from the left. The position of the operator names the side, as it does for every field of the series, and no glyph names it: a right action on $\tilde{Ξ}_{\mathrm{sp}}$ is the left action of $\tilde\nabla_{\mathrm{gco}}^{\natural}$ on $\tilde{Ξ}_{\mathrm{sp}}^{\natural}$, by the exchange of §*The Two Sides and the Renaming Theorem*.

**The curvature and the square.** The components do not commute, and their commutator carries no derivative:

$$
[\tilde\nabla_{\mathrm{gco},\mu},\tilde\nabla_{\mathrm{gco},\nu}]=\frac{iϙ}{\hbar}F_{\mu\nu},
\qquad
\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\nabla_{\mathrm{gco}}=\sum_{\mu\in\{t,x,y,z\}}\bigl(\tilde\nabla_{\mathrm{gco},\mu}\bigr)^{2}+\frac{iϙ}{\hbar}\tilde F,
$$

with $\tilde F=\mathrm{Vect}(\tilde\nabla^{\natural}\tilde A)$ the curvature. The scalar part of the square is the covariant d'Alembertian and the vector part is the curvature; both are read in *The Covariant Derivative and Gauge Connection in Biquaternionic Form*.

**The coupling, and the letter $\kappa$.** A few articles write the same operator as $\tilde\nabla+i\kappa\mathcal A$, with $\kappa$ the coupling and $\mathcal A$ the connection. That is one object under two spellings, $\kappa=ϙ/\hbar$ and $\mathcal A=\tilde A$. The series writes $\frac{iϙ}{\hbar}\tilde A$, so that $\kappa$ stays free for the retarded denominator $\kappa=1-\vec u_R\cdot\vec\beta$ of *Algebra and Element Conventions*, which is not a coupling.

## The Pair Operator and Its Symbol

**The pair.** The two first-order equations of the series, $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m\,\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=m\,\tilde{Ξ}_{\mathrm{sp},R}$, are one operator on $\mathbb{B}\oplus\mathbb{B}$. With $\tilde{Ξ}_{\mathrm{sp}}=(\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R})$ it is

$$
\mathbb{D}\tilde{Ξ}_{\mathrm{sp}}=\bigl(\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R},\ \tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}\bigr),
\qquad
\mathbb{D}^2=\Box I ,
$$

and the massive equation is $(\mathbb{D}-m)\tilde{Ξ}_{\mathrm{sp}}=0$, with massless limit $\mathbb{D}\tilde{Ξ}_{\mathrm{sp}}=0$. The operator is the pair written once: it carries no matrix generator, no Clifford index and no chart, and its only content is which gradient acts on which part. The mass is the off-diagonal coupling of the two parts and is the identity on $\mathbb{B}$ in each place it acts. Every component equation of the series is a **coordinate form** of that pair and not a second dynamics.

**Neither gradient squares to the d'Alembertian, and their composition does.** Written as a product of elements, $\tilde\nabla^2$ is not $\Box$: $e_t$ commutes with the three spatial units, so the mixed derivatives survive and the square is not scalar. Only the composition with the conjugate is scalar, $\tilde\nabla^{\natural}\tilde\nabla=\tilde\nabla\tilde\nabla^{\natural}=\Box$, and this is why the pair is the least object that carries a first-order massive equation: one gradient on one field is first order and cannot equal a second-order operator, so no one-field first-order massive equation exists in this algebra. The free equation stays first order on one field, and the mass is what needs the pair.

**Written on one element.** Where the field is carried on one element, the same operator is written with its two sides in position,

$$
\mathbb{D}:\ \tilde X\longmapsto-\frac{1}{c}\frac{\partial\tilde X}{\partial r'_t}\,\vec e_x-\sum_k\vec e_k\frac{\partial\tilde X}{\partial R_k}\,\vec e_y ,
$$

and the sides are the whole of the content. The time term is a right multiplication by $\vec e_x$ alone; each space term carries $\vec e_k$ on the left and $\vec e_y$ on the right, and the two multipliers are fixed basis elements that select the chiral slots and do not depend on the field. Left and right multiplications commute and the pure units anticommute, $\vec e_x\vec e_y=-\vec e_y\vec e_x$, with $\vec e_x^2=\vec e_y^2=-e_t$, so the cross terms cancel and the square is the d'Alembertian of the material sector, $\Delta-c^{-2}\partial^2/\partial {r'_{t}}^2$. The factor $1/c$ is the one carried by the coordinate derivative, $\partial/\partial R_t=-(i/c)\partial/\partial r'_t$, with the $i$ absorbed in the multiplier; this is the pair read on one element and not a second definition.

**The symbol.** On a plane wave the two gradients act as left multiplication by the momentum element and its conjugate, $\tilde K=i\tilde P=-E\,e_t+i\vec p$ with $\tilde K\tilde K^{\natural}=E^2-\lvert\vec p\rvert^2=p^2$, so the symbol of the pair is

$$
\mathbb{D}_p:\ (w_L,w_R)\longmapsto\bigl(\tilde K\,w_R,\ \tilde K^{\natural}w_L\bigr),
\qquad
\mathbb{D}_p^2=p^2 I ,
$$

and on one element it reads $\mathbb{D}_p:\tilde X\mapsto iE\,\tilde X\vec e_x-i\sum_kp_k\,\vec e_k\tilde X\vec e_y$. The square of the element is not the scalar: $\tilde K^2$ has scalar part $E^2+\lvert\vec p\rvert^2$ and a vector part that does not cancel, and only the composition with the conjugate returns $p^2$. On the mass shell $p^2=m^2$ the symbol of $\mathbb{D}-m$ is therefore singular exactly there and nowhere else, and the two chiral slots share the one condition.

**The inverse is a Green matrix.** With $G$ the Green's function of the d'Alembertian, $(\Box-m^2)G=\delta$, the Green matrix of the pair is $\mathcal{S}=(\mathbb{D}+m)G$, and $(\mathbb{D}-m)\mathcal{S}=(\mathbb{D}^2-m^2)G=\delta I$. The inverse introduces no new object: the scalar mass commutes with $\mathbb{D}$, and the factorization is the algebraic identity $(\mathbb{D}-m)(\mathbb{D}+m)=\mathbb{D}^2-m^2$.

**The glyph and its marks.** The glyph is $\mathbb{D}$, and it takes a mark for the factor and never for the chart. A subscript names the factor when that factor is not the material gradient — $\mathbb{D}_p$ for the constant momentum covector, which is the symbol — and an element in parentheses is an argument, $\mathbb{D}(\tilde K)$, because a letter on the right without parentheses, $\mathbb{D}\tilde{Ξ}_{\mathrm{sp}}$, is the field acted on. The gradient follows the same rule: $\tilde\nabla$ bare, $\natural$ or a sector label only where a second gradient is in play. The pair is never written $\mathbb{D}_{\mathbb{M}_-}$ or $\mathbb{D}^{\natural}$; the sector enters through the coordinate, and the conjugate of the pair is the pair with its two gradients exchanged.

**The pair is sector-free.** On $\mathbb{M}_-$ and on $\mathbb{M}_+$ the operator is the same and only the four derivatives change, $\partial/\partial R_t=-(i/c)\,\partial/\partial r'_t$ against $\partial/\partial R_t=(1/c)\,\partial/\partial r_t$. Its square follows the d'Alembertian of §*The Quaternionic Bilinear Product, Its Form and Its Norm*: $\Delta-c^{-2}\partial^2/\partial {r'_{t}}^2$ on the material sector and $c^{-2}\partial^2/\partial r_t^2-\Delta|_{\mathbb{M}_+}$ on the informational one, and a reader who moves the pair from one sector to the other moves one overall sign and no operator.

## The Transposition of the Gradient

**The transposed reading.** A gradient acts on the factor written to its right, $\tilde\nabla\tilde Q_1$. The long arrow over the glyph marks the other reading: the operator acts on the factor written to its left, and the arrow points at that factor, $\tilde Q_1\overleftarrow{\tilde\nabla}$. The mark belongs to the operator and not to the field, and it is not the short arrow of the pure part, which sits on an element and marks its vector part alone. Read this way, the gradient has its derivative to the right of the element it differentiates,

$$
\tilde Q_1\overleftarrow{\tilde\nabla}:=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial\tilde Q_1}{\partial R_\mu}\,e_\mu ,
$$

the same four coefficients in the same four directions, with the unit written after each. The integration articles write this object $\nabla^{R}$ and use it wherever a derivative has to be moved off a product. It is not a second operator: it is the gradient with its two factors exchanged, and the exchange is what the identity below computes.

**The identity.** For every element-valued field $\tilde Q_1$,

$$
\boxed{\;\bigl(\tilde Q_1\overleftarrow{\tilde\nabla}\bigr)^{\natural}=\tilde\nabla^{\natural}\tilde Q_1^{\natural}\;}
\qquad\Longrightarrow\qquad
\tilde Q_1\overleftarrow{\tilde\nabla}=\bigl(\tilde\nabla^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}.
$$

**The proof is one term.** The involution is $\mathbb{C}$-linear, it acts on the units at fixed coordinate, and it commutes with $\partial/\partial R_\mu$; and $e_\mu^{\natural}=\varepsilon_\mu e_\mu$. The $\mu$-th term on the left, $(\partial\tilde Q_1/\partial R_\mu)^{\natural}(e_\mu)^{\natural}$, is therefore $\varepsilon_\mu e_\mu\,\partial\tilde Q_1^{\natural}/\partial R_\mu$, which is the $\mu$-th term of $\tilde\nabla^{\natural}\tilde Q_1^{\natural}$. Summing over $\mu$ gives the boxed line, and $\natural^{2}=\mathrm{id}$ gives the arrow back.

**What it says.** A right action is the conjugation of a left action: conjugate the field, apply the conjugate gradient from the left, conjugate the result. In the notation of §*The Two Sides and the Renaming Theorem*, $R_{\tilde\nabla}=\natural\circ L_{\tilde\nabla^{\natural}}\circ\natural$, read on a differential operator rather than on a multiplication. The statement needs no equation, no mass, no chirality and no pair of fields. It is an identity between operators, true of any $\tilde Q_1$: a solution, a non-solution, a product, a constant.

**With a connection nothing changes.** The components of $\tilde\nabla_{\mathrm{gco}}$ are central scalars, so the same term-by-term computation gives $\bigl(\tilde Q_1\overleftarrow{\tilde\nabla_{\mathrm{gco}}}\bigr)^{\natural}=\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde Q_1^{\natural}$, at the same residual, with $\natural$ again fixing the coefficients and reading the units alone.

**The instance that hides the generality.** The chiral pair is the case usually quoted. From $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=m\tilde{Ξ}_{\mathrm{sp},R}$, transposing with $\tilde Q_1=\tilde{Ξ}_{\mathrm{sp},L}^{\natural}$ and using $m^{\natural}=m$,

$$
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=m\,\tilde{Ξ}_{\mathrm{sp},R}
\qquad\Longrightarrow\qquad
\tilde{Ξ}_{\mathrm{sp},L}^{\natural}\overleftarrow{\tilde\nabla}=m\,\tilde{Ξ}_{\mathrm{sp},R}^{\natural},
$$

one line, with the derivative now written to the right of $\tilde{Ξ}_{\mathrm{sp},L}^{\natural}$ and the same mass in place. Read alone, the pair suggests that the right action is a property of the Dirac equation. It is not: the two lines hold of $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=m\tilde{Ξ}_{\mathrm{sp},L}$ as well, of a massless field, and of any equation in which one field stands to the right of a derivative. The equation supplies the right-hand side; the identity does not depend on it.

**Why the superscript $R$ is nevertheless written.** The identity holds for a field, and a product of fields is a field. What it does not do is move the derivative off one factor of a product while the other stays. On $\tilde Q_1\tilde Q_2$ the Leibniz rule gives

$$
(\tilde Q_1\tilde Q_2)\overleftarrow{\tilde\nabla}=\sum_{\mu\in\{t,x,y,z\}}\Bigl(\frac{\partial\tilde Q_1}{\partial R_\mu}\tilde Q_2+\tilde Q_1\frac{\partial\tilde Q_2}{\partial R_\mu}\Bigr)e_\mu ,
$$

with the unit after the bracket. It does not pass to the left of $\tilde Q_2$: that is a commutation with the units, allowed only when $\tilde Q_2$ is central. Nor is the rule $\sum_\mu(\partial\tilde Q_1/\partial R_\mu)e_\mu\tilde Q_2$, which differs from the first term by the defect $\sum_\mu(\partial\tilde Q_1/\partial R_\mu)[\tilde Q_2,e_\mu]$. That is the case §*The Two Sides and the Renaming Theorem* excludes, and the case the integration articles meet. There the derivative is named $\nabla^{R}$ after the factor it differentiates, and the name is a position, not a second operator.

**The slots.** The transposition is the exchange of the two slots of a cell, read on a differential operator. In the language of *Operator Chirality on the Biquaternion Algebra*, §*Conjugation Exchanges the Sides*, the map that carries a left multiplier to a right multiplier is $\mathsf C$, the conjugation written as a congruence, $\mathsf C L(a^{\natural})\mathsf C=R(a)$, which in the axis-free frame is the switch $\mathsf D=\operatorname{diag}(1,-1,-1,-1)$ and is the $N$ of the matrix form above. A left action of the gradient and a right action of the same gradient therefore have arrays that agree up to that sign and that order, which is where the phases of the two sides come from.

**What it is not.** Not a transpose without conjugation: $N$ is not the identity, and $N^{\mathsf T}N=I$ with $\det N=-1$ make the congruence a congruence and not a similarity. Not the adjoint either: the dagger carries the integration by parts and the boundary term, while $\natural$ carries the units alone at fixed coordinate; the two agree on the gradient, $\tilde\nabla^{*}=\tilde\nabla^{\natural}$, and part on a general element.

**Verified.** On random polynomial fields in the four coordinates the boxed line holds at residual $0.0$, the reconstruction from the conjugate at $0.0$, the chiral instance at $0.0$, and the product rule above at $0.0$; on $\tilde Q_1=r_x\vec e_x$ and $\tilde Q_2=\vec e_y$ the naive rule returns $-\vec e_y$ where the product rule returns $+\vec e_y$. The anti-automorphism it uses holds at residual $1.0\times10^{-15}$ over $200$ random pairs; the automorphism that would be needed if the units were not reversed fails at $2.7\times10^{1}$.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate, $Q_\mu$ or $x_\mu$. There is one metric, $\delta_{\mu\nu}=(1,1,1,1)$, and a display never names it.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

An operator whose letter is the letter of an element is that element: the tilde and the arrow are read on it as on the element, and no mark says operator. The named operators are left and right multiplication, the two-sided operator, the sandwich and the inner derivation. The side of an action is position, $D\tilde{Ξ}_{\mathrm{sp}}$ against $\tilde{Ξ}_{\mathrm{sp}} D$; the two are exchanged by the natural conjugation, $(\tilde{Ξ}_{\mathrm{sp}} D)^{\natural}=D^{\natural}\tilde{Ξ}_{\mathrm{sp}}^{\natural}$, so a right action on a field is a left action on the conjugate field, and no glyph marks a side. The superscript $R$ marks the right derivative, the one case the exchange does not reach, and on the gradient even that case is a conjugation: $\tilde Q_1\overleftarrow{\tilde\nabla}=\bigl(\tilde\nabla^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}$, so a right action is the left action of the conjugate gradient on the conjugate field, and the identity needs no equation. The dagger is the general adjoint of an operator and not a fifth conjugation, and it adds to the element's mark rather than replacing it. A Kraus operator is an element, not an array. The Fock operator is the one operator that is not an element, and its superscript is fixed with the other tokens.

A subscript is a component or a label, never a derivative; every partial derivative is written with $\partial$ and its variable. A caret is a power and never a label: every label, coordinate, component, basis vector, frame cell and sign symbol is written low, and a contraction is a form with the sign vector. The coordinate derivative is unhalved, $\partial/\partial R_\mu=\frac{1}{c_\mu}\bigl(\partial/\partial r_\mu-i\,\partial/\partial r'_\mu\bigr)$, and a sector keeps one of its two halves. The gradient is $\tilde\nabla$, not pure. The d'Alembertian is $\Box=\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\partial^2/\partial R_t^2+\Delta_Q$, read on the material sector as $\Delta-c^{-2}\partial^2/\partial {r'_{t}}^2$, and every article uses this one operator with the mass equation $(\Box-m^2c^2/\hbar^2)\tilde{Ξ}_{\mathrm{sp}}=0$. The gauge-covariant gradient is the same sum with the coefficient replaced, $\tilde\nabla_{\mathrm{gco}}=\sum_\mu e_\mu\tilde\nabla_{\mathrm{gco},\mu}=\tilde\nabla+\frac{iϙ}{\hbar}\tilde A$, and it carries a label rather than a letter of its own.

The gradient and its conjugate are read once as one operator on a pair of elements, the **pair operator** $\mathbb{D}$ of §*The Pair Operator and Its Symbol*, whose square is $\Box I$ and whose symbol is left multiplication by the momentum element; the pair carries the mass off the diagonal and no matrix generator.

The four forms remain four distinct conventions and the norms two, because each form conjugates its own slot. The four product subsections read the same gradient through the plain, quaternionic, Hermitian and Krein products, each with its form and its norm, and the signs follow from the algebra rather than from a choice of metric.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q}, R_{\tilde Q}$ | Left and right multiplication by the element; the glyph of the operator is the glyph of the element |
| $L_{\tilde Q_4}R_{\tilde Q_1}$ | The two-sided operator, $\tilde Q_2\mapsto\tilde Q_4\tilde Q_2\tilde Q_1$ |
| $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ | The sandwich, the congruence by the element |
| $\operatorname{ad}_{\tilde Q}$ | The inner derivation, $[\tilde Q,\cdot]$ |
| $^{\dagger}$ | The general adjoint of an operator; $(L_a)^{\dagger}=L_{a^{*}}$ |
| $\partial/\partial R_\mu$ | The unhalved coordinate derivative, $\frac{1}{c_\mu}\bigl(\partial/\partial r_\mu-i\,\partial/\partial r'_\mu\bigr)$; a display writing $\partial/\partial Q_\mu$ names the same slot |
| $\tilde\nabla$ | The biquaternionic gradient, four components, not pure |
| $\tilde\nabla_{\mathrm{gco}}$ | The gauge-covariant gradient, $\tilde\nabla+\frac{iϙ}{\hbar}\tilde A$; its component $\tilde\nabla_{\mathrm{gco},\mu}=\partial/\partial R_\mu+\frac{iϙ}{\hbar}A_\mu$, its conjugate $\tilde\nabla_{\mathrm{gco}}^{\natural}$ |
| $\Box$ | The d'Alembertian, $\tilde\nabla\tilde\nabla^{\natural}=\partial^2/\partial R_t^2+\Delta_Q$ |
| $\mathbb{D}$ | The pair operator on $\mathbb{B}\oplus\mathbb{B}$, $\mathbb{D}(\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R})=(\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R},\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L})$, with $\mathbb{D}^2=\Box I$; $\mathbb{D}_p$ is its symbol |
| $^{\natural}$ | The natural conjugation, $a^{\natural}=(a_0,-a_1,-a_2,-a_3)$; an anti-automorphism, $(ab)^{\natural}=b^{\natural}a^{\natural}$ |
| $(\tilde{Ξ}_{\mathrm{sp}} D)^{\natural}=D^{\natural}\tilde{Ξ}_{\mathrm{sp}}^{\natural}$ | The exchange of the two sides: a right action on $\tilde{Ξ}_{\mathrm{sp}}$ is a left action on $\tilde{Ξ}_{\mathrm{sp}}^{\natural}$ |
| $\nabla^{R}$ | The right gradient, $F\nabla^{R}=\sum_\mu(\partial F/\partial R_\mu)e_\mu$; used only where a derivative meets two distinct factors |
| $\overleftarrow{\ }$ | The long arrow over an operator: it acts on the factor written to its left, and the arrow points at that factor; it is not the short arrow of the pure part |
| $\tilde Q_1\overleftarrow{\tilde\nabla}$ | The same gradient transposed, $\sum_\mu(\partial\tilde Q_1/\partial R_\mu)e_\mu$; the right action, equal to $\bigl(\tilde\nabla^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html), for the algebra and the element glyphs.
- [Conventions of the Products and the Forms](product-and-form-conventions.html), for the four products read on the gradient.
- [Conventions of the Norms and the Pairings](norm-and-pairing-conventions.html), for the norms of those products.
- [Conventions of the Units, the Indices and the Notation](unit-index-and-notation-conventions.html), for the Fock superscript and the subscript rules.
- [The Element and Operator Representations](element-and-operator-representations-the-three-actions.html), companion article, for the three actions and their matrices.
