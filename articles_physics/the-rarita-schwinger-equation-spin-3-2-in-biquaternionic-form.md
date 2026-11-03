# __The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form__

## Introduction

The Proca equation carries spin one, and the Dirac equation carries spin one-half, and both describe a single field. Spin three-halves is the first case that requires a field with two indices: the **Rarita–Schwinger field** $\psi_\mu$ is a four-vector whose components are Dirac spinors, sixteen complex components in all, and its equation removes twelve of them, leaving the four states of a spin-$\tfrac32$ particle. The equation was written down by Rarita and Schwinger in 1941, and it is the field equation of the gravitino in supergravity; it is also the place where the standard field theory of higher spin first becomes delicate, since under minimal coupling to electromagnetism the field propagates superluminally.

This article writes the Rarita–Schwinger system in biquaternionic form and reduces it in the rest frame, where the spin-$\tfrac32$ content is transparent. The framework treats the field as a **biquaternion-valued four-vector**, a family $\tilde{\Psi}_\mu\in\mathbb{B}$ with $\mu=0,1,2,3$, and the equation as three statements. The first is a **chiral pair** on each component: two Dirac equations, one for each chiral half, and the place where the two-sided operator structure and chirality meet. The right-handed half obeys the equation driven by the gradient acting from the left,
$$
\tilde\nabla\tilde\Psi_{\mu,R}=m\tilde\Psi_{\mu,L},
$$
and the left-handed half obeys the equation driven by the conjugate gradient,
$$
\tilde\nabla^{\natural}\tilde\Psi_{\mu,L}=m\tilde\Psi_{\mu,R},
\qquad \mu=0,1,2,3 .
$$
Neither half closes on its own: each equation maps one half into the other, so the mass is the off-diagonal pairing of the pair. Read from either side, the statement is that every component of the vector-spinor is a Dirac field, and the two readings are the two chiralities.

The second is a **trace constraint**: the four cells contracted with the vector index annihilate the field, and in the algebra that contraction reads as one element, the right multiplier $\vec e_z$ being what the three spatial cells leave behind. The third is its companion **divergence constraint**:

$$
\begin{aligned}
\tilde\Psi_0+\sum_k\vec e_k\tilde\Psi_k\,\vec e_z&=0,\\
\sum_\mu\varepsilon_\mu\,\partial/\partial x_\mu\,\tilde\Psi_\mu&=0,
\end{aligned}
$$

with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the frame. The antisymmetrized cell equation is the compact transcription of this system, not a second dynamics: its kinetic coefficient is a cell of the cell algebra, not an element of $\mathbb{B}$. In the rest frame the system forces the time component to vanish, forces the spatial components to their upper (positive-frequency) parts, and imposes the single vector condition $\boldsymbol{\sigma}\cdot\vec\chi=0$ on the spatial amplitudes. The surviving space is exactly four-dimensional, and it carries the spin-$\tfrac32$ quartet. The construction also exhibits the spin-$\tfrac32$ projector: the transverse projector on the vector index, $P_{ij} = \delta_{ij} - \tfrac13\sigma_i\sigma_j$, which is idempotent and selects precisely the constrained spatial amplitudes.

Two features of the standard theory are recorded and read in the algebra. First, in the massless case the system has a gauge freedom $\psi_\mu\to\psi_\mu+\partial/\partial x_\mu\,\epsilon$, with $\epsilon$ an arbitrary Dirac spinor; the freedom removes the spin-$\tfrac12$ branches that the representation theory places in the field, leaving the two helicities $\pm\tfrac32$. Second, in the massive case the constraint structure is more rigid and the minimal coupling is known to be inconsistent: the field propagates acausally in an external electromagnetic background, the Velo–Zwanziger obstruction, and a consistent interacting theory requires either a gravitational background or a gauge principle. The framework represents these facts; it does not remove them.

The conventions are those of the companion articles. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$, central scalar imaginary $i$, gradient $\tilde{\nabla}=e_t\partial/\partial Q_t+\nabla$ with conjugate $\tilde{\nabla}^{\natural}$ and d'Alembertian $\Box=\tilde{\nabla}\tilde{\nabla}^{\natural}=\partial^2/\partial Q_t^2+\Delta$. The frame is written in cells of the algebra that acts on $\mathbb{B}$ by two-sided multiplication: a cell is a pair of multipliers, $L_{a}R_{b}\psi=a\psi b$, with $L_{a}R_{b}L_{c}R_{d}=L_{ac}R_{db}$ and identity cell $I_4=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$. The frame cells are

$$
\gamma_\mu:=iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\quad(\nu(0)=x,\ \nu(k)=y),
\qquad
\gamma_5:=-iR_{\vec e_z}^{\mathrm{axf}},
$$

that is $\gamma_0=iR_{\vec e_x}^{\mathrm{axf}}$ and $\gamma_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ for $k=1,2,3$. The label $\mu$ of a cell is the coordinate index of its left multiplier, and the index is always written low. The right multiplier is always a spatial unit — the direction $\nu(\mu)$ is one of $x,y,z$ by construction, never $t$ — so it carries the arrow, $\vec e_{\nu(\mu)}$; the left multiplier carries the arrow only when its index is written out as spatial, $L_{\vec e_k}^{\mathrm{axf}}$; the generic $L_{e_\mu}^{\mathrm{axf}}$ is left plain, since $\mu=0$ gives the scalar $e_t=1$. The one factor $i$ in a cell is a normalisation and not a choice: it is what makes the four Clifford generators of the frame, and divided by $i$ the cells would square to $-g_{\mu\nu}$ and the signature would be reversed. Where a second $i$ meets the $i$ of a cell the two collapse, $i^2=-1$, so that $i\,\gamma_\mu=-L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$ and the Dirac operator $i\,\gamma_\mu\partial/\partial x_\mu$ of the frame is minus the plain two-sided contraction. Every display below is written in these glyphs, so that the factor $i$ of a cell is read once, here, and not at each occurrence; where the two multipliers carry the argument — the algebra element of the mass term, the reading of the trace — the cell is spelled out. The cells are elements of the cell algebra $\mathbb{B}^{\mathrm e}\cong M_4(\mathbb{C})$, not of $\mathbb{B}$, and the frame is a coordinate choice.

The informational basis is $e_t,i\vec e_x,i\vec e_y,i\vec e_z$ — the four units that square to $+e_t$ — and it is distinct from the coordinate basis $e_\mu=(e_t,\vec e_x,\vec e_y,\vec e_z)$, whose three spatial legs carry no factor $i$. With the mostly-minus metric $g=\mathrm{diag}(+1,-1,-1,-1)$,

$$
(\gamma_0)^2=+I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\bigl\{\gamma_\mu,\gamma_\nu\bigr\}=2g_{\mu\nu}I_4 .
$$

No index is raised or lowered, and the metric enters only through the **sign vector** $\varepsilon_\mu:=g_{\mu\mu}$, $\varepsilon_0=+1$, $\varepsilon_k=-1$: where two low indices are contracted with the metric, the term carries $\varepsilon_\mu$. The chirality cell is the product of the four frame cells,

$$
\gamma_5=i\,\gamma_0\gamma_1\gamma_2\gamma_3,
$$

with $i$ the central imaginary of $\mathbb{B}$, and the antisymmetrized products are $\tfrac12[\gamma_\mu,\gamma_\nu]$ for a pair and $\tfrac1{3!}\sum_{\mathrm{perms}}\pm \gamma_\mu\gamma_\nu\gamma_\rho$ for a triple. The antisymmetric symbol is $\epsilon_{\mu\nu\rho\sigma}$ with $\epsilon_{0123}=+1$. The explicit rest-frame computation below uses the frame in which $\gamma_0$ is diagonal and the three spatial cells carry the Pauli matrices between its two halves; the cells are the same objects in either frame.

**Coordinates and frames.** The displays are written in the $\mathbb{M}_-$ frame, with $\partial/\partial x_\mu$ the derivative in the physical coordinates $x_\mu=(t',x,y,z)$ and the frame cells the ones declared above. The algebra's own coordinate is $Q_t=ict'$, and $\partial/\partial t'=i\partial/\partial Q_t$; the gradient is $\tilde\nabla=e_t\partial/\partial Q_t+\sum_k\,\vec e_k\partial/\partial Q_k=-ie_t\partial/\partial t'+\sum_k\,\vec e_k\partial/\partial x_k$. A display with $\partial/\partial Q_\mu$ in place of $\partial/\partial x_\mu$ is not a frame: the mixed contraction $i\,\gamma_\mu\partial/\partial Q_\mu$ belongs to neither frame and is not used (*Matrix Representations Conventions*, §*The Clifford Structure and the Frame*). The covariant divergence of a vector-spinor is $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\psi_\mu$, and it is written $\operatorname{div}\psi$ below.

## The Standard Rarita–Schwinger Field

### The field and its equation

The Rarita–Schwinger field is a vector-spinor: a four-vector index and a Dirac spinor index, written $\psi_{\mu\alpha}$ with $\mu=0,1,2,3$ and $\alpha=1,\dots,4$. The equation is written through two objects of the frame, the totally antisymmetrized triple and the antisymmetrized pair,

$$
T_{\mu\nu\rho}:=\tfrac1{3!}\sum_{\mathrm{perms}}\pm \gamma_\mu\,\gamma_\nu\,\gamma_\rho,
\qquad
h_{\mu\nu}:=\tfrac12\bigl[\gamma_\mu,\gamma_\nu\bigr],
$$

the triple antisymmetric in all three indices and vanishing when two of them coincide, the pair antisymmetric in its two. These are the two composites of the gamma dictionary, $T_{\mu\nu\rho}=\gamma_{\mu\nu\rho}$ and $h_{\mu\nu}=\gamma_{\mu\nu}$, written $T$ and $h$ for the two roles they play: the kinetic structure and the mass structure. In the massless case the equation is

$$
T_{\mu\nu\rho}\,\partial/\partial x_\rho\,\psi_\nu = 0,
$$

and in the massive case it is

$$
T_{\mu\nu\rho}\,\partial/\partial x_\rho\,\psi_\nu + i\,m\,h_{\mu\nu}\psi_\nu = 0 .
$$

The literature writes the kinetic term with the antisymmetric symbol instead, and the two writings are related by the duality identity of the frame,

$$
\varepsilon_\mu\varepsilon_\rho\varepsilon_\sigma\,\epsilon_{\mu\nu\rho\sigma}\,\gamma_5\,\gamma_\nu = i\,T_{\mu\sigma\rho},
$$

which holds for every value of the free indices, the summed one being $\nu$, both sides vanishing when two of $\mu,\rho,\sigma$ coincide; it states that the chirality cell is the volume cell of the frame. The three factors $\varepsilon_\mu\varepsilon_\rho\varepsilon_\sigma$ are the metric weights of the free indices of the symbol; with every index written low they cannot be dropped, and they are the same sign vector that the conventions attach to every metric contraction. With the identity, the epsilon writing of the massive equation is

$$
\varepsilon_\mu\varepsilon_\rho\varepsilon_\sigma\,\epsilon_{\mu\nu\rho\sigma}\,\gamma_5\,\gamma_\nu\,\partial/\partial x_\rho\,\psi_\sigma - m\,h_{\mu\nu}\psi_\nu = 0,
$$

which is the trivector equation term by term, up to the factor $i$ that the identity carries: the epsilon kinetic term is $i\,T_{\mu\nu\rho}\partial/\partial x_\rho\psi_\nu$, and multiplication of the display by $-i$ returns the trivector form, with $+i\,m\,h_{\mu\nu}\psi_\nu$ in place of $-m\,h_{\mu\nu}\psi_\nu$. The massless case is the same display with $m=0$.

The factor $i$ is not a convention. The two displays are one equation multiplied by $-i$, and the multiplication reaches both terms: the epsilon kinetic term carries the factor $i$ relative to $T$, so the mass term beside it is $-m\,h$ and the mass term beside $T$ is $+i\,m\,h$. Written with a real mass term in either display the equation has no solutions at all: the sixteen-component momentum-space operator is then invertible on the mass shell, its determinant not vanishing at $k^2=m^2$, while with $\pm i\,m$ it has the four-dimensional kernel of the quartet. The overall sign is then a convention, and the two conventions are exchanged by the chirality rotation $\psi_\mu\mapsto\gamma_5\psi_\mu$, which anticommutes with the three cells of $T$ and commutes with the two of $h$; the displayed sign is the one whose positive-frequency solutions have the rest-frame frequency $\omega=m$ in the upper half of the frame, as the reduction below shows.

The equation is the Euler–Lagrange equation of the Rarita–Schwinger Lagrangian, whose kinetic term is the same antisymmetrized combination and whose mass term is the antisymmetrized pair $h_{\mu\nu}$,

$$
\mathcal{L} = -\tfrac12\,\bar{\psi}_\mu\Bigl(\varepsilon_\mu\varepsilon_\rho\varepsilon_\sigma\,\epsilon_{\mu\nu\rho\sigma}\,\gamma_5\,\gamma_\nu\,\partial/\partial x_\rho\,\psi_\sigma - m\,h_{\mu\nu}\psi_\nu\Bigr),
$$

up to the overall normalisation, which is a convention; varying with respect to $\bar{\psi}_\mu$ returns the equation displayed above. The index structure is fixed by the requirement that the equation be first order and that its free solutions carry spin $\tfrac32$. No first-order equation for a single lower-spin field can do that: the two-index structure is necessary, and the antisymmetrizations are what make the equation carry an irreducible spin-$\tfrac32$ rather than a reducible sum. The Lagrangian also shows where the mass term sits: it is the antisymmetrized pair $h_{\mu\nu}$, not the Clifford metric $g_{\mu\nu}$, and this is what distinguishes the spin-$\tfrac32$ mass term from the Proca mass term $\tfrac12m^2\sum_\mu A_\mu A_\mu$.

### The constraint and the reduction

The massive equation implies the trace in two contractions, and the same two contractions deliver the reduced dynamics. Write $S:=\gamma_\sigma\psi_\sigma$ for the trace spinor. Taking the divergence of the equation kills the kinetic term, because $T$ is antisymmetric in its first and third indices, and leaves, using $h_{\mu\sigma}=\gamma_\mu\gamma_\sigma-g_{\mu\sigma}I_4$,

$$
0 = h_{\mu\sigma}\,\partial/\partial x_\mu\,\psi_\sigma
= \gamma_\mu\,\partial/\partial x_\mu\,S
- \sum_\sigma\varepsilon_\sigma\,\partial/\partial x_\sigma\psi_\sigma ,
$$

the weight $\varepsilon_\sigma$ sitting on the single surviving term of $g_{\mu\sigma}\psi_\sigma$.

Contracting the equation with $\varepsilon_\mu \gamma_\mu$ instead — the raised cell — and using the two traces of the frame,

$$
\sum_\mu\varepsilon_\mu\,\gamma_\mu\,T_{\mu\sigma\rho}=2\,h_{\sigma\rho},
\qquad
\sum_\mu\varepsilon_\mu\,\gamma_\mu\,h_{\mu\sigma}=3\,\gamma_\sigma,
$$

which are $\gamma_\mu\gamma^{\mu\nu\rho}=2\gamma^{\nu\rho}$ and $\gamma_\mu\gamma^{\mu\sigma}=3\gamma^\sigma$ read in the sign-vector convention, leaves

$$
2\,h_{\sigma\rho}\,\partial/\partial x_\rho\,\psi_\sigma + 3\,i\,m\,S = 0 ,
$$

the derivative index sitting on the second slot of $h$, as it does in the equation. The first term vanishes with the divergence relation above: the antisymmetry of $h$ turns one pairing into the other, $h_{\sigma\rho}\partial/\partial x_\rho\psi_\sigma=-h_{\mu\sigma}\partial/\partial x_\mu\psi_\sigma$, and the right-hand side of that identity is the left-hand side of the relation. The display therefore reduces to $3\,i\,m\,S=0$, and for $m\neq0$ the trace vanishes,

$$
\gamma_\mu\psi_\mu = 0 ,
$$

and with it the covariant divergence $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\psi_\mu=0$: the first display of this section, read as $\gamma_\mu\partial/\partial x_\mu S=h_{\mu\sigma}\partial/\partial x_\mu\psi_\sigma+\sum_\sigma\varepsilon_\sigma\partial/\partial x_\sigma\psi_\sigma$, has zero on both the left-hand side, once $S$ vanishes, and the first term on the right, which is the divergence of the equation; the last term is what remains. The trace is therefore a consequence of the massive equation and not an independent condition, and so is the divergence.

The trace in turn linearises the double product. Multiplying $\gamma_\mu\gamma_\sigma=h_{\mu\sigma}+g_{\mu\sigma}I_4$ by $\psi_\sigma$ and summing over $\sigma$ gives $h_{\mu\sigma}\psi_\sigma=-\varepsilon_\mu\psi_\mu$ when the trace vanishes, the weight being the one of the single surviving metric term. Substituting this, the vanishing of $h_{\sigma\rho}\partial/\partial x_\rho\psi_\sigma$, and the vanishing of $\sum_\sigma \gamma_\sigma\partial/\partial x_\mu\psi_\sigma=\partial/\partial x_\mu S$, into the identity

$$
T_{\mu\sigma\rho}=\gamma_\mu\,h_{\sigma\rho}-g_{\mu\sigma}\,\gamma_\rho+g_{\mu\rho}\,\gamma_\sigma,
$$

leaves

$$
E_\mu=i\,\varepsilon_\mu\bigl(\mathbb{D}-m\bigr)\psi_\mu\qquad\text{(no sum on }\mu\text{)} ,
$$

with $\mathbb{D}:=i\,\gamma_\nu\partial/\partial x_\nu$ the Dirac operator of the frame. The factor $i\varepsilon_\mu$ is a nonzero multiple, the metric weight of the free index, and it is the same for every component, so the equation vanishes exactly when the component Dirac equation holds,

$$
(\mathbb{D}-m)\psi_\mu=0\quad\text{for each }\mu .
$$

The antisymmetrized equation is thus equivalent to the Dirac equation on each component together with the trace, and, through them, the covariant divergence. The mass term regenerates the Dirac operator on each component, so that the reduced dynamics is the one the companion Dirac article supplies. The trace constraint removes one Dirac spinor's worth of components from the sixteen, and it is the part of the reduction that the algebra can state as a single contraction.

The massless case separates the constraints, and the separation is what the gauge freedom is for. For $m=0$ the same two contractions no longer force the trace: $\gamma_\mu\psi_\mu=0$ is not contained in the equation, and adjoining it lowers the solution space from six dimensions to four. The covariant divergence is a different matter, because its four components are linear combinations of the components of the equation: $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\psi_\mu=0$ remains a consequence of the equation even when the mass vanishes. It is in the massless case that the **gauge freedom**

$$
\psi_\mu \longrightarrow \psi_\mu + \partial/\partial x_\mu\,\epsilon,
$$

appears, with $\epsilon$ an arbitrary Dirac spinor: the antisymmetrized kinetic structure is built from the field strength $\partial/\partial x_\rho\,\psi_\sigma$, which changes by a symmetric derivative that the antisymmetrization discards. The gauge freedom is the spin-$\tfrac32$ analogue of the electromagnetic gauge freedom, it is what removes the spin-$\tfrac12$ branch that the vector index introduces, and it is also what makes the trace usable: the trace values that occur on the massless solution space are exactly the ones a gauge transformation can shift, so the gauge $\gamma_\mu\psi_\mu=0$ is attainable and the trace is a complete gauge choice rather than a derived constraint.

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

Two independent conditions remove the spin-$\tfrac12$ content, and because they act on different structures their effects add. The **algebraic trace** $\gamma_\mu\psi_\mu=0$ removes one Dirac spinor's worth of components, which is two spin-$\tfrac12$ multiplets. The **gauge freedom** in the massless case removes another Dirac spinor's worth, another two spin-$\tfrac12$ multiplets. What is left is the two spin-$\tfrac32$ multiplets, of total dimension eight, and for each frequency sign that is the four-dimensional quartet of a spin-$\tfrac32$ particle. In the massive case the gauge freedom is absent, and the second pair of spin-$\tfrac12$ multiplets is removed instead by the subsidiary conditions that follow from the equation; the physical count is the same four states per charge.

The counting is therefore representation-theoretic and does not depend on the detailed form of the antisymmetrizations: any first-order equation whose solutions are pure spin-$\tfrac32$ must remove exactly the four spin-$\tfrac12$ multiplets from the tensor product, and the trace constraint and the gauge freedom are the two mechanisms that do it. This is the reason the field is the minimal carrier of spin $\tfrac32$: the next tensor product that could carry it, the three-index object, would carry still more lower-spin admixture, and the two-index object is the smallest that contains $\tfrac32$ at all.

### The known difficulties

In the massive case the constraint structure is rigid: the equation implies the trace $\gamma_\mu\psi_\mu=0$ and the covariant divergence $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\psi_\mu=0$, there is no gauge freedom to remove the remaining components, and the resulting theory has the right free-field content but is known to be inconsistent upon minimal coupling to an external electromagnetic field. The propagation becomes acausal for sufficiently strong backgrounds — the Velo–Zwanziger obstruction — and a consistent interacting spin-$\tfrac32$ theory requires a gravitational or gauge principle rather than a fixed background. This is the standard status of the field, and it is recorded here because the biquaternion formulation does not alter it: the algebra rewrites the free equation faithfully, and the difficulties belong to the coupling.

## The Vector-Spinor Field in the Biquaternion Framework

### The carrier

The biquaternion carrier of a spin-$\tfrac32$ field is a **biquaternion-valued four-vector**,

$$
\tilde{\Psi}_\mu \in \mathbb{B}, \qquad \mu=0,1,2,3,
$$

that is, a family of four elements of the algebra, one for each spacetime index. In components, $\tilde{\Psi}_\mu = \Psi_{\mu,0}e_t + \Psi_{\mu,1}\vec e_x + \Psi_{\mu,2}\vec e_y + \Psi_{\mu,3}\vec e_z$ with complex coefficients, so that the carrier has $4\times4 = 16$ complex components, matching the standard field. The vector index is carried by the algebra's own four-vector structure, as it is for the Proca potential, and the spinor index by the regular module of the algebra, as it is for the Dirac field, whose carrier is the sum of the two minimal left ideals of $\mathbb{B}$. The frame cells act on that module; the odd ones are not left multiplications. The Rarita–Schwinger field is therefore a **mixed object**: neither an element of a module over $\mathbb{B}$ nor a pure element of $\mathbb{B}$ transforming by conjugation, but a tensor product of the two. This is the structural reason it lies outside the algebra's native spin content, a point the final article of the subcategory develops.

### The components of the equation

The standard equation is transcribed component by component, using the correspondence between the frame cells and the algebra's units. The correspondence is the frame identity of *Matrix Representations Conventions*: each of the four units of the informational basis is read as the fixed odd cell $\gamma_0$ times a representative carrying its direction,

$$
e_t \longmapsto \gamma_0^2 = +I_4, \qquad
i\vec e_k \longmapsto \gamma_0\,\gamma_k \quad (k=x,y,z) ,
$$

with the comparison map onto the even Clifford algebra; equivalently, a four-vector contracted with the cells is the fixed cell times the image of the corresponding element of the **informational** sector $\mathbb{M}_+$, whose basis is $\{e_t, i\vec e_x, i\vec e_y, i\vec e_z\}$. A product of two images is not the image of the product, because the fixed cell is not central: it passes the image of $e_t$ without a sign change and the images of the three $i\vec e_k$ with one, $\gamma_0\gamma_k\gamma_0=-\gamma_k$. Hence the product of the images of two informational units is

$$
s_\mu\,\gamma_\mu \gamma_\nu, \qquad s_0 = +1, \quad s_k = -1 ,
$$

with the sign fixed by the left factor alone, a relation verified for all sixteen index pairs in the frame. The four images themselves are even cells and square to $+I_4$. The reading is linear and injective; multiplicativity belongs to the algebra elements, and the four units are a spanning set, not a subalgebra, so the product of two units — which is the identity, a unit, or $i$ times a unit — is not in general the image of that unit. Nothing below uses that product.

The mass term, the antisymmetrized pair, comes out of the same rule, and it is where the two multipliers separate. The timelike bivector is the image of $i\vec e_k$, $\tfrac12[\gamma_0,\gamma_k]=\gamma_0\gamma_k$. The spacelike bivector is a pure left multiplier,
$$
\tfrac12[\gamma_j,\gamma_k]=\pm\,L_{\vec e_\lambda}^{\mathrm{axf}}\qquad(\lambda\ \text{the remaining index}),
$$
with the plus sign for the cyclic order $(\vec e_x,\vec e_y,\vec e_z)$: the two spatial cells of the product carry the same right multiplier $\vec e_y$, and $\vec e_y\vec e_y=-e_t$, so the right multiplier cancels and only the left one survives. The two families therefore are not of one shape, and the frame needs both: the timelike pair carries the right multiplier of the spatial cells, the spacelike pair does not. This is the sense in which the timelike bivectors are the informational sector's images and the spacelike ones the material sector's left multipliers.

The trivectors, which carry the kinetic structure, are the fixed odd cell times those left multipliers,
$$
\gamma_0\,L_{\vec e_\lambda}^{\mathrm{axf}}=i\,L_{\vec e_\lambda}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=\gamma_0\gamma_j\gamma_k ,
\qquad
\gamma_1\gamma_2\gamma_3=-i\,R_{\vec e_y}^{\mathrm{axf}},
$$
four cells, one for each choice of three indices, with the same cyclic sign rule, as *Matrix Representations Conventions* records.

Chirality is the one place where the correspondence needs a word. The comparison map sends the biquaternion imaginary to minus the pseudoscalar, $i\mapsto-\omega$, so the chirality operator is the product of the two commuting square roots of $-1$,

$$
\gamma_5 = i_{\mathrm{Cl}}\,\omega = -\Phi_{\mathbb{C}}\!\left(i_{\mathrm{Cl}}\,i\right),
$$

the external complex unit $i_{\mathrm{Cl}}$ of the complexified Clifford algebra and the biquaternion imaginary $i$. It is not an element of $\mathbb{B}$: it needs both units. It anticommutes with every cell of the frame and commutes with every even element, hence with the whole biquaternion image, and its eigenspaces are the chiral halves of the spinor space. The transcriptions are the same ones used for the Dirac equation and are the content of the comparison between the Dirac algebra and the biquaternions.

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

where the first line is the algebra reading of the cell trace $\sum_\mu\gamma_\mu\tilde\Psi_\mu=0$, derived two paragraphs below, $\varepsilon=(1,-1,-1,-1)$ is the sign vector of the frame, and $\tilde\Psi_\mu=\tilde\Psi_{\mu,L}+\tilde\Psi_{\mu,R}$ is the decomposition of each component into its two chiral ideals, the two minimal left ideals of $\mathbb{B}$. The first display is two Dirac equations per component — the two-sided structure of the gradient, $\tilde\nabla$ on the right half and $\tilde\nabla^{\natural}$ on the left, with the mass as the off-diagonal pairing. Every object in these displays is an element of $\mathbb{B}$ or a derivative of one; no cell of the frame appears.

The equivalence with the antisymmetrized equation is the standard free-field reduction. If each component satisfies the chiral pair, and if the trace and divergence constraints hold, then the antisymmetrized equation follows; conversely, the antisymmetrized equation implies the pair and the trace, and the divergence. The cell form of the pair is the module transcription of the first display, and the two constraints are the module transcription of the second; the biquaternion form is the pair and the constraints.

**The trace in the algebra.** The cell trace collapses onto one algebra element, and the right multiplier of the spatial cells is part of the answer. Since $\gamma_0=iR_{\vec e_x}^{\mathrm{axf}}$ and $\gamma_k=iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, the product $\gamma_0\gamma_k$ carries both multipliers and the right one moves to the far right,
$$
\gamma_0\gamma_k\psi=i\,\bigl(i\vec e_k\psi\vec e_y\bigr)\vec e_x=\vec e_k\psi\,\vec e_z ,
$$
so $\gamma_0\gamma_k=L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ as cells. Multiplying the cell trace by the invertible $\gamma_0$ therefore gives
$$
\gamma_0\sum_\mu\gamma_\mu\tilde{\Psi}_\mu
=\tilde{\Psi}_0+\sum_k\vec e_k\tilde{\Psi}_k\,\vec e_z ,
$$
an element of $\mathbb{B}$ and nothing else. The constraint $\sum_\mu\gamma_\mu\tilde\Psi_\mu=0$ is equivalent to the vanishing of that element, which is the trace constraint written above, and the two forms carry the same four complex conditions. The right multiplier $\vec e_z$ is not decoration: dropping it changes the condition off the free solutions, and it is what the $\vec e_y$ of the three spatial cells leaves behind when the trace is read in the algebra. The condition itself is frame-free: the left side is a cell, the right side is one element of $\mathbb{B}$, and the fixed odd cell cancels between the two sides rather than being chosen.

**The mass term is frame-free.** With the bivectors read as in the two paragraphs above, the mass term of the $\mu$-th equation is left multiplication by an element of $\mathbb{B}$,
$$
\Gamma_{\mu\nu}\longmapsto \tfrac12[\gamma_\mu,\gamma_\nu],
\qquad
\Gamma_{0k}=i\vec e_k,\quad \Gamma_{k0}=-i\vec e_k,\quad
\Gamma_{jk}=\pm\vec e_l ,
$$
with $\Gamma_{00}=0$ and the sign of $\Gamma_{jk}$ fixed by the orientation $\vec e_x\vec e_y=\vec e_z$, as *Matrix Representations Conventions* records in §*The Clifford Structure and the Frame*. No cell of the frame appears in the result.

**The compact operator is a cell.** The antisymmetrized kinetic operator $\varepsilon_\mu\varepsilon_\rho\varepsilon_\sigma\epsilon_{\mu\nu\rho\sigma}\,\gamma_5\,\gamma_\nu\partial/\partial x_\rho$ is a cell of $\mathbb{B}^{\mathrm e}$, not an element of $\mathbb{B}$: $\gamma_5\gamma_\nu$ is odd, and the odd part of the cell algebra lies outside the biquaternion algebra. It is a compact rewriting of the pair, not the primary object. The frame enters only here, in the choice of the odd cell; the dynamics is the pair and the two constraints above. In the rest-frame computation below the contraction is carried out with the frame cells directly, as a check in one frame.

## The Rest-Frame Reduction

### Setting up

**Time convention.** The check is performed in the $\mathbb{M}_-$ frame, with $x_0=t'$ and the frame cells declared above. The series' algebra coordinate is $Q_t=ict'$; the two are related by $\partial/\partial t'=i\partial/\partial Q_t$, not by relabelling $Q_t$ as $t'$. The substitution is applied to the whole operator, $\mathbb{D}-m$, at once. The mixed contraction $i\,\gamma_\mu\partial/\partial Q_\mu-m$ is a different operator, obtained by replacing only the time derivative; at rest it is $i\,\gamma_0(-m)-m=m(R_{\vec e_x}^{\mathrm{axf}}-I_4)$, and since $(R_{\vec e_x}^{\mathrm{axf}})^2=-I_4$ its eigenvalues are $m(-1\pm i)$, so it has no kernel at all. The upper-half result below therefore belongs to the $\mathbb{M}_-$ frame and is not obtained by substituting $Q_t$ for $t'$ in the operator.

The computation below is a frame check: it evaluates the standard transcription in the frame of the cells. The invariant statement is the pair and the constraints. Take the field at rest and of positive frequency, so that each component is proportional to $\exp(-imt'/\hbar)$ in natural units; the derivative is $\partial/\partial t'\to -im$, equivalently $\partial/\partial Q_t\to -m$. The Dirac operator becomes

$$
i\,\gamma_\mu\partial/\partial x_\mu - m \;\longrightarrow\; i\,\gamma_0(-im) - m ,
$$

the product of the two imaginary units collapses, $i^2=-1$, and because $\gamma_0=iR_{\vec e_x}^{\mathrm{axf}}$ one has $i\,\gamma_0(-im)=i\,mR_{\vec e_x}^{\mathrm{axf}}$, so the operator is

$$
imR_{\vec e_x}^{\mathrm{axf}} - m = m\left(\gamma_0 - I_4\right),
$$

acting on each component. Since $(\gamma_0)^2=I_4$, with eigenvalues $\pm1$, the operator $m(\gamma_0-I_4)$ annihilates exactly the **upper** half of $\mathbb{B}$, the $+1$ eigenspace of $\gamma_0$, and annihilates nothing else; the equation on the spatial components therefore forces them into that half.

The algebra gives the same count without the frame split. At rest $\tilde\nabla\to -me_t$, and the pair becomes the rest-frame form of the off-diagonal mass pairing: the first member determines $\tilde\Psi_{\mu,L}$ from $\tilde\Psi_{\mu,R}$ through that pairing, and the second returns the same relation, so the pair is consistent and leaves two complex components per $\mu$, eight in all. The trace constraint $\tilde\Psi_0+\sum_k\vec e_k\tilde\Psi_k\vec e_z=0$ is four complex conditions, so the free solution space is four complex dimensional, the same count as the cell reduction. The split into upper and lower halves is the energy split of the $\mathbb{M}_-$ frame, not a property of the algebra.

### The trace constraint at rest

Write $\psi_0$ and $\psi_k$ for the components, and use the trace constraint $\sum_\mu \gamma_\mu\psi_\mu = \gamma_0\psi_0 + \gamma_k\psi_k = 0$. The equation at rest forces $\psi_0=0$ and forces the spatial components to their upper halves. Each spatial cell maps the upper half onto the lower one, and the three maps are the Pauli matrices up to signs and a relabelling of the three directions; with the frame labelled so that the relabelling is the identity, the lower-half amplitude of the image is minus the Pauli matrix applied to the upper amplitude. Writing $\chi_k$ for the two-component upper amplitude of $\psi_k$,

$$
\gamma_k\chi_k = -\sigma_k\chi_k ,
$$

so the trace constraint reads, in its upper and lower halves,

$$
\boxed{\;\psi_0 = 0 \quad\text{(upper)}, \qquad
-\boldsymbol{\sigma}\cdot\vec\chi = 0 \quad\text{(lower)}\;}.
$$

These are the upper and lower halves of the frame, not chirality eigenstates: $\gamma_5$ maps each half onto the other, so the trace constraint does not split into chiral halves.

The lower equation gives $\boldsymbol{\sigma}\cdot\vec\chi=0$; the upper gives $\psi_0 = 0$. The trace constraint therefore forces the time component to vanish **and** imposes the single vector condition $\boldsymbol{\sigma}\cdot\vec\chi=0$ on the three spatial amplitudes. The combined system of the Dirac equation on all four components and the trace constraint has nullity four, the constraint $\boldsymbol{\sigma}\cdot\vec\chi=0$ has nullity four, and the two solution spaces coincide.

### The spin-one-half content and its removal

The three spatial amplitudes $\chi_k$ carry $3\times2 = 6$ complex components before the condition. Under the rotation group the spatial index is a spin-one object and the two-component spinor a spin-$\tfrac12$ object, so

$$
1\otimes\tfrac12 = \tfrac32 \oplus \tfrac12, \qquad 3\times2 = 4 + 2 ,
$$

and the condition $\boldsymbol{\sigma}\cdot\vec\chi=0$ removes exactly the spin-$\tfrac12$ piece of dimension two. What remains is a four-dimensional space, the spin-$\tfrac32$ quartet, with states of spin projection $\pm\tfrac32$ and $\pm\tfrac12$ along any axis. The representation-theory count of the field had two spin-$\tfrac32$ multiplets; the one found here is the positive-frequency or particle multiplet, and the negative-frequency or antiparticle multiplet is obtained by the conjugate choice of frequency and has the same four states. The four spin-$\tfrac12$ multiplets of the field are removed, two by the trace constraint and two by the Dirac equation, exactly as the general consistency analysis requires.

### Verification

The reduction was checked by explicit complex-matrix computation in the frame of the cells, with $\gamma_0$ diagonal and the three spatial cells the Pauli blocks between its halves, and $m$ a fixed nonzero parameter. At rest the sixteen-component operator has vanishing diagonal blocks and every remaining block of norm $m$: the time component couples to the spatial ones through $i\,m\,h_{0k}$, and the spatial components couple among themselves through $i\,m(h_{kl}-T_{kl0})$, the trivector $T_{kl0}$ being nonzero only for $k\neq l$. The operator is therefore not diagonal in the vector index, and its four-dimensional null space is reached through the coupling of the components and not component by component; on that null space the time component vanishes and the spatial components are upper, and the component Dirac equation $E_\mu=i\varepsilon_\mu(\mathbb{D}-m)\psi_\mu$ is what remains after the trace and the divergence have been used. The trace constraint was assembled as the $4\times16$ matrix of $\gamma_\mu$ on the four component blocks, its algebra reading $\gamma_0\sum_\mu\gamma_\mu\tilde\Psi_\mu=\tilde\Psi_0+\sum_k\vec e_k\tilde\Psi_k\vec e_z$ was checked to machine precision on random components, and its null space on the solution space was verified to be the whole of it, so that the trace is implied and adjunction does not lower the dimension; the null space of the combined $20\times16$ system, and of the equation alone, have dimension four. The null space of the single condition $\boldsymbol{\sigma}\cdot\vec\chi=0$ on the six spatial upper components is also four, and the two spaces agree element by element. The antisymmetrized form of the equation gives the same four-dimensional null space, confirming the equivalence of the trace form and the antisymmetrized form at the level of the free solutions. The check was performed on a basis of the solution space, not on a single wavefunction, and the frame is the one declared above.

Three further checks were run at a generic on-shell momentum, where $\vec k$ has three distinct nonzero components, so that no rest-frame degeneracy can hide a mismatch. The duality identity was verified as a matrix identity in the free vector index for all index values, with residual zero, so that the epsilon kinetic term is $i$ times the trivector one; the same check gives the value of the mass term, because with a real coefficient in place of $i\,m$ the momentum-space operator has no zero singular value anywhere on the mass shell, and with $i\,m$ it has four, which is the nullity of the solution space. The antisymmetrized equation has null space of dimension $4$, and it coincides with the null space of the component-Dirac-plus-trace system and with that of the same system augmented by the contracted divergence condition $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\psi_\mu=0$, so that in the massive case the trace and the covariant divergence are consequences of the equation rather than additional conditions; a single-component amplitude was checked to fail the equation by an amount of order $m$, so that the solution space is genuinely a constrained subspace and not the whole space. For the massless equation at a generic lightlike momentum the same computation gives a null space of dimension $6$, of which the four-dimensional space of pure-gauge modes $\psi_\mu\propto\partial/\partial x_\mu\,\epsilon$ is a subspace; the trace condition is not implied, the covariant divergence condition is, and the two-dimensional quotient is the two helicities. The trace values of the massless solutions span exactly the two-dimensional space of trace shifts that the gauge transformation can produce, which is the precise sense in which the trace condition is a gauge choice and the counting is unchanged. The projector $P_{ij}$ was checked to be idempotent to machine precision, to annihilate the longitudinal modes $\chi_i=\sigma_i\xi$, and to have the constrained space as its image, with trace $4$ over the six-dimensional space of spatial amplitudes.

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

The projector is the rest-frame form of the covariant spin-$\tfrac32$ projector of the standard theory, which is obtained by replacing the rest-frame $\gamma_0$ by $\gamma_\mu p_{\mu}/m$ and the spatial delta by the transverse projector with respect to $p_\mu$. In the biquaternion framework the boost is effected by rotor conjugation, so the covariant projector is the rotor conjugate of the rest-frame combination above; the algebra supplies the boost without a separate construction.

## The Massless Case and the Gauge Freedom

### The gauge transformation in the algebra

In the massless case the antisymmetrized equation and the trace constraint leave a gauge freedom, and in the biquaternion form the transformation is

$$
\tilde{\Psi}_\mu \;\longrightarrow\; \tilde{\Psi}_\mu + \partial/\partial x_\mu\,\epsilon,
$$

where $\epsilon$ is a Dirac-spinor parameter and $\partial/\partial x_\mu$ is the coordinate derivative of the $\mathbb{M}_-$ frame. The shift is the derivative of the parameter, not the gradient with the basis factor attached, $e_\mu\,\partial/\partial x_\mu$ with $\mu$ fixed: that factor would survive the antisymmetrization and the invariance would fail. The transformation shifts the field by a gradient, and the antisymmetrized kinetic structure of the equation is insensitive to it, just as the electromagnetic field strength is insensitive to a gradient of the potential. The number of gauge parameters is the number of components of $\epsilon$, namely four, which is one Dirac spinor; and the gauge freedom removes two of the four spin-$\tfrac12$ multiplets of the representation content. The remaining two are removed by the trace condition and the equations of motion — with the difference, recorded above, that in the massless case the trace is a gauge choice and the divergence condition is the consequence of the equation, so that the two mechanisms do not simply add but interlock. What is left is a single spin-$\tfrac32$ multiplet per frequency sign, that is, the two helicities $\pm\tfrac32$.

### Helicities and the two physical states

The physical content of the massless field is therefore two states per wavevector, the helicities $\pm\tfrac32$. There is no longitudinal or scalar helicity, and the count is the spin-$\tfrac32$ analogue of the two transverse helicities of the photon: in both cases the gauge freedom and the constraint together halve-and-halve the naive index content. The parallel is exact at the level of the representation theory. The photon's two-form is the antisymmetric square of the four-vector, $(1,0)\oplus(0,1)$; the massless Rarita–Schwinger field's two physical states are the two helicities of the $(1,\tfrac12)$ and $(\tfrac12,1)$ summands after the spin-$\tfrac12$ pieces are gauged away. In both cases the framework's self-dual split is the algebraic trace of the helicity structure, and in both cases the massless limit is the case in which the third and lower states are removed by gauge rather than retained by a mass.

## The Massive Case

For $m\neq0$ the mass term

$$
- m\,\tfrac12[\gamma_\mu,\gamma_\nu]\tilde{\Psi}_\nu
$$

is the antisymmetrized pair of frame cells acting on the field; its biquaternion image is left multiplication by the algebra element $\Gamma_{\mu\nu}$ given above, contracted with the corresponding component of the field. In the trace form of the equation it is simply the Dirac mass on each component. The mass term plays the same structural role as in the Proca and Dirac cases: it is linear in the field, it is what remains when the gauge freedom is absent, and it fixes the dispersion relation on the physical shell through the Dirac operator. In the rest frame the massive reduction above is the whole story: time component zero, spatial components upper, $\boldsymbol{\sigma}\cdot\vec\chi=0$, four states.

The massive case is also where the known difficulty lives. The constraint analysis that produces $\gamma_\mu\psi_\mu=0$ and $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\psi_\mu=0$ is rigid when $m\neq0$, and its consequences for the interacting theory are the Velo–Zwanziger obstruction: minimal coupling to a background electromagnetic field makes some modes propagate faster than light, and the theory is not causal as a fixed-background field theory. The biquaternion formulation reproduces the free constraint structure exactly and says nothing different about the coupling, because the coupling is an additional structure that no rewriting of the free equation can supply. This is the analogue, for spin $\tfrac32$, of the statement recorded for the Proca field: the algebra represents the free field faithfully, and what the free algebra cannot decide is the interaction.

### The dispersion relation

Because each component satisfies the Dirac equation, each component satisfies the Klein–Gordon equation on squaring, exactly as in the spin-$\tfrac12$ case. For a biquaternion plane wave of the component,

$$
\tilde{\Psi}_\mu = \tilde{\Psi}_{\mu,0}\,\exp(\,i\,\mathrm{Sc}(\tilde P\tilde Q^{\natural})/\hbar),
$$

the Dirac equation on the component requires $\tilde P\tilde P^{\natural}=-m^2c^2$ in the normalization of the companion Dirac article, that is,

$$
\frac{\omega^2}{c^2} - \vec k^2 = \frac{m^2c^2}{\hbar^2},
\qquad\text{i.e.}\qquad
\omega^2 = c^2\vec k^2 + \frac{m^2c^4}{\hbar^2},
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

**The algebra's part.** Three statements are the framework's. First, the natural carrier of the field is the family of biquaternion-valued components $\tilde{\Psi}_\mu$, and the two structural conditions of the free theory — the chiral pair on each component and the trace constraint $\tilde{\Psi}_0+\sum_k\vec e_k\tilde{\Psi}_k\vec e_z=0$ — are each single algebraic statements in $\mathbb{B}$ rather than lists of component equations. The compact cell equation is a cell transcription of the pair, not a third condition. Second, chirality is carried by the two commuting square roots of $-1$ that the comparison identifies, the biquaternion central imaginary and the external complex unit of the complexified Clifford algebra, $\gamma_5=-\Phi_{\mathbb{C}}(i_{\mathrm{Cl}}i)$; it commutes with the whole biquaternion image, so the vector-spinor's chirality structure needs no independent operator beyond the two units the comparison already supplies. Third, the rest-frame projector $P_{ij}=\delta_{ij}-\tfrac13\sigma_i\sigma_j$ is obtained from the constraint by elementary algebra, and its boosted form is the rotor conjugate of the rest-frame object, so the covariant spin-$\tfrac32$ projector is available without a separate construction.

**What is imported.** The identification of the field with a spin-$\tfrac32$ particle, the value of the mass, the existence of a consistent interaction, and the resolution of the Velo–Zwanziger problem are inputs beyond the free algebra. The canonical quantisation of the field and its propagator belong to the field-theoretic companion subcategory.

The structural point that this article makes for the subcategory is that the field is a tensor product of the algebra's vector structure with its spinor structure, so its spin-$\tfrac32$ content is not native to the algebra but arises from the product. The final article of the subcategory states this in general and proves that the algebra's own modules carry only spin zero and spin one-half.

The conventions are those of three companion articles:

- Companion article *The Dirac Equation in Biquaternionic Form*, for the biquaternion chiral pair and its cell transcription.
- Companion article *Matrix Representations Conventions*, §*The Clifford Structure and the Frame*, for the translation of the frame cells and their antisymmetrized products into the algebra's units.
- Companion article *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector*, for the vector part of the algebra and the four-vector representation from which the vector-spinor is built.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra, and the transcription introduces no new symbol: the $\gamma_\mu$ and $\gamma_5$ of the literature are the cells declared in the conventions, $\gamma_\mu=iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}$ and $\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$. The two vocabularies therefore name the same five objects in one chosen frame of the cell algebra, and no translation between two algebras is needed; what the literature adds is the matrix representation of those objects, not a second set of generators.

The cells act by $L_a\psi=a\psi$ and $R_b\psi=\psi b$. They form a complex vector space of dimension sixteen, and $c(M)$ is the coefficient matrix of a cell $M$ in the basis of the sixteen products, with $\ell(M)=\operatorname{rank}c(M)$. A single product is a pure tensor; the products form the seven-dimensional cone $\ell(M)\le1$, and a general element is a sum of at most four.

$\gamma_5$ is the reference-frame cell of the chirality operator, and it is a cell, not an element of the algebra. The central grading is the element $\chi=i\tilde\Xi_{\mathrm{ad}}$, with $\tilde\Xi_{\mathrm{ad}}^2=-e_t$ the central root of $-1$ of the double and $\chi=e_+-e_-$ the difference of the two central idempotents, so that $\chi^2=e_t$; the element $\chi$ is represented by the cell $\gamma_5$ on the Dirac module, and the two are not to be identified.

The correspondence is complex-linear, and it is a correspondence of algebras and not of elements: over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$, which is why the frame lives in the cell algebra $\mathbb{B}^{\mathrm{e}}\cong M_4(\mathbb{C})$ and not in $\mathbb{B}$.

**The display.** Where this section prints a matrix it prints the Peirce display, labelled $\mathrm{pau}$, because these are the arrays the literature prints; the body of the article writes the same operators in the axis-free display, $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant. The label names the array and not the operator.

## Summary

The Rarita–Schwinger field is a vector-spinor of sixteen complex components. Its equation is written with the antisymmetrized triple of frame cells,

$$
T_{\mu\nu\rho}\,\partial/\partial x_\rho\,\psi_\nu + i\,m\,h_{\mu\nu}\psi_\nu = 0,
\qquad
h_{\mu\nu}=\tfrac12\bigl[\gamma_\mu,\gamma_\nu\bigr],
$$

with $T_{\mu\nu\rho}$ the total antisymmetrization over the three indices, and with $m=0$ giving the massless equation. The epsilon writing of the literature is the same equation, through the duality identity of the frame,

$$
\varepsilon_\mu\varepsilon_\rho\varepsilon_\sigma\,\epsilon_{\mu\nu\rho\sigma}\,\gamma_5\,\gamma_\nu=i\,T_{\mu\sigma\rho},
$$

so that the epsilon kinetic term is $i$ times the trivector one and the two writings carry the mass term $-m\,h_{\mu\nu}\psi_\nu$ and $+i\,m\,h_{\mu\nu}\psi_\nu$, the same operator; the factor $i$ is fixed by the mass shell, and the overall sign of the term is the free convention, because $\psi_\mu\to\gamma_5\psi_\mu$ exchanges the two possibilities. In the massive case the equation implies the algebraic trace $\gamma_\mu\psi_\mu=0$ and the covariant divergence, and it is equivalent to the component Dirac equation $(\mathbb{D}-m)\psi_\mu=0$ together with the trace; the massless theory instead has the gauge freedom $\psi_\mu\to\psi_\mu+\partial/\partial x_\mu\,\epsilon$ with a single Dirac-spinor parameter, under which the trace is a complete gauge choice while the covariant divergence remains a consequence of the equation.

In the biquaternion framework the carrier is a family of biquaternion-valued components $\tilde{\Psi}_\mu\in\mathbb{B}$, one for each spacetime index, and the free system is the chiral pair on each component together with the algebraic constraints $\tilde{\Psi}_0+\sum_k\vec e_k\tilde{\Psi}_k\vec e_z=0$ and $\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\tilde{\Psi}_\mu=0$. Every term is an element of $\mathbb{B}$ or a derivative of one. Chirality is the product of the two square roots of $-1$ of the comparison, $\gamma_5=-\Phi_{\mathbb{C}}(i_{\mathrm{Cl}}i)$, and the cells are a frame in the cell algebra, the four informational units reading as $e_t\mapsto I_4$ and $i\vec e_k\mapsto \gamma_0\gamma_k$; the compact antisymmetrized equation is the cell transcription of the pair and the two constraints.

In the rest frame the system forces the time component to vanish and the spatial amplitudes to satisfy $\boldsymbol{\sigma}\cdot\vec\chi=0$. The surviving space is four-dimensional and carries the spin-$\tfrac32$ quartet; the projector onto it is $P_{ij}=\delta_{ij}-\tfrac13\sigma_i\sigma_j$, idempotent and of vector-index rank two. The representation content $2\times\tfrac32\oplus4\times\tfrac12$ loses its four spin-$\tfrac12$ multiplets to the constraint and the gauge freedom, and the massless field retains the two helicities $\pm\tfrac32$.

The field is a tensor product of the algebra's vector structure and its spinor structure, so spin $\tfrac32$ is not native to the algebra. The free equation is represented faithfully; the known difficulty of the interacting theory, the Velo–Zwanziger acausal propagation under minimal coupling, is a property of the coupling and is not removed by the rewriting.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Central scalar imaginary of $\mathbb{B}$, $i^2=-1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| Dictionary | Map onto the even Clifford algebra; $e_t\mapsto I_4$ and $i\vec e_k\mapsto \gamma_0\gamma_k$; the cells are not elements of $\mathbb{B}$ |
| $\mathbb{B}^{\mathrm e}\cong M_4(\mathbb{C})$ | Cell algebra of the regular module; the Clifford map lands here, not in $\mathbb{B}$ |
| $e_t$, $i\vec e_k$ | Informational basis, the four units that square to $+e_t$; frame-free trace and mass terms |
| $\gamma_5=-iR_{\vec e_z}^{\mathrm{axf}}=-\Phi_{\mathbb{C}}(i_{\mathrm{Cl}}i)$, $i_{\mathrm{Cl}}$ | Chirality cell, the product of the two commuting square roots of $-1$, the biquaternion $i$ and the external imaginary $i_{\mathrm{Cl}}$ |
| $\tilde{\Psi}_\mu\in\mathbb{B}$ | Biquaternion-valued components of the vector-spinor |
| $\epsilon$ | Dirac-spinor parameter of the massless shift symmetry |
| $L_{a}R_{b}$, $L_{a}R_{b}\psi=a\psi b$ | A cell: one left and one right multiplier, $L_{a}R_{b}L_{c}R_{d}=L_{ac}R_{db}$; the identity cell is $I_4=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$; the frame is written with the two multipliers |
| $\gamma_\mu=iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$, $\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4$ | Frame cells, one factor $i$ each, $g=\mathrm{diag}(+1,-1,-1,-1)$; the four gamma cells of the dictionary |
| $\gamma_{\mu\nu}:=\tfrac12[\gamma_\mu,\gamma_\nu]=h_{\mu\nu}$ | Antisymmetrized pair, the mass-term structure; image of $\Gamma_{\mu\nu}$ |
| $\Gamma_{0k}=i\vec e_k$, $\Gamma_{k0}=-i\vec e_k$, $\Gamma_{jk}=\pm\vec e_l$ | Mass-term coefficients in $\mathbb{B}$ |
| $\gamma_{\mu\nu\rho}:=\tfrac1{3!}\sum_{\mathrm{perms}}\pm \gamma_\mu\,\gamma_\nu\,\gamma_\rho=T_{\mu\nu\rho}$ | Antisymmetrized triple, kinetic structure of the equation |
| $\varepsilon_\mu=g_{\mu\mu}=(1,-1,-1,-1)$ | Sign vector of the frame; the metric weight of a contracted low index |
| $T_{\mu\nu\rho}=\gamma_{\mu\nu\rho}$, $h_{\mu\nu}=\gamma_{\mu\nu}$ | Antisymmetrized triple and pair of frame cells; the kinetic structure and the mass structure, the mass term entering as $+i\,m\,h_{\mu\nu}\psi_\nu$ in the trivector writing and as $-m\,h_{\mu\nu}\psi_\nu$ in the epsilon writing |
| $\mathbb{D}=i\,\gamma_\mu\partial/\partial x_\mu$ | Dirac operator of the frame; the reduced equation is $(\mathbb{D}-m)\psi_\mu=0$ |
| $S=\gamma_\sigma\psi_\sigma$ | Trace spinor |
| $\operatorname{div}\psi=\sum_\mu\varepsilon_\mu\partial/\partial x_\mu\psi_\mu$ | Covariant divergence; a consequence of the equation for every $m$ |
| $\varepsilon_\mu\varepsilon_\rho\varepsilon_\sigma\,\epsilon_{\mu\nu\rho\sigma}\,\gamma_5\,\gamma_\nu=i\,T_{\mu\sigma\rho}$ | Duality identity: the epsilon kinetic term is $i$ times the trivector one, which is the factor $i$ that the mass term carries |
| $\tilde{\Psi}^{\text{tr}}=\tilde{\Psi}_0+\sum_k\vec e_k\tilde{\Psi}_k\vec e_z$ | Trace constraint in $\mathbb{B}$, the algebra reading of $\gamma_\mu\psi_\mu=0$ |
| $\tilde\nabla\tilde\Psi_{\mu,R}=m\tilde\Psi_{\mu,L}$, $\tilde\nabla^{\natural}\tilde\Psi_{\mu,L}=m\tilde\Psi_{\mu,R}$ | Chiral pair on each component; the dynamics |
| $\psi_\mu=(\chi_\mu,\eta_\mu)$ | Upper and lower two-component parts, the $\pm1$ halves of $\gamma_0$ |
| $\vec\chi$ | Spatial amplitudes; constraint $\boldsymbol{\sigma}\cdot\vec\chi=0$ |
| $P_{ij}=\delta_{ij}-\tfrac13\sigma_i\sigma_j$ | Spin-$\tfrac32$ projector on the vector index |
| $2\times\tfrac32\oplus4\times\tfrac12$ | $SU(2)$ content of the vector-spinor |

## Further Reading

- William Rarita and Julian Schwinger, "On a theory of particles with half-integral spin", *Physical Review* 60 (1941) 61, for the original field equation for spin three-halves.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. III: Supersymmetry* (Cambridge, 2000), for the Rarita–Schwinger field, its gauge structure, and its role in supergravity.
- Daniel Z. Freedman and Antoine Van Proeyen, *Supergravity* (Cambridge, 2012), for the spin-$\tfrac32$ field, its constraints, and the counting of its physical states.
- Giorgio Velo and Daniel Zwanziger, "Noncausality and other defects of interaction Lagrangians for particles with spin one and higher", *Physical Review* 188 (1969) 2218, for the acausality of minimally coupled higher-spin fields.
- Claude Itzykson and Jean-Bernard Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the free higher-spin equations and the constraint analysis of the vector-spinor.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw-Hill, 1965), for the Dirac equation, the trace constraints, and the reduction of vector-spinors in the rest frame.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the antisymmetrized products of a Clifford frame and the reduction of their representations.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the spacetime-algebra treatment of the Clifford algebra and the chiral structure of spinors.
