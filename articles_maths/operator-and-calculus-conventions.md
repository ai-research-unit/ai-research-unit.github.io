# __Operator and Calculus Conventions__

## Introduction

An operator that acts by multiplication is the element it multiplies by, and its glyph is the glyph of that element; an operator written as an array carries no tilde. This article fixes the named operators, the dagger, the array rule and the Fock exception, and then the calculus: the derivative marks, the gradient, the d'Alembertian, and the four products read on the gradient. The calculus half states one rule that holds in every article of the series: every derivative operator carries the subscript $\Phi$, and no gradient, Laplacian or d'Alembertian is written without it.

The order follows the dependence. The operators come before the calculus because the gradient is an operator and its glyph follows the operator rule. The derivation comes before the four products read on it, because the products are read with the derivative already fixed.

The article assumes the base of *Algebra and Element Conventions*, the products and forms of *Product and Form Conventions*, and the norms of *Norm and Unitary Conventions*. It cites the superscript rule of *Index and Notation Conventions* for the Fock mark.

## The Operators

**An operator acting by multiplication is the element it multiplies by.** Every element acts on the algebra, on the left $L_{\tilde Q}$ or on the right $R_{\tilde Q}$, and an operator whose letter is the letter of an element **is** that element. The glyph of the operator is therefore the glyph of its element, and the marks are read on it as on the element: the tilde marks the quaternionic element read with its scalar part, the arrow the pure element read on its vector part alone. Neither mark says that a glyph is an operator, and no mark is added to say it.

**The named operators.** The structural operators take an upright capital letter and carry the element in the subscript, where it keeps its own mark:

| Operator | Glyph |
|---|---|
| left multiplication | $L_{\tilde Q_1}(\tilde Q_2)=\tilde Q_1\tilde Q_2$ |
| right multiplication | $R_{\tilde Q_1}(\tilde Q_2)=\tilde Q_2\tilde Q_1$ |
| two-sided | $L_{\tilde Q_1}R_{\tilde Q_2}(\tilde Q_3)=\tilde Q_1\tilde Q_3\tilde Q_2=L_{\tilde Q_1}R_{\tilde Q_2}$ |
| two-sided operator (default: bilinear) | $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}=L_{\tilde Q}R_{\tilde Q^{*}}=\operatorname{H}_{\tilde Q}$ |
| inner derivation | $\operatorname{ad}_{\tilde Q_4}(\tilde Q_1)=[\tilde Q_4,\tilde Q_1]$ |
| automorphism | $\operatorname{Ad}_{\tilde Q_4}$ |

**The default two-sided operator.** *Two-Sided Operator* with no qualifier is the **bilinear two-sided operator** $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$. The qualifier separates it from the **sesquilinear two-sided operator** $\mathcal{T}_{a,b}=L_{a}R_{b}\circ\varkappa$, $\mathcal{T}_{a,b}(\tilde Q_1)=a\tilde Q_1^{*}b$, whose star acts on the argument. The bilinear two-sided operator is quadratic in $\tilde Q$, not bilinear: $\mathrm{Sd}_{\lambda\tilde Q}=\lvert\lambda\rvert^{2}\mathrm{Sd}_{\tilde Q}$. The word *bilinear* names the family $L_{a}R_{b}$ from which the two-sided operator is cut. The dagger is the adjoint of an operator and is never part of an operator's name.

The tilde sits in the subscript because it belongs to the element, not to the operator: $L_{\tilde Q}$ is an operator, $\tilde Q$ is the element that generates it. In $L_{\tilde Q_1}R_{\tilde Q_2}$ the subscripts are positional: the first is the left multiplier and the second the right multiplier, while the argument occupies the third slot.

**The basis operators.** The four units are written in the subscript, $L_{e_\mu}$ and $R_{e_\mu}$, and nowhere else: the short form $L_\mu$ is not used in this corpus. The right family is read from the left one by the exchange $\mathsf S$ of the two mixed Peirce units, $R_{e_\nu}=\mathsf S L_{e_\nu}^{\mathsf T}\mathsf S^{-1}$, and the sixteen two-sided operators $L_{e_\mu}R_{e_\nu}$ are the matrix basis and the basis operator table of *Matrix Representations Conventions*, §*The Clifford Structure*; the gamma set is five of them up to $i$, $\gamma_0=iL_{e_t}R_{\vec e_x}$, $\gamma_1=iL_{\vec e_x}R_{\vec e_y}$, $\gamma_2=iL_{\vec e_y}R_{\vec e_y}$, $\gamma_3=iL_{\vec e_z}R_{\vec e_y}$, $\gamma_5=-iL_{e_t}R_{\vec e_z}$; the last of them is the fifth frame operator, written $\mathsf{V}_{\mathrm{vol}}$ in the operator articles.

**The spin operator and the words built on it.** The generator of the rotations is $\tilde S_k=\tfrac12 i\vec e_k$, an operator whose glyph is the glyph of its element, like every operator of this section. The three words built on it — the **spin**, the **elementary spinor** and the **Dirac spinor** — are fixed in *Special Element and Peirce Conventions*, §*The Spin Convention* and §*The Spinor Convention*, and are not restated here.

**The two marks on a glyph that is also an operator.** An operator read through its element follows the element rule in full.

- A glyph read with its scalar part, four components: the tilde. The biquaternionic gradient $\tilde\nabla_\Phi$ of §*The Gradient* is the algebraic example, and the canonical momentum $\tilde p=p_te_t+\vec p$ carries the same mark.
- A pure glyph, three components: the arrow. The momentum $\vec p=\sum_{k\in\{x,y,z\}}\vec e_kp_k$ is the example, and $\vec\nabla_\Phi=\sum_{k\in\{x,y,z\}}\,\vec e_k\,\partial/\partial r_k$ is the fixed spatial gradient, which carries no second mark (§*The Gradient*).

The gradient decides the case cleanly: $\tilde\nabla_\Phi$ is not pure, because its $e_t$ term carries $-i\,\partial/\partial r'_t$, while $\vec\nabla_\Phi$ is pure. The case follows the layer: a pure operator of the quaternion layer stays lower case, $\vec p$, and one of the biquaternion layer takes the upper case, $\vec P$; where the letter already names another object of the layer, a subscript fixes the operator.

**The mark of a part, and the side carried by position.** The only arrow on a glyph is the short one, and it marks the **pure part**: $\vec e_x$, $\vec p$. The long arrow that sits over an operator is a different mark and not a second arrow of the same kind: it is the mark of the transposed reading, fixed in §*The Transposition of the Gradient*. The side of an action is not marked at all. It is carried by position, $b\psi$ against $\psi b$, the actor written on the side from which it acts, and position is unambiguous because the operand is itself a glyph.

**What names a side where position is not enough.** Three signs, each of which the corpus needs for a purpose of its own.

- $\natural$ marks the conjugation of an element, $a^{\natural}=(a_0,-a_1,-a_2,-a_3)$, and it is what carries a change of side, because it is an anti-automorphism: $(ab)^{\natural}=b^{\natural}a^{\natural}$, hence $(\psi D)^{\natural}=D^{\natural}\psi^{\natural}$, and a right action on $\psi$ is a left action on $\psi^{\natural}$. The theorem is below, §*The Two Sides and the Renaming Theorem*.
- $L_a$ and $R_a$ name a side outright when a statement is about operators rather than about fields, and the basis operator $L_{a}R_{b}$ prints both sides at once. The label of the side of a basis operator is the **operator chirality** — the left slot, the right slot, or both — fixed in *Operator Family Conventions*, §*The Slot Label, Which Is the Chirality*.
- The superscript $R$ marks the one case that position alone leaves genuinely ambiguous: a derivative that differentiates the factor written to its left, $F\vec\nabla_\Phi^{R}=-i\,(\partial F/\partial r'_t)\,e_t+\sum_{k\in\{x,y,z\}}(\partial F/\partial r_k)\,\vec e_k$. It is used only inside a product of two distinct factors, which is where the theorem below does not reach.

**The dagger.** The dagger is the general adjoint of an operator, never of an element: $(L_a)^{\dagger}=L_{a^{*}}$. Several adjoints arise at once — one for each form, and one for each of the two-sided operators — and the dagger is the mark that covers them all, of which the others are the instances. It is not a fifth conjugation: it belongs to the operators and not to the algebra. Where a dagger is written on an element the writing is an abuse: the mark that was meant is the star for the Hermitian conjugation, or the sign ${}^{\natural}$ for the quaternion conjugation, according to the conjugation in view. The dagger is added to the glyph and does not replace the element's mark: the arrow states purity, which the adjoint preserves; the tilde states a glyph read with its scalar part, which the adjoint also preserves. Where the adjoint in view is the formal algebraic one of the definite form, the two marks are written together, dagger first: $(L_a)^{\dagger}=(L_a)^{*}=L_{a^{*}}$ and $\tilde\nabla_\Phi^{\dagger}=\tilde\nabla_\Phi^{*}=(\tilde\nabla_\Phi)^{\natural}$. The identification is formal: the $L^2$ adjoint of a derivative carries the sign of the integration by parts, and it is not the dagger of this convention.

**An operator written as an array carries no tilde.** The element rule above governs an operator that acts on the algebra by multiplication, because such an operator is the element. An operator written as a linear map on a coordinate column, as a matrix in the $2\times2$ image, or as a regular matrix $\mathsf{M}_{4L}$, is an array: it carries no tilde, its elements keep theirs inside the argument, $\mathsf{M}_2(\tilde Q)$, and its adjoint is the dagger and not the star. A Kraus operator, where the physics corpus uses one, is written in the element reading, $\tilde K_l\in\mathbb{B}$, because it multiplies the state on both sides; its matrix image $\mathsf{M}_2(\tilde K_l)$ carries no tilde.

**The Fock exception.** A Fock operator is not an element of the algebra; its superscript $\mathrm{fop}$ and the order of the two marks are fixed in *Index and Notation Conventions*, §*The Labels*.

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

**In matrix form it is one congruence.** With $\mathsf C=\operatorname{diag}(1,-1,-1,-1)$ the matrix of $\natural$ on a coordinate column,

$$
\mathsf C\,R_D\,\mathsf C=L_{D^{\natural}},
\qquad
\mathsf C\,L_D\,\mathsf C=R_{D^{\natural}},
\qquad\text{both at residual }0 .
$$

$\mathsf C$ is the change of basis that exchanges the two families, and $\mathsf C^{\mathsf T}\mathsf C=I$, $\det\mathsf C=-1$.

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
\bigl\langle R_D-L_{D^{\natural}}\\bigr\rangle_*^{1/2}=8.4853\neq0 ,
$$

so the two arrays differ and neither may be substituted for the other at sight. What is equal is the pair of solution sets after renaming, not the operators.

**Where the theorem does not reach.** Three cases, and each is stated where it is used.

1. **More than one field.** The anti-automorphism reverses the whole order, $(\psi D\chi)^{\natural}=\chi^{\natural}D^{\natural}\psi^{\natural}$, residual $1.3\times10^{-14}$ over $200$ random triples. The two fields exchange places, so renaming alone does not suffice, and where the two fields are not the same object the reordering changes the statement. The bilinear identities of the integration articles stand in this case, and it is why they carry the superscript $R$ on the derivative.
2. **A carrier without $\natural$.** On a column $\psi\in\mathbb{C}^{4}$ there is no quaternion conjugation, only the antilinear Dirac adjoint; on a space of functions of two variables, as in a star product, $\natural$ is not the involution in play. The theorem is a theorem about fields valued in $\mathbb{B}$.
3. **The side itself on display.** For the two-sided action $a\psi b$, the mirror coupling, or the exchange of the two slots of a basis operator, conjugating the field destroys what is being displayed. There both factors stay in place and the side is named by position, or by $L_a$ and $R_a$.

**The consequence for the corpus.** Every equation that acts on a single biquaternion field is written on the left. The ones that would read as acting on the right are the same equations on the conjugate field, and the chiral pair is the instance: with $\Phi=\tilde\Psi^{\natural}$, the pair $\tilde\nabla_\Phi\tilde\Psi_R=m\tilde\Psi_L$ and $(\tilde\nabla_\Phi)^{\natural}\tilde\Psi_L=m\tilde\Psi_R$ is complete as written, both equations acting from the left, and $\natural$ is what separates them. Across the $404$ files and $10\,196$ display equations of the physics corpus no glyph names a side: the side is position, the conjugation is $\natural$, and the exchange is $N$.

## Conventions for Derivation

In this work, subscripts denote vector components, not partial derivatives as in the PDE convention; every partial derivative is written explicitly with $\partial$ followed by its variable, and no subscript is ever attached to the $\partial$ of a derivative. A subscript is therefore a component index, as in $v_x$ for the component of a velocity along an axis, or a label, as in $\tilde U_{\mathrm b}$; it never denotes a derivative. The derivative with respect to a coordinate is written with its parameter named, $\partial/\partial r'_t$ for the fourth slot and $\partial/\partial r_x$, $\partial/\partial r_y$ or $\partial/\partial r_z$ for the three space slots; a parameter is never left under the $\partial$, so none of the abbreviated spellings occurs, and the rule admits no exception for a derivative, neither on a free index nor on any other. A derivative with respect to a variable that is not a coordinate is written the same way, its variable named in full: the Lagrangian derivative puts the function in the numerator, $\partial L/\partial w$, so that where a PDE text writes $L_u$ and $L_p$ the calculus-of-variations and partial-differential-equation articles write $\partial L/\partial w$ and $\partial L/\partial p$; the second derivative has the same shape, $\partial^2 L/\partial w^2$. The function is named in the numerator whenever it is a letter of its own, as for a Lagrangian, a Hamiltonian or a generating function; the slashed form $\partial/\partial u$ is kept where the symbol is an operator or where the operand is a compound expression rather than a single letter. The fourth coordinate is the imaginary time $r'_t$, a real parameter, so the derivative along the slot is written out as $\partial/\partial r'_t$; the factor $-i$ that the imaginary unit brings stands on the coefficient of the gradient and never on the derivative.

**A subscript on an operator names its degree, its place, its bundle or its sector.** The rule governs the derivative of a function or a field, which names its variable after the $\partial$. It does not forbid a label on an operator that differentiates nothing: the chain boundary is $\partial_n:C_n\to C_{n-1}$ and the face maps are $\partial_i$, with the degree in the subscript; the distinguished boundary of a polydisc is $\partial_0D$; the tame symbol is $\partial_v$, with the place; the twisted Dolbeault operator is $\bar\partial_E$, with the bundle. These are operator labels, in the sense of *Index and Notation Conventions*, §*The Subscripts*, and they stand as written. The sector is one of them, and it is fixed in §*The Gradient*: $\tilde\nabla_{\Phi}$ and $\Box_{\Phi}$ name the material sector, the only sector in which the corpus writes a derivative, and the letter is never the name of a coordinate.

**These studies do not use the covariant index conventions: subscripts are not coordinate indices or derivatives, partial derivatives are written with explicit operators, and structural information is carried by the algebra of the objects themselves.**

**A contraction is written as an explicit sum, and the sum carries its scope.** Every index that is contracted is named under a $\sum$, and the $\sum$ also names the set the index runs over, so no reader has to infer a range. The space index runs over the three space letters, $\sum_{k\in\{x,y,z\}}$, and the coordinate index over the four, $\sum_{\mu\in\{t,x,y,z\}}$. The gradient is $\tilde\nabla_\Phi=-i\,e_t\partial/\partial r'_t+\sum_{k\in\{x,y,z\}}\vec e_k\partial/\partial r_k$, the spatial gradient $\sum_{k\in\{x,y,z\}}\vec e_k\partial/\partial r_k$, a basis-vector contraction $\sum_{k\in\{x,y,z\}}\vec e_kA_k$, and a sign-symbol contraction $\sum_{i,j\in\{x,y,z\}}\varepsilon_{ijk}A_iB_j$. No index is summed by convention, a repeated index is never left without its sum, and a sum is never left without its set.

### The Derivative Marks

**No dot.** No derivative is written with a dot. The total derivative with respect to a parameter is written with a fraction and the parameter named: $\frac{d}{dt}$ for the parameter $t$, $\frac{d}{d\tau}$ for the parameter $\tau$, $\frac{d}{dt_r}$ for the parameter $t_r$; inline, the same derivative is written $dq/dt$. The partial derivative is written $\frac{\partial}{\partial t}$ or, inline, $\partial/\partial t$. A higher derivative is written $\frac{d^2}{dt^2}$, $\frac{\partial^2}{\partial t^2}$. The derivative binds to its whole argument, so a power is written outside a bracket, $\left(\frac{dx}{dt}\right)^2$, never as $\frac{dx^2}{dt}$.

**The prime marks the imaginary coordinate, and nothing else.** A prime marks the imaginary coordinate of a complex number: the second coefficient of a complex, split-complex or dual element, $R = r + ir'$ in the complex case, and of a biquaternion coefficient, $R_\mu = r_\mu + ir'_\mu$. It never marks a derivative: a function of one variable is differentiated as $df/dx$, a second derivative as $d^2f/dx^2$, and the value at a point as $\frac{df}{dx}(a)$; a derivative with respect to a coordinate is written $\partial/\partial r'_t$ or $\partial/\partial r_k$ (§*Conventions for Derivation*). No further use of the prime is admitted.

**Labels that are not derivatives.** The second Lorentz label is written $\bar l$, and a spinor index of the conjugate representation is written $\bar\alpha$; the bar on an index marks the conjugate spinor. The conjugate matrix is $\bar\Pi$. These are labels, not derivatives.

**The dual-number derivation is a named operator.** The derivation in the nilpotent direction is written $\partial_{\mathrm{nil}}$, the upright name in the superscript saying which derivation it is, and it is defined by $\partial_{\mathrm{nil}}(q+\varepsilon q')=\varepsilon q'$. It is a derivation of the algebra, not a derivative with respect to a coordinate, so no coordinate is written under its $\partial$; its iterates are $(\partial_{\mathrm{nil}})^2$ and $\exp(t\,\partial_{\mathrm{nil}})$.

**The scope mark.** In geometric calculus the factor differentiated is marked with an underline, $\underline{\partial}(AB)=\underline{\partial}A\,B+\underline{A}\,\underline{\partial}B$, not with a dot.

### The Gradient

**One operator of each order, and every glyph of them carries $\Phi$.** The corpus writes two derivative operators and no more: the **biquaternionic gradient** $\tilde\nabla_\Phi$ of the first order and the **d'Alembertian** $\Box_\Phi$ of the second, together with the two parts they carry, the **spatial gradient** $\vec\nabla_\Phi$ and the **Laplacian** $\Delta_\Phi$. All four glyphs carry the subscript $\Phi$, and the rule admits no exception: no gradient, no Laplacian and no d'Alembertian is written in this corpus without it, and a derivative glyph standing alone does not occur in any article of the series. This section is the only place where the four are defined; every other article writes them as they are fixed here.

**The element, written once.** The coordinate biquaternion is

$$
\tilde R=\sum_{\mu\in\{t,x,y,z\}}R_\mu e_\mu,\qquad R_\mu=r_\mu+i r'_\mu,
$$

four complex coefficients on the four units and eight real parameters. The capital is written here and in the table of §*Index and Notation Conventions*, and nowhere in the calculus: every derivative below is written against a lowercase parameter.

**The derivatives are operators on the material parameters, and on nothing else.** Four of the eight real parameters are differentiated in this series: the imaginary time $r'_t$ and the three real space numbers $r_k$. They are the material ones, and $\Phi$ is their name. The other four, the real time $r_t$ and the three imaginary space numbers $r'_k$, are never written under a $\partial$: they are read on elements, and no article of the series differentiates against them. So a derivative has one of two shapes, $\partial/\partial r'_t$ or $\partial/\partial r_k$, and no derivative of the corpus is written against $R_\mu$, against $\bar R_\mu$ or against any other parameter.

**The coefficient carries no dilation.** The four material parameters are lengths in one and the same unit, and the derivative, the gradient and every sign follow from the algebra alone. A dilation in front of the whole derivative would divide all of its terms and would change no structure, so it is a normalisation and not an object of the theory. No dilation is written, and the fourth coordinate therefore carries no unit the three vector coordinates do not.

**The gradient.** The first-order operator is the sum of the four unit-weighted derivatives on the four material parameters,

$$
\tilde\nabla_\Phi:=-i\,e_t\frac{\partial}{\partial r'_t}+\sum_{k\in\{x,y,z\}}\vec e_k\frac{\partial}{\partial r_k},
\qquad
(\tilde\nabla_\Phi)^{\natural}:=-i\,e_t\frac{\partial}{\partial r'_t}-\sum_{k\in\{x,y,z\}}\vec e_k\frac{\partial}{\partial r_k},
$$

whose tilde marks its scalar part beside its vector part (*Biquaternion Analysis*, §*The Biquaternionic Gradient*). The coefficient of the fourth slot is $-i$ and the coefficient of each space slot is $1$; the vector part of the glyph is the three space slots together, which is why the glyph carries the tilde and not the arrow. It is this conjugate, and no other, that the series composes with.

**The spatial gradient and the Laplacian.** The three space slots are the pure spatial gradient, and its second-order companion is the Laplacian of the corpus,

$$
\vec\nabla_\Phi:=\sum_{k\in\{x,y,z\}}\vec e_k\frac{\partial}{\partial r_k},
\qquad
\Delta_\Phi:=\sum_{k\in\{x,y,z\}}\frac{\partial^2}{\partial r_k^2},
$$

with the divergence $\vec\nabla_\Phi\cdot\vec Q_{\mathrm f}$ and the curl $\vec\nabla_\Phi\times\vec Q_{\mathrm f}$ of the element-valued field $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$ read as the ordinary divergence and curl of its vector part.

**The d'Alembertian.** The second-order operator is the quaternionic norm of the gradient, that is the quaternionic form at its two equal arguments:

$$
\Box_\Phi:=\langle\tilde\nabla_\Phi\rangle_{\natural}=\mathrm{Sc}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\bigr)=\sum_{k\in\{x,y,z\}}\frac{\partial^2}{\partial r_k^2}-\frac{\partial^2}{\partial {r'_t}^2}=\Delta_\Phi-\frac{\partial^2}{\partial {r'_t}^2}.
$$

The three space terms enter with a plus and the fourth with a minus, and the sign is the algebra's own: the temporal coefficient is imaginary and squares to $-1$, while each spatial unit squares to $-e_t$ and the second factor returns $+1$. That is the $(-,+,+,+)$ signature read on the two halves of the sum. The operator is scalar, it acts coefficient by coefficient, and no article of the series defines a second d'Alembertian or writes it without its subscript.

**Why the subscript stands on every glyph.** The derivative is written on the material parameters and on no others, and $\Phi$ is their name: the glyph carries the name of the four parameters it differentiates. An article that writes the informational part writes an element, and no derivative of the corpus is taken against it.

**The low slot spells the operator, or names its component, and nothing else.** A label in the low slot names a distinct operator by spelling what makes it that operator. The label is roman and is read as written, $\tilde\nabla_{\mathrm{gco},\Phi}$ with its companion $\Box_{\mathrm{gco},\Phi}$. A single component index may follow, $\tilde\nabla_{\mathrm{gco},\Phi,\mu}$, and nothing may follow that. Nothing else enters the slot, and the list of what may not is the list of everything that distinguishes one instance of an operator from another rather than one operator from another.

Never a number. A shift is written out, $\tilde\nabla_\Phi+\kappa$, and the glyph keeps its name while the number varies; a glyph such as $\tilde\nabla_{\kappa,\Phi}$ would make the operator a function of a parameter and would have to be read as a different operator at every value of it.

Never a sign or a factor. The operators $-\Box_\Phi$ and $i\tilde\nabla_\Phi$ are written as they stand, and no glyph is reserved for a signed or scaled copy of another: the source's mutual bigradients are $\vec\nabla_{+} = i\tilde\nabla_\Phi$ and $\vec\nabla_{-} = i(\tilde\nabla_\Phi)^{\natural}$, and its wave operator is $-\Box_\Phi$.

Never a subspace or a carrier. On a subspace the gradient is $\tilde\nabla_\Phi$ in the coordinates of that subspace, the coordinates being named in the display and not in the glyph; on $\mathbb{B}_{iH}$ it is $-i$ times the gradient of $\mathbb{B}_{H}$, which is a statement about a coefficient and not a new operator.

Never a coordinate, a chart, a representation, or the variable the operator differentiates. The d'Alembertian is $\Box_\Phi$ and not $\Box_{\Phi,x}$, the covariant gradient is $\tilde\nabla_{\mathrm{gco},\Phi}$ for every field because the representation is a property of the field and is written on it, $\tilde\Xi_\psi$, and a Green's function says in words which of its arguments the operator acts on, $\Box_\Phi G(\tilde R_\Phi,\tilde R_{\Phi,2})$, rather than writing the argument in the slot, $\Box_{\tilde R_\Phi}$.

**A pair of mutual operators is two glyphs, never one glyph with a plus-or-minus.** A pair is written out, one operator at a time, and a formula that holds for both members is written twice: the source's bigradients are $\vec\nabla_{+} = i\tilde\nabla_\Phi$ and $\vec\nabla_{-} = i(\tilde\nabla_\Phi)^{\natural}$, and her wave operator is $\Box_A = \partial^2/\partial\tau^2-\Delta_\Phi$, in her letters and never wearing a $\Phi$ of its own. The rule governs the parameter shifts in the same way: $\tilde\nabla_\Phi+\kappa$ and $\tilde\nabla_\Phi-\kappa$ are two operators and both are written, and $\kappa$ itself is never a subscript.

The reason for the whole rule is one. A coefficient belongs to the element and an argument belongs to the field, so neither may enter the name of the operator, which is one operator for every value, every argument and every chart.

**The Levi-Civita derivative is not this operator.** A curved background carries a metric connection, and the articles on curved spacetime write its covariant derivative as $\nabla_\mu$, with the index it differentiates. It is a differential-geometric object of the manifold, it acts on tensors and not on the algebra, and it is never the gradient of this series. The two never meet in one computation: where a curved background meets a field of this series, the article says which of the two it has written, and the biquaternionic gradient keeps its $\Phi$.

**The sum is written.** The gradient is a sum, and the sum is always spelled out. The shorthand $\vec e_k\partial/\partial r_k$ is not used, because it repeats the index without summing it; the same holds for every contraction of a basis vector, a gamma or a field component with a derivative.

**The conjugates of the gradient.** The gradient is an operator, and its marks are read on the invertibles at fixed parameter: the derivative symbols are held fixed and only the units are conjugated. This fixes the scope of the star, and it is not a claim that $\partial/\partial r'_t$ is real. Read on the units, the quaternion conjugation reverses the three spatial units and fixes the temporal one, $e_t^{\natural}=e_t$ and $\vec e_k^{\natural}=-\vec e_k$, and the Hermitian conjugation does the same, so the two marks agree on the gradient term by term:

$$
\tilde\nabla_\Phi^{*}=(\tilde\nabla_\Phi)^{\natural}.
$$

The gradient carries the coefficient $-i$ on the fourth slot and $1$ on the three space slots, so the fourth term is fixed by both marks and the three spatial terms are reversed by both. That is why it is anti-Hermitian in its temporal slot and Hermitian in its spatial ones, and why the d'Alembertian above is central.

**The forms stay four, the norms are two.** The four forms keep their four conventions, named above in this section, each conjugating its own slot: the quaternionic form conjugates the first argument and the Hermitian form the second, so on a general second argument they are not the same statement. But read at the two equal arguments they give two operators, the Hermitian norm coinciding with the quaternionic bilinear norm and the Krein norm with the plain bilinear norm. The four subsections below carry the four forms, and their norms are the two operators $\Box_\Phi$ and $-\partial^2/\partial {r'_t}^2-\Delta_\Phi$.

**Reading the operator term by term.** The coefficient of the fourth parameter is $-i$ and the coefficient of each of the three space parameters is $1$. There the time derivative is imaginary and the space derivatives are the physical ones, so the spatial operations are the ordinary $\vec\nabla_\Phi=\sum_{k\in\{x,y,z\}}\vec e_k\partial/\partial r_k$, $\Delta_\Phi=\sum_{k\in\{x,y,z\}}\partial^2/\partial r_k^2$, and the ordinary divergence and curl.

The operators, in one table:

| symbol | definition | the parameters it differentiates |
| --- | --- | --- |
| $\tilde R$ | $\sum_{\mu\in\{t,x,y,z\}}R_\mu e_\mu$ with $R_\mu=r_\mu+i r'_\mu$ | the element; the capital is written here and nowhere in the calculus |
| $\tilde\nabla_\Phi$ | $-i\,e_t\partial_{r'_t}+\sum_{k\in\{x,y,z\}}\vec e_k\partial_{r_k}$ | $r'_t,\ r_x,\ r_y,\ r_z$ |
| $(\tilde\nabla_\Phi)^{\natural}$ | $-i\,e_t\partial_{r'_t}-\sum_{k\in\{x,y,z\}}\vec e_k\partial_{r_k}$ | $r'_t,\ r_x,\ r_y,\ r_z$ |
| $\vec\nabla_\Phi$ | $\sum_{k\in\{x,y,z\}}\vec e_k\partial_{r_k}$ | $r_x,\ r_y,\ r_z$ |
| $\Delta_\Phi$ | $\sum_{k\in\{x,y,z\}}\partial^2_{r_k}$ | $r_x,\ r_y,\ r_z$ |
| $\Box_\Phi$ | $\Delta_\Phi-\partial^2_{r'_t}$ | $r'_t,\ r_x,\ r_y,\ r_z$ |

### The Plain Bilinear Product, Its Form and Its Norm

**The product.** The general plain bilinear product is one of the four general products of *Product and Form Conventions*, §*The Twelve Products and Their Names*. On the gradient, with the element-valued field $\tilde Q_{\mathrm f}$ of §*The Gradient*, it is read with $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and $\vec e_j\vec e_k=-\delta_{jk}e_t+\epsilon_{jkl}\vec e_l$, so that the three spatial units carry the field back onto the scalar unit.

A **product** is algebra-valued, and this one holds the divergence, the gradient and the curl of the field in a single object; for the field strength $\tilde F$ the equation $\tilde\nabla_\Phi\tilde F=-\sqrt{\mu}\,\tilde J$, with $\tilde J=ic\rho\,e_t+\vec J$, is the series' Maxwell equation. **Read on the material parameters**, $\vec\nabla_\Phi$ is the physical spatial gradient, so the space part is the ordinary one and the fourth-coordinate part carries the factor $-i$:

$$
\tilde\nabla_\Phi\tilde Q_{\mathrm f}=\Bigl(-i\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}-\vec\nabla_\Phi\cdot\vec Q_{\mathrm f}\Bigr)e_t-i\frac{\partial\vec Q_{\mathrm f}}{\partial r'_t}+\vec\nabla_\Phi Q_{\mathrm{f}t}+\vec\nabla_\Phi\times\vec Q_{\mathrm f} .
$$

The display is the general product with the four material factors of §*The Gradient* substituted: the divergence and the curl carry their own sign on $\mathbb{B}_{\Phi}$. Nothing is redefined: a reader who substitutes the four factors obtains the line, and a reader who does not substitute keeps the general display, which is the operator's own form.

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
\langle\tilde\nabla_\Phi,\tilde Q_{\mathrm f}\rangle=\mathrm{Sc}(\tilde\nabla_\Phi\tilde Q_{\mathrm f})=-i\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}-\vec\nabla_\Phi\cdot\vec Q_{\mathrm f} ,
$$

a scalar, the **contraction** of the derivative with the field in the sign vector $\varepsilon$, the fourth-coordinate slot imaginary and the divergence real. The sign vector $\varepsilon$ belongs to the product and the factors belong to the parameters it differentiates, and the two never merge into one symbol.

**The norm.** The norm is defined with the form, as that form at its two equal arguments:

$$
\langle\tilde\nabla_\Phi\rangle=\langle\tilde\nabla_\Phi,\tilde\nabla_\Phi\rangle=\mathrm{Sc}(\tilde\nabla_\Phi\tilde\nabla_\Phi)=-\frac{\partial^2}{\partial {r'_{t}}^2}-\Delta_\Phi ,
$$

the cross terms cancelling and every second derivative negative, the fourth slot through the coefficient $(-i)^2=-1$ and the three space slots through $\vec e_k\vec e_k=-e_t$. This is not the series' d'Alembertian, which is $\Box_\Phi=\Delta_\Phi-\partial^2/\partial {r'_t}^2$ (§*The Quaternionic Bilinear Product, Its Form and Its Norm*), and it differs from the d'Alembertian by one overall sign.

### The Quaternionic Bilinear Product, Its Form and Its Norm

**The product.** The general quaternionic bilinear product is the second of the four general products of *Product and Form Conventions*, §*The Twelve Products and Their Names*; on the gradient it is $(\tilde\nabla_\Phi)^{\natural}\tilde Q_{\mathrm f}$, the conjugate derivative, read with the same rules, the three spatial units now carrying the field back onto the scalar unit with the opposite sign,

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

a scalar, the **contraction** of the conjugate derivative with the field. It differs from the plain form by the three signs of $\varepsilon$, which are **computed from the product** $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and not assumed: the divergence is back with a plus because the conjugate derivative has already applied $\varepsilon$.

**The norm, and the definition of the d'Alembertian.** The norm is defined with the form, as that form at its two equal arguments, and the two orders of the product agree:

$$
\Box_\Phi=\langle\tilde\nabla_\Phi\rangle_{\natural}=\langle\tilde\nabla_\Phi,\tilde\nabla_\Phi\rangle_{\natural}
=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi)=\mathrm{Sc}(\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural})
=-\frac{\partial^{2}}{\partial {r'_{t}}^{2}}+\Delta_\Phi .
$$

**This is the definition of the d'Alembertian**: the quaternionic norm of the gradient, one operator and one only (*The Four Forms, the Four Algebraic Norms and the Change of Scalars*). It is **scalar**: it multiplies by $e_t$ and acts coefficient by coefficient,

$$
\Box_\Phi\tilde Q_{\mathrm f}=\sum_{\mu\in\{t,x,y,z\}}\bigl(\Box_\Phi Q_{\mathrm{f}\mu}\bigr)e_\mu .
$$

The glyph carries the subscript $\Phi$ like every derivative of the corpus, and **no article of the series defines a second d'Alembertian**; no mass-term sign is left to a local convention.

**There is no second reading.** The operator is $\Box_\Phi=\Delta_\Phi-\partial^2/\partial {r'_t}^2$ everywhere in the corpus: the temporal coefficient of the gradient is $-i$, so the fourth second derivative enters with a minus and the three space ones with a plus. The sign is the algebra's, not a slice's, and no article chooses between two conventions of the operator.

### The Hermitian Product, Its Form and Its Norm

**The product.** The general plain sesquilinear product is the third of the four general products of *Product and Form Conventions*, §*The Twelve Products and Their Names*; it is the plain product applied to the **conjugated** field $\tilde Q_{\mathrm f}^{*}=\bar Q_{\mathrm{f}t}e_t-\overline{\vec Q_{\mathrm f}}$, so that on the gradient it is $\tilde\nabla_\Phi\tilde Q_{\mathrm f}^{*}$, conjugate-linear in the field while the first slot stays $\mathbb{C}$-linear,

$$
\tilde\nabla_\Phi\tilde Q_{\mathrm f}^{*}=\Bigl(-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}+\vec\nabla_\Phi\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t+i\frac{\partial\overline{\vec Q_{\mathrm f}}}{\partial r'_t}+\vec\nabla_\Phi\bar Q_{\mathrm{f}t}-\vec\nabla_\Phi\times\overline{\vec Q_{\mathrm f}} .
$$

The two plus signs on the vector slot are the work of the conjugation, which reversed the sign of the vector part of the field before any derivative met it. The display makes the Hermitian product usable, because its scalar slot is the one that survives the conjugate transpose: the material reading carries an imaginary fourth-coordinate derivative and a real divergence.

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

a scalar, the **contraction** of the derivative with the **conjugated** field in the sign vector $\varepsilon$. Taken on the scalar field it gives the **kinetic density**, the scalar part of the product of the two conjugated gradients,

$$
\mathrm{Sc}\bigl[((\tilde\nabla_\Phi)^{\natural}\tilde\Phi^{*})(\tilde\nabla_\Phi\tilde\Phi)\bigr]=-\frac{\partial\Phi^{*}}{\partial r'_t}\frac{\partial\Phi}{\partial r'_t}+\sum_{k\in\{x,y,z\}}\frac{\partial\Phi^{*}}{\partial r_k}\frac{\partial\Phi}{\partial r_k}
$$

in which the conjugate stands on the first factor and no absolute value is taken; the two time derivatives are imaginary, so that scalar part is $-\lvert\partial\phi/\partial r'_t\rvert^2+\lvert\vec\nabla_\Phi\phi\rvert^2$, and the kinetic term the series writes is

$$
\mathcal L_{\mathrm{kin}}=-\mathrm{Sc}\bigl[((\tilde\nabla_\Phi)^{\natural}\tilde\Phi^{*})(\tilde\nabla_\Phi\tilde\Phi)\bigr]=\Bigl|\frac{\partial\phi}{\partial r'_t}\Bigr|^2-\lvert\vec\nabla_\Phi\phi\rvert^2 ,
$$

the kinetic density of the Klein–Gordon article (*Hamiltonian Field Theory in Biquaternionic Form*). **On the gradient** the form itself is $-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}+\vec\nabla_\Phi\cdot\overline{\vec Q_{\mathrm f}}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments. By §*The Gradient*, $\tilde\nabla_\Phi^{*}=(\tilde\nabla_\Phi)^{\natural}$, and


so the Hermitian norm of the gradient is the d'Alembertian, the same operator as its quaternionic bilinear norm. The **Hermitian form is the one positive-definite form of the four on the biquaternion layer**, $\langle\tilde Q\rangle_{*}=\sum_{\mu\in\{t,x,y,z\}}\lvert R_\mu\rvert^2$ on the elements, and its square root is the topological norm $\lVert\tilde Q\rVert$; positivity is a property of the elements, the norm of this subsection being the operator $\Box_\Phi$. **On the gradient** it is the same operator, $\Box_\Phi=\Delta_\Phi-\partial^2/\partial (r'_t)^2$. Positivity is untouched by the sign pattern: the form is positive on the elements, and what changes is the operator's own sign and not the form's.

### The Krein Product, Its Form and Its Norm

**The product.** The general quaternionic sesquilinear product is the fourth of the four general products of *Product and Form Conventions*, §*The Twelve Products and Their Names*; it is the conjugate derivative applied to the conjugated field, $(\tilde\nabla_\Phi)^{\natural}\tilde Q_{\mathrm f}^{*}$, the companion of the quaternionic bilinear product in the second slot,

$$
(\tilde\nabla_\Phi)^{\natural}\tilde Q_{\mathrm f}^{*}=\Bigl(-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}-\vec\nabla_\Phi\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t+i\frac{\partial\overline{\vec Q_{\mathrm f}}}{\partial r'_t}-\vec\nabla_\Phi\bar Q_{\mathrm{f}t}+\vec\nabla_\Phi\times\overline{\vec Q_{\mathrm f}} .
$$

The two lines are the companions of the quaternionic pair: the four products of the section are four readings of one derivative on one set of material coordinates, and no line needs a convention beyond the four factors of §*The Gradient*.

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

a scalar, the **contraction** of the conjugate derivative with the conjugated field, read on the material part. **On the gradient** it is $-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}-\vec\nabla_\Phi\cdot\overline{\vec Q_{\mathrm f}}$, the divergence back with a plus because the conjugate derivative has already applied $\varepsilon$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments; on the gradient, since $\tilde\nabla_\Phi^{*}=(\tilde\nabla_\Phi)^{\natural}$ (§*The Gradient*),

$$
\langle\tilde\nabla_\Phi,\tilde\nabla_\Phi\rangle_{\natural*}=\langle\tilde\nabla_\Phi\rangle_{\natural*}=\mathrm{Sc}\bigl((\tilde\nabla_\Phi)^{\natural}(\tilde\nabla_\Phi)^{\natural}\bigr)=-\frac{\partial^2}{\partial {r'_t}^2}-\Delta_\Phi
$$

so the Krein norm of the gradient **coincides with the plain bilinear norm**. It is the indefinite partner of the Hermitian form, and on the elements it is the form of inertia $(1,3)$ whose diagonal on the material parameters is ${r'_t}^2-r_x^2-r_y^2-r_z^2$: Hermitian, indefinite — positive where ${r'_t}^2>r_x^2+r_y^2+r_z^2$ and negative where the opposite inequality holds — so it carries no positivity. It is the form of the indefinite theory — the Krein space — and not of the contractions of these subsections. Read on the gradient, it is $-\frac{\partial^2}{\partial {r'_{t}}^2}-\Delta_\Phi$, both terms negative. The two norms agree with each other, and both differ from $\Box_\Phi$ by one overall sign, which is the sign separating the indefinite pair from the definite one.

**A contraction is a form, never an index.** The series has one metric, the unit metric $\delta_{\mu\nu}=(1,1,1,1)$, and it is the identity, so no index is raised and none is lowered: a raised index would be the same index. What the product carries is the plain weight $\varepsilon$, and the weight is not a metric. Where a text with covariant indices contracts a derivative with a field through a raised and a lowered index, the series writes the quaternionic form $\langle\tilde\nabla_\Phi,\tilde Q_{\mathrm f}\rangle_{\natural}$; where it contracts two derivatives, the series writes the quaternionic norm $\langle\tilde\nabla_\Phi\rangle_{\natural}=\Box_\Phi$; and where it moves an index through a metric, the series writes the element $\tilde Q_{\mathrm f}$ itself, the weight being the sign vector inside the product.

**The rule is one rule on both slices.** A contraction never raises an index and never lowers one, on $\mathbb{B}_{\Phi}$ or on $\mathbb{B}_{\Psi}$, because the metric is the identity on both. What changes between the slices is only the coefficient the contraction carries: on $\mathbb{B}_{\Phi}$ the fourth-coordinate component is multiplied by $-i$ and the three space components by $1$, while on $\mathbb{B}_{\Psi}$ the fourth-coordinate component is multiplied by $1$ and the three space components by $-i$. A reader who checks a component formula on either slice checks those four numbers and nothing else, and the check is complete.

## The Two First-Order Equations and Their Symbol

**The pair operator is not allowed.** The two chiral equations are two equations, and the series writes two equations. No letter gathers them into one object on $\mathbb{B}\oplus\mathbb{B}$: no $\mathbb{D}$, no two-by-two array and no subscripted glyph. The gathered letter hides the four statements that carry the algebra. Its adjoint is a single sign, so it cannot hold a derivative term that is anti-Hermitian and a mass term that is Hermitian, and $\mathbb{D}^{\dagger}=-\mathbb{D}$ covers the massless operator only. Its metric is chosen silently, diagonal on the two slots and never written. Its inertia is invisible, because the square reports one scalar for the two members. And its carrier is ambiguous, eight complex dimensions or four, with no mark to say which. The two equations state all four, one after the other.

**The two equations.** The dynamics of a field of mass $m$ is

$$
\tilde\nabla_\Phi\Psi_R=m\,\Psi_L,
\qquad
(\tilde\nabla_\Phi)^{\natural}\Psi_L=m\,\Psi_R,
$$

and the massless limit is the same two lines at $m=0$. Every coordinate form of a field equation in the corpus is a **coordinate form** of these two and not a second dynamics.

**The mass is the coupling.** Each line multiplies one chiral part and returns a multiple of the other. $m$ is real and central, it commutes with both gradients, and it is the only term of either line that names the other part.

**Neither gradient squares to the d'Alembertian, and their composition does.** Written as a product of elements, $\tilde\nabla_\Phi^{2}$ is not $\Box_\Phi$: $e_t$ commutes with the three spatial units, so the mixed derivatives survive and the square is not scalar. Only the composition with the conjugate is scalar, $(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\Box_\Phi$, and this is why the massive dynamics needs two lines and not one: one gradient on one field is first order and cannot equal a second-order operator, so no one-field first-order massive equation exists in this algebra. The free equation stays first order on one field, and the mass is what needs the second field.

**The square, line by line.** Composing each line with the conjugate of the other gives

$$
(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi\Psi_R=m^{2}\Psi_R,
\qquad
\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}\Psi_L=m^{2}\Psi_L,
$$

that is $(\Box_\Phi-m^{2})\Psi_R=0$ and $(\Box_\Phi-m^{2})\Psi_L=0$. Each part obeys the Klein–Gordon equation on its own, with the same second-order operator.

**The symbol.** On a plane wave the gradient acts as left multiplication by the momentum element, $\tilde K=i\tilde Q_2=-p_t\,e_t+i\vec p$ with $\tilde K\tilde K^{\natural}=p_t^{2}-\lvert\vec p\rvert^{2}$. The symbol of the two equations is the two lines with each gradient read at its plane-wave value,

$$
\tilde K\,w_R=m\,w_L,
\qquad
\tilde K^{\natural}\,w_L=m\,w_R,
$$

and the two lines share one condition. Composing them returns $\tilde K^{\natural}\tilde K\,w=\bigl(p_t^{2}-\lvert\vec p\rvert^{2}\bigr)w$, so the symbol is singular exactly on $p_t^{2}-\lvert\vec p\rvert^{2}=m^{2}$ and nowhere else.

**The inverse is one scalar and two kernels.** With $G$ the Green's function of the d'Alembertian, $(\Box_\Phi-m^{2})G=\delta$, the solution of the two lines with a source is the pair of kernels

$$
S_L=i\bigl(\tilde\nabla_\Phi+m\bigr)G,
\qquad
S_R=i\bigl((\tilde\nabla_\Phi)^{\natural}+m\bigr)G,
$$

and substitution returns $i\delta$ in each line, because the cross terms cancel and $\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=(\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi=\Box_\Phi$ with $m$ central. The inverse introduces no new object.

**Marks.** There is no glyph for the two equations and no subscript for a sector or a chart. A subscript on a kernel names the part it carries, $S_L$ and $S_R$. The gradient has one spelling with one subscript, $\tilde\nabla_\Phi$, and $\natural$ for its conjugate; there is no unsubscripted form of it, and no derivative of the corpus carries $\Psi$.

**The equations are material.** The two lines are written on the material parameters, in the letters $r'_t$ and $r_k$, and the corpus writes no informational twin of them. There is no second gradient to change and no $\Psi$ on an operator. The second-order operator is the d'Alembertian of §*The Quaternionic Bilinear Product, Its Form and Its Norm*, $\Box_\Phi=\Delta_\Phi-\partial^2/\partial {r'_{t}}^2$.

## The Transposition of the Gradient

**The transposed reading.** A gradient acts on the factor written to its right, $\tilde\nabla_\Phi\tilde Q_1$. The long arrow over the glyph marks the other reading: the operator acts on the factor written to its left, and the arrow points at that factor, $\tilde Q_1\overleftarrow{\tilde\nabla_\Phi}$. The mark belongs to the operator and not to the field, and it is not the short arrow of the pure part, which sits on an element and marks its vector part alone. Read this way, the gradient has its derivative to the right of the element it differentiates,

$$
\tilde Q_1\overleftarrow{\tilde\nabla_\Phi}:=-i\frac{\partial\tilde Q_1}{\partial r'_t}\,e_t+\sum_{k\in\{x,y,z\}}\frac{\partial\tilde Q_1}{\partial r_k}\,\vec e_k ,
$$

the same four coefficients in the same four directions, with the unit written after each. The integration articles write this object $\vec\nabla_\Phi^{R}$ and use it wherever a derivative has to be moved off a product. It is not a second operator: it is the gradient with its two factors exchanged, and the exchange is what the identity below computes.

**The identity.** For every element-valued field $\tilde Q_1$,

$$
\boxed{\;\bigl(\tilde Q_1\overleftarrow{\tilde\nabla_\Phi}\bigr)^{\natural}=(\tilde\nabla_\Phi)^{\natural}\tilde Q_1^{\natural}\;}
\qquad\Longrightarrow\qquad
\tilde Q_1\overleftarrow{\tilde\nabla_\Phi}=\bigl((\tilde\nabla_\Phi)^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}.
$$

**The proof is one term.** The involution is $\mathbb{C}$-linear, it acts on the units at fixed parameter, and it commutes with the derivative, because a derivative holds its parameter fixed. Written out, the gradient is $-i\,e_t\,\partial/\partial r'_t+\sum_{k\in\{x,y,z\}}\vec e_k\,\partial/\partial r_k$, so every term is a scalar coefficient, a unit and a derivative, and the involution reads only the unit: $e_t^{\natural}=e_t$ and $\vec e_k^{\natural}=-\vec e_k$. The temporal term on the left is therefore $(\partial\tilde Q_1/\partial r'_t)^{\natural}(-i\,e_t)=-i\,e_t\,\partial\tilde Q_1^{\natural}/\partial r'_t$, which is the temporal term of $(\tilde\nabla_\Phi)^{\natural}\tilde Q_1^{\natural}$, and each space term is $(\partial\tilde Q_1/\partial r_k)^{\natural}(-\vec e_k)=-\vec e_k\,\partial\tilde Q_1^{\natural}/\partial r_k$, which is the corresponding space term. Adding the four gives the boxed line, and $\natural^{2}=\mathrm{id}$ gives the arrow back.

**What it says.** A right action is the conjugation of a left action: conjugate the field, apply the conjugate gradient from the left, conjugate the result. In the notation of §*The Two Sides and the Renaming Theorem*, $R_{\tilde\nabla_\Phi}=\natural\circ L_{(\tilde\nabla_\Phi)^{\natural}}\circ\natural$, read on a differential operator rather than on a multiplication. The statement needs no equation, no mass, no chirality and no pair of fields. It is an identity between operators, true of any $\tilde Q_1$: a solution, a non-solution, a product, a constant.

**The instance that hides the generality.** The chiral pair is the case usually quoted. From $(\tilde\nabla_\Phi)^{\natural}\Psi_L=m\Psi_R$, transposing with $\tilde Q_1=\Psi_L^{\natural}$ and using $m^{\natural}=m$,

$$
(\tilde\nabla_\Phi)^{\natural}\Psi_L=m\,\Psi_R
\qquad\Longrightarrow\qquad
\Psi_L^{\natural}\overleftarrow{\tilde\nabla_\Phi}=m\,\Psi_R^{\natural},
$$

one line, with the derivative now written to the right of $\Psi_L^{\natural}$ and the same mass in place. Read alone, the pair suggests that the right action is a property of the Dirac equation. It is not: the two lines hold of $\tilde\nabla_\Phi\Psi_R=m\Psi_L$ as well, of a massless field, and of any equation in which one field stands to the right of a derivative. The equation supplies the right-hand side; the identity does not depend on it.

**Why the superscript $R$ is nevertheless written.** The identity holds for a field, and a product of fields is a field. What it does not do is move the derivative off one factor of a product while the other stays. On $\tilde Q_1\tilde Q_2$ the Leibniz rule gives

$$
(\tilde Q_1\tilde Q_2)\overleftarrow{\tilde\nabla_\Phi}=-i\Bigl(\frac{\partial\tilde Q_1}{\partial r'_t}\tilde Q_2+\tilde Q_1\frac{\partial\tilde Q_2}{\partial r'_t}\Bigr)e_t+\sum_{k\in\{x,y,z\}}\Bigl(\frac{\partial\tilde Q_1}{\partial r_k}\tilde Q_2+\tilde Q_1\frac{\partial\tilde Q_2}{\partial r_k}\Bigr)\vec e_k ,
$$

with the unit after each bracket. It does not pass to the left of $\tilde Q_2$: that is a commutation with the units, allowed only when $\tilde Q_2$ is central. Nor is the rule $-i(\partial\tilde Q_1/\partial r'_t)e_t\tilde Q_2+\sum_{k\in\{x,y,z\}}(\partial\tilde Q_1/\partial r_k)\vec e_k\tilde Q_2$, which differs from the first term by the defect $-i(\partial\tilde Q_1/\partial r'_t)[\tilde Q_2,e_t]+\sum_{k\in\{x,y,z\}}(\partial\tilde Q_1/\partial r_k)[\tilde Q_2,\vec e_k]$. That is the case §*The Two Sides and the Renaming Theorem* excludes, and the case the integration articles meet. There the derivative is named $\vec\nabla_\Phi^{R}$ after the factor it differentiates, and the name is a position, not a second operator.

**The slots.** The transposition is the exchange of the two slots of a basis operator, read on a differential operator. In the language of *Operator Chirality on the Biquaternion Algebra*, §*Conjugation Exchanges the Sides*, the map that carries a left multiplier to a right multiplier is $\mathsf C$, the conjugation written as a congruence, $\mathsf C L(a^{\natural})\mathsf C=R(a)$, which in the axis-free frame is the switch $\mathsf D=\operatorname{diag}(1,-1,-1,-1)$ and is the $\mathsf C$ of the matrix form above. A left action of the gradient and a right action of the same gradient therefore have arrays that agree up to that sign and that order, which is where the phases of the two sides come from.

**What it is not.** Not a transpose without conjugation: $\mathsf C$ is not the identity, and $\mathsf C^{\mathsf T}\mathsf C=I$ with $\det\mathsf C=-1$ make the congruence a congruence and not a similarity. Not the adjoint either: the dagger carries the integration by parts and the boundary term, while $\natural$ carries the invertibles alone at fixed coordinate; the two agree on the gradient, $\tilde\nabla_\Phi^{*}=(\tilde\nabla_\Phi)^{\natural}$, and part on a general element.

**Verified.** On random polynomial fields in the four coordinates the boxed line holds at residual $0.0$, the reconstruction from the conjugate at $0.0$, the chiral instance at $0.0$, and the product rule above at $0.0$; on $\tilde Q_1=x\vec e_x$ and $\tilde Q_2=\vec e_y$ the naive rule returns $-\vec e_y$ where the product rule returns $+\vec e_y$. The anti-automorphism it uses holds at residual $1.0\times10^{-15}$ over $200$ random pairs; the automorphism that would be needed if the units were not reversed fails at $2.7\times10^{1}$.

## Summary

An operator acting by multiplication **is** the element it multiplies by, so its glyph is the glyph of that element and the marks are read on it as on the element. The named operators take an upright capital and carry the element in the subscript: left multiplication $L_{\tilde Q}$, right multiplication $R_{\tilde Q}$, the two-sided $L_{\tilde Q_1}R_{\tilde Q_2}$, the two-sided operator $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$, the inner derivation $\operatorname{ad}_{\tilde Q}$ and the automorphism $\operatorname{Ad}_{\tilde Q}$. The two-sided operator with no qualifier is the bilinear one, and it is quadratic in $\tilde Q$, not bilinear. The side of an action is position, $D\psi$ against $\psi D$; the two are exchanged by the quaternion conjugation, $(\psi D)^{\natural}=D^{\natural}\psi^{\natural}$, so a right action on a field is a left action on the conjugate field, and no glyph marks a side. The superscript $R$ marks the right derivative, the one case the exchange does not reach, and on the gradient even that case is a conjugation: $\tilde Q_1\overleftarrow{\tilde\nabla_\Phi}=\bigl((\tilde\nabla_\Phi)^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}$, so a right action is the left action of the conjugate gradient on the conjugate field, and the identity needs no equation.

The **dagger** is the general adjoint of an operator, never of an element, and it is not a fifth conjugation: several adjoints arise at once, one for each form and one for each two-sided operator, and the dagger is the mark that covers them all. An operator written as an array — a linear map on a coordinate column, a matrix in the $2\times2$ image or a regular matrix — carries no tilde. The **Fock exception** is the one mark that says a glyph is an operator and not an element of the algebra, and its superscript $\mathrm{fop}$ is fixed in *Index and Notation Conventions*.

No derivative is written with a dot, and a prime marks the imaginary coordinate and nothing else. Every partial derivative is written with $\partial$ and its variable, the subscript is a component index and never a derivative, and every derivative is written against a material parameter, $\partial/\partial r'_t$ or $\partial/\partial r_k$, with no factor of two and no dilation in front. Every derivative operator of the corpus carries the subscript $\Phi$: the gradient $\tilde\nabla_\Phi$, its conjugate $(\tilde\nabla_\Phi)^{\natural}$, the spatial gradient $\vec\nabla_\Phi$, the Laplacian $\Delta_\Phi$ and the d'Alembertian $\Box_\Phi$. None of the five is ever written without it, and no glyph of the corpus names a gradient, a Laplacian or a d'Alembertian of the informational part.

The two derivative operators of the corpus are the **biquaternionic gradient** $\tilde\nabla_\Phi=-i\,e_t\partial/\partial r'_t+\sum_{k\in\{x,y,z\}}\vec e_k\partial/\partial r_k$ and the **d'Alembertian** $\Box_\Phi=\langle\tilde\nabla_\Phi\rangle_{\natural}=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde\nabla_\Phi)$, the quaternionic norm of the gradient, with the **spatial gradient** $\vec\nabla_\Phi$ and the **Laplacian** $\Delta_\Phi$ as their parts; every one of the five glyphs carries the subscript and none is written without it; the operator is scalar and acts coefficient by coefficient. The two derivatives act on two chiral parts, and the series writes the dynamics as two equations, $\tilde\nabla_\Phi\Psi_R=m\Psi_L$ and $(\tilde\nabla_\Phi)^{\natural}\Psi_L=m\Psi_R$, of §*The Two First-Order Equations and Their Symbol*. The pair operator $\mathbb{D}$ is not allowed: it hides the adjoint, the metric and the signs, and its square is $\Box_\Phi$ on each part only after composing the two lines. On $\mathbb{B}_{\Phi}$ the operator is $\Delta_\Phi-\partial^2/\partial {r'_t}^2$, which is the series' d'Alembertian and not the wave operator of the opposite overall sign. A low sector mark names the sector of the coefficients and not a slice.

The four products are read on the gradient: the plain bilinear product holds the divergence, the gradient and the curl of a field in one object; the quaternionic bilinear product reads the conjugate derivative; the Hermitian product gives the definite form; and the Krein product gives the indefinite one, whose norm coincides with the plain bilinear norm. **A contraction is a form, never an index**: the metric is the sign vector inside the product, and no index is raised or lowered.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q}$, $R_{\tilde Q}$ | Left and right multiplication by the element |
| $L_{\tilde Q_1}R_{\tilde Q_2}$ | The two-sided operator, $L_{\tilde Q_1}R_{\tilde Q_2}$ |
| $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ | The bilinear two-sided operator; $\mathcal{T}_{a,b}$ the sesquilinear one |
| $\operatorname{ad}_{\tilde Q}$, $\operatorname{Ad}_{\tilde Q}$ | The inner derivation and the automorphism |
| ${}^{\dagger}$ | The general adjoint of an operator, never of an element |
| $\partial/\partial r'_t$, $\partial/\partial r_k$ | The two shapes a derivative takes: the material time and a material space coordinate; real parameters, so no dilation stands in front |
| $\tilde\nabla_\Phi=-i\,e_t\partial_{r'_t}+\sum_{k\in\{x,y,z\}}\vec e_k\partial_{r_k}$ | The biquaternionic gradient, the one first-order derivative operator of the corpus |
| $\vec\nabla_\Phi=\sum_{k\in\{x,y,z\}}\,\vec e_k\,\partial/\partial r_k$ | The pure spatial gradient |
| $\Box_\Phi=\langle\tilde\nabla_\Phi\rangle_{\natural}$ | The d'Alembertian, the quaternionic norm of the gradient |
| $\tilde R=\sum_{\mu\in\{t,x,y,z\}} R_\mu e_\mu$ | The variable, $R_\mu=r_\mu+i r'_\mu$; the capital is written once, at the definition of the gradient, and every derivative after it is written on a lowercase parameter |
| $\tilde\nabla_{\Phi}$, $(\tilde\nabla_{\Phi})^{\natural}$ | The gradient and its conjugate on the material coordinates, $\tilde\nabla_{\Phi}=-i\,e_t\partial_{r'_t}+\sum_{k\in\{x,y,z\}}\vec e_k\partial_{r_k}$ and $(\tilde\nabla_\Phi)^{\natural}=-i\,e_t\partial_{r'_t}-\sum_{k\in\{x,y,z\}}\vec e_k\partial_{r_k}$, with the tuples $(-i,1,1,1)$ and $(-i,-1,-1,-1)$ on $r'_t$ and $r_k$; both anti-Hermitian |
| $\vec\nabla_{\Phi}$, $\Delta_{\Phi}$, $\Box_{\Phi}$ | The spatial gradient, the spatial Laplacian and the d'Alembertian of the corpus, $\vec\nabla_{\Phi}=\sum_{k\in\{x,y,z\}}\vec e_k\partial_{r_k}$ and $\Box_{\Phi}=\Delta_{\Phi}-\partial^2/\partial {r'_t}^2$ |
| $\mathrm{fop}$ | The Fock-operator mark, the one exception to the element rule |
| $^{\natural}$ | The quaternion conjugation, $a^{\natural}=(a_0,-a_1,-a_2,-a_3)$; an anti-automorphism, $(ab)^{\natural}=b^{\natural}a^{\natural}$ |
| $(\psi D)^{\natural}=D^{\natural}\psi^{\natural}$ | The exchange of the two sides: a right action on $\psi$ is a left action on $\psi^{\natural}$ |
| $\vec\nabla_\Phi^{R}$ | The right gradient, $F\vec\nabla_\Phi^{R}=-i\,(\partial F/\partial r'_t)\,e_t+\sum_{k\in\{x,y,z\}}(\partial F/\partial r_k)\,\vec e_k$; used only where a derivative meets two distinct factors |
| $\overleftarrow{\ }$ | The long arrow over an operator: it acts on the factor written to its left, and the arrow points at that factor; it is not the short arrow of the pure part |
| $\tilde Q_1\overleftarrow{\tilde\nabla_\Phi}$ | The same gradient transposed, $-i(\partial\tilde Q_1/\partial r'_t)e_t+\sum_{k\in\{x,y,z\}}(\partial\tilde Q_1/\partial r_k)\vec e_k$; the right action, equal to $\bigl((\tilde\nabla_\Phi)^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853). The original formulation, and the source of the quaternion conjugation and its notation.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636. The biquaternion conjugations and the conventions of the complexified algebra in the applied literature.
