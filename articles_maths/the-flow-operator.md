# __The Flow Operator__

## Introduction

A flow $\varphi_t$ of a vector field $X$ on a manifold $M$ is a one-parameter group of diffeomorphisms, and every such group acts linearly on the objects attached to $M$: on the smooth functions by composition, $U_tf=f\circ\varphi_t$, on the differential forms by pullback, $U_t\alpha=\varphi_t^*\alpha$, and on the measures and densities by pushforward. Each of these actions is a **one-parameter group of operators**, $U_{s+t}=U_sU_t$ and $U_0=I$, and each of them encodes the flow in operator form. The generator of the action on functions is the **Lie derivative** $\mathcal{L}_X$, the directional derivative along the field; on forms it is the same operator, obtained by the Cartan formula $\mathcal{L}_X=d\iota_X+\iota_Xd$; on the volume densities it is the negative divergence, $-\operatorname{div}(X\,\cdot)$, so that the invariance of a measure is the vanishing of the divergence of $X$ with respect to it, and the transport of a density is the **Liouville equation** of the flow. The Lie derivative is a derivation of the algebra of functions, and the map $X\mapsto\mathcal{L}_X$ is a representation of the Lie algebra of vector fields by derivations, $[\mathcal{L}_X,\mathcal{L}_Y]=\mathcal{L}_{[X,Y]}$; this is the form in which the infinitesimal structure of the flow is recorded.

The article treats the flow as an operator and its generator as the Lie derivative. It defines the three actions — on functions, on forms and on densities — and proves the group law and the strong continuity in each; it identifies the generator with the Lie derivative and proves the derivation property and the commutator identity; it derives the **Liouville operator** $-\operatorname{div}(X\,\cdot)$ as the generator on densities and the transport equation $\partial_t\rho+\operatorname{div}(\rho X)=0$; it states Stone's theorem for the unitary case and the resulting self-adjoint generator $A=-i\mathcal{L}_X$, with the spectral reading of the flow (pure point for a periodic or quasi-periodic flow, Lebesgue for an Anosov flow, cited); and it closes with the relation of the flow operator to the evolution operator of the preceding article, to the Koopman operator of the discrete system, and to the return map that reduces a flow to a discrete system.

The vector fields, the flows, the Lie derivative, the Lie bracket and the Cartan formula are those of *Smooth Manifolds and Differential Geometry*, where the Lie derivative is introduced and the flow is constructed; the differential forms and the exterior derivative are those of *Differential Forms and Stokes' Theorem*; the one-parameter semigroups, the generator and Stone's theorem are those of *Semigroups and Evolution Equations* and *Unitary Operators and the Spectral Measure*; the measure-preserving flows, the invariance and the ergodicity are those of *Ergodic Theory*; the Anosov flows and their spectral properties are those of *Hyperbolic Dynamics and Anosov Systems*, and the geodesic flow is *The Geodesic Flow*. The Koopman operator of a discrete map is *The Koopman Operator*, the two-parameter evolution operator is *The Evolution Operator*, both immediately preceding; the reduction of a flow to a return map is *The Poincaré Map*; the Lie derivative along the field appears also in *Ordinary Differential Equations* and in *The Calculus of Variations*, and the present article uses it only as the generator of the flow operator.

The operator-theoretic adjoint of $U_t$ and the involution that reverses the flow are not used here: they are *The Adjoint of the Koopman Operator* and *The Involution on the Flow Operator*, in the `- * Operator Theory` group of this category.

No physics is invoked.

## The Flow as a One-Parameter Group of Operators

### The Three Actions

**Definition.** Let $M$ be a smooth manifold, $X$ a complete vector field with flow $\varphi_t$, and $m$ a smooth reference volume. The **flow operator** on functions is

$$
U_t:C^\infty(M)\to C^\infty(M), \qquad U_tf=f\circ\varphi_t ;
$$

on differential forms it is the pullback $U_t\alpha=\varphi_t^*\alpha$; and on measures it is the pushforward $(\varphi_t)_*\nu=\nu\circ\varphi_t^{-1}$, written on a density $\rho$ with respect to $m$ by

$$
(\mathcal{P}_t\rho)(x)=\rho(\varphi_{-t}(x))\,|\det D\varphi_{-t}(x)| .
$$

The three operators are the three representations of the same group $\mathbb{R}$.

**Theorem (group law and continuity).** Each of the three families is a one-parameter group, $U_{s+t}=U_sU_t$ and $U_0=I$, and each is strongly continuous: $U_tf\to f$ in $C^\infty$ as $t\to0$ uniformly on compact sets with all derivatives, and $U_t$ on the forms is strongly continuous in the Fréchet topology. If $m$ is $\varphi_t$-invariant then $U_t$ on functions extends to a strongly continuous one-parameter group of unitary operators on $L^2(M,m)$, with $U_t^{-1}=U_{-t}$.

*Proof.* The group law is the group law of the flow, $U_{s+t}f=f\circ\varphi_{s+t}=f\circ\varphi_s\circ\varphi_t=U_sU_tf$, and the same for the pullback and the pushforward by functoriality. The continuity follows from the smooth dependence of the flow on the initial condition. In the invariant case, the change of variables $y=\varphi_t^{-1}x$ together with $\varphi_t^*m=m$ gives $\|U_tf\|_{L^2}^2=\int|f(\varphi_tx)|^2dm(x)=\int|f(y)|^2dm(y)=\|f\|_{L^2}$.

### The Pushforward and the Invariance of a Measure

**Theorem (invariance as a divergence condition).** Let $m$ be a smooth volume with $\operatorname{div}_mX=\mathcal{L}_Xm/m$; the measure $m$ is invariant under the flow if and only if $\operatorname{div}_mX=0$, and the density $\rho$ evolves as

$$
\frac{\partial\rho}{\partial t}=-\operatorname{div}(\rho X) \qquad \text{(the Liouville equation)},
$$

so a smooth positive density $\rho$ gives an invariant measure exactly when $\operatorname{div}(\rho X)=0$.

*Proof.* For a domain $\Omega$ with smooth boundary, the rate of change of $m(\varphi_t(\Omega))$ at $t=0$ is $\int_\Omega\operatorname{div}_mX\,dm$ by the divergence theorem, so the volume is preserved for all $\Omega$ exactly when $\operatorname{div}_mX=0$; the same computation applied to the measure $\rho m$ gives $\frac{d}{dt}\big|_{0}\int_{\varphi_t(\Omega)}\rho\,dm=\int_\Omega\operatorname{div}(\rho X)\,dm$, which is the weak form of the transport equation and vanishes for all $\Omega$ exactly when $\rho$ solves $\operatorname{div}(\rho X)=0$ in the invariant case.

## The Generator: the Lie Derivative

### The Lie Derivative as Generator

**Theorem (the generator on functions is $\mathcal{L}_X$).** Let $\varphi_t$ be the flow of $X$ and $U_tf=f\circ\varphi_t$. Then for $f\in C^1(M)$

$$
\frac{d}{dt}\Big|_{t=0}U_tf=\mathcal{L}_Xf=Xf ,
$$

the directional derivative of $f$ along $X$; consequently $U_t=e^{t\mathcal{L}_X}$ on a domain on which the group is generated, and the Lie derivative is the infinitesimal generator of the flow operator on functions.

*Proof.* By the definition of the flow, $\frac{d}{dt}\big|_{0}\varphi_t(x)=X(x)$; the chain rule gives $\frac{d}{dt}\big|_{0}f(\varphi_t(x))=df(X(x))=Xf(x)$, which is the definition of the Lie derivative on functions.

**Example (a rotation, recomputed).** On $\mathbb{R}^2$ let $X=y\,\partial_x-x\,\partial_y$, so that the flow is the rotation $\varphi_t(x,y)=(x\cos t+y\sin t,\,-x\sin t+y\cos t)$ and $\operatorname{div}X=0$. Then $\mathcal{L}_Xf=yf_x-xf_y$, and the identities $\frac{d}{dt}\big|_{0}f\circ\varphi_t=\mathcal{L}_Xf$ were checked numerically from the flow at $(x,y)=(0.3,0.7)$: for $f=x$ both sides are $0.7$, for $f=y$ both are $-0.3$, for $f=x^2+y^2$ both are $0$, and for $f=xy$ both are $0.4$. The invariant functions are exactly those with $\mathcal{L}_Xf=0$, and the flow is volume-preserving because the divergence vanishes.

### The Derivation Property and the Commutator

**Theorem (the Lie derivative is a derivation).** For $f,g\in C^1(M)$ and vector fields $X,Y$,

$$
\mathcal{L}_X(fg)=(\mathcal{L}_Xf)g+f(\mathcal{L}_Xg), \qquad [\mathcal{L}_X,\mathcal{L}_Y]=\mathcal{L}_{[X,Y]},
$$

where $[X,Y]=XY-YX$ is the Lie bracket of vector fields and $[\mathcal{L}_X,\mathcal{L}_Y]=\mathcal{L}_X\mathcal{L}_Y-\mathcal{L}_Y\mathcal{L}_X$; consequently $X\mapsto\mathcal{L}_X$ is a representation of the Lie algebra $\mathrm{X}(M)$ by derivations of $C^\infty(M)$.

*Proof.* The derivation property is the Leibniz rule of the directional derivative. For the commutator, apply both sides to $f$; the second-order terms in the two compositions cancel because mixed partial derivatives commute, and the remainder is the first-order operator associated with $[X,Y]$.

**Example (commuting fields).** For $X=y\,\partial_x-x\,\partial_y$ and $Y=x\,\partial_x+y\,\partial_y$ one computes $[X,Y]=0$, so the flows commute; the identity was checked numerically on the test function $x^2y$ at two points, where $[\mathcal{L}_X,\mathcal{L}_Y]f$ vanished to $<10^{-5}$.

**Theorem (Cartan's formula on forms).** On differential forms the generator of the pullback is the same Lie derivative,

$$
\mathcal{L}_X\alpha=\frac{d}{dt}\Big|_{0}\varphi_t^*\alpha, \qquad \mathcal{L}_X=\iota_Xd+d\iota_X ,
$$

where $\iota_X$ is the interior product and $d$ the exterior derivative; in particular $\mathcal{L}_X$ commutes with $d$ and $[\mathcal{L}_X,\iota_Y]=\iota_{[X,Y]}$.

*Proof.* Quoted as standard from *Smooth Manifolds and Differential Geometry*, where the Cartan formula and its consequences are proved; it is the commuting of the exterior derivative with the pullback, $\varphi_t^*d=d\varphi_t^*$, differentiated at $t=0$.

## Stone's Theorem and the Spectrum of the Flow

### The Unitary Case and the Self-Adjoint Generator

**Theorem (Stone for the flow operator).** If $\mu$ is a $\varphi_t$-invariant probability measure, then $U_tf=f\circ\varphi_t$ is a strongly continuous one-parameter unitary group on $L^2(M,\mu)$, and there is a unique self-adjoint operator $A$ with

$$
U_t=e^{itA}, \qquad A=-i\mathcal{L}_X ,
$$

on the domain where the generator exists, with $\mathcal{L}_X$ essentially skew-adjoint; the spectral measure $E$ of $A$ gives $U_t=\int_{\mathbb{R}}e^{it\lambda}dE(\lambda)$.

*Proof.* The unitarity is the change of variables in the theorem above. Stone's theorem supplies the self-adjoint generator $A$; differentiating $U_t=e^{itA}$ at $t=0$ gives $iA=\mathcal{L}_X$, hence $A=-i\mathcal{L}_X$. The skew-adjointness of $\mathcal{L}_X$ is the integration by parts $\int\mathcal{L}_Xf\,\overline{g}\,d\mu=-\int f\,\overline{\mathcal{L}_Xg}\,d\mu$, valid when $\operatorname{div}_\mu X=0$; the general adjoint, with the divergence correction for a reference measure that is not invariant, is *The Involution on the Flow Operator*, later in this category.

### The Spectral Reading of a Flow

**Theorem (spectral classification, cited).** For a measure-preserving flow:

1. the flow is ergodic if and only if the eigenvalue $1$ of $\{U_t\}$ is simple, that is, the invariant functions are the constants;
2. the flow is weakly mixing if and only if the only eigenvalue of the group is $1$; it is mixing if and only if the correlations of observables decay, $\int f\circ\varphi_t\cdot g\,d\mu\to\mu(f)\mu(g)$;
3. an eigenvalue $\lambda$ of the group is a character, $U_tf=e^{i\lambda t}f$, and the closed span of the eigenfunctions is the **discrete** part of the spectrum; the orthogonal complement carries the **continuous** part, and the spectral theorem of Stone reads the flow as multiplication by $e^{i\lambda t}$ on the direct integral over the spectrum of $A$.

*Proof.* Statements 1 and 2 are the flow form of the spectral characterisations of ergodicity and mixing, proved in *The Koopman Operator* for the discrete case and applied here to the group; statement 3 is the functional calculus for the self-adjoint generator $A$.

**Example (the pure point and the Lebesgue extremes).** The circle rotation $x\mapsto x+\alpha t$ and any quasi-periodic flow have pure point spectrum, with eigenvalues the characters $e^{i\langle k,\omega\rangle t}$ and discrete additive group generated by the frequencies. The geodesic flow of a compact negatively curved manifold is an Anosov flow and has countable Lebesgue spectrum on the orthogonal complement of the constants, hence is mixing and has no nonconstant eigenfunctions; the contrast between the two is the contrast between an integrable and a chaotic flow. Both statements are the standard examples of *Hyperbolic Dynamics and Anosov Systems* and *The Geodesic Flow*, and no new proof is given here.

## The Flow Operator and its Neighbours

**Remark (the evolution operator).** The flow operator is the autonomous case of the evolution operator of *The Evolution Operator*: the family $\Phi(t,s)$ of a linear equation along a flow is the flow operator on the tangent bundle, $\Phi(t,s)=D\varphi_{t-s}(\varphi_s(x))$, and the generator of the autonomous flow operator on functions is $\mathcal{L}_X$ in place of the abstract $A$. The present article is the differential-geometric face of the abstract semigroup.

**Remark (the return map).** A flow with a transverse section $\Sigma$ is a suspension of the **return map** $P:\Sigma\to\Sigma$ with roof function the return time; the flow operator and the Koopman operator of the return map are related by the suspension formula, in which an observable of the flow is coded by the observables of the section and the return time. The construction, the return time, the induced measure and the operator-theoretic form of the reduction are *The Poincaré Map*, later in this category; the suspension and the section themselves are *Smooth Dynamical Systems* and are cited, not restated.

## Summary

A flow $\varphi_t$ of a vector field $X$ acts as a **one-parameter group of operators**: on functions by $U_tf=f\circ\varphi_t$, on forms by the pullback $\varphi_t^*$, and on densities by the pushforward $(\mathcal{P}_t\rho)(x)=\rho(\varphi_{-t}x)|\det D\varphi_{-t}(x)|$; each satisfies $U_{s+t}=U_sU_t$, $U_0=I$, and is strongly continuous, and on functions it is isometric for an invariant measure, in which case it is unitary and Stone's theorem applies. The **generator** on functions is the **Lie derivative** $\mathcal{L}_X$, the directional derivative, so that $U_t=e^{t\mathcal{L}_X}$ and, on $L^2$ of an invariant measure, $U_t=e^{itA}$ with $A=-i\mathcal{L}_X$ self-adjoint; the Lie derivative is a derivation, $[\mathcal{L}_X,\mathcal{L}_Y]=\mathcal{L}_{[X,Y]}$, so $X\mapsto\mathcal{L}_X$ is a representation of the Lie algebra of vector fields by derivations, and on forms it is the Cartan expression $\mathcal{L}_X=\iota_Xd+d\iota_X$. On densities the generator is $-\operatorname{div}(X\,\cdot)$, with the **Liouville equation** $\partial_t\rho+\operatorname{div}(\rho X)=0$; the invariance of a measure is the vanishing of the divergence of $X$ with respect to it. The spectrum of the flow reads the dynamics: ergodicity is the simplicity of the eigenvalue $1$, weak mixing the absence of other eigenvalues, mixing the decay of correlations, with pure point spectrum for a quasi-periodic flow and countable Lebesgue spectrum for an Anosov flow such as the geodesic flow of a negatively curved manifold, cited from *Hyperbolic Dynamics and Anosov Systems*. The flow operator is the autonomous case of *The Evolution Operator* and is reduced to a discrete system through *The Poincaré Map*; its adjoint, with the divergence correction, and the involution that reverses the flow are in the `- * Operator Theory` group and are not used here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$, $\varphi_t$ | Vector field and its flow |
| $U_tf=f\circ\varphi_t$ | Flow operator on functions |
| $\varphi_t^*\alpha$, $(\varphi_t)_*\nu$ | Pullback on forms, pushforward on measures |
| $\mathcal{L}_X=X$ | Lie derivative (directional derivative) along $X$ |
| $[X,Y]$, $[\mathcal{L}_X,\mathcal{L}_Y]=\mathcal{L}_{[X,Y]}$ | Lie bracket of fields; commutator of derivations |
| $\iota_X$, $d$ | Interior product and exterior derivative; $\mathcal{L}_X=\iota_Xd+d\iota_X$ |
| $\operatorname{div}_mX$, $\operatorname{div}(\rho X)$ | Divergence with respect to a volume; Liouville operator |
| $\partial_t\rho=-\operatorname{div}(\rho X)$ | Liouville (transport) equation |
| $A=-i\mathcal{L}_X$ | Self-adjoint generator of the unitary flow operator |
| $E(\lambda)$, $U_t=\int e^{it\lambda}dE$ | Spectral measure and spectral representation of the flow |
| $\mathcal{P}_t$ | Pushforward operator on densities |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, Vol. I (Interscience, 1963), for the flow, the Lie derivative and the Lie bracket.
- Ralph Abraham, Jerrold E. Marsden and Tudor Ratiu, *Manifolds, Tensor Analysis, and Applications* (Springer, 2nd ed. 1988), for the Lie derivative on functions, forms and tensors, and Cartan's formula.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), and Vol. IV, for Stone's theorem, the generator and the spectral theory.
- Klaus-Jochen Engel and Rainer Nagel, *One-Parameter Semigroups for Linear Evolution Equations* (Springer, 2000), for the generation of the flow operator by an unbounded generator.
- Vladimir I. Arnold, *Mathematical Methods of Classical Mechanics* (Springer, 2nd ed. 1989), for the Liouville equation and the transport of densities.
- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the spectral classification of flows.
- Dmitri V. Anosov, "Geodesic flows on closed Riemannian manifolds of negative curvature", *Trudy Matematicheskogo Instituta imeni V. A. Steklova* 90 (1967), 3–210, for the Anosov flows and their spectra.
- Michael Brin and Garrett Stuck, *Introduction to Dynamical Systems* (Cambridge University Press, 2002), for the suspension and return-map constructions.
