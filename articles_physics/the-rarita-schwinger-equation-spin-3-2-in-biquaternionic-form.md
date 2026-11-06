# __The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form__

## Introduction

The Proca equation carries spin one, and the Dirac equation carries spin one-half, and both describe a single field. Spin three-halves is the first case that requires a field with two indices: the **Rarita–Schwinger field** $\tilde{Ξ}^{\mathrm{sp}}_\mu$ is a four-vector whose four components are each a Dirac field, sixteen complex components in all, and its equation removes twelve of them, leaving the four states of a spin-$\tfrac32$ particle. The equation was written down by Rarita and Schwinger in 1941, and it is the field equation of the gravitino in supergravity; it is also the place where the standard field theory of higher spin first becomes delicate, since under minimal coupling to electromagnetism the field propagates superluminally.

**The article writes the system in biquaternionic form and reduces it in the rest frame**, where the spin-$\tfrac32$ content is visible. The carrier is a family of four elements of the algebra, $\tilde{Ξ}^{\mathrm{sp}}_\mu\in\mathbb{B}$ with $\mu=0,1,2,3$, and the equation is three statements. The first is the **chiral pair** of the companion Dirac article, written once for each component,
$$
\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_{\mu,R}=m\tilde{Ξ}^{\mathrm{sp}}_{\mu,L},
\qquad
\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_{\mu,L}=m\tilde{Ξ}^{\mathrm{sp}}_{\mu,R},
\qquad \mu=0,1,2,3 .
$$
The two subscripts take the two values $L$ and $R$ of *Special Element Conventions*, §*The Chirality Convention*, and the derivative is the gradient of *Operator and Calculus Conventions*, §*The Gradient*. Neither value closes on its own: each equation carries one value into the other, so the mass is the pairing of the two. Read from either side, every component of the field is a Dirac field.

**The calculus is the corpus's and is cited, not restated.** The first-order operator is the biquaternionic gradient $\tilde\nabla$, its quaternion conjugate is $\tilde\nabla^{\natural}$, and the d'Alembertian $\Box$ is the quaternionic norm of the gradient, all three as fixed in *Operator and Calculus Conventions*, §*The Gradient* and §*The Quaternionic Bilinear Product, Its Form and Its Norm*. The pair operator $\mathbb{D}$ and its square are those of §*The Gradient* of the same article, under **The pair operator**. No other letter names a derivative below.

**The gradient does not square to a scalar, and that is why the massive equation is a pair.** With $\tilde K=K_0e_t+K_x\vec e_x+K_y\vec e_y+K_z\vec e_z$ the symbol of the gradient, the time unit commutes with the three spatial units and the mixed derivatives are symmetric, so the square keeps a vector part,
$$
\tilde K^2=\bigl(K_0^2-K_x^2-K_y^2-K_z^2\bigr)e_t+2K_0\bigl(K_x\vec e_x+K_y\vec e_y+K_z\vec e_z\bigr).
$$
The computation is a derived form of this article. It says that $\tilde\nabla^2$ is neither a scalar nor the d'Alembertian, so no first-order operator with scalar square exists in this algebra, and a single field carries no mass. The massless equation is one equation on one element, $\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}=0$, and the massive equation is the pair above, whose scalar square is $\Box$.

**The second and third statements are the two constraints.** The first is the **trace constraint**, one element equation in which the three spatial directions multiply their component on the left and the axis $\vec e_z$ on the right; the second is the **divergence constraint**,
$$
\begin{aligned}
\tilde{Ξ}^{\mathrm{sp}}_0+\sum_k\vec e_k\tilde{Ξ}^{\mathrm{sp}}_k\,\vec e_z&=0,\\
\sum_\mu\varepsilon_\mu\,\partial/\partial x_\mu\,\tilde{Ξ}^{\mathrm{sp}}_\mu&=0,
\end{aligned}
$$
with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the frame, as fixed in *Unit, Index and Notation Conventions*, §*The Subscripts*. The source states the three statements as one antisymmetrized equation; the algebra states them as the pair and the two constraints, and the translation between the two writings is made once, in §*The Field in the Biquaternion Framework*.

**In the rest frame the pair leaves four complex parameters, and they are the quartet.** The pair forces the time component of the family to vanish, the three spatial components satisfy one vector condition, $\sum_k\vec e_k\tilde{Ξ}^{\mathrm{sp}}_k=0$, and the surviving space is exactly four-dimensional. It carries the spin-$\tfrac32$ quartet, and the condition on the vector index acts on the three directions as the transverse map of §*The Transverse Condition on the Vector Index*.

**Two features of the standard theory are recorded and read in the algebra.** First, in the massless case the system has a gauge freedom $\tilde{Ξ}^{\mathrm{sp}}_\mu\to\tilde{Ξ}^{\mathrm{sp}}_\mu+\partial/\partial x_\mu\,\epsilon$, with $\epsilon$ an arbitrary Dirac field; the freedom removes the spin-$\tfrac12$ branches that the representation theory places in the field, leaving the two helicities $\pm\tfrac32$. Second, in the massive case the constraint structure is more rigid and the minimal coupling is known to be inconsistent: the field propagates acausally in an external electromagnetic background, the Velo–Zwanziger obstruction, and a consistent interacting theory requires either a gravitational background or a gauge principle. The framework represents these facts; it does not remove them.

**The conventions are those of the companion articles.** The algebra and its units are those of *Algebra and Element Conventions*, the gradient and the d'Alembertian those of *Operator and Calculus Conventions*, and the frame, its coordinate and its metric those of *Frame and Metric Conventions*. None is restated here.

**The source's letters, fixed once.** Where a letter of the source is kept, it is read in $\mathbb{B}$. The source's $i$, wherever it acts on the field, is the right multiplier
$$
\omega=-\vec e_z,\qquad \omega^2=-e_t,
$$
and it acts on the right, $\tilde{Ξ}^{\mathrm{sp}}\mapsto\tilde{Ξ}^{\mathrm{sp}}\omega=-\tilde{Ξ}^{\mathrm{sp}}\vec e_z$. It is, up to the factor $i$, the multiplier of the chirality operator of *Special Element Conventions*, §*The Chirality Convention*: it has eigenvalue $+i$ on the $L$ value and $-i$ on the $R$ value. It is not the central imaginary $i$ of $\mathbb{B}$, which stays free and keeps its name. The side is part of the definition: the left action $\omega\tilde{Ξ}^{\mathrm{sp}}=-\vec e_z\tilde{Ξ}^{\mathrm{sp}}$ is a different element of $\mathbb{B}$ and is not the source's $i$. The label $\mu$ of a component is the coordinate index of its spacetime direction, and the index is always written low.

**Coordinates and frames.** The displays are written in the $\mathbb{M}_-$ frame, with $\partial/\partial x_\mu$ the derivative in the physical coordinates $x_\mu=(r'_t,r_x,r_y,r_z)$. The algebra's own coordinate is $Q_t=i c r'_t$, and $\partial/\partial r'_t=i\partial/\partial R_t$; the reading of the gradient on that sector is the one of *Operator and Calculus Conventions*, §*The Gradient*, and $c=1$ in what follows until the dispersion relation restores it. A display that mixes the algebra's time derivative with the frame's spatial derivatives is not a frame, and none is used. The covariant divergence of the family is $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\tilde{Ξ}^{\mathrm{sp}}_\mu$, written $\operatorname{div}\tilde{Ξ}^{\mathrm{sp}}$ below: four coordinate derivatives with the metric weights $\varepsilon_\mu$ and no unit attached, because the four components carry the four directions as an index and not as an algebra unit. It is a contraction of the family, not a further operator, and it is not the gradient: the gradient carries a unit on each term and an $i$ on the time one.

## The Standard Rarita–Schwinger Field

### The field and its equation

The Rarita–Schwinger field is a four-vector whose components are Dirac fields: a vector index $\mu=0,1,2,3$ and the four-component index of the Dirac field, written $\tilde{Ξ}^{\mathrm{sp}}_{\mu\alpha}$ with $\alpha=1,\dots,4$. The source writes its equation through two objects: a totally antisymmetrized triple $T_{\mu\nu\rho}$, antisymmetric in all three indices and vanishing when two of them coincide, and an antisymmetrized pair $h_{\mu\nu}$, antisymmetric in its two. Both are objects of one chosen display of the source, representatives and not elements of $\mathbb{B}$, and the two carry the two roles: the triple the kinetic structure and the pair the mass structure.

**The source's own equation** is one antisymmetrized equation: the triple contracted with the derivative and with the field, plus $i\,m$ times the pair contracted with the field. In the algebra it is the three statements of the introduction, and the translation is made once here. The kinetic structure is the **gradient pair**: the antisymmetrized triple contracts the derivative index with the three spatial directions, and the contraction on a component is $\tilde\nabla$ on the $R$ value and $\tilde\nabla^{\natural}$ on the $L$ value. The mass structure is **left multiplication by an element** $\Gamma_{\mu\nu}\in\mathbb{B}$, the table of which is given in §*The Field in the Biquaternion Framework*. Nothing else of the source's composites survives the translation, because nothing else of them is an operator on $\mathbb{B}$.

**The factor $i$ is not a convention.** The source has two writings of the same equation, one with the triple and a real mass term and one with the epsilon combination and an imaginary one. The epsilon combination is $\pm i$ times the triple, the sign being the metric weight of the raised index, so the two writings differ by the right multiplier $\omega$ and an overall sign. Written with a real mass term in place of $i\,m$ the equation has no solutions at all: the sixteen-component momentum-space operator of that display is then invertible on the mass shell, its determinant not vanishing at $k^2=m^2$, while with $\pm i\,m$ it has the four-dimensional kernel of the quartet. The check was run at three masses: the nullity is $4$ with the imaginary mass and $0$ with the real one. The overall sign is then a free convention of the source's writing, and this article keeps the one whose positive-frequency solutions have the rest-frame frequency $\varpi=m$.

The equation is the Euler–Lagrange equation of the Rarita–Schwinger Lagrangian, whose kinetic term is the same antisymmetrized combination and whose mass term is the antisymmetrized pair, up to an overall normalisation that is a convention. The index structure is fixed by the requirement that the equation be first order and that its free solutions carry spin $\tfrac32$. No first-order equation for a single lower-spin field can do that: the two-index structure is necessary, and the antisymmetrizations are what make the equation carry an irreducible spin-$\tfrac32$ rather than a reducible sum. The Lagrangian also shows where the mass term sits: it is the antisymmetrized pair, not the metric term $\varepsilon_\mu\delta_{\mu\nu}$, and this is what distinguishes the spin-$\tfrac32$ mass term from the Proca mass term $\tfrac12m^2\sum_\mu A_\mu A_\mu$.

### The constraint and the reduction

**The massive equation implies the trace in two contractions**, and the same two contractions deliver the reduced dynamics. Write $\tilde S:=\tilde{Ξ}^{\mathrm{sp}}_0+\sum_k\vec e_k\tilde{Ξ}^{\mathrm{sp}}_k\vec e_z$ for the trace element of the family. The first contraction is the divergence of the equation: the kinetic structure is antisymmetric in its first and third indices, so the divergence kills it, and what survives is the divergence of the trace. The second is the contraction with the raised direction, which turns the equation into the trace element itself. In the algebra the two results are the two constraints of the framework, and for $m\neq0$ both hold as consequences and not as conditions:
$$
\tilde S=0,\qquad \sum_\mu\varepsilon_\mu\,\partial/\partial x_\mu\,\tilde{Ξ}^{\mathrm{sp}}_\mu=0 ,
$$
the second following from the divergence of the equation once the first holds. The trace is therefore a consequence of the massive equation, and so is the divergence. Both were checked at generic on-shell momenta: the solution space of the equation is four-dimensional, the trace element and the divergence vanish on it to machine precision, and adjoining either condition does not lower the dimension.

**The trace in turn linearises the equation.** With the trace in force, the mass structure reduces to left multiplication by $\Gamma_{\mu\nu}$ on the component, contracted with the corresponding component of the field, and the kinetic structure reduces to the gradient pair, so the equation of the $\mu$-th component is the pair on that component alone. That pair is the pair operator of *Operator and Calculus Conventions*, §*The Pair Operator and Its Symbol*, applied to one component, so the massive component equation is the massive equation of that section, and no object of a display enters it.

**The antisymmetrized equation is thus equivalent to the pair on each component together with the trace**, and, through them, the covariant divergence. The mass term regenerates the pair on each component, so that the reduced dynamics is the one the companion Dirac article supplies. The trace constraint removes one Dirac field's worth of components from the sixteen, and it is the part of the reduction that the algebra can state as a single element.

**The massless case separates the constraints**, and the separation is what the gauge freedom is for. For $m=0$ the same two contractions no longer force the trace: $\tilde S=0$ is not contained in the equation, and adjoining it lowers the solution space from six dimensions to four. Both numbers were checked at generic lightlike momenta. The covariant divergence is a different matter, because its four components are linear combinations of the components of the equation: $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\tilde{Ξ}^{\mathrm{sp}}_\mu=0$ remains a consequence of the equation even when the mass vanishes, and adjoining it lowers nothing. It is in the massless case that the **gauge freedom**
$$
\tilde{Ξ}^{\mathrm{sp}}_\mu \longrightarrow \tilde{Ξ}^{\mathrm{sp}}_\mu + \partial/\partial x_\mu\,\epsilon,
$$
appears, with $\epsilon$ an arbitrary Dirac field: the antisymmetrized kinetic structure is built from the field strength $\partial/\partial x_\rho\,\tilde{Ξ}^{\mathrm{sp}}_\sigma$, which changes by a symmetric derivative that the antisymmetrization discards. The gauge freedom is the spin-$\tfrac32$ analogue of the electromagnetic gauge freedom, it is what removes the spin-$\tfrac12$ branch that the vector index introduces, and it is also what makes the trace usable: the trace values that occur on the massless solution space span a space of dimension two, exactly the space of trace shifts a gauge transformation can produce, so the gauge $\tilde S=0$ is attainable and the trace is a complete gauge choice rather than a derived constraint.

### Representation content

**The Lorentz transformation character of the field is read off from the two indices.** The vector index carries $(\tfrac12,\tfrac12)$ and the four-component index carries $(\tfrac12,0)\oplus(0,\tfrac12)$, so the field transforms in the tensor product
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
under $SU(2)$, of dimensions $2\cdot4 + 4\cdot2 = 16$. Two spin-$\tfrac32$ multiplets, one for the particle and one for the antiparticle, and four spin-$\tfrac12$ multiplets. The whole content of the Rarita–Schwinger equation and of its gauge structure is the removal of those four spin-$\tfrac12$ multiplets, and the rest-frame computation below exhibits the removal explicitly.

### Counting the physical states

**Two independent conditions remove the spin-$\tfrac12$ content**, and because they act on different structures their effects add on the component count. The **algebraic trace** $\tilde S=0$ removes one Dirac field's worth of components, which is two spin-$\tfrac12$ multiplets. The **gauge freedom** in the massless case removes another Dirac field's worth, another two spin-$\tfrac12$ multiplets. What is left is the two spin-$\tfrac32$ multiplets, of total dimension eight, and for each frequency sign that is the four-dimensional quartet of a spin-$\tfrac32$ particle. In the massive case the gauge freedom is absent, and the second pair of spin-$\tfrac12$ multiplets is removed instead by the subsidiary conditions that follow from the equation; the physical count is the same four states per charge.

The counting is therefore representation-theoretic and does not depend on the detailed form of the antisymmetrizations: any first-order equation whose solutions are pure spin-$\tfrac32$ must remove exactly the four spin-$\tfrac12$ multiplets from the tensor product, and the trace constraint and the gauge freedom are the two mechanisms that do it. This is the reason the field is the minimal carrier of spin $\tfrac32$: the next tensor product that could carry it, the three-index object, would carry still more lower-spin admixture, and the two-index object is the smallest that contains $\tfrac32$ at all.

### The known difficulties

In the massive case the constraint structure is rigid: the equation implies the trace $\tilde S=0$ and the covariant divergence $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\tilde{Ξ}^{\mathrm{sp}}_\mu=0$, there is no gauge freedom to remove the remaining components, and the resulting theory has the right free-field content but is known to be inconsistent upon minimal coupling to an external electromagnetic field. The propagation becomes acausal for sufficiently strong backgrounds, the Velo–Zwanziger obstruction, and a consistent interacting spin-$\tfrac32$ theory requires a gravitational or gauge principle rather than a fixed background. This is the standard status of the field, and it is recorded here because the biquaternion formulation does not alter it: the algebra rewrites the free equation faithfully, and the difficulties belong to the coupling.

## The Field in the Biquaternion Framework

### The carrier

**The carrier of a spin-$\tfrac32$ field is a biquaternion-valued four-vector**,
$$
\tilde{Ξ}^{\mathrm{sp}}_\mu \in \mathbb{B}, \qquad \mu=0,1,2,3,
$$
that is, a family of four elements of the algebra, one for each spacetime index. In components, $\tilde{Ξ}^{\mathrm{sp}}_\mu = \tilde{Ξ}^{\mathrm{sp}}_{\mu,0}e_t + \tilde{Ξ}^{\mathrm{sp}}_{\mu,1}\vec e_x + \tilde{Ξ}^{\mathrm{sp}}_{\mu,2}\vec e_y + \tilde{Ξ}^{\mathrm{sp}}_{\mu,3}\vec e_z$ with complex coefficients, so that the carrier has $4\times4 = 16$ complex components, matching the standard field. The vector index is carried by the algebra's own four-vector structure, as it is for the Proca potential, and the four-component index by the algebra itself, as it is for the Dirac field, whose carrier is $\mathbb{B}$ (*Special Element Conventions*). The gradient acts from the left and carries an element into an element. The Rarita–Schwinger field is therefore a **family of four elements**: not one element read as a four-vector, and not one element read as a Dirac field, but the tensor product of the two structures. This is the structural reason it lies outside the algebra's native spin content, a point the final article of the subcategory develops.

### The correspondence with the source's frame

**The source's equation is transcribed component by component**, and the transcription is one linear map. The source contracts its four-vector index with four generators; the algebra's four units that square to $+e_t$ carry the same index, as fixed in *Algebra and Element Conventions*, §*The Algebra and Its Basis*. Write $E_\mu$ for the source's generator with index $\mu$, an object of the display and not an element of $\mathbb{B}$, and assign
$$
E_\mu \;\longmapsto\; e_t \ (\mu=0), \qquad E_\mu \;\longmapsto\; i\vec e_k \ (\mu=k).
$$
From the span of the four generators onto $\mathbb{B}$ this is a complex-linear isomorphism, and the two sides are different kinds of object throughout: an object of the display on the left, an element on the right. It carries the index and nothing else. It is not multiplicative, and no product of images is used below: the equation needs two structures only, the gradient for the kinetic term and one element of $\mathbb{B}$ for each index pair of the mass term.

**The kinetic structure is the gradient.** The antisymmetrized triple of the source contracts the derivative index with the three spatial directions and antisymmetrizes over all three. In the algebra that contraction is the gradient: $\tilde\nabla$ on the $R$ value of each component, $\tilde\nabla^{\natural}$ on the $L$ value, with the material time derivative carried by the $e_t$ term alone. No other first-order structure enters, and the triple itself is not needed once the contraction is made.

**The mass structure is an element.** The antisymmetrized pair of the source is, in the algebra, left multiplication by an element of $\mathbb{B}$,
$$
\Gamma_{\mu\nu}\longmapsto \Gamma_{0k}=i\vec e_k,\quad \Gamma_{k0}=-i\vec e_k,\quad \Gamma_{jk}=\pm\vec e_l,\quad \Gamma_{00}=0,
$$
with the sign of $\Gamma_{jk}$ fixed by the orientation $\vec e_x\vec e_y=\vec e_z$ and $\vec e_l$ the remaining direction. The six entries with one time index are imaginary multiples of a spatial unit and square to $+e_t$; the six entries with two spatial indices are spatial units and square to $-e_t$. All twelve were checked, and the orientation $\vec e_x\vec e_y=\vec e_z$ gives $\Gamma_{12}=\vec e_z$, $\Gamma_{23}=\vec e_x$ and $\Gamma_{31}=\vec e_y$. The mass term of the $\mu$-th equation is $\sum_\nu\Gamma_{\mu\nu}\tilde{Ξ}^{\mathrm{sp}}_\nu$, left multiplication by an element contracted with the corresponding component of the field. Nothing of the source's pair survives beyond this element, and the element is frame-free: it is written in the units and carries no reference to a frame.

### The equivalent constraint form

**The biquaternion form of the free field is the chiral pair on each component**,
$$
\boxed{\;
\begin{aligned}
\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_{\mu,R}&=m\tilde{Ξ}^{\mathrm{sp}}_{\mu,L},\\
\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_{\mu,L}&=m\tilde{Ξ}^{\mathrm{sp}}_{\mu,R},
\end{aligned}
\qquad\text{for each }\mu\;}
$$
together with the two constraints,
$$
\boxed{\;
\begin{aligned}
\tilde{Ξ}^{\mathrm{sp}}_0+\sum_k\vec e_k\tilde{Ξ}^{\mathrm{sp}}_k\,\vec e_z&=0,\\
\sum_\mu\varepsilon_\mu\,\partial/\partial x_\mu\,\tilde{Ξ}^{\mathrm{sp}}_\mu&=0,
\end{aligned}\;}
$$
where the first line of the second display is the algebra reading of the source's trace, derived in the paragraph **The trace in the algebra** below, $\varepsilon=(1,-1,-1,-1)$ is the sign vector of the frame, and $\tilde{Ξ}^{\mathrm{sp}}_\mu=\tilde{Ξ}^{\mathrm{sp}}_{\mu,L}+\tilde{Ξ}^{\mathrm{sp}}_{\mu,R}$ writes each component in its two values. The first display is two Dirac equations per component, with the mass as the pairing of the two values. Every object in these displays is an element of $\mathbb{B}$ or a derivative of one; no frame appears.

**The equivalence with the antisymmetrized equation is the standard free-field reduction.** If each component satisfies the chiral pair, and if the trace and divergence constraints hold, then the antisymmetrized equation follows; conversely, the antisymmetrized equation implies the pair and the trace, and the divergence. The pair is the component transcription of the antisymmetrized kinetic structure, and the two constraints are the transcription of the two contractions; the biquaternion form is the pair and the constraints.

**The trace in the algebra.** The source's trace contracts the family with the four directions. Each of the three spatial components is multiplied by its direction on the left and by $\vec e_z$ on the right, the time component by neither, and the four results are added into one element of $\mathbb{B}$,
$$
\tilde S=\tilde{Ξ}^{\mathrm{sp}}_0+\sum_k\vec e_k\tilde{Ξ}^{\mathrm{sp}}_k\,\vec e_z ,
$$
so the source's condition is equivalent to $\tilde S=0$. The two forms carry the same four complex conditions, and the map from the sixteen complex components to those four has rank four, checked exactly. The right multiplier $\vec e_z$ is what the three spatial directions leave behind, and it is not decoration: without it the condition is a different map of the same rank, with a different kernel, checked. The condition is frame-free: both sides are elements of $\mathbb{B}$, and no frame enters.

**The mass term is frame-free.** With the entries read as above, the mass term of the $\mu$-th equation is left multiplication by the element $\Gamma_{\mu\nu}$ of $\mathbb{B}$, contracted with the corresponding component. No frame appears in the result, and the mass term is therefore a statement about the algebra and not about a display.

## The Rest-Frame Reduction

### Setting up

**Time convention.** The check is performed in the $\mathbb{M}_-$ frame, with $x_0=r'_t$. The series' algebra coordinate is $Q_t=i c r'_t$; the two are related by $\partial/\partial r'_t=i\partial/\partial R_t$, not by relabelling $Q_t$ as $r'_t$, and the substitution is applied to the whole pair at once.

**At rest the two operators of the pair agree.** The spatial derivatives vanish, and the two operators differ only in the signs of those derivatives, so both take the same value; for the phase $\exp(-imr'_t)$ used here that value is $-me_t$. That coincidence is the content of the rest-frame check: the pair degenerates to one condition per component, and the two members of the pair give the same condition. The condition relates the two values of the component, and one value then fixes the other, so a component carries the two complex parameters of one value and the four components carry eight in all. The trace constraint is four complex conditions on those eight, so the free solution space is four complex dimensional, the count the check below confirms.

### The trace constraint at rest

**The trace constraint is one element equation, and at rest it reads on the components.** With the components of the form above,
$$
\tilde{Ξ}^{\mathrm{sp}}_0+\sum_k\vec e_k\tilde{Ξ}^{\mathrm{sp}}_k\vec e_z=0 .
$$
Read on the family it says two things. The time component vanishes, $\tilde{Ξ}^{\mathrm{sp}}_0=0$. The three spatial components satisfy the single vector condition
$$
\sum_k\vec e_k\tilde{Ξ}^{\mathrm{sp}}_k=0,
$$
which is the algebraic form of the transverse condition on the three spatial amplitudes. Both statements were checked on the whole solution space and not on a single wavefunction: the time component vanishes identically, and the vector condition cuts the six complex parameters of the three spatial components to four.

**The constraint is diagonal in the two values.** The multiplier $\omega=-\vec e_z$ commutes with the $\vec e_z$ that closes every spatial term of the trace, so
$$
\tilde S(\tilde{Ξ}^{\mathrm{sp}}\omega)=\tilde S(\tilde{Ξ}^{\mathrm{sp}})\,\omega ,
$$
and the constraint therefore constrains each value on its own.

**The combined system of the pair on all four components and the trace constraint has nullity four.** The constraint alone has nullity four, and the two solution spaces coincide.

### The spin-one-half content and its removal

**The three spatial components carry $3\times2 = 6$ complex parameters before the condition.** Under the rotation group the three directions carry spin one and the two complex parameters of one value carry spin-$\tfrac12$, so
$$
1\otimes\tfrac12 = \tfrac32 \oplus \tfrac12, \qquad 3\times2 = 4 + 2 ,
$$
and the vector condition removes exactly the spin-$\tfrac12$ piece of dimension two. What remains is a four-dimensional space, the spin-$\tfrac32$ quartet, with states of spin projection $\pm\tfrac32$ and $\pm\tfrac12$ along any axis. The representation-theory count of the field had two spin-$\tfrac32$ multiplets; the one found here is the positive-frequency or particle multiplet, and the negative-frequency or antiparticle multiplet is obtained by the conjugate choice of frequency and has the same four states. The four spin-$\tfrac12$ multiplets of the field are removed, two by the trace constraint and two by the equation, exactly as the general consistency analysis requires.

### Verification

**Every number below is recorded in both languages, the algebra and a display of the source, and the two agree; no check uses more than one hundred cases.**

*At rest.* The pair and the trace leave a four-dimensional solution space. In the display of the source the sixteen-component operator couples the time component to the spatial ones and the spatial components among themselves, and the four-dimensional null space is reached through that coupling and not component by component. On that null space the time component vanishes identically. The trace map has rank four on the sixteen components and annihilates the whole four-dimensional null space, so in the massive case the trace is implied and not imposed.

*At generic on-shell momenta*, with three distinct nonzero spatial components so that no rest-frame degeneracy can hide a mismatch: the nullity is four; the trace and the divergence both vanish on the solution space to $10^{-15}$; and adjoining either condition leaves the nullity at four. With a real coefficient in place of $i\,m$ the momentum-space operator has nullity zero, which is the statement that the mass term must be imaginary.

*At generic lightlike momenta*: the nullity is six, the four-dimensional space of pure-gauge modes $\tilde{Ξ}^{\mathrm{sp}}_\mu\propto\partial/\partial x_\mu\epsilon$ is a subspace, the divergence vanishes on the whole solution space, the trace does not, and adjoining the trace leaves four. The trace values of the solutions span a space of dimension two, which is the space of trace shifts the gauge transformation produces.

*In the algebra*: the trace map has rank four on the sixteen complex components. On a null momentum the symbol of the gradient, $\tilde K=K_0e_t+K_x\vec e_x+K_y\vec e_y+K_z\vec e_z$, is a zero divisor. The null condition is its quaternion norm, $\tilde K\tilde K^{\natural}=K_0^2+K_x^2+K_y^2+K_z^2=0$, which for $K_0=i\varpi$ and real $\vec k$ is $\varpi^2=\vec k^2$ and not $\varpi^2=-\vec k^2$. Then left multiplication by $\tilde K$ has rank two and a two-dimensional kernel, checked on four independent null momenta. On a non-null momentum the same left multiplication has rank four and no kernel. That kernel is where the two helicities live, and it is the algebraic reason the massless count is the count it is.

*The transverse map.* The map $T$ of §*The Transverse Condition on the Vector Index* was checked on fifty generic families of three components: it is unchanged by a second application to $3\times10^{-16}$, it annihilates every longitudinal family $\tilde\xi_k=\vec e_k\tilde\zeta$, it fixes every family with $\sum_k\vec e_k\tilde\xi_k=0$, and its rank over the vector index is two.

## The Transverse Condition on the Vector Index

**The vector condition acts on the three directions through one map.** The spatial components are an element each and a direction each, so the condition $\sum_k\vec e_k\tilde\xi_k=0$ singles out a subspace of the six complex parameters they carry. The map that produces it is written with the units alone,
$$
T(\tilde\xi)_k=\tilde\xi_k+\tfrac13\vec e_k\sum_j\vec e_j\tilde\xi_j .
$$

**The map is unchanged by a second application.** The contraction of its output vanishes, because $\sum_k\vec e_k\vec e_k=-3e_t$:
$$
\sum_k\vec e_k\,T(\tilde\xi)_k=\sum_k\vec e_k\tilde\xi_k+\tfrac13\Bigl(\sum_k\vec e_k\vec e_k\Bigr)\sum_j\vec e_j\tilde\xi_j=\sum_k\vec e_k\tilde\xi_k-\sum_j\vec e_j\tilde\xi_j=0 .
$$

**Its kernel is the longitudinal family, and its fixed families are the constrained ones.** The equation $T(\tilde\xi)=0$ reads $\tilde\xi_k=-\tfrac13\vec e_k\sum_j\vec e_j\tilde\xi_j$, which is the longitudinal family $\tilde\xi_k=\vec e_k\tilde\zeta$ with one element $\tilde\zeta$ for the three directions, the spin-$\tfrac12$ admixture; and every family that satisfies the condition is carried into itself. Its rank over the vector index is $3-1=2$, so it keeps two of the three directions, and with the two complex parameters of each it leaves the four states of spin $\tfrac32$.

**The covariant form refers the same map to the four-momentum.** The standard transverse condition of the theory is the condition above with the fixed direction replaced by the four-momentum $p_\mu$; at $p_\mu=(m,0,0,0)$ the two agree. In the biquaternion framework a boost is a rotor conjugation, so the covariant form is the rotor conjugate of the rest-frame map, and the algebra supplies the boost without a separate construction.

## The Massless Case and the Gauge Freedom

### The gauge transformation in the algebra

**In the massless case the antisymmetrized equation and the trace constraint leave a gauge freedom**, and in the biquaternion form the transformation is
$$
\tilde{Ξ}^{\mathrm{sp}}_\mu \;\longrightarrow\; \tilde{Ξ}^{\mathrm{sp}}_\mu + \partial/\partial x_\mu\,\epsilon,
$$
where $\epsilon$ is a Dirac field and $\partial/\partial x_\mu$ is the coordinate derivative of the $\mathbb{M}_-$ frame. The shift carries no direction unit. $\tilde\nabla$ is the sum of its four terms with a unit attached to each, and it maps one element of $\mathbb{B}$ to one element; the shift adds to each of the four components its own coordinate derivative and no unit, which is what makes it a shift of a family of four components rather than the action of the gradient on one. The antisymmetrized kinetic structure of the equation is insensitive to the shift, just as the electromagnetic field strength is insensitive to the coordinate gradient of the potential. The number of gauge parameters is the number of components of $\epsilon$, namely four, which is one Dirac field; and the gauge freedom removes two of the four spin-$\tfrac12$ multiplets of the representation content. The remaining two are removed by the trace condition and the equations of motion, with the difference, recorded above, that in the massless case the trace is a gauge choice and the divergence condition is the consequence of the equation, so that the two mechanisms do not simply add but interlock. What is left is a single spin-$\tfrac32$ multiplet per frequency sign, that is, the two helicities $\pm\tfrac32$.

### Helicities and the two physical states

**The physical content of the massless field is two states per wavevector**, the helicities $\pm\tfrac32$. There is no longitudinal or scalar helicity, and the count is the spin-$\tfrac32$ analogue of the two transverse helicities of the photon: in both cases the gauge freedom and the constraint together halve-and-halve the naive index content. The parallel is exact at the level of the representation theory. The photon's two-form is the antisymmetric square of the four-vector, $(1,0)\oplus(0,1)$; the massless Rarita–Schwinger field's two physical states are the two helicities of the $(1,\tfrac12)$ and $(\tfrac12,1)$ summands after the spin-$\tfrac12$ pieces are gauged away. In both cases the two physical states are the two conjugate summands of the representation content, which is why the self-dual split of the spin-one article has a counterpart here, and in both cases the massless limit is the case in which the lower states are removed by gauge rather than retained by a mass.

## The Massive Case

**For $m\neq0$ the mass term of the $\mu$-th equation is**
$$
m\sum_\nu \Gamma_{\mu\nu}\,\tilde{Ξ}^{\mathrm{sp}}_\nu ,
$$
left multiplication by the element of $\mathbb{B}$ tabulated in §*The Field in the Biquaternion Framework*, contracted with the corresponding component of the field. In the trace form of the equation it is simply the mass on each component, and the mass plays the same structural role as in the Proca and Dirac cases: it is linear in the field, it is what remains when the gauge freedom is absent, and it fixes the dispersion relation on the physical shell through the pair. In the rest frame the massive reduction above is the whole story: time component zero, the three spatial components transverse, four states.

**The massive case is also where the known difficulty lives.** The constraint analysis that produces $\tilde S=0$ and $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\tilde{Ξ}^{\mathrm{sp}}_\mu=0$ is rigid when $m\neq0$, and its consequences for the interacting theory are the Velo–Zwanziger obstruction: minimal coupling to a background electromagnetic field makes some modes propagate faster than light, and the theory is not causal as a fixed-background field theory. The biquaternion formulation reproduces the free constraint structure exactly and says nothing different about the coupling, because the coupling is an additional structure that no rewriting of the free equation can supply. This is the analogue, for spin $\tfrac32$, of the statement recorded for the Proca field: the algebra represents the free field faithfully, and what the free algebra cannot decide is the interaction.

### The dispersion relation

**Because each component satisfies the Dirac equation, each component satisfies the Klein–Gordon equation on squaring**, exactly as in the spin-$\tfrac12$ case. For a biquaternion plane wave of the component,
$$
\tilde{Ξ}^{\mathrm{sp}}_\mu = \tilde{Ξ}^{\mathrm{sp}}_{\mu,0}\,\exp(\,i\,\mathrm{Sc}(\tilde P\tilde Q^{\natural})/\hbar),
$$
with $\tilde Q=x_0e_t+\sum_k x_k\vec e_k$ the coordinate element and $\tilde P=p_0e_t+\sum_k p_k\vec e_k$ its conjugate momentum, the Dirac equation on the component requires $\tilde P\tilde P^{\natural}=-m^2c^2$ in the normalization of the companion Dirac article, that is,
$$
\frac{\varpi^2}{c^2} - \vec k^2 = \frac{m^2c^2}{\hbar^2},
\qquad\text{i.e.}\qquad
\varpi^2 = c^2\vec k^2 + \frac{m^2c^4}{\hbar^2},
$$
the same physical massive shell as the Proca field. The trace constraint and the subsidiary conditions then reduce the sixteen components to the four states of the quartet, with the three-momentum on the shell. The dispersion relation is therefore common to the massive spin-one and spin-$\tfrac32$ fields, as it must be: the mass shell is a property of the representation's Casimir and not of the index structure.

## Comparison with Spin One and Spin One-Half

**The three field equations of this subcategory and its lower-spin neighbours form a sequence**, and the sequence is the clearest statement of what the biquaternion framework does and does not carry natively.

| Field | Standard carrier | Components | Constraints | Physical components |
|---|---|---|---|---|
| Dirac, spin $\tfrac12$ | a Dirac field | $4$ | the equation alone, removing $2$ | $2$ |
| Proca, spin $1$ | four-vector | $4$ | Lorenz, removing $1$ | $3$ |
| Rarita–Schwinger, spin $\tfrac32$ | four-vector of Dirac fields | $16$ | trace and subsidiary, removing $12$ | $4$ |

In each row the physical component count is $2s+1$ for the particle, and the equation together with its constraints removes the remainder. The role that the field's index structure plays is to supply a carrier large enough to contain the spin: the Dirac field is an element of the algebra and needs no index; the Proca field adds a four-vector index, which the algebra carries by conjugation on $\mathbb{M}_-$; the Rarita–Schwinger field adds a vector index to the Dirac field, which the algebra carries only as a tensor product of the two structures. Each step multiplies the carrier by the four-vector and each step therefore adds lower-spin admixture that a constraint has to remove.

**The biquaternion description follows the same sequence.** The Dirac field is an element of the algebra; the Proca field is an element of the material sector $\mathbb{M}_-$ with the field strength in the vector part; the Rarita–Schwinger field is a family of elements of $\mathbb{B}$ indexed by the spacetime direction. The pattern is that the algebra carries the four-vector index by conjugation and the four-component index by left multiplication, and that no carrier beyond these two is available. This is the structural observation that the final article of the subcategory turns into a statement about the algebra's own elements: the spin content accessible to them is bounded, and it is $\{0,\tfrac12\}$.

## What Is Standard and What the Algebra Adds

**The standard part.** The vector-valued field, the antisymmetrized equation, the trace constraint, the gauge freedom, the reduction to the Dirac equation, the spin-$\tfrac32$ content, and the Velo–Zwanziger difficulty are all standard and are transcribed here. The representation-theory count $2\times\tfrac32\oplus4\times\tfrac12$ and the reduction $1\otimes\tfrac12=\tfrac32\oplus\tfrac12$ are standard.

**The algebra's part.** Three statements are the framework's. First, the natural carrier of the field is the family of biquaternion-valued components $\tilde{Ξ}^{\mathrm{sp}}_\mu$, and the two structural conditions of the free theory, the chiral pair on each component and the trace constraint $\tilde S=0$, are each single algebraic statements in $\mathbb{B}$ rather than lists of component equations. The antisymmetrized equation is a transcription of the pair, not a third condition. Second, the source's $i$ is the right multiplier $\omega=-\vec e_z$, whose square is $-e_t$; it commutes with the trace map and with the pair, so the structure of the field's two values needs no operator beyond the units the algebra already has. Third, the condition $\sum_k\vec e_k\tilde\xi_k=0$ gives the transverse map $T$ by elementary algebra, and its boosted form is the rotor conjugate of the rest-frame map, so the covariant condition is available without a separate construction.

**What is imported.** The identification of the field with a spin-$\tfrac32$ particle, the value of the mass, the existence of a consistent interaction, and the resolution of the Velo–Zwanziger problem are inputs beyond the free algebra. The canonical quantisation of the field and its propagator belong to the field-theoretic companion subcategory.

**The display the literature uses is a choice of generators, not the algebra.** The reasons the biquaternion writing replaces it are the subject of the article *Why AXF Matrices instead of Pauli and Gamma Matrices*, and they are not restated here.

**The structural point that this article makes for the subcategory** is that the field is a tensor product of the algebra's four-vector structure with its Dirac-field structure, so its spin-$\tfrac32$ content is not native to the algebra but arises from the product. The final article of the subcategory states this in general and proves that the algebra's own elements carry only spin one-half, the scalar living in the centre and the vector in the adjoint.

**The conventions are those of two companion articles:**

- Companion article *The Dirac Equation in Biquaternionic Form*, for the biquaternion chiral pair and its equivalence with the component Dirac equation.
- Companion article *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector*, for the vector part of the algebra and the four-vector representation from which the family of components is built.

## Summary

The Rarita–Schwinger field is a four-vector whose components are Dirac fields, of sixteen complex components. Its equation, in the source's writing, is one antisymmetrized equation; in the algebra it is the chiral pair on each component together with the two constraints

$$
\tilde{Ξ}^{\mathrm{sp}}_0+\sum_k\vec e_k\tilde{Ξ}^{\mathrm{sp}}_k\,\vec e_z=0,
\qquad
\sum_\mu\varepsilon_\mu\,\partial/\partial x_\mu\,\tilde{Ξ}^{\mathrm{sp}}_\mu=0,
$$

with the mass as the pairing of the two values and the mass term of each component a left multiplication by the element $\Gamma_{\mu\nu}$. In the massive case both constraints are consequences of the equation: the solution space is four-dimensional and the trace and the divergence vanish on it. In the massless case the divergence is still a consequence and the trace is not; the gauge freedom $\tilde{Ξ}^{\mathrm{sp}}_\mu\to\tilde{Ξ}^{\mathrm{sp}}_\mu+\partial/\partial x_\mu\,\epsilon$ shifts the trace by exactly the two-dimensional space the trace values occupy, so the trace is a complete gauge choice.

In the rest frame the system forces the time component to vanish and the three spatial components to satisfy $\sum_k\vec e_k\tilde{Ξ}^{\mathrm{sp}}_k=0$. The surviving space is four-dimensional and carries the spin-$\tfrac32$ quartet; the map onto it is $T(\tilde\xi)_k=\tilde\xi_k+\tfrac13\vec e_k\sum_j\vec e_j\tilde\xi_j$, unchanged by a second application and of vector-index rank two. The representation content $2\times\tfrac32\oplus4\times\tfrac12$ loses its four spin-$\tfrac12$ multiplets to the constraint and the gauge freedom, and the massless field retains the two helicities $\pm\tfrac32$.

The field is a tensor product of the algebra's four-vector structure and its Dirac-field structure, so spin $\tfrac32$ is not native to the algebra. The free equation is represented faithfully; the known difficulty of the interacting theory, the Velo–Zwanziger acausal propagation under minimal coupling, is a property of the coupling and is not removed by the rewriting.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Central scalar imaginary of $\mathbb{B}$, $i^2=-1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$ | The gradient and its quaternion conjugate; the only first-order operators of the article |
| $\Box$ | The d'Alembertian, the quaternionic norm of the gradient |
| $\mathbb{D}$ | The pair operator of *Operator and Calculus Conventions*, §*The Pair Operator and Its Symbol* |
| $\tilde K$ | Symbol of the gradient, $K_0e_t+K_x\vec e_x+K_y\vec e_y+K_z\vec e_z$ |
| $\omega=-\vec e_z$, $\omega^2=-e_t$ | The right multiplier that carries the source's $i$; eigenvalue $+i$ on the $L$ value and $-i$ on the $R$ value |
| $e_t$, $i\vec e_k$ | The four units that square to $+e_t$; the images of the source's four generators |
| $\tilde{Ξ}^{\mathrm{sp}}_\mu\in\mathbb{B}$ | Biquaternion-valued components of the field, $\mu=0,1,2,3$ |
| $\tilde{Ξ}^{\mathrm{sp}}_{\mu,L}$, $\tilde{Ξ}^{\mathrm{sp}}_{\mu,R}$ | The two values of a component |
| $\epsilon$ | Dirac-field parameter of the massless shift symmetry |
| $\Gamma_{0k}=i\vec e_k$, $\Gamma_{k0}=-i\vec e_k$, $\Gamma_{jk}=\pm\vec e_l$ | Mass-term coefficients in $\mathbb{B}$; the mass term is left multiplication by $\Gamma_{\mu\nu}$ |
| $\varepsilon_\mu=-g_{\mu\mu}=(1,-1,-1,-1)$ | Sign vector of the frame; the metric weight of a contracted low index |
| $\tilde S=\tilde{Ξ}^{\mathrm{sp}}_0+\sum_k\vec e_k\tilde{Ξ}^{\mathrm{sp}}_k\vec e_z$ | Trace element; the source's trace, four complex conditions of rank four |
| $\operatorname{div}\tilde{Ξ}^{\mathrm{sp}}=\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\tilde{Ξ}^{\mathrm{sp}}_\mu$ | Covariant divergence; a consequence of the equation for every $m$ |
| $\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_{\mu,R}=m\tilde{Ξ}^{\mathrm{sp}}_{\mu,L}$, $\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_{\mu,L}=m\tilde{Ξ}^{\mathrm{sp}}_{\mu,R}$ | Chiral pair on each component; the dynamics |
| $\tilde\xi_k$ | The three spatial components at rest |
| $T(\tilde\xi)_k=\tilde\xi_k+\tfrac13\vec e_k\sum_j\vec e_j\tilde\xi_j$ | The transverse map on the vector index; unchanged by a second application, of rank two |
| $T_{\mu\nu\rho}$, $h_{\mu\nu}$ | The source's antisymmetrized triple and pair, objects of one display; kinetic and mass structures |
| $E_\mu$ | The source's generator with index $\mu$, an object of the display and not an element of $\mathbb{B}$ |
| $\varpi$ | Angular frequency of a plane wave; not $\omega$ |
| $\tilde Q$, $\tilde P$ | Coordinate and momentum elements of a plane wave, $\tilde Q=x_0e_t+\sum_kx_k\vec e_k$ |
| $2\times\tfrac32\oplus4\times\tfrac12$ | $SU(2)$ content of the field |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the biquaternion formulation replaces a display of generators.
- William Rarita and Julian Schwinger, "On a theory of particles with half-integral spin", *Physical Review* 60 (1941) 61, for the original field equation for spin three-halves.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. III: Supersymmetry* (Cambridge, 2000), for the Rarita–Schwinger field, its gauge structure, and its role in supergravity.
- Daniel Z. Freedman and Antoine Van Proeyen, *Supergravity* (Cambridge, 2012), for the spin-$\tfrac32$ field, its constraints, and the counting of its physical states.
- Giorgio Velo and Daniel Zwanziger, "Noncausality and other defects of interaction Lagrangians for particles with spin one and higher", *Physical Review* 188 (1969) 2218, for the acausality of minimally coupled higher-spin fields.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the free higher-spin equations and the constraint analysis.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the Dirac equation, the trace constraints, and the rest-frame reduction.
