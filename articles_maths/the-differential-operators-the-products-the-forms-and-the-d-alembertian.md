# __The Differential Operators, the Products, the Forms and the D'Alembertian__

## Introduction

The corpus fixes its derivative conventions once, in §*Conventions for Derivation* of *Conventions in Mathematics*, and this
article walks that section in its own order: the subscripts, the prime, the two derivative operators, and the four general
products read on the gradient, each with its product, its symmetric and antisymmetric parts, its form and its norm. Nothing is
proved here. Every statement restates the convention or an article that owns it, and every owner is cited where it is used.

The four general products are *The Four General Products of the Biquaternioid $\mathbb{C}$ Space*, among the twelve operations of
*The 12 Products of the Biquaternioid $\mathbb{C}$ Space*; their four scalar parts are *The 4 Forms over the Biquaternioid
$\mathbb{C}$ Space*; the four norms are *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space*; and the gradient, its
conjugate and the d'Alembertian are developed at length in *Biquaternion Analysis*, §*The Differential Operators*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$,
$e_t=1$, $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, and central imaginary $i$. An element is $\tilde F=F_te_t+\vec F$
with $\vec F=F_x\vec e_x+F_y\vec e_y+F_z\vec e_z$, its four coefficients complex; the field is element-valued and depends on the
coordinates $Q_t,Q_x,Q_y,Q_z$. The conjugations are the natural one $\tilde F^{\natural}$, the coefficientwise one
$\bar{\tilde F}$ and the star $\tilde F^{*}=\bar{\tilde F}^{\natural}$; the scalar part is $\mathrm{Sc}$; and the sign vector is
$\varepsilon=(1,-1,-1,-1)$. All conventions are those of *Conventions in Mathematics*.

## Conventions for Derivation

In this work, subscripts denote vector components, not partial derivatives as in the PDE convention; every partial derivative is
written explicitly with $\partial$ followed by its variable, and no subscript is ever attached to the $\partial$. A subscript is
therefore a component index, as in $v_x$ for the component of a velocity along an axis, or a label, as in
$\tilde U_{\mathrm{r}}$; it never denotes a derivative. The derivative with respect to a coordinate is written
$\partial/\partial Q_\mu$, and in a fixed direction $\partial/\partial Q_t$, $\partial/\partial Q_x$, $\partial/\partial Q_y$ or
$\partial/\partial Q_z$; a coordinate is never left under the $\partial$, so none of the abbreviated spellings of a
partial-differential-equations text occurs, and the rule admits no exception, neither on a free index nor on any other. A
derivative with respect to a variable that is not a coordinate is written the same way, its variable named in full: the
Lagrangian derivative puts the function in the numerator, $\partial L/\partial u$, so that where a PDE text writes $L_u$ and
$L_p$ the corpus writes $\partial L/\partial u$ and $\partial L/\partial p$; the second derivative has the same shape,
$\partial^2 L/\partial u^2$. The function is named in the numerator whenever it is a letter of its own, as for a Lagrangian, a
Hamiltonian or a generating function; the slashed form $\partial/\partial u$ is kept where the symbol is an operator or where the
operand is a compound expression rather than a single letter. The time derivative $\partial/\partial Q_t$ is the imaginary-time
derivative: on the material sector, where $Q_t=ict$, it equals $-\frac{i}{c}\,\partial/\partial t$, and $t$ is not one of the
coordinates, so the real-time partial derivative is written out as $\partial/\partial t$. The rule holds on every object of the corpus,
whether the letter names an element of the algebra, an element-valued field, a kernel or an operator.

**These studies do not use the covariant index conventions: subscripts are not coordinate indices or derivatives, partial derivatives
are written with explicit operators, and the structural information is carried by the algebra of the objects themselves.**

**The derivative marks.** No derivative is written with a dot. The total derivative is written $\frac{d}{dt}$ or $\frac{d}{d\tau}$ with the parameter named; the partial derivative is written $\frac{\partial}{\partial t}$ or, inline, $\partial/\partial t$. A higher derivative is $\frac{d^2}{dt^2}$. The prime is reserved for the derivative with respect to the single argument of a function of one variable, and a second derivative is written with $\partial$, never with a repeated subscript. The scope mark of geometric calculus is an underline, not a dot. These rules are fixed in *Conventions in Mathematics*, §*The Derivative Marks*.

### The Gradient

The two derivative operators of the corpus carry a glyph of their own and are fixed in the conventions and in no other place;
every other partial derivative is written with $\partial$.

The coordinate derivative is written $\partial/\partial Q_\mu$, and the **biquaternionic gradient** is the element-valued operator

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial Q_\mu},
$$

whose tilde marks its scalar part beside its vector part (*Conventions in Mathematics*, §*The Gradient*; *Biquaternion Analysis*),
with its quaternion conjugate $\tilde\nabla^{\natural}=\sum_\mu\varepsilon_\mu e_\mu\,\partial/\partial Q_\mu$ and
$\varepsilon=(1,-1,-1,-1)$. Write $\nabla=\sum_k\vec e_k\,\partial/\partial Q_k$ for the spatial gradient, with divergence
$\nabla\cdot\vec F$ and curl $\nabla\times\vec F$, and
$\Delta_Q=\partial^2/\partial Q_x^2+\partial^2/\partial Q_y^2+\partial^2/\partial Q_z^2$ for the Laplacian in the three vector
coordinates; on the material sector it is the physical $\Delta$.

**The conjugates of the gradient.** The coefficients of $\tilde\nabla$ are the coordinate derivatives $\partial/\partial Q_\mu$,
and such a derivative is real, so conjugation leaves each coefficient as it stands and only the units are affected. The quaternion
conjugation and the Hermitian conjugation both reverse the three spatial units, so the two act on the gradient alike,

$$
\tilde\nabla^{*}=\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial Q_\mu},
\qquad \overline{\tilde\nabla}=\tilde\nabla .
$$

**The forms stay four, the norms are two.** The four forms keep their four conventions, named in §*The Twelve Products and Their
Names* of *Conventions in Mathematics*, each conjugating its own slot: the quaternionic form conjugates the first argument and
the Hermitian form the second, so on a general second argument they are not the same statement. But read at the two equal
arguments they give two operators, the Hermitian norm coinciding with the quaternionic bilinear norm and the Krein norm with the
plain bilinear norm. The four subsections below carry the four forms, and their norms are the two operators $\Box$ and
$\partial^2/\partial Q_t^2-\Delta_Q$.

**On the material sector $\mathbb{M}_-$**, where $Q_t=ict$ and $Q_k=q_k$, the time derivative reads
$\partial/\partial Q_t=-\frac{i}{c}\,\partial/\partial t$, and the gradient is

$$
\tilde\nabla\big|_{\mathbb{M}_-}=-\frac{i}{c}\,e_t\frac{\partial}{\partial t}+\sum_k\vec e_k\frac{\partial}{\partial Q_k}.
$$

### The Plain Bilinear Product, Its Form and Its Norm

**The product.** The general plain bilinear product is one of the four of *The 12 Products of the Biquaternioid $\mathbb{C}$
Space*. On the gradient, with an element-valued field $\tilde F=F_te_t+\vec F$, it is read with
$\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and $\vec e_j\vec e_k=-\delta_{jk}e_t+\epsilon_{jkl}\vec e_l$, so that
the three spatial units carry the field back onto the scalar unit,

$$
\tilde\nabla\tilde F=\Bigl(\frac{\partial}{\partial Q_t}F_t-\nabla\cdot\vec F\Bigr)e_t+\frac{\partial}{\partial Q_t}\vec F+\nabla F_t+\nabla\times\vec F .
$$

A **product** is algebra-valued, and this one holds the divergence, the gradient and the curl of the field in a single object; the
equation $\tilde\nabla\tilde F=-\tilde R$ is the Maxwell equation, whose physical reading belongs to the physics corpus. **On the
material sector** the same product is read with $\partial/\partial Q_t=-\frac{i}{c}\,\partial/\partial t$, the space part being
unchanged.

**The symmetric and antisymmetric parts.** Read with two arguments, the product splits as in §*The Twelve Products and Their
Names* of *Conventions in Mathematics*. The half-sum keeps the form as its scalar part,

$$
\tilde\nabla\bullet\tilde F=\tfrac12\bigl(\tilde\nabla\tilde F+\tilde F\tilde\nabla\bigr)=\Bigl[\frac{\partial}{\partial Q_t}F_t-(\nabla,\vec F)\Bigr]e_t+\frac{\partial}{\partial Q_t}\vec F+F_t\nabla=\Bigl[\frac{\partial}{\partial Q_t}F_t-\nabla\cdot\vec F\Bigr]e_t+\frac{\partial}{\partial Q_t}\vec F+\nabla F_t ,
$$

and the half-difference is the curl,

$$
\tilde\nabla\wedge\tilde F=\tfrac12\bigl(\tilde\nabla\tilde F-\tilde F\tilde\nabla\bigr)=\tfrac12\bigl(\nabla\times\vec F+\nabla\times\vec F\bigr)=\nabla\times\vec F ,
$$

a pure vector, so the plain form carries the whole scalar content of the product. Throughout these four subsections the pair
$(\nabla,\vec X)$ is read as the divergence $\nabla\cdot\vec X$ and $X\nabla$ as the gradient $\nabla X$, the derivative acting on
the coefficient it multiplies, and the coordinate formulas substituted are those of *The 12 Products of the Biquaternioid
$\mathbb{C}$ Space*.

**The form.** The **plain form** is the scalar part of the product read in two arguments,

$$
\langle\tilde\nabla,\tilde F\rangle=\mathrm{Sc}(\tilde\nabla\tilde F)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial}{\partial Q_\mu}F_\mu=\frac{\partial}{\partial Q_t}F_t-\nabla\cdot\vec F ,
$$

a scalar, the **contraction** of the derivative with the field in the sign vector $\varepsilon$. **On the material sector** it is
$-\frac{i}{c}\frac{\partial F_t}{\partial t}-\nabla\cdot\vec F$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments:

$$
\langle\tilde\nabla\rangle=\langle\tilde\nabla,\tilde\nabla\rangle=\mathrm{Sc}\bigl(\tilde\nabla\tilde\nabla\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}-\Delta_Q ,
$$

the cross terms cancelling. **On the material sector** it is $-c^{-2}\frac{\partial^2}{\partial t^2}-\Delta$, the negative of the
wave operator; it is **not** the corpus's d'Alembertian.

### The Quaternionic Bilinear Product, Its Form and Its Norm

**The product.** The general quaternionic bilinear product is the second of the four of *The 12 Products of the Biquaternioid
$\mathbb{C}$ Space*; on the gradient it is $\tilde\nabla^{\natural}\tilde F$, the conjugate derivative, read with the same rules,
the three spatial units now carrying the field back onto the scalar unit with the opposite sign,

$$
\tilde\nabla^{\natural}\tilde F=\Bigl(\frac{\partial}{\partial Q_t}F_t+\nabla\cdot\vec F\Bigr)e_t+\frac{\partial}{\partial Q_t}\vec F-\nabla F_t-\nabla\times\vec F .
$$

**On the material sector** the same substitution $\partial/\partial Q_t=-\frac{i}{c}\,\partial/\partial t$ applies.

**The symmetric and antisymmetric parts.** The half-sum is central and is the quaternionic form itself,

$$
\tilde\nabla\bullet_{\natural}\tilde F=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde F+\tilde F^{\natural}\tilde\nabla\bigr)=\Bigl[\frac{\partial}{\partial Q_t}F_t+(\nabla,\vec F)\Bigr]e_t=\Bigl(\frac{\partial}{\partial Q_t}F_t+\nabla\cdot\vec F\Bigr)e_t ,
$$

and the half-difference is the vector part of the product,

$$
\tilde\nabla\wedge_{\natural}\tilde F=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde F-\tilde F^{\natural}\tilde\nabla\bigr)=\frac{\partial}{\partial Q_t}\vec F-F_t\nabla-\nabla\times\vec F=\frac{\partial}{\partial Q_t}\vec F-\nabla F_t-\nabla\times\vec F .
$$

**The form.** The **quaternionic form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla,\tilde F\rangle_{\natural}=\mathrm{Sc}\bigl(\tilde\nabla^{\natural}\tilde F\bigr)=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial}{\partial Q_\mu}F_\mu=\frac{\partial}{\partial Q_t}F_t+\nabla\cdot\vec F ,
$$

a scalar, the **contraction** of the derivative with the field in the $ict$ metric. It differs from the plain form by the three
signs of $\varepsilon$, which are **computed from the product** $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ and not
assumed. **On the material sector** it is $-\frac{i}{c}\frac{\partial F_t}{\partial t}+\nabla\cdot\vec F$.

**The norm, and the definition of the d'Alembertian.** The norm is defined with the form, as that form at its two equal
arguments, and the two orders of the product agree:

$$
\Box=\langle\tilde\nabla\rangle_{\natural}=\langle\tilde\nabla,\tilde\nabla\rangle_{\natural}
=\mathrm{Sc}\bigl(\tilde\nabla^{\natural}\tilde\nabla\bigr)=\mathrm{Sc}\bigl(\tilde\nabla\tilde\nabla^{\natural}\bigr)
=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q .
$$

**This is the definition of the d'Alembertian**: the quaternionic norm of the gradient, an operator on the whole algebra, one and
the same before any sector is named (*The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space*). The coordinates $Q_\mu$
are those of the algebra and are complex in general; the operator is $\partial^2/\partial Q_t^2+\Delta_Q$ whatever the sector, and
it is **scalar**: it multiplies by $e_t$ and acts coefficient by coefficient, $\Box\tilde F=\sum_\mu(\Box F_\mu)e_\mu$. It is the
identity above, and not the $ict$ substitution, that fixes it, and **no article of the corpus defines a second d'Alembertian**; no
mass-term sign is left to a local convention.

**The special case of the material sector.** On $\mathbb{M}_-$ the coordinates are the material ones, $Q_t=ict$ and $Q_k=q_k$,
and the $ict$ substitution flips the sign of the time second derivative,
$\partial^2/\partial Q_t^2=-c^{-2}\,\partial^2/\partial t^2$, so the same operator reads

$$
\Box\big|_{\mathbb{M}_-}=\frac{\partial^2}{\partial Q_t^2}+\Delta=\Delta-c^{-2}\,\frac{\partial^2}{\partial t^2},
$$

a plus on the spatial part and a minus on the time part. On $\mathbb{M}_-$ this reading is the corpus convention, used by the
majority of the articles. **The $ict$ substitution is a statement about the material sector, not about the operator**, which in
every case is $\partial^2/\partial Q_t^2+\Delta_Q$; its signature is not a property of the operator but of the **slice** it is
read on, since on a named subspace some of the $Q_\mu$ are purely imaginary. The operator is one, and every article writes it the
same way.

### The Hermitian Product, Its Form and Its Norm

**The product.** The general plain sesquilinear product is the third of the four of *The 12 Products of the Biquaternioid
$\mathbb{C}$ Space*; it is the plain product applied to the **conjugated** field
$\tilde F^{*}=\bar F_te_t-\overline{\vec F}$, so that on the gradient it is $\tilde\nabla\tilde F^{*}$, conjugate-linear in the
field while the first slot stays $\mathbb{C}$-linear,

$$
\tilde\nabla\tilde F^{*}=\Bigl(\frac{\partial}{\partial Q_t}\bar F_t+\nabla\cdot\overline{\vec F}\Bigr)e_t-\frac{\partial}{\partial Q_t}\overline{\vec F}+\nabla\bar F_t-\nabla\times\overline{\vec F} .
$$

**The symmetric and antisymmetric parts.** Under the conjugate transpose the half-sum is central and is the Hermitian form
itself,

$$
\tilde\nabla\bullet_{*}\tilde F=\mathrm{Sc}\bigl(\tilde\nabla\tilde F^{*}\bigr)=\Bigl[\frac{\partial}{\partial Q_t}\bar F_t+(\nabla,\overline{\vec F})\Bigr]e_t=\Bigl(\frac{\partial}{\partial Q_t}\bar F_t+\nabla\cdot\overline{\vec F}\Bigr)e_t ,
$$

and the half-difference is the vector part,

$$
\tilde\nabla\wedge_{*}\tilde F=\mathrm{Vect}\bigl(\tilde\nabla\tilde F^{*}\bigr)=-\frac{\partial}{\partial Q_t}\overline{\vec F}+\bar F_t\nabla-\nabla\times\overline{\vec F}=-\frac{\partial}{\partial Q_t}\overline{\vec F}+\nabla\bar F_t-\nabla\times\overline{\vec F} .
$$

**The form.** The **Hermitian form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla,\tilde F\rangle_{*}=\mathrm{Sc}\bigl(\tilde\nabla\tilde F^{*}\bigr)=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial}{\partial Q_\mu}\bar F_\mu=\frac{\partial}{\partial Q_t}\bar F_t+\nabla\cdot\overline{\vec F} ,
$$

a scalar, the **contraction** of the derivative with the **conjugated** field in the sign vector $\varepsilon$. Taken on the
scalar field it gives the scalar part of the product of the two conjugated gradients,

$$
\mathrm{Sc}\bigl[(\tilde\nabla^{\natural}\tilde\Phi^{*})(\tilde\nabla\tilde\Phi)\bigr]=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial\Phi^{*}}{\partial Q_\mu}\frac{\partial\Phi}{\partial Q_\mu} ,
$$

in which the conjugate stands on the first factor and no absolute value is taken; the two time derivatives are imaginary on the
material sector, so that scalar part is $-c^{-2}\lvert\partial\phi/\partial t\rvert^2+\lvert\nabla\phi\rvert^2$. Its physical
reading is the kinetic density, and it belongs to the physics corpus. **On the material sector** the form itself is
$-\frac{i}{c}\frac{\partial\bar F_t}{\partial t}+\nabla\cdot\overline{\vec F}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments. By §*The Gradient*,
$\tilde\nabla^{*}=\tilde\nabla^{\natural}$, and

$$
\langle\tilde\nabla,\tilde\nabla\rangle_{*}=\langle\tilde\nabla\rangle_{*}=\mathrm{Sc}\bigl(\tilde\nabla\tilde\nabla^{*}\bigr)=\mathrm{Sc}\bigl(\tilde\nabla\tilde\nabla^{\natural}\bigr)=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q=\Box ,
$$

so the Hermitian norm of the gradient is the d'Alembertian, the same operator as its quaternionic bilinear norm. The **Hermitian
form is the one positive-definite form of the four**, $\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^2$ on the elements,
and its square root is the topological norm $\lVert\tilde Q\rVert_E$; positivity is a property of the elements, the norm of this
subsection being the operator $\Box$. **On the material sector** it is the same operator,
$\Box|_{\mathbb{M}_-}=\Delta-c^{-2}\,\partial^2/\partial t^2$.

### The Krein Product, Its Form and Its Norm

**The product.** The general quaternionic sesquilinear product is the fourth of the four of *The 12 Products of the Biquaternioid
$\mathbb{C}$ Space*; it is the conjugate derivative applied to the conjugated field, $\tilde\nabla^{\natural}\tilde F^{*}$, the
companion of the quaternionic bilinear product in the second slot,

$$
\tilde\nabla^{\natural}\tilde F^{*}=\Bigl(\frac{\partial}{\partial Q_t}\bar F_t-\nabla\cdot\overline{\vec F}\Bigr)e_t-\frac{\partial}{\partial Q_t}\overline{\vec F}-\nabla\bar F_t+\nabla\times\overline{\vec F} .
$$

**The symmetric and antisymmetric parts.** Under the conjugate transpose the half-sum is

$$
\tilde\nabla\bullet_{\natural*}\tilde F=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde F^{*}+\tilde F^{*}\tilde\nabla^{\natural}\bigr)=\Bigl[\frac{\partial}{\partial Q_t}\bar F_t-(\nabla,\overline{\vec F})\Bigr]e_t-\frac{\partial}{\partial Q_t}\overline{\vec F}-\bar F_t\nabla=\Bigl[\frac{\partial}{\partial Q_t}\bar F_t-\nabla\cdot\overline{\vec F}\Bigr]e_t-\frac{\partial}{\partial Q_t}\overline{\vec F}-\nabla\bar F_t ,
$$

whose scalar part is the Krein form, and the half-difference is the curl of the conjugated field,

$$
\tilde\nabla\wedge_{\natural*}\tilde F=\tfrac12\bigl(\tilde\nabla^{\natural}\tilde F^{*}-\tilde F^{*}\tilde\nabla^{\natural}\bigr)=\tfrac12\bigl(\nabla\times\overline{\vec F}+\nabla\times\overline{\vec F}\bigr)=\nabla\times\overline{\vec F} ,
$$

a pure vector.

**The form.** The **Krein form** is the scalar part of that product read in two arguments,

$$
\langle\tilde\nabla,\tilde F\rangle_{\natural*}=\mathrm{Sc}\bigl(\tilde\nabla^{\natural}\tilde F^{*}\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial}{\partial Q_\mu}\bar F_\mu=\frac{\partial}{\partial Q_t}\bar F_t-\nabla\cdot\overline{\vec F} ,
$$

a scalar, the **contraction** of the conjugate derivative with the conjugated field in the $ict$ metric. **On the material
sector** it is $-\frac{i}{c}\frac{\partial\bar F_t}{\partial t}-\nabla\cdot\overline{\vec F}$.

**The norm.** The norm is defined with the form, as that form at its two equal arguments; on the gradient, since
$\tilde\nabla^{*}=\tilde\nabla^{\natural}$ (§*The Gradient*),

$$
\langle\tilde\nabla,\tilde\nabla\rangle_{\natural*}=\langle\tilde\nabla\rangle_{\natural*}=\mathrm{Sc}\bigl(\tilde\nabla^{\natural}\tilde\nabla^{*}\bigr)=\mathrm{Sc}\bigl(\tilde\nabla^{\natural}\tilde\nabla^{\natural}\bigr)=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu\frac{\partial^2}{\partial Q_\mu^2}=\frac{\partial^2}{\partial Q_t^2}-\Delta_Q ,
$$

so the Krein norm of the gradient **coincides with the plain bilinear norm**. It is the indefinite partner of the Hermitian form,
and on the elements it is the form of signature $(1,3)$ whose diagonal is
$\lvert Q_t\rvert^2-\lvert Q_x\rvert^2-\lvert Q_y\rvert^2-\lvert Q_z\rvert^2$: Hermitian, and negative on a nonzero element, so
it carries no positivity. It is the form of the indefinite theory — the Krein space — and not of the contractions of these
subsections. **On the material sector** it is $-c^{-2}\frac{\partial^2}{\partial t^2}-\Delta$.

**A contraction is a form, never an index.** The metric of the corpus is the sign vector $\varepsilon$ inside the product, so no
index is raised and none is lowered. Where a text with covariant indices contracts a derivative with a field through a raised and
a lowered index, the corpus writes the quaternionic form $\langle\tilde\nabla,\tilde F\rangle_{\natural}$; where it contracts two
derivatives, the corpus writes the quaternionic norm $\langle\tilde\nabla\rangle_{\natural}=\Box$; and where it moves an index
through a metric, the corpus writes the element $\tilde F$ itself, the metric being the sign vector inside the product.

## The Table of the Two Second-Order Operators

| form | norm | operator | on the material sector |
|---|---|---|---|
| general plain bilinear | $\langle\tilde\nabla\rangle$ | $\dfrac{\partial^2}{\partial Q_t^2}-\Delta_Q$ | $-c^{-2}\dfrac{\partial^2}{\partial t^2}-\Delta$ |
| general quaternionic bilinear | $\langle\tilde\nabla\rangle_{\natural}=\Box$ | $\dfrac{\partial^2}{\partial Q_t^2}+\Delta_Q$ | $\Delta-c^{-2}\dfrac{\partial^2}{\partial t^2}$ |
| general plain sesquilinear (Hermitian) | $\langle\tilde\nabla\rangle_{*}=\Box$ | $\dfrac{\partial^2}{\partial Q_t^2}+\Delta_Q$ | $\Delta-c^{-2}\dfrac{\partial^2}{\partial t^2}$ |
| general quaternionic sesquilinear (Krein) | $\langle\tilde\nabla\rangle_{\natural*}$ | $\dfrac{\partial^2}{\partial Q_t^2}-\Delta_Q$ | $-c^{-2}\dfrac{\partial^2}{\partial t^2}-\Delta$ |

## Worked Examples

**A scalar field.** $\tilde F=Q_te_t$: the four products all equal $e_t$, the four forms all equal $1$, and $\Box\tilde F$
vanishes, as a first-degree field requires.

**A single vector coordinate.** $\tilde F=Q_x\vec e_x$: the products are $-e_t$, $e_t$, $e_t$, $-e_t$ in the plain, quaternionic,
Hermitian and Krein readings, and the four forms are $-1$, $+1$, $+1$, $-1$; the example shows the two sign patterns in one line,
and $\Box\tilde F$ vanishes.

**Two coordinates.** $\tilde F=Q_te_t+Q_x\vec e_x$: the plain product vanishes because
$\partial F_t/\partial Q_t=\nabla\cdot\vec F=1$, the quaternionic and Hermitian products equal $2e_t$, and the Krein product
vanishes; the quaternionic and Hermitian forms are $2$, the other two are $0$.

**A quadratic field.** $\tilde F=Q_t^2\vec e_x$: the products are $2Q_t\vec e_x$, $2Q_t\vec e_x$, $-2Q_t\vec e_x$, $-2Q_t\vec e_x$,
the four forms vanish, and $\Box\tilde F=2\vec e_x$, the derivative of degree two.

**A mixed field.** $\tilde F=Q_tQ_x\vec e_y$: the plain product is $Q_x\vec e_y+Q_t\vec e_z$, the quaternionic product is
$Q_x\vec e_y-Q_t\vec e_z$, the Hermitian product is $-Q_x\vec e_y-Q_t\vec e_z$, the Krein product is
$-Q_x\vec e_y+Q_t\vec e_z$; the four forms vanish, the scalar component and the divergence being zero, and $\Box\tilde F$ vanishes.

## Summary

The corpus writes every partial derivative with $\partial$ and names its variable, never with a subscript, and reserves the prime for a
function of one variable. Two operators carry a glyph of their own: the biquaternionic gradient
$\tilde\nabla=\sum_\mu e_\mu\partial/\partial Q_\mu$ and its quaternion conjugate
$\tilde\nabla^{\natural}=\sum_\mu\varepsilon_\mu e_\mu\partial/\partial Q_\mu$, which is also its Hermitian conjugate, the
coefficientwise conjugate leaving the gradient unchanged. The four general products read on the gradient give four
algebra-valued objects and four scalar forms: the plain form $\frac{\partial F_t}{\partial Q_t}-\nabla\cdot\vec F$, the quaternionic form
$\frac{\partial F_t}{\partial Q_t}+\nabla\cdot\vec F$, the Hermitian form $\frac{\partial\bar F_t}{\partial Q_t}+\nabla\cdot\overline{\vec F}$ and the Krein form
$\frac{\partial\bar F_t}{\partial Q_t}-\nabla\cdot\overline{\vec F}$, one to each slot that is conjugated. At the two equal arguments the four forms
give two norms: the d'Alembertian $\Box=\partial^2/\partial Q_t^2+\Delta_Q$, which is the quaternionic bilinear and the Hermitian
norm of the gradient, and its partner $\partial^2/\partial Q_t^2-\Delta_Q$, which is the plain bilinear and the Krein norm. The
d'Alembertian is one operator, scalar and fixed by the identity $\Box=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde\nabla)$; the
material sector reads it as $\Delta-c^{-2}\partial^2/\partial t^2$, the signature belonging to the slice and not to the operator.
A contraction is a form and never an index, the metric being the sign vector inside the product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\partial/\partial Q_\mu$ | the coordinate derivative, written with an explicit operator; a subscript is never a partial derivative |
| $\tilde\nabla=\sum_\mu e_\mu\partial/\partial Q_\mu$ | the biquaternionic gradient, the Cauchy–Riemann operator |
| $\tilde\nabla^{\natural}=\tilde\nabla^{*}$ | its quaternion conjugate, the involution of the norm |
| $\nabla$, $\nabla\cdot\vec F$, $\nabla\times\vec F$ | the spatial gradient, the divergence and the curl |
| $\Delta_Q=\sum_k\partial^2/\partial Q_k^2$ | the Laplacian in the three vector coordinates |
| $\tilde\nabla\tilde F$ | the plain product, holding divergence, gradient and curl |
| $\langle\tilde\nabla,\tilde F\rangle=\frac{\partial F_t}{\partial Q_t}-\nabla\cdot\vec F$ | the plain form |
| $\langle\tilde\nabla,\tilde F\rangle_{\natural}=\frac{\partial F_t}{\partial Q_t}+\nabla\cdot\vec F$ | the quaternionic form |
| $\langle\tilde\nabla,\tilde F\rangle_{*}=\frac{\partial\bar F_t}{\partial Q_t}+\nabla\cdot\overline{\vec F}$ | the Hermitian form |
| $\langle\tilde\nabla,\tilde F\rangle_{\natural*}=\frac{\partial\bar F_t}{\partial Q_t}-\nabla\cdot\overline{\vec F}$ | the Krein form |
| $\Box=\langle\tilde\nabla\rangle_{\natural}=\langle\tilde\nabla\rangle_{*}$ | the d'Alembertian $\partial^2/\partial Q_t^2+\Delta_Q$ |
| $\langle\tilde\nabla\rangle=\langle\tilde\nabla\rangle_{\natural*}$ | the partner operator $\partial^2/\partial Q_t^2-\Delta_Q$ |

## Further Reading

- *Conventions in Mathematics* (`articles_maths/conventions-in-mathematics.md`), §*Conventions for Derivation*, for the
conventions this article re-states
- *Biquaternion Analysis* (`articles_maths/biquaternion-analysis.md`), for the gradient, its conjugate and the d'Alembertian at
length
- *The 12 Products of the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-12-products-of-the-biquaternioid-complex-space.md`),
for the twelve operations and the four general products
- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*
(`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the four forms and their signatures
- *The 4 Algebraic Norms over the Biquaternioid $\mathbb{C}$ Space*
(`articles_maths/the-4-algebraic-norms-over-the-biquaternioid-c-space.md`), for the four norms as the diagonals of the forms
- *Remarkable Subspaces and the Analysis* (`articles_maths/remarkable-subspaces-and-the-analysis.md`), for the operator of the
norm read on each remarkable subspace
