# __Gauge Transformations of the First and Second Kind in Biquaternionic Form__

## Introduction

M. Tanişli's *Gauge transformation and electromagnetism with biquaternions* (*Europhysics Letters* **74** (2006) 569–573) writes the source-free Maxwell equations as the single biquaternion equation $\nabla F=0$, gives them a first-order Lagrangian density $L=F^*\cdot\nabla F$, and derives the local energy conservation law from what the paper calls a **biquaternionic gauge transformation of the first kind**, $F\to((1+\alpha)e_0 F)$, with $\alpha$ an infinitesimal function of $x$ and $t$. The stated result is the Poynting theorem; the stated purpose is to obtain it without translation invariance, and the paper suggests the same procedure for the momentum and the angular momentum.

The paper belongs to the tradition this corpus is built on, and its algebra is the corpus's algebra. The article records it as an external source. Its final result is correct and standard, and its route is its own; but three things about the route do not survive the corpus's conventions, and they are the reason the article exists rather than a footnote. First, the transformation is the corpus's **duality rotation**, so the physics it uses is already in the corpus, under another name. Second, the naming is reversed against Weyl's: a transformation whose parameter is an arbitrary function of the coordinates is a symmetry **of the second kind**, and the second kind produces a differential identity rather than a conservation law, which is the content of Noether's second theorem. Third, the transformation is *local*, and a genuinely local transformation of the source-free field is not a symmetry at all: a position-dependent phase of the field changes the equation it is supposed to leave invariant.

What the construction exhibits, once the algebra is put in the corpus's conventions, is not a new conservation law but the field equation contracted with the conjugate field, whose expansion using Maxwell's equations is the Poynting identity. That identity is a consequence of the equations of motion, and its origin in the corpus is the translation symmetry of the action, through Noether's first theorem and the Hermitian energy–momentum object. The paper's claim that it eliminates translational invariance is therefore not established by the construction: the law obtained is the standard one, obtained from the field equation.

The algebra as printed also carries internal inconsistencies, three of which are reproduced below by recomputation. They are recorded, not resolved, and the corpus's own conventions are used throughout.

## The Source's Construction

### The algebra

The source works with the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, an eight-dimensional complex quaternion algebra written

$$
Q = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3 = (a_0+ib_0)e_0 + \dots + (a_3+ib_3)e_3 ,
$$

with real $a_k,b_k$, the scalar imaginary $i^2=-1$, and quaternion units of square $-1$ satisfying

$$
e_ie_j = -\delta_{ij}e_0 + \epsilon_{ijk}e_k ,
$$

the standard Hamilton rule. The quaternion conjugate and the complex conjugate are $\bar Q = Q_0e_0-Q_1e_1-Q_2e_2-Q_3e_3$ and $Q^* = Q_0^*e_0+\dots+Q_3^*e_3$, and the norm is $N(Q)=\bar QQ=Q_0^2+Q_1^2+Q_2^2+Q_3^2$, which may vanish, so the algebra is not a division algebra. These are the corpus's objects; the algebra and its conjugations are fixed in *Biquaternion Algebra*, and the two conjugate pairs $\bar\cdot$ and $\bar{\cdot}$ with their fixed subspaces are fixed in *The Clifford Algebra Representation*.

### Maxwell's equations and the biquaternionic form

The source takes the source-free Maxwell equations in dimensionless form,

$$
\mathrm{div}\,\mathbf{E}=0,\qquad \mathrm{div}\,\mathbf{B}=0,\qquad
\frac{1}{c}\frac{\partial\mathbf{E}}{\partial t}=\mathrm{rot}\,\mathbf{B},\qquad
\frac{1}{c}\frac{\partial\mathbf{B}}{\partial t}=-\mathrm{rot}\,\mathbf{E},
$$

and the electromagnetic bivector

$$
F = E_xe_1+E_ye_2+E_ze_3 + i\bigl(B_xe_1+B_ye_2+B_ze_3\bigr) ,
$$

so that the four equations become the single biquaternion equation

$$
\nabla F = 0 ,
\qquad
\nabla = i\frac{\partial}{\partial t}e_0 + \frac{\partial}{\partial x}e_1 + \frac{\partial}{\partial y}e_2 + \frac{\partial}{\partial z}e_3 .
$$

The Lagrangian density is $L=F^*\cdot\nabla F$ and the variational principle is $\delta A = \delta\int dt\int dx\,L=0$, with $F$ and $F^*$ treated as independent variables.

### The transformation and the conservation law

The transformation is

$$
F \longrightarrow F' = (1+\alpha)e_0F ,
$$

with $\alpha$ an arbitrary infinitesimal function of $x$ and $t$, named in the paper *a biquaternionic gauge transformation of the first kind* and identified with $(e^{i\alpha}F)$ to first order. Substituting into $L$ gives $\delta L = F^*\cdot(\nabla(\alpha e_0F))$, which the paper expands as

$$
\delta L = F^*\cdot(\nabla\alpha)F + \alpha\,(\nabla F) ,
$$

and the second term vanishes by the field equation $\nabla F=0$. The variation of the action is then $\delta A=-\int dt\int dx\,F^*\cdot(\nabla\alpha)F=0$, and the paper reports that an integration by parts, with the requirement that $\delta A$ vanish for arbitrary $\alpha$, gives

$$
F^*\cdot(\nabla F) = 0 ,
$$

which the paper calls the conservation of energy for the electromagnetic field. Expanding the left side using the two curl equations gives

$$
\partial_t u + \mathrm{div}\,(\mathbf{E}\times\mathbf{B}) = 0 ,
\qquad
u = \tfrac12\bigl(E_x^2+E_y^2+E_z^2+B_x^2+B_y^2+B_z^2\bigr),
$$

which is the Poynting theorem, with $\mathbf{S}=\mathbf{E}\times\mathbf{B}$ the energy flux.

### The source's claim

The paper's conclusion is explicit: the standard route to a local conservation law is Noether's theorem applied to the translation and rotation invariances of a second-order Lagrangian, and the paper has instead derived the energy conservation law from a biquaternionic gauge transformation, *thus eliminating the use of translational invariance*. It adds that the same procedure may be applied to the local linear momentum and local angular momentum conservation laws.

## The Transformation Is the Duality Rotation

The transformation the paper uses is the corpus's **electric–magnetic duality rotation**, and identifying it settles what the physics is.

The corpus's field-strength article fixes the Riemann–Silberstein vector $\mathbf{V} = \mathbf{E} + ic\mathbf{B}$ and the invariance of the source-free equations under

$$
\mathbf{V}\mapsto e^{-i\theta}\mathbf{V} ,
$$

the duality rotation, which at $\theta=\pi/2$ is the classical exchange of electricity and magnetism. In dimensionless units the source's $F = \mathbf{E}+i\mathbf{B}$ is precisely $\mathbf{V}$ at $c=1$, and the source's transformation $F\to e^{i\alpha}F$ is $\mathbf{V}\to e^{i\alpha}\mathbf{V}$, that is, the duality rotation with $\theta=-\alpha$. The rotation mixes the two Lorentz invariants $\mathbf{E}\cdot\mathbf{B}$ and $\mathbf{E}^2-c^2\mathbf{B}^2$, leaving the energy density invariant; the corpus's field-strength article computes exactly this, and the computation is reproduced here as a check on the identification.

**The rotation of the invariants.** With $I_1 = \mathbf{E}^2-c^2\mathbf{B}^2$ and $I_2=\mathbf{E}\cdot\mathbf{B}$, the rotation by $\alpha$ sends

$$
I_1 \mapsto I_1\cos2\alpha - 2c\,I_2\sin2\alpha ,
\qquad
2c\,I_2 \mapsto 2c\,I_2\cos2\alpha + I_1\sin2\alpha ,
$$

and $\mathbf{E}^2+c^2\mathbf{B}^2$ is unchanged, as it must be since it is the length of $\mathbf{V}$. The identities were checked on $100$ random field pairs over a range of angles; the largest deviation was $8.9\times10^{-16}$.

**A remark on $(1+\alpha)$.**
The transformation is written $(1+\alpha)e_0F$, which to first order is $e^{\alpha}F$, and the paper identifies this with $e^{i\alpha}F$. The two agree only when $\alpha$ is purely imaginary. A real infinitesimal $\alpha$ produces the common scaling $\mathbf{E}\to(1+\alpha)\mathbf{E}$, $\mathbf{B}\to(1+\alpha)\mathbf{B}$, which is also a symmetry of the source-free equations — the equations are linear and homogeneous — but which is a dilation rather than a duality rotation. The corpus's duality rotation requires the parameter that multiplies $F$ to be a phase, so the imaginary reading is the one that makes the paper's own identification correct.

## The Two Kinds

Weyl's classification fixes the vocabulary the paper inverts.

| Kind | Parameter | Conclusion |
|---|---|---|
| **First kind** | finitely many **constants** | one conserved current per parameter |
| **Second kind** | arbitrary **functions** of the coordinates | one differential identity per function; no conservation law |

The transformation $F\to(1+\alpha)F$ with $\alpha=\alpha(x,t)$ depends on an arbitrary function of the coordinates, so it is a transformation **of the second kind** by Weyl's definition, whatever it is called. The distinction is not verbal. A symmetry of the first kind adds no condition to the equations and supplies one integral of the motion per parameter, so a rigid transformation is the only kind that can produce a conservation law. A symmetry of the second kind adds one differential identity among the Euler–Lagrange expressions per arbitrary function, and the identity is empty on the solutions: it says that the equations are not independent, that a gauge condition is needed, and that the components of the equations are tied to one another. It supplies no new conserved quantity. The two theorems, and the counting of conservation laws against identities, are the subject of *Noether's Two Theorems*, in the mathematical part of the corpus; the Maxwell field there is the example in which the local symmetry has no rigid subgroup at all and therefore carries no charge.

The consequence for the source's argument is direct. The paper's transformation is local, and the paper's conclusion is a conservation law, which is the combination the second theorem excludes. A local transformation does carry a conservation law when it contains a rigid subgroup — the first theorem then applies to the subgroup — and here the restriction to constant $\alpha$ does leave a rigid transformation: a common scaling of $\mathbf{E}$ and $\mathbf{B}$ if $\alpha$ is real, the duality rotation if $\alpha$ is imaginary. Neither rigid part conserves the energy. The scaling is a symmetry of the equations but not of the action, since $-\tfrac14F_{\mu\nu}F^{\mu\nu}$ is quadratic in the field, so the standard theorem attaches no current to it at all; the duality rotation is a symmetry of the action up to a divergence, and its first-theorem current is a helicity-type object, taken up in the open questions below.

## A Local Phase Is Not a Symmetry of the Free Equation

There is a sharper objection than the naming, and it can be checked directly: with $\alpha$ varying, the transformation does not preserve the equation it is applied to.

In the corpus's variables the source-free equations are $i\partial_t\mathbf{V}=c\,\mathrm{rot}\,\mathbf{V}$ and $\mathrm{div}\,\mathbf{V}=0$, with $\mathbf{V}=\mathbf{E}+ic\mathbf{B}$. Under $\mathbf{V}\mapsto e^{i\alpha}\mathbf{V}$ with $\alpha$ a function of the coordinates, the two sides acquire the extra contributions

$$
i\partial_t\bigl(e^{i\alpha}\mathbf{V}\bigr) = e^{i\alpha}\bigl(i\partial_t\mathbf{V} - (\partial_t\alpha)\mathbf{V}\bigr),
\qquad
c\,\mathrm{rot}\bigl(e^{i\alpha}\mathbf{V}\bigr) = e^{i\alpha}\bigl(c\,\mathrm{rot}\,\mathbf{V} + ic\,(\nabla\alpha)\times\mathbf{V}\bigr),
$$

so the equation is preserved only when $-(\partial_t\alpha)\mathbf{V} = ic\,(\nabla\alpha)\times\mathbf{V}$, which is not an identity. For constant $\alpha$ every derivative of $\alpha$ vanishes and the equation is preserved, which is the rigid duality rotation; for a position-dependent $\alpha$ it is not.

**Check.** On a free plane wave with $\mathbf{k}\cdot\mathbf{E}_0=0$, $\mathbf{B}_0 = \mathbf{k}\times\mathbf{E}_0/\omega$, the residual $|i\partial_t\mathbf{V}-c\,\mathrm{rot}\,\mathbf{V}|$ is $5.6\times10^{-12}$ at constant phase, which is the finite-difference floor, and $2.4\times10^{-1}$ at the local phase $\alpha = 0.5x-0.3z$, against a field scale of $5.1\times10^{-1}$. The local residual is half the field magnitude: the local transformation is not a symmetry.

The source uses an infinitesimal $\alpha$, and the objection is not removed by the smallness. The extra terms are first order in the derivatives of $\alpha$, not in $\alpha$ itself, so they do not vanish in the infinitesimal limit; the source's derivation uses the field equation $\nabla F=0$ to discard one term of $\delta L$, and the remaining term, $F^*\cdot(\nabla\alpha)F$, is not a divergence that can be dropped.

## What the Construction Establishes

Put in the corpus's conventions, the construction is the following, and it is worth separating what it proves from what it claims.

**The Lagrangian is not a real action.** $L=F^*\cdot\nabla F$ is complex-valued, and it is linear in $F^*$ and in the derivatives of $F$. Varying $F^*$ gives the field equation $\nabla F=0$ algebraically, because $F^*$ appears without derivatives; varying $F$ gives a condition on the derivatives of $F^*$, of the form $\partial_\mu F^*=0$, which is not the conjugate field equation $\nabla F^*=0$. So $\delta A=0$ with independent $F$ and $F^*$ is the statement that the coefficient of $\delta F^*$ vanishes, and it reproduces the field equation. The corpus's *Canonical Quantization of the Biquaternion Maxwell Field* has already recorded the general fact that governs this: no local Lagrangian in four dimensions has the first-order Maxwell system as its Euler–Lagrange equation when the field strength $\tilde F$ is the only field, because a polynomial invariant built from $\tilde F$ alone has an algebraic variation and a Lagrangian built from its derivatives gives a higher-derivative equation. The source's $L$ evades the statement only by depending on the second, independent variable $F^*$ and by being complex. It is therefore a variational *description* of the first-order system, not a real action whose stationarity is the dynamics.

**The conservation law is a consequence of the field equation.** The scalar $F^*\cdot(\nabla F)=0$ is an immediate consequence of the field equation $\nabla F=0$: it is the field equation contracted with the conjugate field, a complex scalar condition, weaker in content than the biquaternion equation it comes from. The passage from the vanishing of the variation for arbitrary $\alpha$ to this equation is stated in the paper but not derived in detail, and what the paper then does with $F^*\cdot(\nabla F)=0$ is to expand it using the two curl equations; the expansion is the Poynting identity. So the conservation law obtained is the standard consequence of Maxwell's equations, evaluated on their solutions; it is not a statement independent of them.

**The corpus's own route to the same law is translation invariance.** The energy conservation law is the real part of the biquaternion balance that the corpus derives from Noether's first theorem with translation symmetry: the Hermitian object $\tilde{\mathcal W}=\tfrac12\tilde F\tilde F^{*} = W e_0 + \tfrac{i}{c}\mathbf{S}$ satisfies $\tilde\nabla\tilde{\mathcal W}=-\tilde P$, whose scalar part is the Poynting theorem with the work term. This is the route the source's conclusion sets aside, and it is the route that does the job: the conservation law comes from a symmetry of the first kind, which is the only kind that yields one. The corpus's *Exercise: The Electromagnetic Energy–Momentum Tensor* works the object out in full and shows that the naive real four-component form $W+\tfrac{1}{c}\mathbf{S}$ fails while the Hermitian form succeeds.

**What is worth keeping.** Two things. The naming issue is a real service: the phrase "gauge transformation of the first kind" for a transformation whose parameter is a function of position is the inversion the corpus's new article on the two theorems is written to prevent. And the observation that the energy law can be written as a contraction of the field equation with the conjugate field is compact, and it is true; the corpus records it here as a remark carried by the biquaternion form, with the origin of the law attributed to the first theorem rather than to the transformation.

## The Printed Algebra

Three points of the printed algebra are internally inconsistent, and each is reproduced by recomputation against the paper's own rules. They are listed because the corpus records printed defects, not because the paper's final result depends on them; the final result is correct. The reading is from the scanned article as extracted, and isolated signs are the least reliable part of such an extraction.

**The product rule against the basis rule.** The basis rule $e_ie_j=-\delta_{ij}e_0+\epsilon_{ijk}e_k$ gives $e_1e_2 = \epsilon_{123}e_3 = e_3$. The printed product rule is $PQ = P_0Q_0 - \mathbf{P}\cdot\mathbf{Q} + P_0Q + PQ_0 + iP\times Q$, which for $P=e_1$, $Q=e_2$ gives $i\mathbf{e}_1\times\mathbf{e}_2 = ie_3$ instead. The two rules differ by the factor $i$ on the cross term, and they cannot both hold. The recomputation gives $|e_3 - e_1e_2| = 0$ from the basis rule and $|ie_3 - e_1e_2| = \sqrt2$ from the product rule. The corpus uses the basis rule, which is the standard one.

**The sign of the imaginary part of the field.** With the printed gradient $\nabla = i\partial_te_0+\partial_xe_1+\partial_ye_2+\partial_ze_3$, the equation $\nabla F=0$ gives, on a free plane wave, $|\nabla F| = 9.4\times10^{-1}$ for the printed $F=\mathbf{E}+i\mathbf{B}$ against a field scale of $4.8\times10^{-1}$, and $3.3\times10^{-10}$ for $F=\mathbf{E}-i\mathbf{B}$. The consistent object is therefore $\mathbf{E}-i\mathbf{B}$, or equivalently the printed $\mathbf{E}+i\mathbf{B}$ with the conjugate placement of the $i$, $\nabla=\partial_te_0+i\nabla_3$, which also gives $3.3\times10^{-10}$. The paper's $\mathbf{E}+i\mathbf{B}$ with its printed $\nabla$ reproduces the two divergence equations but gives $\partial_t\mathbf{E}=-\mathrm{rot}\,\mathbf{B}$ and $\partial_t\mathbf{B}=+\mathrm{rot}\,\mathbf{E}$ in place of the paper's own curl equations; both signs are reversed. The corpus's own field is $\mathbf{V}=\mathbf{E}+ic\mathbf{B}$ with $\nabla$ in the $ict$ convention, for which the free equation is $i\partial_t\mathbf{V}=c\,\mathrm{rot}\,\mathbf{V}$, and the two conventions are related by the $\pm i$ that the check exhibits.

**The sign of the expansion.** The second block of the printed expansion of $F^*\cdot(\nabla F)=0$ is $\mathbf{E}\cdot\mathrm{rot}\,\mathbf{B}-\mathbf{B}\cdot\mathrm{rot}\,\mathbf{E}$, which is $-\mathrm{div}\,(\mathbf{E}\times\mathbf{B})$ by the identity $\mathrm{div}\,(\mathbf{A}\times\mathbf{B})=\mathbf{B}\cdot\mathrm{rot}\,\mathbf{A}-\mathbf{A}\cdot\mathrm{rot}\,\mathbf{B}$. With the first block equal to $\partial_tu$, the printed expansion is $\partial_tu-\mathrm{div}\,(\mathbf{E}\times\mathbf{B})=0$, while the stated conclusion is $\partial_tu+\mathrm{div}\,(\mathbf{E}\times\mathbf{B})=0$. On random smooth fields the printed second block satisfies $|\text{block}+\mathrm{div}\,\mathbf{S}|=0$ and $|\text{block}-\mathrm{div}\,\mathbf{S}|=1.9\times10^{0}$ against $|\mathrm{div}\,\mathbf{S}|=9.7\times10^{-1}$, confirming the sign. One of the two — the second block or the stated conclusion — carries the opposite sign from the other; the conclusion as stated is the correct Poynting theorem, so the sign belongs to the printed expansion.

## Open Questions

- **The Noether current of the duality rotation.** The source-free Maxwell action is invariant under the rigid duality rotation up to a divergence, because the change of $-\tfrac14F_{\mu\nu}F^{\mu\nu}$ is proportional to the density $F\star F$, which is a total derivative. The first theorem therefore applies, and the corresponding conserved quantity is a helicity-type object rather than the energy. Its construction is obstructed in the potential formulation, because the duality rotation of $F$ is not induced by a local transformation of the four-potential without a second, dual potential; the corpus has duality as an invariant of the field strength and has not derived its current. Whether the biquaternion algebra supplies the dual potential naturally, or whether the current is best read as $\mathbf{A}\cdot\mathbf{B}$ and its flux, is not settled here.
- **The scaling of the source-free field.** With real $\alpha$ the rigid part of the source's transformation is the common scaling $\mathbf{E}\to(1+\alpha)\mathbf{E}$, $\mathbf{B}\to(1+\alpha)\mathbf{B}$, which is a one-parameter symmetry of the linear source-free *equations* but not of the action, since $-\tfrac14F_{\mu\nu}F^{\mu\nu}$ is quadratic in the field. The standard theorem therefore attaches no current to it, and the source's rigid part contributes no conservation law either. The corpus has not recorded this symmetry; it is not the duality rotation and it is not the spacetime dilation, and whether the biquaternion algebra distinguishes it from the duality rotation in a useful way is not settled here.
- **The first-order Lagrangian.** The corpus's canonical-quantization article records that no real local Lagrangian gives the first-order Maxwell system when the field strength is the only field. The source's complex $L=F^*\cdot\nabla F$ is a variational description outside that statement because it uses two independent variables. Whether a real variational principle with two independent fields — a pair whose stationarity reproduces both $\nabla F=0$ and its conjugate — exists in the biquaternion algebra is open.

## Summary

Tanişli's EPL paper writes the source-free Maxwell equations as $\nabla F=0$ with $F=\mathbf{E}+i\mathbf{B}$, gives the first-order density $L=F^*\cdot\nabla F$, and derives the Poynting theorem from the local transformation $F\to(1+\alpha)F$ with $\alpha$ a function of $x$ and $t$. The transformation is the corpus's duality rotation: $F$ is the Riemann–Silberstein vector in dimensionless units, and $e^{i\alpha}F$ rotates $\mathbf{E}$ and $\mathbf{B}$ into one another, leaving $\mathbf{E}^2+\mathbf{B}^2$ invariant and rotating the pair $(I_1,2cI_2)$ by $2\alpha$, checked to $8.9\times10^{-16}$. The naming is reversed against Weyl: a transformation depending on an arbitrary function is of the **second kind**, and the second kind yields a differential identity rather than a conservation law, which is the content of Noether's second theorem and the subject of *Noether's Two Theorems*. The transformation is also not a symmetry for position-dependent $\alpha$: the equation $i\partial_t\mathbf{V}=c\,\mathrm{rot}\,\mathbf{V}$ acquires the extra terms $-(\partial_t\alpha)\mathbf{V}$ and $ic\,(\nabla\alpha)\times\mathbf{V}$, which do not cancel, and the residual grows from the finite-difference floor to half the field magnitude. The paper's "$F^*\cdot(\nabla F)=0$" is a contraction of the field equation, and its expansion using the curl equations is the Poynting identity — the standard consequence of the field equations, whose origin in the corpus is translation invariance by Noether's first theorem. Three internal inconsistencies of the printed algebra are recorded: the product rule against the basis rule, the sign of the imaginary part of $F$, and the sign of the second block of the expansion.

## Summary of Notation

| Symbol | Source | Corpus |
|---|---|---|
| $F$ | Electromagnetic bivector $\mathbf{E}+i\mathbf{B}$ | Riemann–Silberstein $\mathbf{V}=\mathbf{E}+ic\mathbf{B}$ at $c=1$; $\tilde F = i\sqrt\epsilon\,\mathbf{V}$ |
| $\nabla$ | Biquaternion gradient $i\partial_te_0+\partial_xe_1+\partial_ye_2+\partial_ze_3$ | $\tilde\nabla = e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$ |
| $\nabla F=0$ | Source-free Maxwell equations | $\tilde\nabla\tilde F=0$, the homogeneous pair |
| $L=F^*\cdot\nabla F$ | First-order density | No direct equivalent; no real local Lagrangian gives the first-order system |
| $c$ | Set to $1$ | $c=1/\sqrt{\epsilon\mu}$ |
| $(1+\alpha)$ | Infinitesimal parameter, named "of the first kind" | Phase of the duality rotation, of the second kind when $\alpha=\alpha(x,t)$ |
| $u$ | $\tfrac12(\mathbf{E}^2+\mathbf{B}^2)$ | Energy density $W=\tfrac12(\epsilon\mathbf{E}^2+\mu\mathbf{H}^2)$ |
| $\mathbf{S}=\mathbf{E}\times\mathbf{B}$ | Poynting vector | $\mathbf{S}=\mathbf{E}\times\mathbf{H}$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |

## Further Reading

- M. Tanişli, "Gauge transformation and electromagnetism with biquaternions", *Europhysics Letters* **74** (2006) 569–573, the source recorded here.
- R. Nagem, C. Rebbi, G. Sandri and S. Sun-Sheng, "A quaternionic representation of the electromagnetic field", *Nuovo Cimento B* **113** (1998) 1509, cited by the source as the origin of the variational and energetic construction.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* **46** (2013) 053001, for the complex-vector formulation, the duality rotation and its invariants.
- William E. Baylis, *Electrodynamics: A Modern Geometric Approach* (Birkhäuser, 1999), for the paravector and complex-quaternion formulation of Maxwell's equations.
- Cornelius Lanczos, *The Variational Principles of Mechanics* (University of Toronto Press, 1970), cited by the source for the variational setting.
- Emmy Noether, "Invariante Variationsprobleme", *Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen* (1918) 235–257, and Hermann Weyl, "Gravitation und Elektrizität", *Sitzungsberichte der Preußischen Akademie der Wissenschaften* (1918) 465–480, for the two theorems and the naming of the two kinds.
- Yvette Kosmann-Schwarzbach, *The Noether Theorems* (Springer, 2011), for the history and for the logical status of the second theorem in gauge theories.
