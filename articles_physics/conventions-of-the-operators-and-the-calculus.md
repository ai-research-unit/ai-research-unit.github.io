# __Conventions of the Operators and the Calculus__

## Introduction

These are the conventions of the operators and of the calculus. An operator acting by multiplication is the element it multiplies by, and its glyph is the glyph of that element; the article fixes the named operators, the dagger, the Kraus operator and the Fock exception. The calculus follows: the derivative marks, the gradient and the d'Alembertian, and the four product-form-norm readings of the gradient that the field equations use.

The article assumes the base of *Conventions in the Biquaternion Universe*, the products and forms of *Conventions of the Products and the Forms*, and the norms of *Conventions of the Norms and the Pairings*. The representations are in *Conventions of the Representations*; the superscripts on operators are in *Conventions of the Units, the Indices and the Notation*.

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

**The two marks on a glyph that is also an operator.** An operator read through its element follows the element rule in full.

- A glyph read with its scalar part, four components: the tilde. The canonical momentum $\tilde p=p_te_t+\vec p$, the Legendre conjugate of $\tilde q$; the biquaternionic gradient $\tilde\nabla$ of §*The Gradient*; the gauge-covariant derivative $\tilde D$.
- A pure glyph, three components: the arrow. The momentum operator $\vec p=-i\hbar\nabla=\vec e_kp_k$.

The gradient decides the case cleanly: $\tilde\nabla$ is not pure, because its $e_t$ term carries $\partial/\partial Q_t$, while $\nabla=\vec e_k\,\partial/\partial Q_k$ is pure and keeps the fixed glyph of §*The Gradient*, which carries no second mark.

**The case follows the layer.** The arrow does not change the case: a pure operator of the quaternion layer stays lower case, $\vec p$, and one of the biquaternion layer takes the upper case, $\vec P$. Where the letter already names another object of the layer, a subscript fixes the operator, $\vec P_{\mathrm{op}}$, or the explicit form $-i\hbar\vec\nabla$ is used. The three-momentum and the momentum operator share $\vec p$, as an eigenvalue and its operator do.

**The dagger.** The dagger is the general adjoint of an operator, never of an element: $(L_a)^{\dagger}=L_{a^{*}}$. Several adjoints arise at once — one for each form, and one for each of the sandwiches — and the dagger is the mark that covers them all, of which the others are the instances. It is not a fifth conjugation: it belongs to the operators and not to the algebra. Where a dagger is written on an element the writing is an abuse: the mark that was meant is the star for the Hermitian conjugation, or the natural sign for the quaternion conjugation, according to the conjugation in view. The dagger is added to the glyph and does not replace the element's mark: the arrow states purity, which the adjoint preserves, so $\vec p^{\dagger}$ is again a pure operator; the tilde states a glyph read with its scalar part, which the adjoint also preserves, so $\tilde\nabla$ keeps its tilde. Where the adjoint in view is the one of the definite form and the operator carries no derivative, the two marks are written together, dagger first: $(L_a)^{\dagger}=(L_a)^{*}=L_{a^{*}}$. A derivative separates them: its dagger is the adjoint and carries the integration by parts, its star conjugates the units alone (§*The Gradient*); the series writes $\tilde\nabla^{*}=\tilde\nabla^{\natural}$ for the star.

**A Kraus operator is an element, not an array.** The Kraus operators of a channel or an instrument multiply the state on both sides, $\Phi(\tilde{Ϛ})=\sum_l\tilde K_l\tilde{Ϛ}\tilde K_l^{*}$, so each $\tilde K_l$ is an element of $\mathbb{B}$ and carries the tilde of the element. It is not a matrix, and the ban on a tilde on an array does not apply to it. Where the same operator is read as an array, that array is its image $\mathsf{M}_2(\tilde K_l)$, which carries no tilde, and its adjoint is the dagger, $\mathsf{M}_2(\tilde K_l)^{\dagger}=\mathsf{M}_2(\tilde K_l^{*})$; the corpus does not use that reading, and the star on the element is not a matrix adjoint.

**The Fock exception.** A Fock operator is not an element of the algebra; its superscript $\mathrm{fop}$ and the order of the two marks are fixed in *Conventions of the Units, the Indices and the Notation*, §*The Superscripts*.

## Conventions for Derivation

In this work, subscripts denote vector components, not partial derivatives as in the PDE convention; every partial derivative is written explicitly with $\partial$ followed by its variable, and no subscript is ever attached to the $\partial$. A subscript is therefore a component index, as in $v_x$ for the component of a velocity along an axis, or a label, as in $\tilde U_{\mathrm r}$; it never denotes a derivative. The derivative with respect to a coordinate is written $\partial/\partial Q_\mu$, and in a fixed direction $\partial/\partial Q_t$, $\partial/\partial Q_x$, $\partial/\partial Q_y$ or $\partial/\partial Q_z$; a coordinate is never left under the $\partial$, so none of the abbreviated spellings occurs, and the rule admits no exception, neither on a free index nor on any other.

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

**These studies do not use the covariant index conventions: subscripts are not coordinate indices or derivatives, partial derivatives are written with explicit operators, and structural information is carried by the algebra of the objects themselves.**

### The Derivative Marks

**No dot.** No derivative is written with a dot. The total derivative with respect to a parameter is written with a fraction and the parameter named: $\frac{d}{dt'}$ for time, $\frac{d}{d\tau}$ for proper time, $\frac{d}{dt'_r}$ for retarded time; inline, the same derivative is written $dq/dt'$. The partial derivative is written $\frac{\partial}{\partial t'}$ or, inline, $\partial/\partial t'$. A higher derivative is written $\frac{d^2}{d{t'}^2}$, $\frac{\partial^2}{\partial {t'}^2}$. The derivative binds to its whole argument, so a power is written outside a bracket, $\left(\frac{dx}{dt'}\right)^2$, never as $\frac{dx^2}{dt'}$.

**The prime marks the imaginary part, and nothing else.** The prime belongs to a coefficient: it marks the imaginary part of a complex number, $q'_\mu$ of $Q_\mu = q_\mu + iq'_\mu$, the part that carries the $i$. It is not a derivative mark, and it is not a label of an element, a field or a coupling. A derivative is written with $d$ or $\partial$ and its variable named: a function of one variable is differentiated as $df/dx$, never as $f'$, and a second derivative as $d^2f/dx^2$ or $\partial^2f/\partial x^2$, never with a repeated prime or a repeated subscript. The complex time is $Q_t = c(t+it')$: its real part $ct$ is the informational time and its imaginary part $ct'$ the material time, with $q_t = ct$ and $q'_t = ct'$. The prime on $t'$ marks the coefficient that carries the $i$, exactly as the primes on $x',y',z'$ mark the imaginary spatial coefficients. Carried by an element glyph, the same prime names the element assembled from the primed coefficients, $\tilde q' = q'_t\,e_t+q'_x\vec e_x+q'_y\vec e_y+q'_z\vec e_z$ in $\tilde Q = \tilde q+i\tilde q'$, the antiquaternion part; it is the coefficient prime read on the whole glyph, not a label of a transformed or distinguished element.

**The prime is not a frame, source or field label.** The primed spatial coordinates $x',y',z'$ are the imaginary parts of the spatial coefficients, $Q_x=x+ix'$, $Q_y=y+iy'$, $Q_z=z+iz'$, with $(q'_x,q'_y,q'_z)=(x',y',z')$; the prime names the coordinate that carries the $i$. The primed time $t'$ is the imaginary part of $Q_t=c(t+it')$, with $q'_t=ct'$; the unprimed time $t$ is its real part, with $q_t=ct$. Outside these uses the prime is not written. A transformed frame is named by a subscript, never by $x'$ or $t'$; a source point, a second point and an integration variable take a numeric or role subscript, never a prime; an element, field, connection, curvature, current, state, coupling, group or map that is transformed or distinguished takes a numeric or role subscript, never a prime; and a derivative is written $df/dx$, never $f'$. The glyph $x'$ cannot be both the imaginary coordinate and a source or boosted coordinate: where both are needed, the source point or the frame takes the subscript.

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

**The conjugates of the gradient.** The gradient is an operator, and the marks are read on its units at fixed coordinate: the derivative symbols are held fixed and only the units are conjugated. This fixes the scope of the star, and it is not a claim that $\partial/\partial Q_\mu$ is real; the unhalved derivative of §*Conventions for Derivation* is complex, and on an element-valued field the star is coefficientwise, carried through the derivative by $\partial/\partial\bar Q_\mu$ rather than by $\partial/\partial Q_\mu$. Read on the units, the quaternion conjugation reverses the three spatial units, and so does the Hermitian conjugation, so the two act on the gradient alike,

$$
\tilde\nabla^{*}=\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial Q_\mu},
\qquad \overline{\tilde\nabla}=\tilde\nabla .
$$

**The forms stay four, the norms are two.** The four forms of *Conventions of the Products and the Forms*, §*The Involutions and the Four Forms* remain four distinct conventions here, because each conjugates its own slot: the quaternionic form conjugates the first argument and the Hermitian form the second, so on a general second argument they are not the same statement. But read at the two equal arguments they give two operators, the Hermitian norm coinciding with the quaternionic bilinear norm, $\langle\tilde\nabla\rangle_{*}=\langle\tilde\nabla\rangle_{\natural}$, and the Krein norm with the plain bilinear norm, $\langle\tilde\nabla\rangle_{\natural*}=\langle\tilde\nabla\rangle$. The four subsections below carry the four forms, and their norms are the two operators $\Box$ and $\partial^2/\partial Q_t^2-\Delta_Q$.

**On the material sector $\mathbb{M}_-$**, where $Q_t=ict'$ and $Q_k=q_k$, the time derivative reads $\partial/\partial Q_t=-\frac{i}{c}\,\partial/\partial t'$, the Laplacian is the physical $\Delta$, and the gradient is

$$
\tilde\nabla\big|_{\mathbb{M}_-}=-\frac{i}{c}\,e_t\frac{\partial}{\partial t'}+\sum_k\vec e_k\frac{\partial}{\partial Q_k}.
$$

### The Plain Bilinear Product, Its Form and Its Norm

**The product.** The general plain bilinear product is one of the four of *Conventions of the Products and the Forms*, §*The Twelve Products and Their Names*. On the gradient, with an element-valued field $\tilde Q_{\mathrm f}=Q_{\mathrm{f}t}e_t+\vec Q_{\mathrm f}$, it is read with $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and $\vec e_j \vec e_k=-\delta_{jk}e_t+\epsilon_{jkl}\vec e_l$, so that the three spatial units carry the field back onto the scalar unit,

$$
\tilde\nabla\tilde Q_{\mathrm f}=\Bigl(\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f}\Bigr)e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}+\nabla Q_{\mathrm{f}t}+\nabla\times\vec Q_{\mathrm f} .
$$

A **product** is algebra-valued, and this one holds the divergence, the gradient and the curl of the field in a single object; for the field strength $\tilde F$ the equation $\tilde\nabla\tilde F=-\sqrt{\mu}\,\tilde J$, with $\tilde J=ic\rho\,e_t+\vec J$, is the series' Maxwell equation. **On the material sector** the same product is read with $\partial/\partial Q_t=-\frac{i}{c}\,\partial/\partial t'$, the space part being unchanged.

**The symmetric and antisymmetric parts.** Read with two arguments, the product splits as in *Conventions of the Products and the Forms*, §*The Twelve Products and Their Names*. The half-sum keeps the form as its scalar part,

$$
\tilde\nabla\bullet\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla\tilde Q_{\mathrm f}+\tilde Q_{\mathrm f}\tilde\nabla\bigr)=\Bigl[\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}-(\nabla,\vec Q_{\mathrm f})\Bigr]e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}+Q_{\mathrm{f}t}\nabla=\Bigl[\frac{\partial}{\partial Q_t}Q_{\mathrm{f}t}-\nabla\cdot\vec Q_{\mathrm f}\Bigr]e_t+\frac{\partial}{\partial Q_t}\vec Q_{\mathrm f}+\nabla Q_{\mathrm{f}t} ,
$$

and the half-difference is the curl,

$$
\tilde\nabla\wedge\tilde Q_{\mathrm f}=\tfrac12\bigl(\tilde\nabla\tilde Q_{\mathrm f}-\tilde Q_{\mathrm f}\tilde\nabla\bigr)=\tfrac12\bigl(\nabla\times\vec Q_{\mathrm f}+\nabla\times\vec Q_{\mathrm f}\bigr)=\nabla\times\vec Q_{\mathrm f} ,
$$

a pure vector, so the plain form carries the whole scalar content of the product. Throughout these four subsections the pair $(\nabla,\vec X)$ is read as the divergence $\nabla\cdot\vec X$ and $X\nabla$ as the gradient $\nabla X$, the derivative acting on the coefficient it multiplies, and the coordinate formulas substituted are those of *Conventions of the Products and the Forms*, §*The Twelve Products and Their Names*.

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

**The product.** The general quaternionic bilinear product is the second of the four of *Conventions of the Products and the Forms*, §*The Twelve Products and Their Names*; on the gradient it is $\tilde\nabla^{\natural}\tilde Q_{\mathrm f}$, the conjugate derivative, read with the same rules, the three spatial units now carrying the field back onto the scalar unit with the opposite sign,

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

a scalar, the **contraction** of the derivative with the field in the $ict'$ metric. It differs from the plain form by the three signs of $\varepsilon$, which are **computed from the product** $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and not assumed. **On the material sector** it is $-\frac{i}{c}\frac{\partial Q_{\mathrm{f}t}}{\partial t'}+\nabla\cdot\vec Q_{\mathrm f}$.

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

**The product.** The general plain sesquilinear product is the third of the four of *Conventions of the Products and the Forms*, §*The Twelve Products and Their Names*; it is the plain product applied to the **conjugated** field $\tilde Q_{\mathrm f}^{*}=\bar Q_{\mathrm{f}t}e_t-\overline{\vec Q_{\mathrm f}}$, so that on the gradient it is $\tilde\nabla\tilde Q_{\mathrm f}^{*}$, conjugate-linear in the field while the first slot stays $\mathbb{C}$-linear,

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

a scalar, the **contraction** of the derivative with the **conjugated** field in the sign vector $\varepsilon$. Taken on the scalar field it gives the **kinetic density**, the scalar part of the product of the two conjugated gradients,

$$
\mathrm{Sc}\bigl[(\tilde\nabla^{\natural}\tilde\Phi^{*})(\tilde\nabla\tilde\Phi)\bigr]=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial\Phi^{*}}{\partial Q_\mu}\frac{\partial\Phi}{\partial Q_\mu} ,
$$

in which the conjugate stands on the first factor and no absolute value is taken; the two time derivatives are imaginary on the material sector, so that scalar part is $-c^{-2}\lvert\partial\phi/\partial t'\rvert^2+\lvert\nabla\phi\rvert^2$, and the kinetic term the series writes is

$$
\mathcal L_{\mathrm{kin}}=-\mathrm{Sc}\bigl[(\tilde\nabla^{\natural}\tilde\Phi^{*})(\tilde\nabla\tilde\Phi)\bigr]=\frac{1}{c^2}\Bigl|\frac{\partial\phi}{\partial t'}\Bigr|^2-\lvert\nabla\phi\rvert^2 ,
$$

the kinetic density of the Klein–Gordon article (*Hamiltonian Field Theory in Biquaternionic Form*). **On the material sector** the form itself is $-\frac{i}{c}\frac{\partial\bar Q_{\mathrm{f}t}}{\partial t'}+\nabla\cdot\overline{\vec Q_{\mathrm f}}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments. By §*The Gradient*, $\tilde\nabla^{*}=\tilde\nabla^{\natural}$, and

$$
\langle\tilde\nabla,\tilde\nabla\rangle_{*}=\langle\tilde\nabla\rangle_{*}=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{*})=\mathrm{Sc}(\tilde\nabla\tilde\nabla^{\natural})=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q=\Box ,
$$

so the Hermitian norm of the gradient is the d'Alembertian, the same operator as its quaternionic bilinear norm. The **Hermitian form is the one positive-definite form of the four**, $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^2$ on the elements, and its square root is the topological norm $\lVert\tilde Q\rVert_E$; positivity is a property of the elements, the norm of this subsection being the operator $\Box$. **On the material sector** it is the same operator, $\Box|_{\mathbb{M}_-}=\Delta-c^{-2}\,\partial^2/\partial {t'}^2$.

### The Krein Product, Its Form and Its Norm

**The product.** The general quaternionic sesquilinear product is the fourth of the four of *Conventions of the Products and the Forms*, §*The Twelve Products and Their Names*; it is the conjugate derivative applied to the conjugated field, $\tilde\nabla^{\natural}\tilde Q_{\mathrm f}^{*}$, the companion of the quaternionic bilinear product in the second slot,

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

**A contraction is a form, never an index.** The metric of the series is the sign vector $\varepsilon$ inside the product, so no index is raised and none is lowered. Where a text with covariant indices contracts a derivative with a field through a raised and a lowered index, the series writes the quaternionic form $\langle\tilde\nabla,\tilde Q_{\mathrm f}\rangle_{\natural}$; where it contracts two derivatives, the series writes the quaternionic norm $\langle\tilde\nabla\rangle_{\natural}=\Box$; and where it moves an index through a metric, the series writes the element $\tilde Q_{\mathrm f}$ itself, the metric being the sign vector inside the product.

## Summary

An operator whose letter is the letter of an element is that element: the tilde and the arrow are read on it as on the element, and no mark says operator. The named operators are left and right multiplication, the two-sided operator, the sandwich and the inner derivation. The dagger is the general adjoint of an operator and not a fifth conjugation, and it adds to the element's mark rather than replacing it. A Kraus operator is an element, not an array. The Fock operator is the one operator that is not an element, and its superscript is fixed with the other tokens.

A subscript is a component or a label, never a derivative; every partial derivative is written with $\partial$ and its variable. The coordinate derivative is unhalved, $\partial/\partial Q_\mu=\partial/\partial q_\mu+\partial/\partial(iq'_\mu)$. The gradient is $\tilde\nabla$, not pure. The d'Alembertian is $\Box=\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\partial^2/\partial Q_t^2+\Delta_Q$, read on the material sector as $\Delta-c^{-2}\partial^2/\partial t'^2$, and every article uses this one operator with the mass equation $(\Box-m^2c^2/\hbar^2)\psi=0$.

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
| $\Box$ | The d'Alembertian, $\tilde\nabla\tilde\nabla^{\natural}=\partial^2/\partial Q_t^2+\Delta_Q$ |

## Further Reading

- [Conventions in the Biquaternion Universe](conventions-in-the-biquaternion-universe.html), for the algebra and the element glyphs.
- [Conventions of the Products and the Forms](conventions-of-the-products-and-the-forms.html), for the four products read on the gradient.
- [Conventions of the Norms and the Pairings](conventions-of-the-norms-and-the-pairings.html), for the norms of those products.
- [Conventions of the Units, the Indices and the Notation](conventions-of-the-units-the-indices-and-the-notation.html), for the Fock superscript and the subscript rules.
- [The Element and Operator Representations](the-element-and-operator-representations.html), companion article, for the three actions and their matrices.
