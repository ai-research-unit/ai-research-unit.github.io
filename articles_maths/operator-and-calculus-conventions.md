# __Operator and Calculus Conventions__

## Introduction

An operator that acts by multiplication is the element it multiplies by, and its glyph is the glyph of that element; an operator written as an array carries no tilde. This article fixes the named operators, the dagger, the array rule and the Fock exception, and then the calculus: the derivative marks, the gradient, the d'Alembertian, and the four products read on the gradient.

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
| sandwich (default: bilinear) | $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}=L_{\tilde Q}R_{\tilde Q^{*}}=\operatorname{H}_{\tilde Q}$ |
| inner derivation | $\operatorname{ad}_{\tilde Q_4}(\tilde Q_1)=[\tilde Q_4,\tilde Q_1]$ |
| automorphism | $\operatorname{Ad}_{\tilde Q_4}$ |

**The default sandwich.** *Sandwich* with no qualifier is the **bilinear sandwich** $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$. The qualifier separates it from the **sesquilinear sandwich** $\mathcal{T}_{a,b}=L_{a}R_{b}\circ\varkappa$, $\mathcal{T}_{a,b}(\tilde Q_1)=a\tilde Q_1^{*}b$, whose star acts on the argument. The bilinear sandwich is quadratic in $\tilde Q$, not bilinear: $\mathrm{Sd}_{\lambda\tilde Q}=\lvert\lambda\rvert^{2}\mathrm{Sd}_{\tilde Q}$. The word *bilinear* names the family $L_{a}R_{b}$ from which the sandwich is cut. The dagger is the adjoint of an operator and is never part of an operator's name.

The tilde sits in the subscript because it belongs to the element, not to the operator: $L_{\tilde Q}$ is an operator, $\tilde Q$ is the element that generates it. In $L_{\tilde Q_1}R_{\tilde Q_2}$ the subscripts are positional: the first is the left multiplier and the second the right multiplier, while the argument occupies the third slot.

**The basis operators.** The four units are written in the subscript, $L_{e_\mu}$ and $R_{e_\mu}$, and nowhere else: the short form $L_\mu$ is not used in this corpus. The right family is read from the left one by the exchange $\mathsf S$ of the two mixed Peirce units, $R_{e_\nu}=\mathsf S L_{e_\nu}^{\mathsf T}\mathsf S^{-1}$, and the sixteen two-sided operators $L_{e_\mu}R_{e_\nu}$ are the matrix basis and the basis operator table of *Matrix Representations Conventions*, §*The Clifford Structure*; the gamma set is five of them up to $i$, $\gamma_0=iL_{e_t}R_{\vec e_x}$, $\gamma_1=iL_{\vec e_x}R_{\vec e_y}$, $\gamma_2=iL_{\vec e_y}R_{\vec e_y}$, $\gamma_3=iL_{\vec e_z}R_{\vec e_y}$, $\gamma_5=-iL_{e_t}R_{\vec e_z}$; the last of them is the fifth basis operator of the frame, written $\mathsf{V}_{\mathrm{vol}}$ in the operator articles.

**The spin operator and the words built on it.** The generator of the rotations is $\tilde S_k=\tfrac12 i\vec e_k$, an operator whose glyph is the glyph of its element, like every operator of this section. The three words built on it — the **spin**, the **elementary spinor** and the **Dirac spinor** — are fixed in *Special Element and Peirce Conventions*, §*The Spin Convention* and §*The Spinor Convention*, and are not restated here.

**The two marks on a glyph that is also an operator.** An operator read through its element follows the element rule in full.

- A glyph read with its scalar part, four components: the tilde. The biquaternionic gradient $\tilde\nabla$ of §*The Gradient* is the algebraic example, and the canonical momentum $\tilde p=p_te_t+\vec p$ carries the same mark.
- A pure glyph, three components: the arrow. The momentum $\vec p=\sum_k\vec e_kp_k$ is the example, and $\nabla=\sum_k\,\vec e_k\,\partial/\partial R_k$ is the fixed spatial gradient, which carries no second mark (§*The Gradient*).

The gradient decides the case cleanly: $\tilde\nabla$ is not pure, because its $e_t$ term carries $\partial/\partial R_t$, while $\nabla$ is pure. The case follows the layer: a pure operator of the quaternion layer stays lower case, $\vec p$, and one of the biquaternion layer takes the upper case, $\vec P$; where the letter already names another object of the layer, a subscript fixes the operator.

**The mark of a part, and the side carried by position.** The only arrow on a glyph is the short one, and it marks the **pure part**: $\vec e_x$, $\vec p$. The long arrow that sits over an operator is a different mark and not a second arrow of the same kind: it is the mark of the transposed reading, fixed in §*The Transposition of the Gradient*. The side of an action is not marked at all. It is carried by position, $b\psi$ against $\psi b$, the actor written on the side from which it acts, and position is unambiguous because the operand is itself a glyph.

**What names a side where position is not enough.** Three signs, each of which the corpus needs for a purpose of its own.

- $\natural$ marks the conjugation of an element, $a^{\natural}=(a_0,-a_1,-a_2,-a_3)$, and it is what carries a change of side, because it is an anti-automorphism: $(ab)^{\natural}=b^{\natural}a^{\natural}$, hence $(\psi D)^{\natural}=D^{\natural}\psi^{\natural}$, and a right action on $\psi$ is a left action on $\psi^{\natural}$. The theorem is below, §*The Two Sides and the Renaming Theorem*.
- $L_a$ and $R_a$ name a side outright when a statement is about operators rather than about fields, and the basis operator $L_{a}R_{b}$ prints both sides at once. The label of the side of a basis operator is the **operator chirality** — the left slot, the right slot, or both — fixed in *Operator Family Conventions*, §*The Slot Label, Which Is the Chirality*.
- The superscript $R$ marks the one case that position alone leaves genuinely ambiguous: a derivative that differentiates the factor written to its left, $F\nabla^{R}=\sum_\mu(\partial F/\partial R_\mu)e_\mu$. It is used only inside a product of two distinct factors, which is where the theorem below does not reach.

**The dagger.** The dagger is the general adjoint of an operator, never of an element: $(L_a)^{\dagger}=L_{a^{*}}$. Several adjoints arise at once — one for each form, and one for each of the sandwiches — and the dagger is the mark that covers them all, of which the others are the instances. It is not a fifth conjugation: it belongs to the operators and not to the algebra. Where a dagger is written on an element the writing is an abuse: the mark that was meant is the star for the Hermitian conjugation, or the natural sign for the quaternion conjugation, according to the conjugation in view. The dagger is added to the glyph and does not replace the element's mark: the arrow states purity, which the adjoint preserves; the tilde states a glyph read with its scalar part, which the adjoint also preserves. Where the adjoint in view is the formal algebraic one of the definite form, the two marks are written together, dagger first: $(L_a)^{\dagger}=(L_a)^{*}=L_{a^{*}}$ and $\tilde\nabla^{\dagger}=\tilde\nabla^{*}=\tilde\nabla^{\natural}$. The identification is formal: the $L^2$ adjoint of a derivative carries the sign of the integration by parts, and it is not the dagger of this convention.

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
3. **The side itself on display.** For the two-sided action $a\psi b$, the mirror coupling, or the exchange of the two slots of a basis operator, conjugating the field destroys what is being displayed. There both factors stay in place and the side is named by position, or by $L_a$ and $R_a$.

**The consequence for the corpus.** Every equation that acts on a single biquaternion field is written on the left. The ones that would read as acting on the right are the same equations on the conjugate field, and the chiral pair is the instance: with $\Phi=\tilde\Psi^{\natural}$, the pair $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$ and $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$ is complete as written, both equations acting from the left, and $\natural$ is what separates them. Across the $404$ files and $10\,196$ display equations of the physics corpus no glyph names a side: the side is position, the conjugation is $\natural$, and the exchange is $N$.

## Conventions for Derivation

In this work, subscripts denote vector components, not partial derivatives as in the PDE convention; every partial derivative is written explicitly with $\partial$ followed by its variable, and no subscript is ever attached to the $\partial$ of a derivative. A subscript is therefore a component index, as in $v_x$ for the component of a velocity along an axis, or a label, as in $\tilde U_{\mathrm b}$; it never denotes a derivative. The derivative with respect to a coordinate is written $\partial/\partial R_\mu$, and in a fixed direction $\partial/\partial R_t$, $\partial/\partial R_x$, $\partial/\partial R_y$ or $\partial/\partial R_z$; a coordinate is never left under the $\partial$, so none of the abbreviated spellings occurs, and the rule admits no exception for a derivative, neither on a free index nor on any other. A derivative with respect to a variable that is not a coordinate is written the same way, its variable named in full: the Lagrangian derivative puts the function in the numerator, $\partial L/\partial w$, so that where a PDE text writes $L_u$ and $L_p$ the calculus-of-variations and partial-differential-equation articles write $\partial L/\partial w$ and $\partial L/\partial p$; the second derivative has the same shape, $\partial^2 L/\partial w^2$. The function is named in the numerator whenever it is a letter of its own, as for a Lagrangian, a Hamiltonian or a generating function; the slashed form $\partial/\partial u$ is kept where the symbol is an operator or where the operand is a compound expression rather than a single letter. The derivative $\partial/\partial R_t$ is the derivative along the fourth coordinate: on the material sector, where $R_t=i r'_t$, it equals $-i\,\partial/\partial r'_t$, and $r'_t$ is a real coefficient and not one of the coordinates, so the derivative with respect to it is written out as $\partial/\partial r'_t$.

**A subscript on an operator names its degree, its place or its bundle.** The rule governs the derivative of a function or a field, which names its variable after the $\partial$. It does not forbid a label on an operator that differentiates nothing: the chain boundary is $\partial_n:C_n\to C_{n-1}$ and the face maps are $\partial_i$, with the degree in the subscript; the distinguished boundary of a polydisc is $\partial_0D$; the tame symbol is $\partial_v$, with the place; the twisted Dolbeault operator is $\bar\partial_E$, with the bundle. These are operator labels, in the sense of *Index and Notation Conventions*, §*The Subscripts*, and they stand as written.

**These studies do not use the covariant index conventions: subscripts are not coordinate indices or derivatives, partial derivatives are written with explicit operators, and structural information is carried by the algebra of the objects themselves.**

**A contraction is written as an explicit sum.** Every index that is contracted is named under a $\sum$: the gradient is $\tilde\nabla=\sum_\mu e_\mu\partial/\partial R_\mu$, the spatial gradient $\sum_k\vec e_k\partial/\partial R_k$, a basis-vector contraction $\sum_k\vec e_kA_k$, and a sign-symbol contraction $\sum_{i,j}\varepsilon_{ijk}A_iB_j$. No index is summed by convention, and a repeated index is never left without its sum.

### The Derivative Marks

**No dot.** No derivative is written with a dot. The total derivative with respect to a parameter is written with a fraction and the parameter named: $\frac{d}{dt}$ for the parameter $t$, $\frac{d}{d\tau}$ for the parameter $\tau$, $\frac{d}{dt_r}$ for the parameter $t_r$; inline, the same derivative is written $dq/dt$. The partial derivative is written $\frac{\partial}{\partial t}$ or, inline, $\partial/\partial t$. A higher derivative is written $\frac{d^2}{dt^2}$, $\frac{\partial^2}{\partial t^2}$. The derivative binds to its whole argument, so a power is written outside a bracket, $\left(\frac{dx}{dt}\right)^2$, never as $\frac{dx^2}{dt}$.

**The prime marks the imaginary coordinate, and nothing else.** A prime marks the imaginary coordinate of a complex number: the second coefficient of a complex, split-complex or dual element, $R = r + ir'$ in the complex case, and of a biquaternion coefficient, $R_\mu = r_\mu + ir'_\mu$. It never marks a derivative: a function of one variable is differentiated as $df/dx$, a second derivative as $d^2f/dx^2$, and the value at a point as $\frac{df}{dx}(a)$; a derivative with respect to a coordinate is written $\partial/\partial R_\mu$ (§*Conventions for Derivation*). No further use of the prime is admitted.

**Labels that are not derivatives.** The second Lorentz label is written $\bar l$, and a spinor index of the conjugate representation is written $\bar\alpha$; the bar on an index marks the conjugate spinor. The conjugate matrix is $\bar\Pi$. These are labels, not derivatives.

**The dual-number derivation is a named operator.** The derivation in the nilpotent direction is written $\partial_{\mathrm{nil}}$, the upright name in the superscript saying which derivation it is, and it is defined by $\partial_{\mathrm{nil}}(q+\varepsilon q')=\varepsilon q'$. It is a derivation of the algebra, not a derivative with respect to a coordinate, so no coordinate is written under its $\partial$; its iterates are $(\partial_{\mathrm{nil}})^2$ and $\exp(t\,\partial_{\mathrm{nil}})$.

**The scope mark.** In geometric calculus the factor differentiated is marked with an underline, $\underline{\partial}(AB)=\underline{\partial}A\,B+\underline{A}\,\underline{\partial}B$, not with a dot.

### The Gradient

**The two derivative operators of the corpus** are the **biquaternionic gradient** $\tilde\nabla$ and the **d'Alembertian** $\Box$; each carries a glyph of its own and is fixed here and in no other place, and every other partial derivative is written with $\partial$.

The coordinate derivative is written $\partial/\partial R_\mu$ and is defined by

$$
\frac{\partial}{\partial R_\mu}:=\Bigl(\frac{\partial}{\partial r_\mu}-i\frac{\partial}{\partial r'_\mu}\Bigr),\qquad R_\mu=r_\mu+ir'_\mu .
$$

The form is the sum form $\partial/\partial r_\mu+\partial/\partial(ir'_\mu)$ with the $i$ resolved: the $i$ is glued to the primed parameter, so the derivative is taken with respect to the product $ir'_\mu$ and not with respect to $r'_\mu$ with the $i$ pulled out in front, and the second term therefore carries a minus and no reciprocal. No factor stands in front of the derivative: both terms are in the unit of the coefficient. It is the formal derivative on the complex coordinate; with $R_\mu$ and $\bar R_\mu$ read as independent, its unhalved normalization gives $\partial R_\mu/\partial R_\mu=2$ and $\partial R_\mu/\partial\bar R_\mu=0$.

**The coefficient carries no dilation.** The four coefficients are lengths in one and the same unit, and the derivative, the gradient and every sign follow from the algebra alone. A dilation in front of the whole derivative would divide both of its terms and would change no structure, so it is a normalisation and not an object of the theory. No dilation is written, and the fourth coordinate therefore carries no unit the three vector coordinates do not.

**One derivative, two halves, and a sector keeps one half.** The two terms of the definition are the two halves of the coefficient, the unprimed term and the primed term. A real sector sets one of them to zero, because the parameter it names is then not a coordinate of that slice, and what is left is the tangential derivative alone.

**On the material sector $\mathbb{B}_{\Phi}$**, with $R_t=i r'_t$ and $R_k=r_k$, $\partial/\partial r_t=0$ and $\partial/\partial r'_k=0$, and the definition reads $\partial/\partial R_t=-i\,\partial/\partial r'_t$ and $\partial/\partial R_k=\partial/\partial r_k$.

**On the informational sector $\mathbb{B}_{\Psi}$**, with $R_t=r_t$ and $R_k=i r'_k$, $\partial/\partial r'_t=0$ and $\partial/\partial r_k=0$, and the definition reads $\partial/\partial R_t=\partial/\partial r_t$ and $\partial/\partial R_k=-i\,\partial/\partial r'_k$.

**The two readings are the parent formula read twice, and the parent formula is the definition.** A reader who substitutes a sector line for the parent formula gains no new object: the parent formula is the definition, and the sector lines are its restrictions.

The conjugate derivative is

$$
\frac{\partial}{\partial\bar R_\mu}:=\Bigl(\frac{\partial}{\partial r_\mu}+i\frac{\partial}{\partial r'_\mu}\Bigr),
$$

with $\partial\bar R_\mu/\partial\bar R_\mu=2$. The **biquaternionic gradient** is the element-valued operator

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial R_\mu},
$$

whose tilde marks its scalar part beside its vector part (*Operator and Calculus Conventions*, §*The Gradient*; *Biquaternion Analysis*), with its quaternion conjugate $\tilde\nabla^{\natural}=\sum_\mu\varepsilon_\mu e_\mu\,\partial/\partial R_\mu$ and $\varepsilon=(1,-1,-1,-1)$. Write $\nabla=\sum_k\vec e_k\,\partial/\partial R_k$ for the spatial gradient, with divergence $\nabla\cdot\vec Q_{\mathrm f}$ and curl $\nabla\times\vec Q_{\mathrm f}$ of the element-valued field $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$, and $\Delta_Q=\partial^2/\partial R_x^2+\partial^2/\partial R_y^2+\partial^2/\partial R_z^2$ for the Laplacian in the three vector coordinates; on the material sector it is the physical $\Delta=\partial^2/\partial r_x^2+\partial^2/\partial r_y^2+\partial^2/\partial r_z^2$, where $R_k=r_k$.

**One operator, two readings, and no third.** The four real coordinates $r_\mu$ and the four $r'_\mu$ are eight real parameters, and a sector is the setting of four of them to zero. The material sector $\mathbb{B}_{\Phi}$ keeps the imaginary time $r'_t$ and the three real space parameters $r_k$; the informational sector $\mathbb{B}_{\Psi}$ keeps the real time $r_t$ and the three imaginary space parameters $r'_k$. The two keep complementary halves. A sector fixes the **value of the coefficients** and not the shape of the operator: on $\mathbb{B}_{\Phi}$ the relation $R_t=i r'_t$ gives $\partial/\partial R_t=-i\,\partial/\partial r'_t$ and $R_k=r_k$ gives $\partial/\partial R_k=\partial/\partial r_k$, while on $\mathbb{B}_{\Psi}$ the relations $R_t=r_t$ and $R_k=i r'_k$ give $\partial/\partial R_t=\partial/\partial r_t$ and $\partial/\partial R_k=-i\,\partial/\partial r'_k$. The four terms of the sum, the units $e_\mu$, the tilde and the $\natural$ belong to the operator and are untouched by either substitution. A sector is a slice, and no article of the corpus defines a second gradient.

**The sum is written.** The gradient is a sum, and the sum is always spelled out. The shorthand $\vec e_k\partial/\partial R_k$ is not used, because it repeats the index without summing it; the same holds for every contraction of a basis vector, a gamma or a field component with a derivative.

**The conjugates of the gradient.** The gradient is an operator, and the marks are read on its units at fixed coordinate: the derivative symbols are held fixed and only the units are conjugated. This fixes the scope of the star, and it is not a claim that $\partial/\partial R_\mu$ is real; the unhalved derivative defined above is complex, and on an element-valued field the star is coefficientwise, carried through the derivative by $\partial/\partial\bar R_\mu$ rather than by $\partial/\partial R_\mu$. Read on the units, the quaternion conjugation reverses the three spatial units, and so does the Hermitian conjugation, so the two act on the gradient alike,

$$
\tilde\nabla^{*}=\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial R_\mu},
\qquad \overline{\tilde\nabla}=\tilde\nabla .
$$

**The forms stay four, the norms are two.** The four forms keep their four conventions, named above in this section, each conjugating its own slot: the quaternionic form conjugates the first argument and the Hermitian form the second, so on a general second argument they are not the same statement. But read at the two equal arguments they give two operators, the Hermitian norm coinciding with the quaternionic bilinear norm and the Krein norm with the plain bilinear norm. The four subsections below carry the four forms, and their norms are the two operators $\Box$ and $\partial^2/\partial R_t^2-\Delta_Q$.

**On the material sector $\mathbb{B}_{\Phi}$**, where $R_t=i r'_t$ and $R_k=r_k$, the derivative along the fourth coordinate reads $\partial/\partial R_t=-i\,\partial/\partial r'_t$, the three space derivatives are the physical ones, $\partial/\partial R_k=\partial/\partial r_k$, the spatial gradient is $\nabla=\sum_k\vec e_k\,\partial/\partial r_k$, its divergence and its curl are the ordinary ones, the Laplacian in the vector coordinates is $\Delta=\sum_k\partial^2/\partial r_k^2$, and the gradient and its conjugate are

$$
\tilde\nabla\big|_{\mathbb{B}_{\Phi}}=-i\,e_t\frac{\partial}{\partial r'_t}+\sum_k\vec e_k\frac{\partial}{\partial r_k},
\qquad
\tilde\nabla^{\natural}\big|_{\mathbb{B}_{\Phi}}=-i\,e_t\frac{\partial}{\partial r'_t}-\sum_k\vec e_k\frac{\partial}{\partial r_k}.
$$

The conjugate moves the three minus signs onto the space slots and leaves the fourth coordinate alone, because $\varepsilon=(1,-1,-1,-1)$ and the substitution touches the coefficients only. In this reading the fourth-coordinate term is imaginary and the three space terms are real, and that is the whole of the arithmetic the four products below perform.

**On the informational sector $\mathbb{B}_{\Psi}$**, where $R_t=r_t$ and $R_k=i r'_k$, the roles are exchanged: the fourth-coordinate derivative is real, $\partial/\partial R_t=\partial/\partial r_t$, and the three space derivatives carry $-i$, $\partial/\partial R_k=-i\,\partial/\partial r'_k$. The three spatial operations are those of the general definitions, read on the sector and marked with the sector and with nothing else: $\nabla|_{\mathbb{B}_{\Psi}}=\sum_k\vec e_k\,\partial/\partial r'_k$ and $\Delta|_{\mathbb{B}_{\Psi}}=\sum_k\partial^2/\partial {r'_k}^2$, the sum spelled out as everywhere and the mark naming the slice and not a chart. Then $\Delta_Q|_{\mathbb{B}_{\Psi}}=-\Delta|_{\mathbb{B}_{\Psi}}$, and

$$
\tilde\nabla\big|_{\mathbb{B}_{\Psi}}=\frac{1}{c}\,e_t\frac{\partial}{\partial r_t}-i\sum_k\vec e_k\frac{\partial}{\partial r'_k},
\qquad
\tilde\nabla^{\natural}\big|_{\mathbb{B}_{\Psi}}=\frac{1}{c}\,e_t\frac{\partial}{\partial r_t}+i\sum_k\vec e_k\frac{\partial}{\partial r'_k}.
$$

Reading the two gradient displays term by term, the fourth-coordinate slot loses its $-i$ and gains a $1$ while the three space slots lose their $1$ and gain a $-i$, and no other difference exists. The $i$ sits on the time coefficient on $\mathbb{B}_{\Phi}$ and on the three space coefficients on $\mathbb{B}_{\Psi}$, so its square is $(-i)^2=-1$ once on the first slice and three times on the second, which is why the two slices carry opposite signature. That sign is a property of the slice and not of the operator: it is read on the operator only after a sector is named, and it is the reason the d'Alembertian below carries the time term positive on one sector and negative on the other.

### The Plain Bilinear Product, Its Form and Its Norm

**The product.** The general plain bilinear product is one of the four general products of *Product and Form Conventions*, §*The Twelve Products and Their Names*. On the gradient, with the element-valued field $\tilde Q_{\mathrm f}$ of §*The Gradient*, it is read with $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and $\vec e_j\vec e_k=-\delta_{jk}e_t+\epsilon_{jkl}\vec e_l$, so that the three spatial units carry the field back onto the scalar unit,

$$
\tilde\nabla\tilde Q_{\mathrm f}=\Bigl(\frac{\partial}{\partial R_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial}{\partial R_t}\vec Q_{\mathrm f}+\nabla Q_{\mathrm{f}t}+\nabla\times\vec Q_{\mathrm f} .
$$

A **product** is algebra-valued, and this one holds the divergence, the gradient and the curl of the field in a single object; for the field strength $\tilde F$ the equation $\tilde\nabla\tilde F=-\sqrt{\mu}\,\tilde J$, with $\tilde J=ic\rho\,e_t+\vec J$, is the series' Maxwell equation. **On the material sector** the same product is read with $\partial/\partial R_t=-i\,\partial/\partial r'_t$ and $\nabla$ the physical spatial gradient, so the space part is unchanged and the fourth-coordinate part gains the factor $-i$:

$$
\tilde\nabla\tilde Q_{\mathrm f}\big|_{\mathbb{B}_{\Phi}}=\Bigl(-i\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}-\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t-i\frac{\partial\vec Q_{\mathrm f}}{\partial r'_t}+\nabla Q_{\mathrm{f}t}+\nabla\times\vec Q_{\mathrm f} .
$$

**On the informational sector** the same product is read with $\partial/\partial R_t=\partial/\partial r_t$ and with the three spatial derivatives carrying $-i$, so the whole spatial part is multiplied by $-i$ and the fourth-coordinate part is real:

$$
\tilde\nabla\tilde Q_{\mathrm f}\big|_{\mathbb{B}_{\Psi}}=\Bigl(\frac{\partial Q_{\mathrm{f}t}}{\partial r_t}+i\,\nabla|_{\mathbb{B}_{\Psi}}\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial\vec Q_{\mathrm f}}{\partial r_t}-i\,\nabla|_{\mathbb{B}_{\Psi}}Q_{\mathrm{f}t}-i\,\nabla|_{\mathbb{B}_{\Psi}}\times\vec Q_{\mathrm f} .
$$

The two displays are one product read on two slices, and they differ in the way the two gradient displays differ: the divergence and the curl carry their own sign on $\mathbb{B}_{\Phi}$ and an $i$ with a change of sign on $\mathbb{B}_{\Psi}$, because $-i$ factors out of three spatial derivatives and multiplies each of them once. Nothing is redefined: a reader who substitutes the four factors of §*The Gradient* into the general display obtains each line, and a reader who does not substitute keeps the general display, which is the operator's own form.

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

a scalar, the **contraction** of the derivative with the field in the sign vector $\varepsilon$. **On the material sector** it is $-i\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}-\nabla\cdot\vec Q_{\mathrm f}$, the fourth-coordinate slot imaginary and the divergence real; **on the informational sector** it is $\frac{\partial Q_{\mathrm{f}t}}{\partial r_t}+i\,\nabla|_{\mathbb{B}_{\Psi}}\cdot\vec Q_{\mathrm f}$, the fourth-coordinate slot real and the divergence imaginary. The sign vector $\varepsilon$ belongs to the product and the factors belong to the slice, and the two never merge into one symbol.

**The norm.** The norm is defined with the form, as that form at its two equal arguments:

$$
\langle\tilde\nabla\rangle=\langle\tilde\nabla,\tilde\nabla\rangle=\mathrm{Sc}(\tilde\nabla\tilde\nabla)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial^2}{\partial R_\mu^2}=\frac{\partial^2}{\partial R_t^2}-\Delta_Q ,
$$

the cross terms cancelling. **On the material sector** it is $-\frac{\partial^2}{\partial {r'_{t}}^2}-\Delta$, which is not the series' d'Alembertian; on this sector the d'Alembertian is $\Delta-\frac{\partial^2}{\partial {r'_{t}}^2}$ (§*The Quaternionic Bilinear Product, Its Form and Its Norm*). **On the informational sector** it is $\frac{\partial^2}{\partial r_t^2}+\Delta|_{\mathbb{B}_{\Psi}}$, both terms positive, the negative of the material reading as the sign pattern of §*The Gradient* requires, and again neither the wave operator nor the d'Alembertian.

### The Quaternionic Bilinear Product, Its Form and Its Norm

**The product.** The general quaternionic bilinear product is the second of the four general products of *Product and Form Conventions*, §*The Twelve Products and Their Names*; on the gradient it is $\tilde\nabla^{\natural}\tilde Q_{\mathrm f}$, the conjugate derivative, read with the same rules, the three spatial units now carrying the field back onto the scalar unit with the opposite sign,

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}=\Bigl(\frac{\partial}{\partial R_t}Q_{\mathrm{f}t}+\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial}{\partial R_t}\vec Q_{\mathrm f}-\nabla Q_{\mathrm{f}t}-\nabla\times\vec Q_{\mathrm f} .
$$

**On the material sector** the same substitution $\partial/\partial R_t=-i\,\partial/\partial r'_t$ applies with $\nabla$ the physical gradient, the space part unchanged and the fourth-coordinate part gaining $-i$:

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}\big|_{\mathbb{B}_{\Phi}}=\Bigl(-i\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}+\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t-i\frac{\partial\vec Q_{\mathrm f}}{\partial r'_t}-\nabla Q_{\mathrm{f}t}-\nabla\times\vec Q_{\mathrm f} .
$$

**On the informational sector** the substitution is $\partial/\partial R_t=\partial/\partial r_t$ with $-i$ on the three space derivatives, and the space signs turn over once more, because the conjugate already carries them and the coefficient carries an $i$:

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}\big|_{\mathbb{B}_{\Psi}}=\Bigl(\frac{\partial Q_{\mathrm{f}t}}{\partial r_t}-i\,\nabla|_{\mathbb{B}_{\Psi}}\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial\vec Q_{\mathrm f}}{\partial r_t}+i\,\nabla|_{\mathbb{B}_{\Psi}}Q_{\mathrm{f}t}+i\,\nabla|_{\mathbb{B}_{\Psi}}\times\vec Q_{\mathrm f} .
$$

Compared with the plain product on the same slice, the two lines differ as the general displays differ, in the sign of the divergence and in the sign of the gradient and the curl, which is the statement that the conjugate derivative is not a second operator but the same operator with $\varepsilon$ applied to its units.

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

a scalar, the **contraction** of the derivative with the field, read on the material sector. It differs from the plain form by the three signs of $\varepsilon$, which are **computed from the product** $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and not assumed. **On the material sector** it is $-i\frac{\partial Q_{\mathrm{f}t}}{\partial r'_t}+\nabla\cdot\vec Q_{\mathrm f}$; **on the informational sector** it is $\frac{\partial Q_{\mathrm{f}t}}{\partial r_t}-i\,\nabla|_{\mathbb{B}_{\Psi}}\cdot\vec Q_{\mathrm f}$, with the divergence back with a minus because the conjugate derivative has already applied $\varepsilon$.

**The norm, and the definition of the d'Alembertian.** The norm is defined with the form, as that form at its two equal arguments, and the two orders of the product agree:

$$
\Box=\langle\tilde\nabla\rangle_{\natural}=\langle\tilde\nabla,\tilde\nabla\rangle_{\natural}
=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{\natural})
=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial R_\mu^2}=\frac{\partial^2}{\partial R_t^2}+\Delta_Q .
$$

**This is the definition of the d'Alembertian**: the quaternionic norm of the gradient, an operator on the whole algebra, one and the same before any sector is named (*The Four Forms, the Four Algebraic Norms and the Change of Scalars*). The coordinates $R_\mu$ are those of the algebra and are complex in general; the operator is $\partial^2/\partial R_t^2+\Delta_Q$ whatever the sector, and it is **scalar**: it multiplies by $e_t$ and acts coefficient by coefficient, $\Box\tilde Q_{\mathrm f}=\sum_\mu(\Box Q_{\mathrm{f}\mu})e_\mu$. It is the identity above, and not the relation $R_t=i r'_t$, that fixes it, and **no article of the series defines a second d'Alembertian**; no mass-term sign is left to a local convention.

**The special case of the material sector.** On $\mathbb{B}_{\Phi}$ the coordinates are $R_t=i r'_t$ and $R_k=r_k$, and the relation $R_t=i r'_t$ flips the sign of the second derivative in $r'_t$, $\partial^2/\partial R_t^2=-\,\partial^2/\partial {r'_{t}}^2$, so the same operator reads

$$
\Box\big|_{\mathbb{B}_{\Phi}}=\frac{\partial^2}{\partial R_t^2}+\Delta=\Delta-\frac{\partial^2}{\partial {r'_{t}}^2},
$$

a plus on the vector part and a minus on the fourth coordinate. On $\mathbb{B}_{\Phi}$, where the series does its work, this reading is the **series convention**, used by the Klein–Gordon article, the Dirac article, the dedicated article *The Biquaternion D'Alembertian and Its Green's Functions*, and the great majority of the series. **The relation $R_t=i r'_t$ is a statement about the material sector, not about the operator**, which in every case is $\partial^2/\partial R_t^2+\Delta_Q$; its signature is not a property of the operator but of the **slice** it is read on, since on a named subspace some of the $R_\mu$ are purely imaginary. The operator is one, and every article writes it the same way.

**The special case of the informational sector.** On $\mathbb{B}_{\Psi}$ the coordinates are $R_t=r_t$ and $R_k=i r'_k$, and the substitution works the other way round: the fourth-coordinate second derivative keeps a plus, $\partial^2/\partial R_t^2=\partial^2/\partial r_t^2$, while each of the three space second derivatives gains a minus, $\partial^2/\partial R_k^2=-\partial^2/\partial {r'_k}^2$, so the same operator reads

$$
\Box\big|_{\mathbb{B}_{\Psi}}=\frac{\partial^2}{\partial R_t^2}+\Delta_Q=\frac{\partial^2}{\partial r_t^2}-\Delta|_{\mathbb{B}_{\Psi}},
$$

a plus on the fourth coordinate and a minus on the vector part, which is the negative of the material line above. The two sector lines are one operator: a slice that keeps a coordinate carrying an $i$ turns one sign, and a slice that keeps the same coordinate without one does not. A reader who moves an equation from one sector to the other moves one overall sign and nothing else, and the series never takes the operator from one sector and the density from the other.

### The Hermitian Product, Its Form and Its Norm

**The product.** The general plain sesquilinear product is the third of the four general products of *Product and Form Conventions*, §*The Twelve Products and Their Names*; it is the plain product applied to the **conjugated** field $\tilde Q_{\mathrm f}^{*}=\bar Q_{\mathrm{f}t}e_t-\overline{\vec Q_{\mathrm f}}$, so that on the gradient it is $\tilde\nabla\tilde Q_{\mathrm f}^{*}$, conjugate-linear in the field while the first slot stays $\mathbb{C}$-linear,

$$
\tilde\nabla\tilde Q_{\mathrm f}^{*}=\Bigl(\frac{\partial}{\partial R_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{\partial}{\partial R_t}\overline{\vec Q_{\mathrm f}}+\nabla\bar Q_{\mathrm{f}t}-\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**On the material sector** the product is read with $\partial/\partial R_t=-i\,\partial/\partial r'_t$ and the physical gradient, so the conjugated field keeps its coefficients and only the factors of the derivatives change:

$$
\tilde\nabla\tilde Q_{\mathrm f}^{*}\big|_{\mathbb{B}_{\Phi}}=\Bigl(-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t+i\frac{\partial\overline{\vec Q_{\mathrm f}}}{\partial r'_t}+\nabla\bar Q_{\mathrm{f}t}-\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

The two plus signs on the vector slot are the work of the conjugation, which reversed the sign of the vector part of the field before any derivative met it. **On the informational sector** the same product is read with $\partial/\partial R_t=\partial/\partial r_t$ and $-i$ on the three space derivatives:

$$
\tilde\nabla\tilde Q_{\mathrm f}^{*}\big|_{\mathbb{B}_{\Psi}}=\Bigl(\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r_t}-i\,\nabla|_{\mathbb{B}_{\Psi}}\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{\partial\overline{\vec Q_{\mathrm f}}}{\partial r_t}-i\,\nabla|_{\mathbb{B}_{\Psi}}\bar Q_{\mathrm{f}t}+i\,\nabla|_{\mathbb{B}_{\Psi}}\times\overline{\vec Q_{\mathrm f}} .
$$

The pair makes the Hermitian product usable, because its scalar slot is the one that survives the conjugate transpose: the two readings are two ways of writing one density, the material one with an imaginary fourth-coordinate derivative and a real divergence, the informational one with a real fourth-coordinate derivative and an imaginary divergence.

**The symmetric and antisymmetric parts.** Under the conjugate transpose the half-sum is central and is the Hermitian form itself,

$$
\tilde\nabla\bullet_{*}\tilde Q_{\mathrm f}=\mathrm{Sc}(\tilde\nabla\tilde Q_{\mathrm f}^{*})\,e_t=\Bigl[\frac{\partial}{\partial R_t}\bar Q_{\mathrm{f}t}+(\nabla,\overline{\vec Q_{\mathrm f}})\Bigr]e_t=\Bigl(\frac{\partial}{\partial R_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t ,
$$

and the half-difference is the vector part,

$$
\tilde\nabla\wedge_{*}\tilde Q_{\mathrm f}=\mathrm{Vect}(\tilde\nabla\tilde Q_{\mathrm f}^{*})=-\frac{\partial}{\partial R_t}\overline{\vec Q_{\mathrm f}}+\bar Q_{\mathrm{f}t}\nabla-\nabla\times\overline{\vec Q_{\mathrm f}}=-\frac{\partial}{\partial R_t}\overline{\vec Q_{\mathrm f}}+\nabla\bar Q_{\mathrm{f}t}-\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**The form.** The **Hermitian form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{*}=\mathrm{Sc}(\tilde\nabla\tilde Q_{\mathrm f}^{*})=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial}{\partial R_\mu}\bar Q_{\mathrm{f}\mu}=\frac{\partial}{\partial R_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}} ,
$$

a scalar, the **contraction** of the derivative with the **conjugated** field in the sign vector $\varepsilon$. Taken on the scalar field it gives the **kinetic density**, the scalar part of the product of the two conjugated gradients,

$$
\mathrm{Sc}\bigl[(\tilde\nabla^{\natural}\tilde\Phi^{*})(\tilde\nabla\tilde\Phi)\bigr]=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial\Phi^{*}}{\partial R_\mu}\frac{\partial\Phi}{\partial R_\mu} ,
$$

in which the conjugate stands on the first factor and no absolute value is taken; the two derivatives in $R_t$ are imaginary on the material sector, so that scalar part is $-\lvert\partial\phi/\partial r'_t\rvert^2+\lvert\nabla\phi\rvert^2$, and the kinetic term the series writes is

$$
\mathcal L_{\mathrm{kin}}=-\mathrm{Sc}\bigl[(\tilde\nabla^{\natural}\tilde\Phi^{*})(\tilde\nabla\tilde\Phi)\bigr]=\Bigl|\frac{\partial\phi}{\partial r'_t}\Bigr|^2-\lvert\nabla\phi\rvert^2 ,
$$

the kinetic density of the Klein–Gordon article (*Hamiltonian Field Theory in Biquaternionic Form*). **On the informational sector** the same sum runs over the same four terms with the other factors, the fourth-coordinate slot contributing $+1$ and each of the three space slots $-1$, so the scalar part is $\lvert\partial\phi/\partial r_t\rvert^2-\lvert\nabla|_{\mathbb{B}_{\Psi}}\phi\rvert^2$ and the kinetic term is its negative. The overall sign belongs to the operator and not to the density, and an article that writes a Lagrangian on $\mathbb{B}_{\Psi}$ fixes the sign of its action there. **On the material sector** the form itself is $-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}$; **on the informational sector** it is $\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r_t}-i\,\nabla|_{\mathbb{B}_{\Psi}}\cdot\overline{\vec Q_{\mathrm f}}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments. By §*The Gradient*, $\tilde\nabla^{*}=\tilde\nabla^{\natural}$, and

$$
\langle\tilde\nabla,\tilde\nabla\rangle_{*}=\langle\tilde\nabla\rangle_{*}=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{*})=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{\natural})=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial R_\mu^2}=\frac{\partial^2}{\partial R_t^2}+\Delta_Q=\Box ,
$$

so the Hermitian norm of the gradient is the d'Alembertian, the same operator as its quaternionic bilinear norm. The **Hermitian form is the one positive-definite form of the four on the biquaternion layer**, $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert R_\mu\rvert^2$ on the elements, and its square root is the topological norm $\lVert\tilde Q\rVert_E$; positivity is a property of the elements, the norm of this subsection being the operator $\Box$. **On the material sector** it is the same operator, $\Box|_{\mathbb{B}_{\Phi}}=\Delta-\partial^2/\partial (r'_t)^2$; **on the informational sector** it is the same operator again, $\Box|_{\mathbb{B}_{\Psi}}=\partial^2/\partial r_t^2-\Delta|_{\mathbb{B}_{\Psi}}$, and the two lines are negatives of each other because the two sectors keep complementary halves of the eight parameters. Positivity is untouched by that sign: the form is positive on the elements in either reading, and what changes is the operator's own sign and not the form's.

### The Krein Product, Its Form and Its Norm

**The product.** The general quaternionic sesquilinear product is the fourth of the four general products of *Product and Form Conventions*, §*The Twelve Products and Their Names*; it is the conjugate derivative applied to the conjugated field, $\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}$, the companion of the quaternionic bilinear product in the second slot,

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}=\Bigl(\frac{\partial}{\partial R_t}\bar Q_{\mathrm{f}t}-\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{\partial}{\partial R_t}\overline{\vec Q_{\mathrm f}}-\nabla\bar Q_{\mathrm{f}t}+\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**On the material sector** the product is read with $\partial/\partial R_t=-i\,\partial/\partial r'_t$ and the physical gradient:

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}\big|_{\mathbb{B}_{\Phi}}=\Bigl(-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}-\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t+i\frac{\partial\overline{\vec Q_{\mathrm f}}}{\partial r'_t}-\nabla\bar Q_{\mathrm{f}t}+\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**On the informational sector** it is read with $\partial/\partial R_t=\partial/\partial r_t$ and $-i$ on the three space derivatives:

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}\big|_{\mathbb{B}_{\Psi}}=\Bigl(\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r_t}+i\,\nabla|_{\mathbb{B}_{\Psi}}\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{\partial\overline{\vec Q_{\mathrm f}}}{\partial r_t}+i\,\nabla|_{\mathbb{B}_{\Psi}}\bar Q_{\mathrm{f}t}-i\,\nabla|_{\mathbb{B}_{\Psi}}\times\overline{\vec Q_{\mathrm f}} .
$$

The two lines are the companions of the quaternionic pair: the four products of the section are the four readings of the same derivative on the two slices, and no line needs a convention beyond the four factors of §*The Gradient*.

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

a scalar, the **contraction** of the conjugate derivative with the conjugated field, read on the material sector. **On the material sector** it is $-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r'_t}-\nabla\cdot\overline{\vec Q_{\mathrm f}}$; **on the informational sector** it is $\frac{\partial\bar Q_{\mathrm{f}t}}{\partial r_t}+i\,\nabla|_{\mathbb{B}_{\Psi}}\cdot\overline{\vec Q_{\mathrm f}}$, the divergence back with a plus, because the conjugate derivative has already applied $\varepsilon$ and the substitution has applied $-i$ three times.

**The norm.** The norm is defined with the form, as that form at its two equal arguments; on the gradient, since $\tilde\nabla^{*}=\tilde\nabla^{\natural}$ (§*The Gradient*),

$$
\langle\tilde\nabla,\tilde\nabla\rangle_{\natural*}=\langle\tilde\nabla\rangle_{\natural*}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla^{*})=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla^{\natural})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial^2}{\partial R_\mu^2}=\frac{\partial^2}{\partial R_t^2}-\Delta_Q ,
$$

so the Krein norm of the gradient **coincides with the plain bilinear norm**. It is the indefinite partner of the Hermitian form, and on the elements it is the form of signature $(1,3)$ whose diagonal is $\lvert R_t\rvert^2-\lvert R_x\rvert^2-\lvert R_y\rvert^2-\lvert R_z\rvert^2$: Hermitian, indefinite — positive where $\lvert R_t\rvert^2>\lvert R_x\rvert^2+\lvert R_y\rvert^2+\lvert R_z\rvert^2$ and negative where the opposite inequality holds — so it carries no positivity. It is the form of the indefinite theory — the Krein space — and not of the contractions of these subsections. **On the material sector**, in the real coefficient $r'_t$ of $R_t=i r'_t$, it is $-\frac{\partial^2}{\partial {r'_{t}}^2}-\Delta$, both terms negative; **on the informational sector** it is $\frac{\partial^2}{\partial r_t^2}+\Delta|_{\mathbb{B}_{\Psi}}$, both terms positive, and the Krein norm there is again the plain bilinear norm and not the d'Alembertian.

**A contraction is a form, never an index.** The series has one metric, the unit metric $\delta_{\mu\nu}=(1,1,1,1)$, and it is the identity, so no index is raised and none is lowered: a raised index would be the same index. What the product carries is the plain weight $\varepsilon$, and the weight is not a metric. Where a text with covariant indices contracts a derivative with a field through a raised and a lowered index, the series writes the quaternionic form $\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural}$; where it contracts two derivatives, the series writes the quaternionic norm $\langle\tilde\nabla\rangle_{\natural}=\Box$; and where it moves an index through a metric, the series writes the element $\tilde Q_{\mathrm f}$ itself, the weight being the sign vector inside the product.

**The rule is one rule on both slices.** A contraction never raises an index and never lowers one, on $\mathbb{B}_{\Phi}$ or on $\mathbb{B}_{\Psi}$, because the metric is the identity on both. What changes between the slices is only the coefficient the contraction carries: on $\mathbb{B}_{\Phi}$ the fourth-coordinate component is multiplied by $-i$ and the three space components by $1$, while on $\mathbb{B}_{\Psi}$ the fourth-coordinate component is multiplied by $1$ and the three space components by $-i$. A reader who checks a component formula on either slice checks those four numbers and nothing else, and the check is complete.

## The Pair Operator and Its Symbol

**The pair.** The two first-order equations of the chiral pair, $\tilde\nabla\Psi_R=m\,\Psi_L$ and $\tilde\nabla^{\natural}\Psi_L=m\,\Psi_R$, are one operator on $\mathbb{B}\oplus\mathbb{B}$. Write $\Psi=(\Psi_L,\Psi_R)$; the pair operator is

$$
\mathbb{D}\Psi=\bigl(\tilde\nabla\Psi_R,\ \tilde\nabla^{\natural}\Psi_L\bigr),
\qquad
\mathbb{D}^2=\Box I ,
$$

and the massive equation is $(\mathbb{D}-m)\Psi=0$, with massless limit $\mathbb{D}\Psi=0$. The operator is the pair written once: it carries no matrix generator, no Clifford index and no chart, and its only content is which gradient acts on which part. The mass is the off-diagonal coupling of the two parts and is the identity on $\mathbb{B}$ in each place it acts.

**Neither gradient squares to the d'Alembertian, and their composition does.** Written as a product of elements, $\tilde\nabla^2$ is not $\Box$: $e_t$ commutes with the three spatial units, so the mixed derivatives survive and the square is not scalar. Only the composition with the conjugate is scalar, $\tilde\nabla^{\natural}\tilde\nabla=\tilde\nabla\tilde\nabla^{\natural}=\Box$, and this is why the pair is the least object that carries a first-order massive equation: one gradient on one field is first order and cannot equal a second-order operator, so no one-field first-order massive equation exists in this algebra. The free equation stays first order on one field, and the mass is what needs the pair.

**Written on one element.** Where the field is carried on one element, the same operator is written with its two sides in position,

$$
\mathbb{D}:\ \tilde X\longmapsto-\frac{\partial\tilde X}{\partial r'_t}\,\vec e_x-\sum_k\vec e_k\frac{\partial\tilde X}{\partial R_k}\,\vec e_y ,
$$

and the sides are the whole of the content. The time term is a right multiplication by $\vec e_x$ alone; each space term carries $\vec e_k$ on the left and $\vec e_y$ on the right, and the two multipliers are fixed basis elements that select the chiral slots and do not depend on the field. Left and right multiplications commute and the pure units anticommute, $\vec e_x\vec e_y=-\vec e_y\vec e_x$, with $\vec e_x^2=\vec e_y^2=-e_t$, so the cross terms cancel and the square is the d'Alembertian of the material sector, $\Delta-\partial^2/\partial {r'_{t}}^2$. The $i$ of the coordinate derivative is absorbed in the multiplier, $\partial/\partial R_t=-i\,\partial/\partial r'_t$, and no factor is left in front of the derivative; this is the pair read on one element and not a second definition.

**The symbol.** On a plane wave the two gradients act as left multiplication by the momentum element and its conjugate, $\tilde K=i\tilde Q_2=-p_t\,e_t+i\vec p$ with $\tilde K\tilde K^{\natural}=p_t^2-\lvert\vec p\rvert^2=p^2$, so the symbol of the pair is

$$
\mathbb{D}_p:\ (w_L,w_R)\longmapsto\bigl(\tilde K\,w_R,\ \tilde K^{\natural}w_L\bigr),
\qquad
\mathbb{D}_p^2=p^2 I ,
$$

and on one element it reads $\mathbb{D}_p:\tilde X\mapsto ip_t\,\tilde X\vec e_x-i\sum_kp_k\,\vec e_k\tilde X\vec e_y$. The square of the element is not the scalar: $\tilde K^2$ has scalar part $p_t^2+\lvert\vec p\rvert^2$ and a vector part that does not cancel, and only the composition with the conjugate returns $p^2$. The symbol of $\mathbb{D}-m$ is therefore singular exactly where $p^2=m^2$ and nowhere else, and the two chiral slots share the one condition.

**The inverse is a Green matrix.** With $G$ the Green's function of the d'Alembertian, $(\Box-m^2)G=\delta$, the Green matrix of the pair is $\mathcal{S}=(\mathbb{D}+m)G$, and $(\mathbb{D}-m)\mathcal{S}=(\mathbb{D}^2-m^2)G=\delta I$. The inverse introduces no new object: the scalar mass commutes with $\mathbb{D}$, and the factorization is the algebraic identity $(\mathbb{D}-m)(\mathbb{D}+m)=\mathbb{D}^2-m^2$.

**The glyph and its marks.** The glyph is $\mathbb{D}$, and it takes a mark for the factor and never for the chart. A subscript names the factor when that factor is not the material gradient — $\mathbb{D}_p$ for the constant momentum covector, which is the symbol — and an element in parentheses is an argument, $\mathbb{D}(\tilde K)$, because a letter on the right without parentheses, $\mathbb{D}\Psi$, is the field acted on. The gradient follows the same rule: $\tilde\nabla$ bare, $\natural$ or a sector label only where a second gradient is in play. The pair is never written $\mathbb{D}_{\mathbb{B}_{\Phi}}$ or $\mathbb{D}^{\natural}$; the sector enters through the coordinate, and the conjugate of the pair is the pair with its two gradients exchanged.

**The pair is sector-free.** On $\mathbb{B}_{\Phi}$ and on $\mathbb{B}_{\Psi}$ the operator is the same and only the four derivatives change, $\partial/\partial R_t=-i\,\partial/\partial r'_t$ against $\partial/\partial R_t=\partial/\partial r_t$. Its square follows the d'Alembertian of §*The Quaternionic Bilinear Product, Its Form and Its Norm*: $\Delta-\partial^2/\partial {r'_{t}}^2$ on the material sector and $\partial^2/\partial r_t^2-\Delta|_{\mathbb{B}_{\Psi}}$ on the informational one, and a reader who moves the pair from one sector to the other moves one overall sign and no operator.

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

**The instance that hides the generality.** The chiral pair is the case usually quoted. From $\tilde\nabla^{\natural}\Psi_L=m\Psi_R$, transposing with $\tilde Q_1=\Psi_L^{\natural}$ and using $m^{\natural}=m$,

$$
\tilde\nabla^{\natural}\Psi_L=m\,\Psi_R
\qquad\Longrightarrow\qquad
\Psi_L^{\natural}\overleftarrow{\tilde\nabla}=m\,\Psi_R^{\natural},
$$

one line, with the derivative now written to the right of $\Psi_L^{\natural}$ and the same mass in place. Read alone, the pair suggests that the right action is a property of the Dirac equation. It is not: the two lines hold of $\tilde\nabla\Psi_R=m\Psi_L$ as well, of a massless field, and of any equation in which one field stands to the right of a derivative. The equation supplies the right-hand side; the identity does not depend on it.

**Why the superscript $R$ is nevertheless written.** The identity holds for a field, and a product of fields is a field. What it does not do is move the derivative off one factor of a product while the other stays. On $\tilde Q_1\tilde Q_2$ the Leibniz rule gives

$$
(\tilde Q_1\tilde Q_2)\overleftarrow{\tilde\nabla}=\sum_{\mu\in\{t,x,y,z\}}\Bigl(\frac{\partial\tilde Q_1}{\partial R_\mu}\tilde Q_2+\tilde Q_1\frac{\partial\tilde Q_2}{\partial R_\mu}\Bigr)e_\mu ,
$$

with the unit after the bracket. It does not pass to the left of $\tilde Q_2$: that is a commutation with the units, allowed only when $\tilde Q_2$ is central. Nor is the rule $\sum_\mu(\partial\tilde Q_1/\partial R_\mu)e_\mu\tilde Q_2$, which differs from the first term by the defect $\sum_\mu(\partial\tilde Q_1/\partial R_\mu)[\tilde Q_2,e_\mu]$. That is the case §*The Two Sides and the Renaming Theorem* excludes, and the case the integration articles meet. There the derivative is named $\nabla^{R}$ after the factor it differentiates, and the name is a position, not a second operator.

**The slots.** The transposition is the exchange of the two slots of a basis operator, read on a differential operator. In the language of *Operator Chirality on the Biquaternion Algebra*, §*Conjugation Exchanges the Sides*, the map that carries a left multiplier to a right multiplier is $\mathsf C$, the conjugation written as a congruence, $\mathsf C L(a^{\natural})\mathsf C=R(a)$, which in the axis-free frame is the switch $\mathsf D=\operatorname{diag}(1,-1,-1,-1)$ and is the $N$ of the matrix form above. A left action of the gradient and a right action of the same gradient therefore have arrays that agree up to that sign and that order, which is where the phases of the two sides come from.

**What it is not.** Not a transpose without conjugation: $N$ is not the identity, and $N^{\mathsf T}N=I$ with $\det N=-1$ make the congruence a congruence and not a similarity. Not the adjoint either: the dagger carries the integration by parts and the boundary term, while $\natural$ carries the units alone at fixed coordinate; the two agree on the gradient, $\tilde\nabla^{*}=\tilde\nabla^{\natural}$, and part on a general element.

**Verified.** On random polynomial fields in the four coordinates the boxed line holds at residual $0.0$, the reconstruction from the conjugate at $0.0$, the chiral instance at $0.0$, and the product rule above at $0.0$; on $\tilde Q_1=x\vec e_x$ and $\tilde Q_2=\vec e_y$ the naive rule returns $-\vec e_y$ where the product rule returns $+\vec e_y$. The anti-automorphism it uses holds at residual $1.0\times10^{-15}$ over $200$ random pairs; the automorphism that would be needed if the units were not reversed fails at $2.7\times10^{1}$.

## Summary

An operator acting by multiplication **is** the element it multiplies by, so its glyph is the glyph of that element and the marks are read on it as on the element. The named operators take an upright capital and carry the element in the subscript: left multiplication $L_{\tilde Q}$, right multiplication $R_{\tilde Q}$, the two-sided $L_{\tilde Q_1}R_{\tilde Q_2}$, the sandwich $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$, the inner derivation $\operatorname{ad}_{\tilde Q}$ and the automorphism $\operatorname{Ad}_{\tilde Q}$. The sandwich with no qualifier is the bilinear one, and it is quadratic in $\tilde Q$, not bilinear. The side of an action is position, $D\psi$ against $\psi D$; the two are exchanged by the natural conjugation, $(\psi D)^{\natural}=D^{\natural}\psi^{\natural}$, so a right action on a field is a left action on the conjugate field, and no glyph marks a side. The superscript $R$ marks the right derivative, the one case the exchange does not reach, and on the gradient even that case is a conjugation: $\tilde Q_1\overleftarrow{\tilde\nabla}=\bigl(\tilde\nabla^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}$, so a right action is the left action of the conjugate gradient on the conjugate field, and the identity needs no equation.

The **dagger** is the general adjoint of an operator, never of an element, and it is not a fifth conjugation: several adjoints arise at once, one for each form and one for each sandwich, and the dagger is the mark that covers them all. An operator written as an array — a linear map on a coordinate column, a matrix in the $2\times2$ image or a regular matrix — carries no tilde. The **Fock exception** is the one mark that says a glyph is an operator and not an element of the algebra, and its superscript $\mathrm{fop}$ is fixed in *Index and Notation Conventions*.

No derivative is written with a dot, and a prime marks the imaginary coordinate and nothing else. Every partial derivative is written with $\partial$ and its variable, the subscript is a component index and never a derivative, and the coordinate derivative is unhalved, $\partial/\partial R_\mu=\bigl(\partial/\partial r_\mu-i\,\partial/\partial r'_\mu\bigr)$, and a sector keeps one of its two halves.

The two derivative operators of the corpus are the **biquaternionic gradient** $\tilde\nabla=\sum_\mu e_\mu\partial/\partial R_\mu$ and the **d'Alembertian** $\Box=\langle\tilde\nabla\rangle_{\natural}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)$, the quaternionic norm of the gradient; the operator is scalar and acts coefficient by coefficient. The two derivatives are read once as one operator on a pair of elements, the **pair operator** $\mathbb{D}$ of §*The Pair Operator and Its Symbol*, whose square is $\Box I$ and whose symbol is left multiplication by the momentum element. On $\mathbb{B}_{\Phi}$ the substitution $R_t=i r'_t$ flips the sign of the time second derivative, $\partial^2/\partial R_t^2=-\partial^2/\partial {r'_t}^2$, so the operator reads $\Delta-\partial^2/\partial {r'_t}^2$ there, which is the series' d'Alembertian on that sector and not the wave operator of the opposite overall sign.

The four products are read on the gradient: the plain bilinear product holds the divergence, the gradient and the curl of a field in one object; the quaternionic bilinear product reads the conjugate derivative; the Hermitian product gives the definite form; and the Krein product gives the indefinite one, whose norm coincides with the plain bilinear norm. **A contraction is a form, never an index**: the metric is the sign vector inside the product, and no index is raised or lowered.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q}$, $R_{\tilde Q}$ | Left and right multiplication by the element |
| $L_{\tilde Q_1}R_{\tilde Q_2}$ | The two-sided operator, $L_{\tilde Q_1}R_{\tilde Q_2}$ |
| $\mathrm{Sd}_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ | The bilinear sandwich; $\mathcal{T}_{a,b}$ the sesquilinear one |
| $\operatorname{ad}_{\tilde Q}$, $\operatorname{Ad}_{\tilde Q}$ | The inner derivation and the automorphism |
| ${}^{\dagger}$ | The general adjoint of an operator, never of an element |
| $\partial/\partial R_\mu$ | The unhalved coordinate derivative, $\bigl(\partial/\partial r_\mu-i\,\partial/\partial r'_\mu\bigr)$; the four coefficients are lengths, so no dilation stands in front |
| $\tilde\nabla=\sum_\mu e_\mu\,\partial/\partial R_\mu$ | The biquaternionic gradient |
| $\nabla=\sum_k\,\vec e_k\,\partial/\partial R_k$ | The pure spatial gradient |
| $\Box=\langle\tilde\nabla\rangle_{\natural}$ | The d'Alembertian, the quaternionic norm of the gradient |
| $\mathbb{D}$ | The pair operator on $\mathbb{B}\oplus\mathbb{B}$, $\mathbb{D}(\Psi_L,\Psi_R)=(\tilde\nabla\Psi_R,\tilde\nabla^{\natural}\Psi_L)$, with $\mathbb{D}^2=\Box I$; $\mathbb{D}_p$ is its symbol |
| $\mathrm{fop}$ | The Fock-operator mark, the one exception to the element rule |
| $^{\natural}$ | The natural conjugation, $a^{\natural}=(a_0,-a_1,-a_2,-a_3)$; an anti-automorphism, $(ab)^{\natural}=b^{\natural}a^{\natural}$ |
| $(\psi D)^{\natural}=D^{\natural}\psi^{\natural}$ | The exchange of the two sides: a right action on $\psi$ is a left action on $\psi^{\natural}$ |
| $\nabla^{R}$ | The right gradient, $F\nabla^{R}=\sum_\mu(\partial F/\partial R_\mu)e_\mu$; used only where a derivative meets two distinct factors |
| $\overleftarrow{\ }$ | The long arrow over an operator: it acts on the factor written to its left, and the arrow points at that factor; it is not the short arrow of the pure part |
| $\tilde Q_1\overleftarrow{\tilde\nabla}$ | The same gradient transposed, $\sum_\mu(\partial\tilde Q_1/\partial R_\mu)e_\mu$; the right action, equal to $\bigl(\tilde\nabla^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853). The original formulation, and the source of the quaternion conjugation and its notation.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636. The biquaternion conjugations and the conventions of the complexified algebra in the applied literature.
