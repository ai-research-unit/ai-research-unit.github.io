# __The Lagrangian and the Non-Abelian Connections__

## Introduction

This article writes the non-abelian connection as the extremum of the Yang–Mills action inside the material sector, and shows that the trace which makes the action invariant is a matrix trace and not the corpus's informational pairing. It is the action-first companion of *Non-Abelian Connections in Biquaternionic Form*, which builds the connection, the covariant derivative and the field strength; this article asks what functional has the Yang–Mills equation as its stationary condition, and which pairing is the one that makes it invariant.

The equation. The parent's equation is the Yang–Mills equation without sources,

$$
D_{\imath} F_{\imath\jmath}=0 ,
\qquad
D_{\imath}=\frac{\partial}{\partial R_{\imath}}+[A_{\imath},\cdot\,],
\qquad
F_{\imath\jmath}=\frac{\partial A_{\jmath}}{\partial R_{\imath}}-\frac{\partial A_{\imath}}{\partial R_{\jmath}}+[A_{\imath},A_{\jmath}] ,
$$

with both the connection and the field strength valued in the $\mathrm{SU}(2)$ factor of the algebra. The article asks what action has this equation as its stationarity condition.

Three things are established.

*First, the action.* With $\mathrm{Tr}$ the matrix trace on $\mathbb{B}\cong M_2(\mathbb{C})$ restricted to the $\mathrm{SU}(2)$ factor,

$$
S_{\mathrm{YM}}=-\frac12\int d^4r\;\mathrm{Tr}\Bigl(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\Bigr),
$$

the stationarity condition is $D_{\imath} F_{\imath\jmath}=0$. The coefficient $\tfrac12$ and the sign are the standard ones once the generators are normalized so that $-4\,\mathrm{Sc}(T_aT_b)=\delta_{ab}$.

*Second, the trace is not the corpus's pairing.* The invariance of the density needs $\mathrm{Tr}(\tilde QF\tilde Q^{-1}\tilde QF\tilde Q^{-1})=\mathrm{Tr}(FF)$, which is the cyclicity of the matrix trace. The corpus's informational reduction $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ is a different functional, and it does not have that property. Using it would give an action that is not invariant, and the distinction is the sharpest technical point of this article. The requirement itself, stated before any sector uses it, is in [The Invariant Density: Which Pairing the Action Can Integrate](the-invariant-density-which-pairing-the-action-can-integrate.html), which also fixes the sign against the Hermiticity of the generators.

*Third, the action reaches $\mathrm{SU}(2)$ and stops.* The algebra's compact group is $\mathrm{U}(2)$, so the construction gives a Yang–Mills theory for $\mathrm{SU}(2)$ and for its abelian factor, and it gives none for $\mathrm{SU}(3)$. The action's existence is therefore a statement about the algebra's ceiling, and the ceiling article is its continuation.

What is not new. The Yang–Mills action is standard, and its derivation is a page of any textbook. What the corpus contributes is the identification of the connection with an algebra-valued one-form in the material sector, the trace-versus-pairing distinction, and the ceiling statement.

## Conventions

The conventions are restated here so that every sign below is checkable from this page. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with $e_t=1$ and $\vec e_{\imath}^{2}=-e_t$; the material sector is $\mathbb{B}_\Phi$; the $\mathrm{SU}(2)$ factor is spanned by the anti-Hermitian generators $T_a$, $a=1,2,3$.

The two traces. $\mathrm{Tr}$ is the matrix trace on $\mathbb{B}\cong M_2(\mathbb{C})$; $\mathrm{Sc}$ is the coefficient of $e_t$ in the element; and $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ is the corpus's informational reduction, which is not used in this article's action and is the subject of the reality section.

The connection and the curvature. $A_{\imath}\in\mathfrak{su}(2)\subset\mathbb{B}_\Phi$, anti-Hermitian, with $A_{\imath}=A_{a,\imath} T_a$; $F_{\imath\jmath}=\partial_{\imath} A_{\jmath}-\partial_{\jmath} A_{\imath}+[A_{\imath},A_{\jmath}]$, also anti-Hermitian and in $\mathfrak{su}(2)$.

The normalization. $-4\,\mathrm{Sc}(T_aT_b)=\delta_{ab}$, so that $T_a=-\tfrac{i}{2}\sigma_a$ in the fundamental representation. With that normalization the coefficient of the action is $\tfrac12$ and the coupling is the one that appears in the covariant derivative.

The sign convention. The action enters with $-\tfrac12$, so that the energy is positive for the corpus's sign rule; the opposite sign would give a theory whose energy is unbounded below.

## The Action in Element Form

The action and its invariance. The density is the trace of the curvature's square,

$$
\mathcal{L}=-\frac12\,\mathrm{Tr}\Bigl(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\Bigr),
\qquad
S_{\mathrm{YM}}=\int d^4r\;\mathcal{L},
$$

and its invariance under $A_{\imath}\mapsto \tilde Q A_{\imath}\tilde Q^{-1}+\tilde Q\partial_{\imath}\tilde Q^{-1}$ follows from the curvature's transformation $F_{\imath\jmath}\mapsto\tilde QF_{\imath\jmath}\tilde Q^{-1}$ and the cyclicity of the trace. The verification is one line:

$$
\mathrm{Tr}\Bigl(\sum_{\imath,\jmath}F_{\mathrm g,\imath\jmath}F_{\mathrm g,\imath\jmath}\Bigr)=\mathrm{Tr}\Bigl(\sum_{\imath,\jmath}\tilde QF_{\imath\jmath}\tilde Q^{-1}\tilde QF_{\imath\jmath}\tilde Q^{-1}\Bigr)=\mathrm{Tr}\Bigl(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\Bigr).
$$

Why the quadratic invariant and not another. At dimension four the only invariant built from the curvature alone is its square; a cubic term does not exist because the trace of an odd number of generators vanishes, and a term with derivatives of the curvature has dimension five. The action is therefore the unique one at this order, and its coefficient is fixed by the normalization of the generators and by no other choice.

Why the commutator term makes the theory interacting. In the abelian case $F_{\imath\jmath}=\partial_{\imath} A_{\jmath}-\partial_{\jmath} A_{\imath}$ is linear in the potential and the action is quadratic. Here the commutator makes $F$ quadratic in $A$, so the action contains cubic and quartic terms, and those terms are the connection's self-coupling. Nothing was added: the self-coupling is the square of a curvature that is itself nonlinear, and that nonlinearity is the statement that the symmetry group is non-abelian.

The components. Expanding in generators gives

$$
\mathcal{L}=-\frac14\sum_{a,\imath,\jmath}F_{a,\imath\jmath}F_{a,\imath\jmath},
\qquad
F_{a,\imath\jmath}=\partial_{\imath} A_{a,\jmath}-\partial_{\jmath} A_{a,\imath}+g\sum_{b,c}\varepsilon_{abc}A_{b,\imath} A_{c,\jmath} ,
$$

which is the standard form, with $g$ absorbed into the normalization of $A_{a,\imath}$. The two forms are the same action; the element form makes the invariance one line and the component form makes the vertices explicit.

The pairing. The pairing is the matrix trace, and it is not the informational reduction. $\mathrm{Tr}(\tilde Q_1\tilde Q_2)$ on $\mathbb{B}\cong M_2(\mathbb{C})$ is a bilinear form invariant under $\tilde Q_1\mapsto\tilde Q\tilde Q_1\tilde Q^{-1}$, $\tilde Q_2\mapsto\tilde Q\tilde Q_2\tilde Q^{-1}$; the corpus's reduction $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ is a different functional, and it is not invariant under that pair of transformations.

Why the difference matters. If the action used the reduction, its density would change under a local transformation and the theory would not be a connection theory. The action works because of the trace's cyclicity, and the reduction does not have it. The two agree only in special cases — when one of the factors is a scalar — and the field strength is not a scalar.

The reality of the trace. For anti-Hermitian $F_{\imath\jmath}$, $\mathrm{Tr}(F_{\imath\jmath}F_{\imath\jmath})$ is real and non-positive, so $-\tfrac12\mathrm{Tr}(FF)$ is real and non-negative. The reality follows from the anti-Hermiticity and not from an extra condition, and the positivity is what makes the energy bounded below.

The type of the coefficient. One dimensionless coupling, and its place is in the commutator. With the generators normalized as above the coefficient of the action is $\tfrac12$ and the coupling $g$ sits in $F_{\imath\jmath}$'s commutator term. Rescaling $A_{\imath}\to A_{\imath}/g$ moves $g$ into the action's overall coefficient as $1/g^2$, and the two placements are the same theory.

Why the coupling cannot be removed. In the abelian case the coupling multiplies the whole action and cancels from the equation; here it does not, because the commutator term has one power of $g$ and the derivative term has none. The ratio of the two is physical, and it is the coupling. That is the sharpest structural difference between the abelian and non-abelian cases, and it is why the non-abelian theory has a running coupling and the abelian one has a free one.

The selection rule. The selection rule is local $\mathrm{SU}(2)$ invariance and dimension four, and they leave exactly one term. The invariant must be built from $F_{\imath\jmath}$ alone, must be a scalar under the trace, and must have dimension four. The square is the only candidate, and its coefficient is fixed by the normalization.

**What reality does not buy. Reality does not buy $\mathrm{SU}(3)$, asymptotic freedom, or a mass gap.** Three things the reality of the action does not supply:

- *No colour.* The algebra carries $\mathrm{SU}(2)$ and the action is $\mathrm{SU}(2)$'s; $\mathrm{SU}(3)$ is outside and the QCD article transcribes it.
- *No running from the classical action.* The beta function is a one-loop object, and the classical action says nothing about it.
- *No mass gap.* Whether the quantum theory has one is a non-perturbative question, and the classical action is silent.

### The Two Settings

The element setting. The action written as $-\tfrac12\mathrm{Tr}(FF)$ with $F$ an element of $\mathfrak{su}(2)\subset\mathbb{B}$. The invariance is one line, and the trace-versus-pairing distinction is visible.

The component setting. The action written as $-\tfrac14\sum_aF_{a,\imath\jmath}F_{a,\imath\jmath}$ with the structure constants explicit. The vertices are visible, and the coupling's place in the commutator is visible.

Why the two settings are not a choice of notation. They differ in what they display and in what they hide. The element form makes the local invariance obvious and the vertices obscure; the component form does the reverse. A reader who knows only one has a partial view of the same object, and the corpus uses both deliberately.

What the comparison shows. The passage between the two is the passage between the trace and the structure constants, and the identity that connects them is $-4\,\mathrm{Sc}(T_aT_b)=\delta_{ab}$ together with $[T_a,T_b]=\sum_c\varepsilon_{abc}T_c$. The two settings are one action read two ways, and the normalization is what makes the readings agree.

## The Variation: The Yang–Mills Equation from the Curvature's Square

The variation. Vary $A_{\imath}\mapsto A_{\imath}+\delta A_{\imath}$ with $\delta A_{\imath}$ in $\mathfrak{su}(2)$ and vanishing at the boundary. The curvature's variation is the covariant derivative of the variation,

$$
\delta F_{\imath\jmath}=D_{\imath}\delta A_{\jmath}-D_{\jmath}\delta A_{\imath} ,
$$

which is the statement that the curvature is a tensor and its variation is a tensor.

The variation of the action. Substituting and integrating by parts,

$$
\delta S=-\int d^4r\;\mathrm{Tr}\Bigl(\sum_{\imath,\jmath}\delta F_{\imath\jmath}F_{\imath\jmath}\Bigr)
=2\int d^4r\;\mathrm{Tr}\Bigl(\sum_{\imath}\delta A_{\imath}\,D_{\jmath} F_{\imath\jmath}\Bigr),
$$

where the antisymmetry of $F$ and the cyclicity of the trace give the factor two, and the boundary term vanishes because $\delta A_{\imath}$ does. Stationarity for every $\delta A_{\imath}$ gives

$$
\boxed{\;D_{\imath} F_{\imath\jmath}=0\;}
$$

which is the parent's equation. The covariant derivative in it is the same object that appeared in the curvature's variation, and that coincidence is the statement that the equation is covariant.

Why the equation is not invariant and the action is. $F_{\imath\jmath}$ transforms homogeneously, so $D_{\imath} F_{\imath\jmath}$ does too, and the equation is covariant; the action is invariant because the trace is cyclic. The difference between covariance and invariance is the difference between the field strength's transformation and the trace's, and both are needed: the action must be invariant to be a number, and the equation must be covariant to be consistent.

**The Bianchi identity, and why it is not the equation.** $D_{\imath} F_{\imath\jmath}+D_{\imath} F_{\jmath k}+D_{\jmath} F_{k\imath}=0$ holds identically for any $A_{\imath}$, because the curvature is a commutator. It is not the equation of motion; it is the integrability condition, and the two are related as the Jacobi identity is related to the structure constants. The equation is the statement that the theory is on shell; the identity is the statement that the curvature exists.

## The Constraints the Action Imposes: Gauss's Law and Two Polarizations

The constraint. The time component of the equation is not an evolution equation but a constraint,

$$
D_j F_{j0}=0 ,
$$

the non-abelian Gauss law, which is first class because the local symmetry is unbroken. It removes one component of $A_{\imath}$ per generator, and the residual redundancy removes another, leaving two physical polarizations per generator.

The count. Four components per generator, minus two, gives two; times three generators gives six physical modes for the $\mathrm{SU}(2)$ field. The counting is the same as in the abelian case per generator, and the difference is that the constraint is now non-linear in the potential.

Why the constraint is non-linear and what that means. $D_jF_{j0}=\partial_jF_{j0}+[A_j,F_{j0}]$ contains the potential, so the Gauss law is a differential equation for $A_0$ with the spatial fields as sources. In the abelian case it is a Poisson equation; here it is a non-linear one, and that non-linearity is the technical content of "the connection carries charge".

The consequence for the canonical treatment. The constraint's non-linearity is why the non-abelian theory's canonical quantisation is not a free-field construction, and why the path-integral treatment with the Faddeev–Popov determinant is the corpus's route. That determinant is field dependent here and field independent in the abelian case, which is the difference the fixing the representative articles record.

## The Structural Consequence: The Ceiling Is in the Algebra and Not in the Action

The statement. The construction works for any subgroup of the algebra's compact group $\mathrm{U}(2)$. It gives $\mathrm{U}(1)$ and $\mathrm{SU}(2)$ exactly, and it gives nothing for $\mathrm{SU}(3)$.

**Why the ceiling is algebraic.** A connection valued in $\mathfrak{su}(3)$ needs three independent anti-Hermitian generators with the $\mathrm{SU}(3)$ commutators, and the algebra's compact part has only four real dimensions. The action's form is not the obstruction; the carrier is. A Yang–Mills action for $\mathrm{SU}(3)$ can be written in components, and the QCD article does write it, but it is not an action on the algebra's own elements.

The consequence for the corpus's four sectors. The electromagnetic and weak sectors have actions on the algebra's elements, with the weak one partial; the strong sector has an action only in components; and gravity has a quadratic action without a carrier. The ceiling is what makes those four statuses different, and the sector hub records the comparison.

What the structure predicts. That the non-abelian sector's local invariance is exact for $\mathrm{SU}(2)$, that the coupling runs, and that no colour can be derived. All three are recorded elsewhere and all three follow from the algebra's dimension.

## The Noether Currents: The Colour Current and Its Own Source

The current. The action's invariance under the global $\mathrm{SU}(2)$ gives the current

$$
j_{a,\imath}=\sum_{b,c}\varepsilon_{abc}F_{b,\imath\jmath}A_{c,\jmath} ,
$$

which is the standard non-abelian current. It is conserved on shell, $D_{\imath} j_{a,\imath}=0$, and its conservation is the equation of motion contracted with the structure constants.

Why the current carries the field. The current is bilinear in the connection and contains $A$ explicitly, not only $F$. That is the statement that the connection carries the charge it couples to, and it is the difference from the abelian current, which contains only $F$.

Why the conservation is covariant and not ordinary. $\partial_{\imath} j_{a,\imath}=0$ fails; $D_{\imath} j_{a,\imath}=0$ holds. The ordinary divergence differs from the covariant one by a term proportional to the connection, and that term is the statement that the current is not invariant by itself.

Energy–momentum. Translation invariance gives $T_{\imath\jmath}=\mathrm{Tr}(F_{\imath k}F_{\jmath k})-\tfrac14g_{\imath\jmath}\mathrm{Tr}(F^2)$-type expression, symmetric and traceless at the classical level. The tracelessness is the classical scale invariance, and its quantum violation is the beta function.

**What there is not.** No topological current in the classical action — the $\theta$ term is a separate total derivative — and no central phase.

## What the Principle Adds and What It Relabels

Adds.

- *The invariance as a consequence of cyclicity.* The action shows why the trace and not the reduction is the right pairing, in one line.
- *The self-coupling as a consequence of the commutator.* The cubic and quartic vertices are not additions; they are the square of a nonlinear curvature.
- *The coupling's survival.* The non-abelian coupling appears in the equation because the commutator carries one power of it, and that is visible in the action.

Relabels.

- *The "non-abelian" of the theory.* It is not a modification of Maxwell's theory; it is the same construction with a curvature that does not commute with itself.
- *The self-interaction.* It is not a vertex added to the theory; it is the geometry of the symmetry group.
- *The ceiling.* It is not a limitation of the action; it is a limitation of the algebra that carries the connection.

The distinction that matters. The action is the square of a curvature, and the curvature is a commutator. Everything that distinguishes the non-abelian theory from the abelian one follows from the commutator, and the commutator is where the algebra's structure constants enter.

## Open Questions

Is the trace the only pairing that works? For the action's invariance, yes at this order: the reduction fails and the trace is the unique invariant bilinear. Whether a different invariant exists at higher order is not explored.

## Summary

The action. $S_{\mathrm{YM}}=-\tfrac12\int d^4r\,\mathrm{Tr}(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath})$ with $F$ the $\mathfrak{su}(2)$-valued curvature. The variation gives $D_{\imath} F_{\imath\jmath}=0$; the density is invariant because the matrix trace is cyclic.

The three findings. The trace is the matrix trace and not the corpus's informational reduction, and using the reduction would break the invariance. The coupling survives in the equation because the commutator carries one power of it, which is why the non-abelian coupling runs. The construction stops at the algebra's $\mathrm{U}(2)$, so $\mathrm{SU}(2)$ is exact and $\mathrm{SU}(3)$ is not reachable.

**The boundary.** The connection, the curvature and the trace are the algebra's; the symmetry group's identity as colour, the running and the mass gap are not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A_{\imath}=A_{a,\imath} T_a$ | $\mathfrak{su}(2)$-valued connection |
| $F_{\imath\jmath}$ | curvature, $\partial_{\imath} A_{\jmath}-\partial_{\jmath} A_{\imath}+[A_{\imath},A_{\jmath}]$ |
| $\mathrm{Tr}$ | matrix trace on $\mathbb{B}\cong M_2(\mathbb{C})$ |
| $2\,\mathrm{Sc}(\cdot)$ | informational reduction, not used in the action |
| $T_a$ | anti-Hermitian generators, $-4\,\mathrm{Sc}(T_aT_b)=\delta_{ab}$ |
| $g$ | coupling, in the commutator's normalization |
| $j_{a,\imath}$ | non-abelian current |

## Further Reading

- [Non-Abelian Connections in Biquaternionic Form](non-abelian-connections-in-biquaternionic-form.html) — the parent: the connection, the curvature, the Bianchi identity, the reality condition.
- [The Lagrangian and the Electromagnetic Field](the-lagrangian-and-the-electromagnetic-field.html) — the abelian case, where the coupling cancels.
- [The Lagrangian and the W and Z Bosons](the-lagrangian-and-the-w-and-z-bosons.html) — the $\mathrm{SU}(2)$ action with a scalar and masses.
- [Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) — the ceiling this article's action stops at.
- [The Lagrangian and Quantum Electrodynamics](the-lagrangian-and-quantum-electrodynamics.html) — the abelian action assembled with its matter.
