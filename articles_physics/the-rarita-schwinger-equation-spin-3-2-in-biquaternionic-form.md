# __The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form__

## Introduction

The Proca equation carries spin one, and the Dirac equation carries spin one-half, and both describe a single field. Spin three-halves is the first case that requires a field with two indices: the **Rarita–Schwinger field** $\psi_\mu$ is a four-vector whose components are Dirac spinors, sixteen complex components in all, and its equation removes twelve of them, leaving the four states of a spin-$\tfrac32$ particle. The equation was written down by Rarita and Schwinger in 1941, and it is the field equation of the gravitino in supergravity; it is also the place where the standard field theory of higher spin first becomes delicate, since under minimal coupling to electromagnetism the field propagates superluminally.

This article writes the Rarita–Schwinger system in biquaternionic form and reduces it in the rest frame, where the spin-$\tfrac32$ content is transparent. The framework treats the field as a **biquaternion-valued four-vector**, a family $\tilde{\Psi}_\mu\in\mathbb{B}$ with $\mu=0,1,2,3$, and the equation as three statements. The first is a **chiral pair** on each component: two Dirac equations, one for each chiral half, and the place where the gradient pair and chirality meet. The right-handed half obeys the equation driven by the gradient acting from the left,
$$
\tilde\nabla\tilde\Psi_{\mu,R}=m\tilde\Psi_{\mu,L},
$$
and the left-handed half obeys the equation driven by the conjugate gradient,
$$
\tilde\nabla^{\natural}\tilde\Psi_{\mu,L}=m\tilde\Psi_{\mu,R},
\qquad \mu=0,1,2,3 .
$$
Neither half closes on its own: each equation maps one half into the other, so the mass is the off-diagonal pairing of the pair. Read from either side, the statement is that every component of the vector-spinor is a Dirac field, and the two readings are the two chiralities.

**The derivative is the gradient, and there is one.** The calculus of this article is the calculus of the corpus:

$$
\tilde\nabla=e_t\frac{\partial}{\partial Q_t}+\vec e_x\frac{\partial}{\partial Q_x}+\vec e_y\frac{\partial}{\partial Q_y}+\vec e_z\frac{\partial}{\partial Q_z},
$$

its quaternion conjugate is

$$
\tilde\nabla^{\natural}=e_t\frac{\partial}{\partial Q_t}-\vec e_x\frac{\partial}{\partial Q_x}-\vec e_y\frac{\partial}{\partial Q_y}-\vec e_z\frac{\partial}{\partial Q_z},
$$

and the d'Alembertian is the quaternionic norm of the gradient,

$$
\Box=\tilde\nabla\tilde\nabla^{\natural}=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q,
\qquad
\Box\big|_{\mathbb{M}_-}=\Delta-c^{-2}\frac{\partial^2}{\partial {t'}^2}.
$$

No other letter names the gradient, and no other first-order operator is introduced below. Every derivative in every display is $\tilde\nabla$, $\tilde\nabla^{\natural}$, or a coordinate derivative $\partial/\partial Q_\mu$ written out.

**The gradient does not square to a scalar, and the massive equation says so.** Write $\tilde K=K_0e_t+K_x\vec e_x+K_y\vec e_y+K_z\vec e_z$ for a symbol of the gradient. The time unit commutes with the three spatial units, the mixed derivatives are symmetric, and the square keeps a vector part,

$$
\tilde K^2=\bigl(K_0^2-K_x^2-K_y^2-K_z^2\bigr)e_t+2K_0\bigl(K_x\vec e_x+K_y\vec e_y+K_z\vec e_z\bigr),
$$

so $\tilde\nabla^2$ is not a scalar and is not the d'Alembertian. A first-order operator with scalar square therefore does not exist in this algebra, and a single field cannot carry a mass. The free equation is first order in one field,

$$
\tilde\nabla\tilde\Psi=0,
$$

and the massive equation is the **chiral pair**, two fields and two equations,

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,
\qquad
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R,
$$

whose scalar square is $\Box$. No one-field first-order massive equation is written in this article, and $\tilde\nabla^2$ is nowhere identified with $\Box$.

The second statement is a **trace constraint**: the four components contracted with the vector index annihilate the field, and in the algebra that contraction reads as one element, the right multiplier $\vec e_z$ being what the three spatial directions leave behind. The third is its companion **divergence constraint**:

$$
\begin{aligned}
\tilde\Psi_0+\sum_k\vec e_k\tilde\Psi_k\,\vec e_z&=0,\\
\sum_\mu\varepsilon_\mu\,\partial/\partial x_\mu\,\tilde\Psi_\mu&=0,
\end{aligned}
$$

with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the frame. The source states the three statements as one antisymmetrized equation; the algebra states them as the pair and the two constraints, and the translation between the two writings is made once, in the next section. In the rest frame the system forces the time component to vanish, forces the spatial components to their upper (positive-frequency) parts, and imposes the single vector condition $\boldsymbol{\sigma}\cdot\vec\chi=0$ on the spatial amplitudes. The surviving space is exactly four-dimensional, and it carries the spin-$\tfrac32$ quartet. The construction also exhibits the spin-$\tfrac32$ projector: the transverse projector on the vector index, $P_{ij} = \delta_{ij} - \tfrac13\sigma_i\sigma_j$, which is idempotent and selects precisely the constrained spatial amplitudes.

Two features of the standard theory are recorded and read in the algebra. First, in the massless case the system has a gauge freedom $\psi_\mu\to\psi_\mu+\partial/\partial x_\mu\,\epsilon$, with $\epsilon$ an arbitrary Dirac spinor; the freedom removes the spin-$\tfrac12$ branches that the representation theory places in the field, leaving the two helicities $\pm\tfrac32$. Second, in the massive case the constraint structure is more rigid and the minimal coupling is known to be inconsistent: the field propagates acausally in an external electromagnetic background, the Velo–Zwanziger obstruction, and a consistent interacting theory requires either a gravitational background or a gauge principle. The framework represents these facts; it does not remove them.

The conventions are those of the companion articles: the algebra, the units, the gradient and the d'Alembertian are those of *Algebra and Element Conventions*, *Operator and Calculus Conventions* and *Frame Conventions*, and the pair operator is the one of *Operator and Calculus Conventions*, §*The Dynamics*. None is restated here.

**The source's letters, fixed once.** Where a letter of the source is kept, it is read in $\mathbb{B}$. The source's $i$, wherever it acts on a spinor, is the pseudoscalar

$$
\omega=-\vec e_z,\qquad \omega^2=-e_t,
$$

and it acts on the **right**, $\psi\mapsto\psi\omega=-\psi\vec e_z$. It is not the central imaginary $i$ of $\mathbb{B}$, which stays free and keeps its name. The side is part of the definition: the left action $\omega\psi=-\vec e_z\psi$ is a different element of $\mathbb{B}$ and is not the source's chirality. The label $\mu$ of a component is the coordinate index of its spacetime direction, and the index is always written low. The sign vector is $\varepsilon_\mu$, the square of the $\mu$-th direction up to its sign, $\varepsilon_0=+1$, $\varepsilon_k=-1$.

The informational basis is $e_t,i\vec e_x,i\vec e_y,i\vec e_z$ — the four units that square to $+e_t$ — and it is distinct from the coordinate basis $e_\mu=(e_t,\vec e_x,\vec e_y,\vec e_z)$, whose three spatial legs carry no factor $i$. With the mostly-minus metric $\varepsilon=(1,-1,-1,-1)$,

$$
e_t^2=+e_t,\qquad (i\vec e_k)^2=+e_t,\qquad \mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}.
$$

No index is raised or lowered, and the metric enters only through the **sign vector** $\varepsilon_\mu$: where two low indices are contracted with the metric, the term carries $\varepsilon_\mu$. The frames themselves are those of *Frame Conventions*, and a frame is a coordinate choice, not a structure of the algebra.

**Coordinates and frames.** The displays are written in the $\mathbb{M}_-$ frame, with $\partial/\partial x_\mu$ the derivative in the physical coordinates $x_\mu=(t',x,y,z)$. The algebra's own coordinate is $Q_t=ict'$, and $\partial/\partial t'=i\partial/\partial Q_t$; the gradient is $\tilde\nabla=-ie_t\partial/\partial t'+\sum_k\vec e_k\partial/\partial x_k$ on that sector, with $c=1$ in what follows until the dispersion relation restores it, its $e_t$ term carrying the material time. A display that mixes the algebra's time derivative with the frame's spatial derivatives is not a frame, and none is used. The covariant divergence of a vector-spinor is $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\psi_\mu$, written $\operatorname{div}\psi$ below. In the algebra it is $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\tilde\Psi_\mu$: four coordinate derivatives with the metric weights $\varepsilon_\mu$ and no unit attached, because the four components carry the four directions as an index and not as an algebra unit. It is a contraction of the family, not a further operator, and it is not the gradient: the gradient carries a unit on each term and an $i$ on the time one.

## The Standard Rarita–Schwinger Field

### The field and its equation

The Rarita–Schwinger field is a vector-spinor: a four-vector index and a Dirac spinor index, written $\psi_{\mu\alpha}$ with $\mu=0,1,2,3$ and $\alpha=1,\dots,4$. The source writes its equation through two objects: a totally antisymmetrized triple $T_{\mu\nu\rho}$, antisymmetric in all three indices and vanishing when two of them coincide, and an antisymmetrized pair $h_{\mu\nu}$, antisymmetric in its two. Both are matrices of one chosen display of the source, representatives and not elements of $\mathbb{B}$, and the two carry the two roles: the triple the kinetic structure and the pair the mass structure.

**The source's own equation** is one antisymmetrized equation: the triple contracted with the derivative and with the field, plus $i\,m$ times the pair contracted with the field. In the algebra it is the three statements of the introduction, and the translation is made once here. The kinetic structure is the **gradient pair**: the antisymmetrized triple contracts the derivative index with the three spatial directions, and the contraction on a component is $\tilde\nabla$ on the right-handed half and $\tilde\nabla^{\natural}$ on the left-handed half. The mass structure is **left multiplication by an element** $\Gamma_{\mu\nu}\in\mathbb{B}$, the table of which is given in *The Vector-Spinor Field in the Biquaternion Framework*. Nothing else of the source's composites survives the translation, because nothing else of them is an operator on $\mathbb{B}$.

**The factor $i$ is not a convention.** The source has two writings of the same equation, one with the triple and a real mass term and one with the epsilon combination and an imaginary one. The epsilon combination is $\pm i$ times the triple, the sign being the metric weight of the raised index, so the two writings differ by the pseudoscalar $\omega$ and an overall sign. Written with a real mass term in place of $i\,m$ the equation has no solutions at all: the sixteen-component momentum-space matrix of that display is then invertible on the mass shell, its determinant not vanishing at $k^2=m^2$, while with $\pm i\,m$ it has the four-dimensional kernel of the quartet. The check was run at three masses: the nullity is $4$ with the imaginary mass and $0$ with the real one. The overall sign is then a free convention of the source's writing, and this article keeps the one whose positive-frequency solutions have the rest-frame frequency $\varpi=m$.

The equation is the Euler–Lagrange equation of the Rarita–Schwinger Lagrangian, whose kinetic term is the same antisymmetrized combination and whose mass term is the antisymmetrized pair, up to an overall normalisation that is a convention. The index structure is fixed by the requirement that the equation be first order and that its free solutions carry spin $\tfrac32$. No first-order equation for a single lower-spin field can do that: the two-index structure is necessary, and the antisymmetrizations are what make the equation carry an irreducible spin-$\tfrac32$ rather than a reducible sum. The Lagrangian also shows where the mass term sits: it is the antisymmetrized pair, not the metric term $\varepsilon_\mu\delta_{\mu\nu}$, and this is what distinguishes the spin-$\tfrac32$ mass term from the Proca mass term $\tfrac12m^2\sum_\mu A_\mu A_\mu$.

### The constraint and the reduction

The massive equation implies the trace in two contractions, and the same two contractions deliver the reduced dynamics. Write $\tilde S:=\tilde\Psi_0+\sum_k\vec e_k\tilde\Psi_k\vec e_z$ for the trace element of the family. The first contraction is the divergence of the equation: the kinetic structure is antisymmetric in its first and third indices, so the divergence kills it, and what survives is the divergence of the trace. The second is the contraction with the raised direction, which turns the equation into the trace element itself. In the algebra the two results are the two constraints of the framework, and for $m\neq0$ both hold as consequences and not as conditions:

$$
\tilde S=0,\qquad \sum_\mu\varepsilon_\mu\,\partial/\partial x_\mu\,\tilde\Psi_\mu=0 ,
$$

the second following from the divergence of the equation once the first holds. The trace is therefore a consequence of the massive equation, and so is the divergence. Both were checked at generic on-shell momenta: the solution space of the equation is four-dimensional, the trace element and the divergence vanish on it to machine precision, and adjoining either condition does not lower the dimension.

The trace in turn linearises the equation. With the trace in force, the mass structure reduces to left multiplication by $\Gamma_{\mu\nu}$ on the component, contracted with the corresponding component of the field, and the kinetic structure reduces to the gradient pair, so the equation of the $\mu$-th component is the pair on that component alone. Written once for a single component, with $\Psi=(\Psi_L,\Psi_R)$, the pair is the pair operator of the conventions,

$$
\mathbb{D}\Psi=\bigl(\tilde\nabla\Psi_R,\ \tilde\nabla^{\natural}\Psi_L\bigr),
\qquad
\mathbb{D}^2=\Box\,I ,
$$

so the massive component equation is $(\mathbb{D}-m)\Psi_\mu=0$. The operator is the pair written once: every entry of it is one of the two gradients, and no matrix of a display enters.

The antisymmetrized equation is thus equivalent to the pair on each component together with the trace, and, through them, the covariant divergence. The mass term regenerates the pair on each component, so that the reduced dynamics is the one the companion Dirac article supplies. The trace constraint removes one Dirac spinor's worth of components from the sixteen, and it is the part of the reduction that the algebra can state as a single element.

The massless case separates the constraints, and the separation is what the gauge freedom is for. For $m=0$ the same two contractions no longer force the trace: $\tilde S=0$ is not contained in the equation, and adjoining it lowers the solution space from six dimensions to four. Both numbers were checked at generic lightlike momenta. The covariant divergence is a different matter, because its four components are linear combinations of the components of the equation: $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\tilde\Psi_\mu=0$ remains a consequence of the equation even when the mass vanishes, and adjoining it lowers nothing. It is in the massless case that the **gauge freedom**

$$
\psi_\mu \longrightarrow \psi_\mu + \partial/\partial x_\mu\,\epsilon,
$$

appears, with $\epsilon$ an arbitrary Dirac spinor: the antisymmetrized kinetic structure is built from the field strength $\partial/\partial x_\rho\,\psi_\sigma$, which changes by a symmetric derivative that the antisymmetrization discards. The gauge freedom is the spin-$\tfrac32$ analogue of the electromagnetic gauge freedom, it is what removes the spin-$\tfrac12$ branch that the vector index introduces, and it is also what makes the trace usable: the trace values that occur on the massless solution space span a space of dimension two, exactly the space of trace shifts a gauge transformation can produce, so the gauge $\tilde S=0$ is attainable and the trace is a complete gauge choice rather than a derived constraint.

### Representation content

The Lorentz transformation character of the field is read off from the two indices. The vector index carries $(\tfrac12,\tfrac12)$ and the spinor index carries $(\tfrac12,0)\oplus(0,\tfrac12)$, so the field transforms in the tensor product

$$
\left(\tfrac12,\tfrac12\right)\otimes\left[\left(\tfrac12,0\right)\oplus\left(0,\tfrac12\right)\right]
= \left(1,\tfrac12\right)\oplus\left(0,\tfrac12\right)\oplus\left(\tfrac12,1\right)\oplus\left(\tfrac12,0\right),
$$

of complex dimension $6+2+6+2=16$, as the component count requires. On restriction to the rotation subgroup, with $s\otimes s_{\mathrm R}$ evaluated at the diagonal,

$$
\left(1,\tfrac12\right)\big|_{SU(2)} = \tfrac32\oplus\tfrac12, \qquad
\left(0,\tfrac12\right)\big|_{SU(2)} = \tfrac12,
$$

and conjugate statements for the other two summands. The field therefore contains

$$
2\times\tfrac32 \;\oplus\; 4\times\tfrac12
$$

under $SU(2)$, of dimensions $2\cdot4 + 4\cdot2 = 16$. Two spin-$\tfrac32$ multiplets — one for the particle and one for the antiparticle — and four spin-$\tfrac12$ multiplets. The whole content of the Rarita–Schwinger equation and of its gauge structure is the removal of those four spin-$\tfrac12$ multiplets, and the rest-frame computation below exhibits the removal explicitly.

### Counting the physical states

Two independent conditions remove the spin-$\tfrac12$ content, and because they act on different structures their effects add. The **algebraic trace** $\tilde S=0$ removes one Dirac spinor's worth of components, which is two spin-$\tfrac12$ multiplets. The **gauge freedom** in the massless case removes another Dirac spinor's worth, another two spin-$\tfrac12$ multiplets. What is left is the two spin-$\tfrac32$ multiplets, of total dimension eight, and for each frequency sign that is the four-dimensional quartet of a spin-$\tfrac32$ particle. In the massive case the gauge freedom is absent, and the second pair of spin-$\tfrac12$ multiplets is removed instead by the subsidiary conditions that follow from the equation; the physical count is the same four states per charge.

The counting is therefore representation-theoretic and does not depend on the detailed form of the antisymmetrizations: any first-order equation whose solutions are pure spin-$\tfrac32$ must remove exactly the four spin-$\tfrac12$ multiplets from the tensor product, and the trace constraint and the gauge freedom are the two mechanisms that do it. This is the reason the field is the minimal carrier of spin $\tfrac32$: the next tensor product that could carry it, the three-index object, would carry still more lower-spin admixture, and the two-index object is the smallest that contains $\tfrac32$ at all.

### The known difficulties

In the massive case the constraint structure is rigid: the equation implies the trace $\tilde S=0$ and the covariant divergence $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\tilde\Psi_\mu=0$, there is no gauge freedom to remove the remaining components, and the resulting theory has the right free-field content but is known to be inconsistent upon minimal coupling to an external electromagnetic field. The propagation becomes acausal for sufficiently strong backgrounds — the Velo–Zwanziger obstruction — and a consistent interacting spin-$\tfrac32$ theory requires a gravitational or gauge principle rather than a fixed background. This is the standard status of the field, and it is recorded here because the biquaternion formulation does not alter it: the algebra rewrites the free equation faithfully, and the difficulties belong to the coupling.

## The Vector-Spinor Field in the Biquaternion Framework

### The carrier

The biquaternion carrier of a spin-$\tfrac32$ field is a **biquaternion-valued four-vector**,

$$
\tilde{\Psi}_\mu \in \mathbb{B}, \qquad \mu=0,1,2,3,
$$

that is, a family of four elements of the algebra, one for each spacetime index. In components, $\tilde{\Psi}_\mu = \Psi_{\mu,0}e_t + \Psi_{\mu,1}\vec e_x + \Psi_{\mu,2}\vec e_y + \Psi_{\mu,3}\vec e_z$ with complex coefficients, so that the carrier has $4\times4 = 16$ complex components, matching the standard field. The vector index is carried by the algebra's own four-vector structure, as it is for the Proca potential, and the spinor index by the regular module of the algebra, as it is for the Dirac field, whose carrier is the sum of the two minimal left ideals of $\mathbb{B}$. The gradient acts on that module from the left and leaves the module structure alone. The Rarita–Schwinger field is therefore a **mixed object**: neither an element of a module over $\mathbb{B}$ nor a pure element of $\mathbb{B}$ transforming by conjugation, but a tensor product of the two. This is the structural reason it lies outside the algebra's native spin content, a point the final article of the subcategory develops.

### The correspondence with the source's frame

The source's equation is transcribed component by component, and the transcription is one linear map. The source contracts its four-vector index with four generators; the algebra's four units of the informational basis carry the same index. Write $E_\mu$ for the source's generator with index $\mu$ — a matrix of the display, not an element of $\mathbb{B}$ — and assign

$$
E_\mu \;\longmapsto\; e_t \ (\mu=0), \qquad E_\mu \;\longmapsto\; i\vec e_k \ (\mu=k).
$$

From the span of the four generators onto $\mathbb{B}$ this is a complex-linear isomorphism, and the two sides are different kinds of object throughout: a matrix on the left, an element on the right. It carries the index and nothing else. It is not multiplicative, and no product of images is used below: the equation needs two structures only, the gradient for the kinetic term and one element of $\mathbb{B}$ for each index pair of the mass term.

**The kinetic structure is the gradient.** The antisymmetrized triple of the source contracts the derivative index with the three spatial directions and antisymmetrizes over all three. In the algebra that contraction is the gradient: $\tilde\nabla$ on the right-handed half of each component, $\tilde\nabla^{\natural}$ on the left-handed half, with the material time derivative carried by the $e_t$ term alone, $\partial/\partial Q_t=-(i/c)\partial/\partial t'$. No other first-order structure enters, and the triple itself is not needed once the contraction is made.

**The mass structure is an element.** The antisymmetrized pair of the source is, in the algebra, left multiplication by an element of $\mathbb{B}$,

$$
\Gamma_{\mu\nu}\longmapsto \Gamma_{0k}=i\vec e_k,\quad \Gamma_{k0}=-i\vec e_k,\quad \Gamma_{jk}=\pm\vec e_l,\quad \Gamma_{00}=0,
$$

with the sign of $\Gamma_{jk}$ fixed by the orientation $\vec e_x\vec e_y=\vec e_z$ and $\vec e_l$ the remaining direction. The six entries with one time index are imaginary multiples of a spatial unit and square to $+e_t$; the six entries with two spatial indices are spatial units and square to $-e_t$. All twelve were checked, and the orientation $\vec e_x\vec e_y=\vec e_z$ gives $\Gamma_{12}=\vec e_z$, $\Gamma_{23}=\vec e_x$ and $\Gamma_{31}=\vec e_y$. The mass term of the $\mu$-th equation is $\sum_\nu\Gamma_{\mu\nu}\tilde\Psi_\nu$ — left multiplication by an element, contracted with the corresponding component of the field. Nothing of the source's pair survives beyond this element, and the element is frame-free: it is written in the units and carries no reference to a frame.

The mass structure is where the two families of the source differ, and the difference is the reason the timelike and the spacelike entries have opposite squares: the timelike entries are built from the informational units, which square to $+e_t$, and the spacelike ones from the coordinate spatial units, which square to $-e_t$. The frame the source uses carries both families, and the algebra needs no frame to state the difference.

### The equivalent constraint form

The biquaternion form of the free field is the chiral pair on each component,

$$
\boxed{\;
\begin{aligned}
\tilde\nabla\tilde\Psi_{\mu,R}&=m\tilde\Psi_{\mu,L},\\
\tilde\nabla^{\natural}\tilde\Psi_{\mu,L}&=m\tilde\Psi_{\mu,R},
\end{aligned}
\qquad\text{for each }\mu\;}
$$

together with the two constraints,

$$
\boxed{\;
\begin{aligned}
\tilde\Psi_0+\sum_k\vec e_k\tilde\Psi_k\,\vec e_z&=0,\\
\sum_\mu\varepsilon_\mu\,\partial/\partial x_\mu\,\tilde\Psi_\mu&=0,
\end{aligned}\;}
$$

where the first line is the algebra reading of the source's trace, derived two paragraphs below, $\varepsilon=(1,-1,-1,-1)$ is the sign vector of the frame, and $\tilde\Psi_\mu=\tilde\Psi_{\mu,L}+\tilde\Psi_{\mu,R}$ is the decomposition of each component into its two chiral halves. The first display is two Dirac equations per component — $\tilde\nabla$ on the right chiral half and $\tilde\nabla^{\natural}$ on the left one, with the mass as the off-diagonal pairing. Every object in these displays is an element of $\mathbb{B}$ or a derivative of one; no frame appears.

The equivalence with the antisymmetrized equation is the standard free-field reduction. If each component satisfies the chiral pair, and if the trace and divergence constraints hold, then the antisymmetrized equation follows; conversely, the antisymmetrized equation implies the pair and the trace, and the divergence. The pair is the component transcription of the antisymmetrized kinetic structure, and the two constraints are the transcription of the two contractions; the biquaternion form is the pair and the constraints.

**The trace in the algebra.** The source's trace contracts the family with the four directions. Each of the three spatial components is multiplied by its direction on the left and by $\vec e_z$ on the right, the time component by neither, and the four results are added into one element of $\mathbb{B}$,

$$
\tilde S=\tilde\Psi_0+\sum_k\vec e_k\tilde\Psi_k\,\vec e_z ,
$$

so the source's condition is equivalent to $\tilde S=0$. The two forms carry the same four complex conditions, and the map from the sixteen complex components to those four has rank four, checked exactly. The right multiplier $\vec e_z$ is what the three spatial directions leave behind, and it is not decoration: without it the condition is a different map of the same rank, with a different kernel, checked. The condition is frame-free: both sides are elements of $\mathbb{B}$, and no frame enters.

**The mass term is frame-free.** With the entries read as above, the mass term of the $\mu$-th equation is left multiplication by the element $\Gamma_{\mu\nu}$ of $\mathbb{B}$, contracted with the corresponding component. No frame appears in the result, and the mass term is therefore a statement about the algebra and not about a display.

## The Rest-Frame Reduction

### Setting up

**Time convention.** The check is performed in the $\mathbb{M}_-$ frame, with $x_0=t'$. The series' algebra coordinate is $Q_t=ict'$; the two are related by $\partial/\partial t'=i\partial/\partial Q_t$, not by relabelling $Q_t$ as $t'$, and the substitution is applied to the whole pair at once. At rest the two operators of the pair take the same value, $\tilde\nabla=-me_t$ and $\tilde\nabla^{\natural}=-me_t$, because the spatial derivatives vanish and the two differ only in the signs of those derivatives. That coincidence is the content of the rest-frame check: the pair degenerates to two copies of one equation.

The computation below is a frame check: it evaluates the standard transcription at rest. The invariant statement is the pair and the constraints. Take the field at rest and of positive frequency, so that each component is proportional to $\exp(-imt')$; the derivative is $\partial/\partial t'\to-im$, equivalently $\partial/\partial Q_t\to-m$. The pair becomes

$$
-m\,\tilde\Psi_{\mu,R}=m\,\tilde\Psi_{\mu,L},
\qquad
-m\,\tilde\Psi_{\mu,L}=m\,\tilde\Psi_{\mu,R},
$$

that is $\tilde\Psi_{\mu,L}=-\tilde\Psi_{\mu,R}$, and the two members give the same condition. Each component of the field is an element of $\mathbb{B}$, four complex; the two halves are independent, and the condition identifies one with the negative of the other, so two complex survive per component, eight in all. The trace constraint is four complex conditions on those eight, so the free solution space is four complex dimensional, the count the frame computation below confirms.

### The trace constraint at rest

The trace constraint at rest is $\tilde\Psi_0+\sum_k\vec e_k\tilde\Psi_k\vec e_z=0$ with the components of the form above, and in the frame of the source its reading is explicit. It forces the time component to vanish and imposes a single two-component condition on the three spatial amplitudes,

$$
\boxed{\;\psi_0 = 0 \quad\text{(upper)}, \qquad
-\boldsymbol{\sigma}\cdot\vec\chi = 0 \quad\text{(lower)}\;},
$$

with $\chi_k$ the two-component amplitude of the $k$-th spatial component and $\sigma_i$ the Pauli matrices acting on that amplitude. Both lines were checked in that display, on the whole solution space and not on a single wavefunction: the time component vanishes identically, the spatial amplitudes lie in one half of the display, and the condition $\boldsymbol{\sigma}\cdot\vec\chi=0$ cuts the six spatial upper components to four.

The split of a component into its upper and lower two-component amplitudes is the split of the display and not the chiral split: chirality is right multiplication by $\omega$, while the two slots are read off the coefficients of the element itself. The trace element respects neither slot: it multiplies each spatial component on the right by $\vec e_z$, which is $-\omega$, and that is why chirality passes through the constraint. Right multiplications commute, so $\tilde S(\Psi\omega)=\tilde S(\Psi)\omega$: the constraint is diagonal in chirality and constrains each chiral half on its own.

The lower equation gives $\boldsymbol{\sigma}\cdot\vec\chi=0$; the upper gives $\psi_0 = 0$. The trace constraint therefore forces the time component to vanish **and** imposes the single vector condition $\boldsymbol{\sigma}\cdot\vec\chi=0$ on the three spatial amplitudes. The combined system of the pair on all four components and the trace constraint has nullity four, the constraint $\boldsymbol{\sigma}\cdot\vec\chi=0$ has nullity four, and the two solution spaces coincide.

### The spin-one-half content and its removal

The three spatial amplitudes $\chi_k$ carry $3\times2 = 6$ complex components before the condition. Under the rotation group the spatial index is a spin-one object and the two-component spinor a spin-$\tfrac12$ object, so

$$
1\otimes\tfrac12 = \tfrac32 \oplus \tfrac12, \qquad 3\times2 = 4 + 2 ,
$$

and the condition $\boldsymbol{\sigma}\cdot\vec\chi=0$ removes exactly the spin-$\tfrac12$ piece of dimension two. What remains is a four-dimensional space, the spin-$\tfrac32$ quartet, with states of spin projection $\pm\tfrac32$ and $\pm\tfrac12$ along any axis. The representation-theory count of the field had two spin-$\tfrac32$ multiplets; the one found here is the positive-frequency or particle multiplet, and the negative-frequency or antiparticle multiplet is obtained by the conjugate choice of frequency and has the same four states. The four spin-$\tfrac12$ multiplets of the field are removed, two by the trace constraint and two by the equation, exactly as the general consistency analysis requires.

### Verification

Every number below was recomputed, in the algebra and in a display of the source, and the two languages agree.

*At rest.* The pair gives two complex components per component of the field, eight in all, and the trace is four independent conditions on those eight, so the solution space is four-dimensional. In the display the sixteen-component operator has vanishing diagonal blocks, so the components are not decoupled: the time component couples to the spatial ones and the spatial components couple among themselves, and the four-dimensional null space is reached through that coupling and not component by component. On that null space the time component vanishes identically and the spatial components lie in the upper half. The trace map has rank four on the sixteen components and annihilates the whole four-dimensional null space, so in the massive case the trace is implied and not imposed.

*At generic on-shell momenta*, with three distinct nonzero spatial components so that no rest-frame degeneracy can hide a mismatch: the nullity is four; the trace and the divergence both vanish on the solution space to $10^{-15}$; and adjoining either condition leaves the nullity at four. With a real coefficient in place of $i\,m$ the momentum-space operator has nullity zero, which is the statement that the mass term must be imaginary.

*At generic lightlike momenta*: the nullity is six, the four-dimensional space of pure-gauge modes $\psi_\mu\propto\partial/\partial x_\mu\epsilon$ is a subspace, the divergence vanishes on the whole solution space, the trace does not, and adjoining the trace leaves four. The trace values of the solutions span a space of dimension two, which is the space of trace shifts the gauge transformation produces.

*In the algebra*: the trace map has rank four on the sixteen complex components. On a null momentum the symbol of the gradient, $\tilde K=K_0e_t+K_x\vec e_x+K_y\vec e_y+K_z\vec e_z$, is a zero divisor. The null condition is its quaternion norm, $\tilde K\tilde K^{\natural}=K_0^2+K_x^2+K_y^2+K_z^2=0$, which for $K_0=i\varpi$ and real $\vec k$ is $\varpi^2=\vec k^2$ and not $\varpi^2=-\vec k^2$. Then left multiplication by $\tilde K$ has rank two and a two-dimensional kernel, checked on four independent null momenta. On a non-null momentum the same left multiplication has rank four and no kernel. That kernel is where the two helicities live, and it is the algebraic reason the massless count is the count it is.

The projector $P_{ij}$ was checked to be idempotent to machine precision, to annihilate the longitudinal modes $\chi_i=\sigma_i\xi$, to fix the transverse ones, and to have trace two over the vector index.

## The Spin-Three-Halves Projector

The constraint $\boldsymbol{\sigma}\cdot\vec\chi=0$ defines a subspace of the six-dimensional space of spatial amplitudes — three vector directions, two spinor components each — and the projector onto it is elementary. Define, on the vector index,

$$
\boxed{\;P_{ij} = \delta_{ij} - \tfrac13\,\sigma_i\sigma_j\;}.
$$

Then $P$ is idempotent,

$$
P_{ik}P_{kj} = \delta_{ij} - \tfrac23\sigma_i\sigma_j + \tfrac19\sigma_i\sigma_k\sigma_k\sigma_j
= \delta_{ij} - \tfrac23\sigma_i\sigma_j + \tfrac13\sigma_i\sigma_j = \delta_{ij} - \tfrac13\sigma_i\sigma_j = P_{ij},
$$

using $\sigma_k\sigma_k = 3I_2$. It annihilates exactly the longitudinal direction, the spin-$\tfrac12$ admixture: applied to $\chi_i=\sigma_i\xi$ it gives $\sigma_i\xi-\tfrac13\sigma_i\sigma_j\sigma_j\xi=\sigma_i\xi-\sigma_i\xi=0$, while applied to a $\chi$ with $\boldsymbol{\sigma}\cdot\vec\chi=0$ it returns $\chi_i$, since the second term is then $\tfrac13\sigma_i(\boldsymbol{\sigma}\cdot\vec\chi)=0$. Its trace over the vector index is $3-1=2$, so it projects the three spatial directions onto two, and combined with the two spinor components it leaves the four states of spin $\tfrac32$.

The projector is the rest-frame form of the covariant spin-$\tfrac32$ projector of the standard theory, which is the transverse projector with respect to the four-momentum $p_\mu$, evaluated at $p_\mu=(m,0,0,0)$. In the biquaternion framework the boost is effected by rotor conjugation, so the covariant projector is the rotor conjugate of the rest-frame combination above; the algebra supplies the boost without a separate construction.

## The Massless Case and the Gauge Freedom

### The gauge transformation in the algebra

In the massless case the antisymmetrized equation and the trace constraint leave a gauge freedom, and in the biquaternion form the transformation is

$$
\tilde{\Psi}_\mu \;\longrightarrow\; \tilde{\Psi}_\mu + \partial/\partial x_\mu\,\epsilon,
$$

where $\epsilon$ is a Dirac-spinor parameter and $\partial/\partial x_\mu$ is the coordinate derivative of the $\mathbb{M}_-$ frame. The shift carries no direction unit. $\tilde\nabla$ is the sum of its four terms with a unit attached to each, and it maps one element of $\mathbb{B}$ to one element; the shift adds to each of the four components its own coordinate derivative and no unit, which is what makes it a shift of a family of four components rather than the action of the gradient on one. The antisymmetrized kinetic structure of the equation is insensitive to the shift, just as the electromagnetic field strength is insensitive to the coordinate gradient of the potential. The number of gauge parameters is the number of components of $\epsilon$, namely four, which is one Dirac spinor; and the gauge freedom removes two of the four spin-$\tfrac12$ multiplets of the representation content. The remaining two are removed by the trace condition and the equations of motion — with the difference, recorded above, that in the massless case the trace is a gauge choice and the divergence condition is the consequence of the equation, so that the two mechanisms do not simply add but interlock. What is left is a single spin-$\tfrac32$ multiplet per frequency sign, that is, the two helicities $\pm\tfrac32$.

### Helicities and the two physical states

The physical content of the massless field is therefore two states per wavevector, the helicities $\pm\tfrac32$. There is no longitudinal or scalar helicity, and the count is the spin-$\tfrac32$ analogue of the two transverse helicities of the photon: in both cases the gauge freedom and the constraint together halve-and-halve the naive index content. The parallel is exact at the level of the representation theory. The photon's two-form is the antisymmetric square of the four-vector, $(1,0)\oplus(0,1)$; the massless Rarita–Schwinger field's two physical states are the two helicities of the $(1,\tfrac12)$ and $(\tfrac12,1)$ summands after the spin-$\tfrac12$ pieces are gauged away. In both cases the two physical states are the two conjugate summands of the representation content, which is why the self-dual split of the spin-one article has a counterpart here, and in both cases the massless limit is the case in which the lower states are removed by gauge rather than retained by a mass.

## The Massive Case

For $m\neq0$ the mass term of the $\mu$-th equation is

$$
m\sum_\nu \Gamma_{\mu\nu}\,\tilde\Psi_\nu ,
$$

left multiplication by the element of $\mathbb{B}$ tabulated above, contracted with the corresponding component of the field. In the trace form of the equation it is simply the mass on each component, and the mass plays the same structural role as in the Proca and Dirac cases: it is linear in the field, it is what remains when the gauge freedom is absent, and it fixes the dispersion relation on the physical shell through the pair. In the rest frame the massive reduction above is the whole story: time component zero, spatial components in one half of the display, $\boldsymbol{\sigma}\cdot\vec\chi=0$, four states.

The massive case is also where the known difficulty lives. The constraint analysis that produces $\tilde S=0$ and $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\tilde\Psi_\mu=0$ is rigid when $m\neq0$, and its consequences for the interacting theory are the Velo–Zwanziger obstruction: minimal coupling to a background electromagnetic field makes some modes propagate faster than light, and the theory is not causal as a fixed-background field theory. The biquaternion formulation reproduces the free constraint structure exactly and says nothing different about the coupling, because the coupling is an additional structure that no rewriting of the free equation can supply. This is the analogue, for spin $\tfrac32$, of the statement recorded for the Proca field: the algebra represents the free field faithfully, and what the free algebra cannot decide is the interaction.

### The dispersion relation

Because each component satisfies the Dirac equation, each component satisfies the Klein–Gordon equation on squaring, exactly as in the spin-$\tfrac12$ case. For a biquaternion plane wave of the component,

$$
\tilde{\Psi}_\mu = \tilde{\Psi}_{\mu,0}\,\exp(\,i\,\mathrm{Sc}(\tilde P\tilde Q^{\natural})/\hbar),
$$

with $\tilde Q=x_0e_t+\sum_k x_k\vec e_k$ the coordinate element and $\tilde P=p_0e_t+\sum_k p_k\vec e_k$ its conjugate momentum, the Dirac equation on the component requires $\tilde P\tilde P^{\natural}=-m^2c^2$ in the normalization of the companion Dirac article, that is,

$$
\frac{\varpi^2}{c^2} - \vec k^2 = \frac{m^2c^2}{\hbar^2},
\qquad\text{i.e.}\qquad
\varpi^2 = c^2\vec k^2 + \frac{m^2c^4}{\hbar^2},
$$

the same physical massive shell as the Proca field. The trace constraint and the subsidiary conditions then reduce the sixteen components to the four states of the quartet, with the three-momentum on the shell. The dispersion relation is therefore common to the massive spin-one and spin-$\tfrac32$ fields, as it must be: the mass shell is a property of the representation's Casimir and not of the index structure.

## Comparison with Spin One and Spin One-Half

The three field equations of this subcategory and its lower-spin neighbours form a sequence, and the sequence is the clearest statement of what the biquaternion framework does and does not carry natively.

| Field | Standard carrier | Components | Constraints | Physical components |
|---|---|---|---|---|
| Dirac, spin $\tfrac12$ | Dirac spinor | $4$ | the equation alone, removing $2$ | $2$ |
| Proca, spin $1$ | four-vector | $4$ | Lorenz, removing $1$ | $3$ |
| Rarita–Schwinger, spin $\tfrac32$ | vector-spinor | $16$ | trace and subsidiary, removing $12$ | $4$ |

In each row the physical component count is $2s+1$ for the particle, and the equation together with its constraints removes the remainder. The role that the field's index structure plays is to supply a carrier large enough to contain the spin: the Dirac spinor is the defining module of the algebra and needs no index; the Proca field adds a four-vector index, which the algebra carries by conjugation on $\mathbb{M}_-$; the Rarita–Schwinger field adds a vector index to the spinor, which the algebra carries only as a tensor product of the two. Each step multiplies the carrier by the four-vector and each step therefore adds lower-spin admixture that a constraint has to remove.

The biquaternion description follows the same sequence. The Dirac field is an element of the spinor module, that is, of the Peirce carrier which is the algebra's minimal left ideal here; the Proca field is an element of the material sector $\mathbb{M}_-$ with the field strength in the vector part; the Rarita–Schwinger field is a family of elements of $\mathbb{B}$ indexed by the spacetime direction. The pattern is that the algebra carries the four-vector index by conjugation and the spinor index by left multiplication, and that no carrier beyond these two is available. This is the structural observation that the final article of the subcategory turns into a statement about the algebra's module category: the spin content accessible to the algebra's own modules is bounded, and it is $\{0,\tfrac12\}$.

## What Is Standard and What the Algebra Adds

**The standard part.** The vector-spinor field, the antisymmetrized equation, the trace constraint, the gauge freedom, the reduction to the Dirac equation, the spin-$\tfrac32$ content, and the Velo–Zwanziger difficulty are all standard and are transcribed here. The representation-theory count $2\times\tfrac32\oplus4\times\tfrac12$ and the reduction $1\otimes\tfrac12=\tfrac32\oplus\tfrac12$ are standard.

**The algebra's part.** Three statements are the framework's. First, the natural carrier of the field is the family of biquaternion-valued components $\tilde{\Psi}_\mu$, and the two structural conditions of the free theory — the chiral pair on each component and the trace constraint $\tilde S=0$ — are each single algebraic statements in $\mathbb{B}$ rather than lists of component equations. The antisymmetrized equation is a transcription of the pair, not a third condition. Second, chirality is the pseudoscalar $\omega=-\vec e_z$ acting on the right, $\psi\mapsto\psi\omega$, whose square is $-e_t$; it commutes with the trace map and with the gradient pair, so the vector-spinor's chirality structure needs no independent operator beyond the units the algebra already has. Third, the rest-frame projector $P_{ij}=\delta_{ij}-\tfrac13\sigma_i\sigma_j$ is obtained from the constraint by elementary algebra, and its boosted form is the rotor conjugate of the rest-frame object, so the covariant spin-$\tfrac32$ projector is available without a separate construction.

**What is imported.** The identification of the field with a spin-$\tfrac32$ particle, the value of the mass, the existence of a consistent interaction, and the resolution of the Velo–Zwanziger problem are inputs beyond the free algebra. The canonical quantisation of the field and its propagator belong to the field-theoretic companion subcategory.

The structural point that this article makes for the subcategory is that the field is a tensor product of the algebra's vector structure with its spinor structure, so its spin-$\tfrac32$ content is not native to the algebra but arises from the product. The final article of the subcategory states this in general and proves that the algebra's own modules carry only spin one-half, the scalar living in the centre and the vector in the adjoint.

The conventions are those of two companion articles:

- Companion article *The Dirac Equation in Biquaternionic Form*, for the biquaternion chiral pair and its equivalence with the component Dirac equation.
- Companion article *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector*, for the vector part of the algebra and the four-vector representation from which the vector-spinor is built.

## Summary

The Rarita–Schwinger field is a vector-spinor of sixteen complex components. Its equation, in the source's writing, is one antisymmetrized equation; in the algebra it is the chiral pair on each component together with the two constraints

$$
\tilde\Psi_0+\sum_k\vec e_k\tilde\Psi_k\,\vec e_z=0,
\qquad
\sum_\mu\varepsilon_\mu\,\partial/\partial x_\mu\,\tilde\Psi_\mu=0,
$$

with the mass as the off-diagonal pairing of the pair and the mass term of each component a left multiplication by the element $\Gamma_{\mu\nu}$. In the massive case both constraints are consequences of the equation: the solution space is four-dimensional and the trace and the divergence vanish on it. In the massless case the divergence is still a consequence and the trace is not; the gauge freedom $\psi_\mu\to\psi_\mu+\partial/\partial x_\mu\,\epsilon$ shifts the trace by exactly the two-dimensional space the trace values occupy, so the trace is a complete gauge choice.

In the rest frame the system forces the time component to vanish and the spatial amplitudes to satisfy $\boldsymbol{\sigma}\cdot\vec\chi=0$. The surviving space is four-dimensional and carries the spin-$\tfrac32$ quartet; the projector onto it is $P_{ij}=\delta_{ij}-\tfrac13\sigma_i\sigma_j$, idempotent and of vector-index rank two. The representation content $2\times\tfrac32\oplus4\times\tfrac12$ loses its four spin-$\tfrac12$ multiplets to the constraint and the gauge freedom, and the massless field retains the two helicities $\pm\tfrac32$.

The field is a tensor product of the algebra's vector structure and its spinor structure, so spin $\tfrac32$ is not native to the algebra. The free equation is represented faithfully; the known difficulty of the interacting theory, the Velo–Zwanziger acausal propagation under minimal coupling, is a property of the coupling and is not removed by the rewriting.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Central scalar imaginary of $\mathbb{B}$, $i^2=-1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$ | The gradient and its quaternion conjugate; the only first-order operators of the article |
| $\Box$ | The d'Alembertian, $\partial^2/\partial Q_t^2+\Delta_Q$, and $\Delta-c^{-2}\partial^2/\partial {t'}^2$ on $\mathbb{M}_-$ |
| $\tilde K$ | Symbol of the gradient, $K_0e_t+K_x\vec e_x+K_y\vec e_y+K_z\vec e_z$ |
| $\mathbb{D}$ | Pair operator on $\mathbb{B}\oplus\mathbb{B}$, $\mathbb{D}\Psi=(\tilde\nabla\Psi_R,\tilde\nabla^{\natural}\Psi_L)$, with $\mathbb{D}^2=\Box I$ |
| $\omega=-\vec e_z$, $\omega^2=-e_t$ | The pseudoscalar; the source's $i$ acting on a spinor, from the right |
| $e_t$, $i\vec e_k$ | Informational basis, the four units that square to $+e_t$; frame-free trace and mass terms |
| $\tilde{\Psi}_\mu\in\mathbb{B}$ | Biquaternion-valued components of the vector-spinor |
| $\epsilon$ | Dirac-spinor parameter of the massless shift symmetry |
| $\Gamma_{0k}=i\vec e_k$, $\Gamma_{k0}=-i\vec e_k$, $\Gamma_{jk}=\pm\vec e_l$ | Mass-term coefficients in $\mathbb{B}$; the mass term is left multiplication by $\Gamma_{\mu\nu}$ |
| $\varepsilon_\mu=-g_{\mu\mu}=(1,-1,-1,-1)$ | Sign vector of the frame; the metric weight of a contracted low index |
| $\tilde S=\tilde\Psi_0+\sum_k\vec e_k\tilde\Psi_k\vec e_z$ | Trace constraint in $\mathbb{B}$; the source's trace, four complex conditions of rank four |
| $\operatorname{div}\psi=\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\psi_\mu$ | Covariant divergence; a consequence of the equation for every $m$ |
| $\tilde\nabla\tilde\Psi_{\mu,R}=m\tilde\Psi_{\mu,L}$, $\tilde\nabla^{\natural}\tilde\Psi_{\mu,L}=m\tilde\Psi_{\mu,R}$ | Chiral pair on each component; the dynamics |
| $\psi_\mu=(\chi_\mu,\eta_\mu)$ | Upper and lower two-component parts, the two halves of the display |
| $\vec\chi$ | Spatial amplitudes; constraint $\boldsymbol{\sigma}\cdot\vec\chi=0$ |
| $P_{ij}=\delta_{ij}-\tfrac13\sigma_i\sigma_j$ | Spin-$\tfrac32$ projector on the vector index |
| $T_{\mu\nu\rho}$, $h_{\mu\nu}$ | The source's antisymmetrized triple and pair, matrices of one display; kinetic and mass structures |
| $E_\mu$ | The source's generator with index $\mu$; a matrix of the display, not an element of $\mathbb{B}$ |
| $\varpi$ | Angular frequency of a plane wave; not the pseudoscalar $\omega$ |
| $\tilde Q$, $\tilde P$ | Coordinate and momentum elements of a plane wave, $\tilde Q=x_0e_t+\sum_kx_k\vec e_k$ |
| $2\times\tfrac32\oplus4\times\tfrac12$ | $SU(2)$ content of the vector-spinor |

## Further Reading

- William Rarita and Julian Schwinger, "On a theory of particles with half-integral spin", *Physical Review* 60 (1941) 61, for the original field equation for spin three-halves.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. III: Supersymmetry* (Cambridge, 2000), for the Rarita–Schwinger field, its gauge structure, and its role in supergravity.
- Daniel Z. Freedman and Antoine Van Proeyen, *Supergravity* (Cambridge, 2012), for the spin-$\tfrac32$ field, its constraints, and the counting of its physical states.
- Giorgio Velo and Daniel Zwanziger, "Noncausality and other defects of interaction Lagrangians for particles with spin one and higher", *Physical Review* 188 (1969) 2218, for the acausality of minimally coupled higher-spin fields.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the free higher-spin equations and the constraint analysis of the vector-spinor.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the Dirac equation, the trace constraints, and the reduction of vector-spinors in the rest frame.
