# __Operator and Calculus Conventions__

## Introduction

An operator that acts by multiplication is the element it multiplies by, and its glyph is the glyph of that element; an operator written as an array carries no tilde. This article fixes the named operators, the dagger, the array rule and the Fock exception, and then the calculus: the derivative marks, the gradient, the d'Alembertian, and the four products read on the gradient.

The order follows the dependence. The operators come before the calculus because the gradient is an operator and its glyph follows the operator rule. The derivation comes before the four products read on it, because the products are read with the derivative already fixed.

The article assumes the base of *Algebra and Element Conventions*, the products and forms of *Product and Form Conventions*, and the norms of *Norm and Unitary Conventions*. It cites the superscript rule of *Index, Notation and Corpus Conventions* for the Fock mark.

## The Operators

**An operator acting by multiplication is the element it multiplies by.** Every element acts on the algebra, on the left $L_{\tilde Q}$ or on the right $R_{\tilde Q}$, and an operator whose letter is the letter of an element **is** that element. The glyph of the operator is therefore the glyph of its element, and the marks are read on it as on the element: the tilde marks the quaternionic element read with its scalar part, the arrow the pure element read on its vector part alone. Neither mark says that a glyph is an operator, and no mark is added to say it.

**The named operators.** The structural operators take an upright capital letter and carry the element in the subscript, where it keeps its own mark:

| Operator | Glyph |
|---|---|
| left multiplication | $L_{\tilde Q_1}(\tilde Q_2)=\tilde Q_1\tilde Q_2$ |
| right multiplication | $R_{\tilde Q_1}(\tilde Q_2)=\tilde Q_2\tilde Q_1$ |
| two-sided | $L_{\tilde Q_1}R_{\tilde Q_2}(\tilde Q_3)=\tilde Q_1\tilde Q_3\tilde Q_2=L_{\tilde Q_1}R_{\tilde Q_2}$ |
| sandwich (default: bilinear) | $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}=L_{\tilde Q}R_{\tilde Q^{*}}=\operatorname{H}_{\tilde Q}$ |
| inner derivation | $\operatorname{ad}_{\tilde Q_4}(\tilde Q_1)=[\tilde Q_4,\tilde Q_1]$ |
| automorphism | $\operatorname{Ad}_{\tilde Q_4}$ |

**The default sandwich.** *Sandwich* with no qualifier is the **bilinear sandwich** $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$. The qualifier separates it from the **sesquilinear sandwich** $\mathcal{T}_{a,b}=L_{a}R_{b}\circ\varkappa$, $\mathcal{T}_{a,b}(\tilde Q_1)=a\tilde Q_1^{*}b$, whose star acts on the argument. The bilinear sandwich is quadratic in $\tilde Q$, not bilinear: $\Theta_{\lambda\tilde Q}=\lvert\lambda\rvert^{2}\Theta_{\tilde Q}$. The word *bilinear* names the family $L_{a}R_{b}$ from which the sandwich is cut. The dagger is the adjoint of an operator and is never part of an operator's name.

The tilde sits in the subscript because it belongs to the element, not to the operator: $L_{\tilde Q}$ is an operator, $\tilde Q$ is the element that generates it. In $L_{\tilde Q_1}R_{\tilde Q_2}$ the subscripts are positional: the first is the left multiplier and the second the right multiplier, while the argument occupies the third slot.

**The basis operators.** The four units are written in the subscript, $L_{e_\mu}$ and $R_{e_\mu}$, and nowhere else: the short form $L_\mu$ is not used in this corpus. The right family is read from the left one by the exchange $\mathsf S$ of the two mixed Peirce units, $R_{e_\nu}=\mathsf S L_{e_\nu}^{\mathsf T}\mathsf S^{-1}$, and the sixteen two-sided operators $L_{e_\mu}R_{e_\nu}$ are the matrix basis and the cell table of *Matrix Representations Conventions*, §*The Clifford Structure*; the gamma set is five of them up to $i$, $\gamma_0=iL_{e_t}R_{\vec e_x}$, $\gamma_1=iL_{\vec e_x}R_{\vec e_y}$, $\gamma_2=iL_{\vec e_y}R_{\vec e_y}$, $\gamma_3=iL_{\vec e_z}R_{\vec e_y}$, $\gamma_5=-iL_{e_t}R_{\vec e_z}$; the last of them is the volume cell of the frame, written $\mathsf{V}^{\mathrm{vol}}$ in the operator articles.

**The spin operator and the words built on it.** The generator of the rotations is $\tilde S_k=\tfrac12 i\vec e_k$, an operator whose glyph is the glyph of its element, like every operator of this section. The three words built on it — the **spin**, the **elementary spinor** and the **Dirac spinor** — are fixed in *Special Element and Peirce Conventions*, §*The Spin Convention* and §*The Spinor Convention*, and are not restated here.

**The two marks on a glyph that is also an operator.** An operator read through its element follows the element rule in full.

- A glyph read with its scalar part, four components: the tilde. The biquaternionic gradient $\tilde\nabla$ of §*The Gradient* is the algebraic example, and the canonical momentum $\tilde p=p_te_t+\vec p$ is the physical one.
- A pure glyph, three components: the arrow. The momentum operator $\vec p=-i\hbar\nabla=\sum_k\vec e_kp_k$ is the physical example, and $\nabla=\sum_k\,\vec e_k\,\partial/\partial Q_k$ is the fixed spatial gradient, which carries no second mark (§*The Gradient*).

The gradient decides the case cleanly: $\tilde\nabla$ is not pure, because its $e_t$ term carries $\partial/\partial Q_t$, while $\nabla$ is pure. The case follows the layer: a pure operator of the quaternion layer stays lower case, $\vec p$, and one of the biquaternion layer takes the upper case, $\vec P$; where the letter already names another object of the layer, a subscript or the explicit form $-i\hbar\vec\nabla$ fixes the operator.

**The mark of a part, and the side carried by position.** The only arrow on a glyph is the short one, and it marks the **pure part**: $\vec e_x$, $\vec p$. The long arrow that sits over an operator is a different mark and not a second arrow of the same kind: it is the mark of the transposed reading, fixed in §*The Transposition of the Gradient*. The side of an action is not marked at all. It is carried by position, $b\psi$ against $\psi b$, the actor written on the side from which it acts, and position is unambiguous because the operand is itself a glyph.

**What names a side where position is not enough.** Three signs, each of which the corpus needs for a purpose of its own.

- $\natural$ marks the conjugation of an element, $a^{\natural}=(a_0,-a_1,-a_2,-a_3)$, and it is what carries a change of side, because it is an anti-automorphism: $(ab)^{\natural}=b^{\natural}a^{\natural}$, hence $(\psi D)^{\natural}=D^{\natural}\psi^{\natural}$, and a right action on $\psi$ is a left action on $\psi^{\natural}$. The theorem is below, §*The Two Sides and the Renaming Theorem*.
- $L_a$ and $R_a$ name a side outright when a statement is about operators rather than about fields, and the cell $L_{a}R_{b}$ prints both sides at once. The label of the side of a cell is the **operator chirality** — the left slot, the right slot, or both — fixed in *Operator Family Conventions*, §*The Slot Label, Which Is the Chirality*.
- The superscript $R$ marks the one case that position alone leaves genuinely ambiguous: a derivative that differentiates the factor written to its left, $F\nabla^{R}=\sum_\mu(\partial F/\partial q_\mu)e_\mu$. It is used only inside a product of two distinct factors, which is where the theorem below does not reach.

**The dagger.** The dagger is the general adjoint of an operator, never of an element: $(L_a)^{\dagger}=L_{a^{*}}$. Several adjoints arise at once — one for each form, and one for each of the sandwiches — and the dagger is the mark that covers them all, of which the others are the instances. It is not a fifth conjugation: it belongs to the operators and not to the algebra. Where a dagger is written on an element the writing is an abuse: the mark that was meant is the star for the Hermitian conjugation, or the natural sign for the quaternion conjugation, according to the conjugation in view. The dagger is added to the glyph and does not replace the element's mark: the arrow states purity, which the adjoint preserves; the tilde states a glyph read with its scalar part, which the adjoint also preserves. Where the adjoint in view is the formal algebraic one of the definite form, the two marks are written together, dagger first: $(L_a)^{\dagger}=(L_a)^{*}=L_{a^{*}}$ and $\tilde\nabla^{\dagger}=\tilde\nabla^{*}=\tilde\nabla^{\natural}$. The identification is formal: the $L^2$ adjoint of a derivative carries the sign of the integration by parts, and it is not the dagger of this convention.

**An operator written as an array carries no tilde.** The element rule above governs an operator that acts on the algebra by multiplication, because such an operator is the element. An operator written as a linear map on a coordinate column, as a matrix in the $2\times2$ image, or as a regular matrix $\mathsf{M}_{4L}$, is an array: it carries no tilde, its elements keep theirs inside the argument, $\mathsf{M}_2(\tilde Q)$, and its adjoint is the dagger and not the star. A Kraus operator, where the physics corpus uses one, is written in the element reading, $\tilde K_l\in\mathbb{B}$, because it multiplies the state on both sides; its matrix image $\mathsf{M}_2(\tilde K_l)$ carries no tilde.

**The Fock exception.** A Fock operator is not an element of the algebra; its superscript $\mathrm{fop}$ and the order of the two marks are fixed in *Index, Notation and Corpus Conventions*, §*The Superscripts*.

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

In this work, subscripts denote vector components, not partial derivatives as in the PDE convention; every partial derivative is written explicitly with $\partial$ followed by its variable, and no subscript is ever attached to the $\partial$ of a derivative. A subscript is therefore a component index, as in $v_x$ for the component of a velocity along an axis, or a label, as in $\tilde U_{\mathrm b}$; it never denotes a derivative. The derivative with respect to a coordinate is written $\partial/\partial Q_\mu$, and in a fixed direction $\partial/\partial Q_t$, $\partial/\partial Q_x$, $\partial/\partial Q_y$ or $\partial/\partial Q_z$; a coordinate is never left under the $\partial$, so none of the abbreviated spellings occurs, and the rule admits no exception for a derivative, neither on a free index nor on any other. A derivative with respect to a variable that is not a coordinate is written the same way, its variable named in full: the Lagrangian derivative puts the function in the numerator, $\partial L/\partial w$, so that where a PDE text writes $L_u$ and $L_p$ the calculus-of-variations and partial-differential-equation articles write $\partial L/\partial w$ and $\partial L/\partial p$; the second derivative has the same shape, $\partial^2 L/\partial w^2$. The function is named in the numerator whenever it is a letter of its own, as for a Lagrangian, a Hamiltonian or a generating function; the slashed form $\partial/\partial u$ is kept where the symbol is an operator or where the operand is a compound expression rather than a single letter. The derivative $\partial/\partial Q_t$ is the derivative along the fourth coordinate: on the material sector, where $Q_t=iq'_t$, it equals $-i\,\partial/\partial q'_t$, and $q'_t$ is a real coefficient and not one of the coordinates, so the derivative with respect to it is written out as $\partial/\partial q'_t$.

**A subscript on an operator names its degree, its place or its bundle.** The rule governs the derivative of a function or a field, which names its variable after the $\partial$. It does not forbid a label on an operator that differentiates nothing: the chain boundary is $\partial_n:C_n\to C_{n-1}$ and the face maps are $\partial_i$, with the degree in the subscript; the distinguished boundary of a polydisc is $\partial_0D$; the tame symbol is $\partial_v$, with the place; the twisted Dolbeault operator is $\bar\partial_E$, with the bundle. These are operator labels, in the sense of *Index, Notation and Corpus Conventions*, §*The Subscripts*, and they stand as written.

**These studies do not use the covariant index conventions: subscripts are not coordinate indices or derivatives, partial derivatives are written with explicit operators, and structural information is carried by the algebra of the objects themselves.**

**A contraction is written as an explicit sum.** Every index that is contracted is named under a $\sum$: the gradient is $\tilde\nabla=\sum_\mu e_\mu\partial/\partial Q_\mu$, the spatial gradient $\sum_k\vec e_k\partial/\partial Q_k$, a basis-vector contraction $\sum_k\vec e_kA_k$, and a sign-symbol contraction $\sum_{i,j}\varepsilon_{ijk}A_iB_j$. No index is summed by convention, and a repeated index is never left without its sum.

### The Derivative Marks

**No dot.** No derivative is written with a dot. The total derivative with respect to a parameter is written with a fraction and the parameter named: $\frac{d}{dt}$ for the parameter $t$, $\frac{d}{d\tau}$ for the parameter $\tau$, $\frac{d}{dt_r}$ for the parameter $t_r$; inline, the same derivative is written $dq/dt$. The partial derivative is written $\frac{\partial}{\partial t}$ or, inline, $\partial/\partial t$. A higher derivative is written $\frac{d^2}{dt^2}$, $\frac{\partial^2}{\partial t^2}$. The derivative binds to its whole argument, so a power is written outside a bracket, $\left(\frac{dx}{dt}\right)^2$, never as $\frac{dx^2}{dt}$.

**The prime marks the imaginary coordinate, and nothing else.** A prime marks the imaginary coordinate of a complex number: the second coefficient of a complex, split-complex or dual element, $Q = q + iq'$ in the complex case, and of a biquaternion coefficient, $Q_\mu = q_\mu + iq'_\mu$. It never marks a derivative: a function of one variable is differentiated as $df/dx$, a second derivative as $d^2f/dx^2$, and the value at a point as $\frac{df}{dx}(a)$; a derivative with respect to a coordinate is written $\partial/\partial Q_\mu$ (§*Conventions for Derivation*). No further use of the prime is admitted.

**Labels that are not derivatives.** The second Lorentz label is written $\bar l$, and a spinor index of the conjugate representation is written $\bar\alpha$; the bar on an index marks the conjugate spinor. The conjugate matrix is $\bar\Pi$. These are labels, not derivatives.

**The dual-number derivation is a named operator.** The derivation in the nilpotent direction is written $\partial^{\mathrm{nil}}$, the upright name in the superscript saying which derivation it is, and it is defined by $\partial^{\mathrm{nil}}(q+\varepsilon q')=\varepsilon q'$. It is a derivation of the algebra, not a derivative with respect to a coordinate, so no coordinate is written under its $\partial$; its iterates are $(\partial^{\mathrm{nil}})^2$ and $\exp(t\,\partial^{\mathrm{nil}})$.

**The scope mark.** In geometric calculus the factor differentiated is marked with an underline, $\underline{\partial}(AB)=\underline{\partial}A\,B+\underline{A}\,\underline{\partial}B$, not with a dot.

### The Gradient

**The two derivative operators of the corpus** are the **biquaternionic gradient** $\tilde\nabla$ and the **d'Alembertian** $\Box$; each carries a glyph of its own and is fixed here and in no other place, and every other partial derivative is written with $\partial$.

The coordinate derivative is written $\partial/\partial Q_\mu$ and is defined by

$$
\frac{\partial}{\partial Q_\mu}:=\frac{\partial}{\partial q_\mu}+\frac{\partial}{\partial(iq'_\mu)},\qquad Q_\mu=q_\mu+iq'_\mu,
$$

the $i$ being glued to the primed coordinate: the derivative is taken with respect to the product $iq'_\mu$, not with respect to $q'_\mu$ with the $i$ pulled out in front. It is the formal derivative on the complex coordinate; with $Q_\mu$ and $\bar Q_\mu$ read as independent, its unhalved normalization gives $\partial Q_\mu/\partial Q_\mu=2$ and $\partial Q_\mu/\partial\bar Q_\mu=0$. On a real sector, where the fields depend on the tangential coordinate alone, the normal derivative is absent; on the material sector, with $Q_t=iq'_t$, the symbol is read with the tangential derivative alone, $\partial/\partial Q_t=-i\,\partial/\partial q'_t$. The conjugate derivative is

$$
\frac{\partial}{\partial\bar Q_\mu}:=\frac{\partial}{\partial q_\mu}-\frac{\partial}{\partial(iq'_\mu)},
$$

with $\partial\bar Q_\mu/\partial\bar Q_\mu=2$. The **biquaternionic gradient** is the element-valued operator

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial Q_\mu},
$$

whose tilde marks its scalar part beside its vector part (*Operator and Calculus Conventions*, §*The Gradient*; *Biquaternion Analysis*), with its quaternion conjugate $\tilde\nabla^{\natural}=\sum_\mu\varepsilon_\mu e_\mu\,\partial/\partial Q_\mu$ and $\varepsilon=(1,-1,-1,-1)$. Write $\nabla=\sum_k\vec e_k\,\partial/\partial Q_k$ for the spatial gradient, with divergence $\nabla\cdot\vec Q_{\mathrm f}$ and curl $\nabla\times\vec Q_{\mathrm f}$ of the element-valued field $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$, and $\Delta_Q=\partial^2/\partial Q_x^2+\partial^2/\partial Q_y^2+\partial^2/\partial Q_z^2$ for the Laplacian in the three vector coordinates; on the material sector it is the physical $\Delta=\partial^2/\partial q_x^2+\partial^2/\partial q_y^2+\partial^2/\partial q_z^2$, where $Q_k=q_k$.

**The sum is written.** The gradient is a sum, and the sum is always spelled out. The shorthand $\vec e_k\partial/\partial Q_k$ is not used, because it repeats the index without summing it; the same holds for every contraction of a basis vector, a gamma or a field component with a derivative.

**The conjugates of the gradient.** The gradient is an operator, and the marks are read on its units at fixed coordinate: the derivative symbols are held fixed and only the units are conjugated. This fixes the scope of the star, and it is not a claim that $\partial/\partial Q_\mu$ is real; the unhalved derivative defined above is complex, and on an element-valued field the star is coefficientwise, carried through the derivative by $\partial/\partial\bar Q_\mu$ rather than by $\partial/\partial Q_\mu$. Read on the units, the quaternion conjugation reverses the three spatial units, and so does the Hermitian conjugation, so the two act on the gradient alike,

$$
\tilde\nabla^{*}=\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial Q_\mu},
\qquad \overline{\tilde\nabla}=\tilde\nabla .
$$

**The forms stay four, the norms are two.** The four forms keep their four conventions, named above in this section, each conjugating its own slot: the quaternionic form conjugates the first argument and the Hermitian form the second, so on a general second argument they are not the same statement. But read at the two equal arguments they give two operators, the Hermitian norm coinciding with the quaternionic bilinear norm and the Krein norm with the plain bilinear norm. The four subsections below carry the four forms, and their norms are the two operators $\Box$ and $\partial^2/\partial Q_t^2-\Delta_Q$.

**On the material sector $\mathbb{M}_-$**, where $Q_t=iq'_t$ and $Q_k=q_k$, the derivative along the fourth coordinate reads $\partial/\partial Q_t=-i\,\partial/\partial q'_t$.

### The Plain Bilinear Product, Its Form and Its Norm

**The product.** The general plain bilinear product is one of the four general products of *Product and Form Conventions*, §*The Twelve Products and Their Names*. On the gradient, with the element-valued field $\tilde Q_{\mathrm f}$ of §*The Gradient*, it is read with $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and $\vec e_j\vec e_k=-\delta_{jk}e_t+\epsilon_{jkl}\vec e_l$, so that the three spatial units carry the field back onto the scalar unit,

$$
\tilde\nabla\tilde Q_{\mathrm f}=\Bigl(\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}+\nabla Q_{\mathrm{f}t}+\nabla\times\vec Q_{\mathrm f} .
$$

A **product** is algebra-valued, and this one holds the divergence, the gradient and the curl of the field in a single object; for the field strength $\tilde F$ the equation $\tilde\nabla\tilde F=-\sqrt{\mu}\,\tilde J$, with $\tilde J=ic\rho\,e_t+\vec J$, is the series' Maxwell equation. **On the material sector** the same product is read with $\partial/\partial Q_t=-i\,\partial/\partial q'_t$, the space part being unchanged.

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

a scalar, the **contraction** of the derivative with the field in the sign vector $\varepsilon$. **On the material sector** it is $-i\frac{\partial Q_{\mathrm{f}t}}{\partial q'_t}-\nabla\cdot\vec Q_{\mathrm f}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments:

$$
\langle\tilde\nabla\rangle=\langle\tilde\nabla,\tilde\nabla\rangle=\mathrm{Sc}(\tilde\nabla\tilde\nabla)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}-\Delta_Q ,
$$

the cross terms cancelling. **On the material sector** it is $-\frac{\partial^2}{\partial (q'_t)^2}-\Delta$, which is not the series' d'Alembertian; on this sector the d'Alembertian is $\Delta-\frac{\partial^2}{\partial (q'_t)^2}$ (§*The Quaternionic Bilinear Product, Its Form and Its Norm*).

### The Quaternionic Bilinear Product, Its Form and Its Norm

**The product.** The general quaternionic bilinear product is the second of the four general products of *Product and Form Conventions*, §*The Twelve Products and Their Names*; on the gradient it is $\tilde\nabla^{\natural}\tilde Q_{\mathrm f}$, the conjugate derivative, read with the same rules, the three spatial units now carrying the field back onto the scalar unit with the opposite sign,

$$
\tilde\nabla^{\natural}\tilde Q_{\mathrm f}=\Bigl(\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}+\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}-\nabla Q_{\mathrm{f}t}-\nabla\times\vec Q_{\mathrm f} .
$$

**On the material sector** the same substitution $\partial/\partial Q_t=-i\,\partial/\partial q'_t$ applies.

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

a scalar, the **contraction** of the derivative with the field in the signature of the material sector. It differs from the plain form by the three signs of $\varepsilon$, which are **computed from the product** $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and not assumed. **On the material sector** it is $-i\frac{\partial Q_{\mathrm{f}t}}{\partial q'_t}+\nabla\cdot\vec Q_{\mathrm f}$.

**The norm, and the definition of the d'Alembertian.** The norm is defined with the form, as that form at its two equal arguments, and the two orders of the product agree:

$$
\Box=\langle\tilde\nabla\rangle_{\natural}=\langle\tilde\nabla,\tilde\nabla\rangle_{\natural}
=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{\natural})
=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q .
$$

**This is the definition of the d'Alembertian**: the quaternionic norm of the gradient, an operator on the whole algebra, one and the same before any sector is named (*The Four Forms, the Four Algebraic Norms and the Change of Scalars*). The coordinates $Q_\mu$ are those of the algebra and are complex in general; the operator is $\partial^2/\partial Q_t^2+\Delta_Q$ whatever the sector, and it is **scalar**: it multiplies by $e_t$ and acts coefficient by coefficient, $\Box\tilde Q_{\mathrm f}=\sum_\mu(\Box Q_{\mathrm{f}\mu})e_\mu$. It is the identity above, and not the relation $Q_t=iq'_t$, that fixes it, and **no article of the series defines a second d'Alembertian**; no mass-term sign is left to a local convention.

**The special case of the material sector.** On $\mathbb{M}_-$ the coordinates are $Q_t=iq'_t$ and $Q_k=q_k$, and the relation $Q_t=iq'_t$ flips the sign of the second derivative in $q'_t$, $\partial^2/\partial Q_t^2=-\partial^2/\partial (q'_t)^2$, so the same operator reads

$$
\Box\big|_{\mathbb{M}_-}=\frac{\partial^2}{\partial Q_t^2}+\Delta=\Delta-\frac{\partial^2}{\partial (q'_t)^2},
$$

a plus on the vector part and a minus on the fourth coordinate. On $\mathbb{M}_-$, where the series does its work, this reading is the **series convention**, used by the Klein–Gordon article, the Dirac article, the dedicated article *The Biquaternion D'Alembertian and Its Green's Functions*, and the great majority of the series. **The relation $Q_t=iq'_t$ is a statement about the material sector, not about the operator**, which in every case is $\partial^2/\partial Q_t^2+\Delta_Q$; its signature is not a property of the operator but of the **slice** it is read on, since on a named subspace some of the $Q_\mu$ are purely imaginary. The operator is one, and every article writes it the same way.

### The Hermitian Product, Its Form and Its Norm

**The product.** The general plain sesquilinear product is the third of the four general products of *Product and Form Conventions*, §*The Twelve Products and Their Names*; it is the plain product applied to the **conjugated** field $\tilde Q_{\mathrm f}^{*}=\bar Q_{\mathrm{f}t}e_t-\overline{\vec Q_{\mathrm f}}$, so that on the gradient it is $\tilde\nabla\tilde Q_{\mathrm f}^{*}$, conjugate-linear in the field while the first slot stays $\mathbb{C}$-linear,

$$
\tilde\nabla\tilde Q_{\mathrm f}^{*}=\Bigl(\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}+\nabla\bar Q_{\mathrm{f}t}-\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**The symmetric and antisymmetric parts.** Under the conjugate transpose the half-sum is central and is the Hermitian form itself,

$$
\tilde\nabla\bullet_{*}\tilde Q_{\mathrm f}=\mathrm{Sc}(\tilde\nabla\tilde Q_{\mathrm f}^{*})\,e_t=\Bigl[\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+(\nabla,\overline{\vec Q_{\mathrm f}})\Bigr]e_t=\Bigl(\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}\Bigr)e_t ,
$$

and the half-difference is the vector part,

$$
\tilde\nabla\wedge_{*}\tilde Q_{\mathrm f}=\mathrm{Vect}(\tilde\nabla\tilde Q_{\mathrm f}^{*})=-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}+\bar Q_{\mathrm{f}t}\nabla-\nabla\times\overline{\vec Q_{\mathrm f}}=-\frac{\partial}{\partial Q_t}\overline{\vec Q_{\mathrm f}}+\nabla\bar Q_{\mathrm{f}t}-\nabla\times\overline{\vec Q_{\mathrm f}} .
$$

**The form.** The **Hermitian form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{*}=\mathrm{Sc}(\tilde\nabla\tilde Q_{\mathrm f}^{*})=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial}{\partial Q_\mu}\bar Q_{\mathrm{f}\mu}=\frac{\partial}{\partial Q_t}\bar Q_{\mathrm{f}t}+\nabla\cdot\overline{\vec Q_{\mathrm f}} ,
$$

a scalar, the **contraction** of the derivative with the **conjugated** field in the sign vector $\varepsilon$. Taken on the scalar field it gives the **kinetic density**, the scalar part of the product of the two conjugated gradients,

$$
\mathrm{Sc}\bigl[(\tilde\nabla^{\natural}\tilde\Phi^{*})(\tilde\nabla\tilde\Phi)\bigr]=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial\Phi^{*}}{\partial Q_\mu}\frac{\partial\Phi}{\partial Q_\mu} ,
$$

in which the conjugate stands on the first factor and no absolute value is taken; the two derivatives in $Q_t$ are imaginary on the material sector, so that scalar part is $-\lvert\partial\phi/\partial q'_t\rvert^2+\lvert\nabla\phi\rvert^2$, and the kinetic term the series writes is

$$
\mathcal L^{\mathrm{kin}}=-\mathrm{Sc}\bigl[(\tilde\nabla^{\natural}\tilde\Phi^{*})(\tilde\nabla\tilde\Phi)\bigr]=\Bigl|\frac{\partial\phi}{\partial q'_t}\Bigr|^2-\lvert\nabla\phi\rvert^2 ,
$$

the kinetic density of the Klein–Gordon article (*Hamiltonian Field Theory in Biquaternionic Form*). **On the material sector** the form itself is $-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial q'_t}+\nabla\cdot\overline{\vec Q_{\mathrm f}}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments. By §*The Gradient*, $\tilde\nabla^{*}=\tilde\nabla^{\natural}$, and

$$
\langle\tilde\nabla,\tilde\nabla\rangle_{*}=\langle\tilde\nabla\rangle_{*}=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{*})=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{\natural})=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q=\Box ,
$$

so the Hermitian norm of the gradient is the d'Alembertian, the same operator as its quaternionic bilinear norm. The **Hermitian form is the one positive-definite form of the four on the biquaternion layer**, $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^2$ on the elements, and its square root is the topological norm $\lVert\tilde Q\rVert_E$; positivity is a property of the elements, the norm of this subsection being the operator $\Box$. **On the material sector** it is the same operator, $\Box|_{\mathbb{M}_-}=\Delta-\partial^2/\partial (q'_t)^2$.

### The Krein Product, Its Form and Its Norm

**The product.** The general quaternionic sesquilinear product is the fourth of the four general products of *Product and Form Conventions*, §*The Twelve Products and Their Names*; it is the conjugate derivative applied to the conjugated field, $\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}$, the companion of the quaternionic bilinear product in the second slot,

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

a scalar, the **contraction** of the conjugate derivative with the conjugated field in the signature of the material sector. **On the material sector** it is $-i\frac{\partial\bar Q_{\mathrm{f}t}}{\partial q'_t}-\nabla\cdot\overline{\vec Q_{\mathrm f}}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments; on the gradient, since $\tilde\nabla^{*}=\tilde\nabla^{\natural}$ (§*The Gradient*),

$$
\langle\tilde\nabla,\tilde\nabla\rangle_{\natural*}=\langle\tilde\nabla\rangle_{\natural*}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla^{*})=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla^{\natural})=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}-\Delta_Q ,
$$

so the Krein norm of the gradient **coincides with the plain bilinear norm**. It is the indefinite partner of the Hermitian form, and on the elements it is the form of signature $(1,3)$ whose diagonal is $\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2$: Hermitian, indefinite — positive where $\lvert Q_t\rvert^2>\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2$ and negative where the opposite inequality holds — so it carries no positivity. It is the form of the indefinite theory — the Krein space — and not of the contractions of these subsections. **On the material sector**, in the real coefficient $q'_t$ of $Q_t=iq'_t$, it is $-\frac{\partial^2}{\partial (q'_t)^2}-\Delta$.

**A contraction is a form, never an index.** The metric of the series is the sign vector $\varepsilon$ inside the product, so no index is raised and none is lowered. Where a text with covariant indices contracts a derivative with a field through a raised and a lowered index, the series writes the quaternionic form $\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural}$; where it contracts two derivatives, the series writes the quaternionic norm $\langle\tilde\nabla\rangle_{\natural}=\Box$; and where it moves an index through a metric, the series writes the element $\tilde Q_{\mathrm f}$ itself, the metric being the sign vector inside the product.

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

## Summary

An operator acting by multiplication **is** the element it multiplies by, so its glyph is the glyph of that element and the marks are read on it as on the element. The named operators take an upright capital and carry the element in the subscript: left multiplication $L_{\tilde Q}$, right multiplication $R_{\tilde Q}$, the two-sided $L_{\tilde Q_1}R_{\tilde Q_2}$, the sandwich $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$, the inner derivation $\operatorname{ad}_{\tilde Q}$ and the automorphism $\operatorname{Ad}_{\tilde Q}$. The sandwich with no qualifier is the bilinear one, and it is quadratic in $\tilde Q$, not bilinear. The side of an action is position, $D\psi$ against $\psi D$; the two are exchanged by the natural conjugation, $(\psi D)^{\natural}=D^{\natural}\psi^{\natural}$, so a right action on a field is a left action on the conjugate field, and no glyph marks a side. The superscript $R$ marks the right derivative, the one case the exchange does not reach, and on the gradient even that case is a conjugation: $\tilde Q_1\overleftarrow{\tilde\nabla}=\bigl(\tilde\nabla^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}$, so a right action is the left action of the conjugate gradient on the conjugate field, and the identity needs no equation.

The **dagger** is the general adjoint of an operator, never of an element, and it is not a fifth conjugation: several adjoints arise at once, one for each form and one for each sandwich, and the dagger is the mark that covers them all. An operator written as an array — a linear map on a coordinate column, a matrix in the $2\times2$ image or a regular matrix — carries no tilde. The **Fock exception** is the one mark that says a glyph is an operator and not an element of the algebra, and its superscript $\mathrm{fop}$ is fixed in *Index, Notation and Corpus Conventions*.

No derivative is written with a dot, and a prime marks the imaginary coordinate and nothing else. Every partial derivative is written with $\partial$ and its variable, the subscript is a component index and never a derivative, and the coordinate derivative is unhalved, $\partial/\partial Q_\mu=\partial/\partial q_\mu+\partial/\partial(iq'_\mu)$.

The two derivative operators of the corpus are the **biquaternionic gradient** $\tilde\nabla=\sum_\mu e_\mu\partial/\partial Q_\mu$ and the **d'Alembertian** $\Box=\langle\tilde\nabla\rangle_{\natural}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)$, the quaternionic norm of the gradient; the operator is scalar and acts coefficient by coefficient. On $\mathbb{M}_-$ the substitution $Q_t=ict'$ flips the sign of the time second derivative, and the same operator reads the wave operator.

The four products are read on the gradient: the plain bilinear product holds the divergence, the gradient and the curl of a field in one object; the quaternionic bilinear product reads the conjugate derivative; the Hermitian product gives the definite form; and the Krein product gives the indefinite one, whose norm coincides with the plain bilinear norm. **A contraction is a form, never an index**: the metric is the sign vector inside the product, and no index is raised or lowered.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q}$, $R_{\tilde Q}$ | Left and right multiplication by the element |
| $L_{\tilde Q_1}R_{\tilde Q_2}$ | The two-sided operator, $L_{\tilde Q_1}R_{\tilde Q_2}$ |
| $\Theta_{\tilde Q}=L_{\tilde Q}R_{\tilde Q^{*}}$ | The bilinear sandwich; $\mathcal{T}_{a,b}$ the sesquilinear one |
| $\operatorname{ad}_{\tilde Q}$, $\operatorname{Ad}_{\tilde Q}$ | The inner derivation and the automorphism |
| ${}^{\dagger}$ | The general adjoint of an operator, never of an element |
| $\partial/\partial Q_\mu$ | The unhalved coordinate derivative |
| $\tilde\nabla=\sum_\mu e_\mu\,\partial/\partial Q_\mu$ | The biquaternionic gradient |
| $\nabla=\sum_k\,\vec e_k\,\partial/\partial Q_k$ | The pure spatial gradient |
| $\Box=\langle\tilde\nabla\rangle_{\natural}$ | The d'Alembertian, the quaternionic norm of the gradient |
| $\mathrm{fop}$ | The Fock-operator mark, the one exception to the element rule |
| $^{\natural}$ | The natural conjugation, $a^{\natural}=(a_0,-a_1,-a_2,-a_3)$; an anti-automorphism, $(ab)^{\natural}=b^{\natural}a^{\natural}$ |
| $(\psi D)^{\natural}=D^{\natural}\psi^{\natural}$ | The exchange of the two sides: a right action on $\psi$ is a left action on $\psi^{\natural}$ |
| $\nabla^{R}$ | The right gradient, $F\nabla^{R}=\sum_\mu(\partial F/\partial q_\mu)e_\mu$; used only where a derivative meets two distinct factors |
| $\overleftarrow{\ }$ | The long arrow over an operator: it acts on the factor written to its left, and the arrow points at that factor; it is not the short arrow of the pure part |
| $\tilde Q_1\overleftarrow{\tilde\nabla}$ | The same gradient transposed, $\sum_\mu(\partial\tilde Q_1/\partial Q_\mu)e_\mu$; the right action, equal to $\bigl(\tilde\nabla^{\natural}\tilde Q_1^{\natural}\bigr)^{\natural}$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853). The original formulation, and the source of the quaternion conjugation and its notation.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636. The biquaternion conjugations and the conventions of the complexified algebra in the applied literature.
