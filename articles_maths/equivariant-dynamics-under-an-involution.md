# __Equivariant Dynamics under an Involution__

## Introduction

A dynamical system has an **equivariant symmetry** when an involution of the phase space commutes with the dynamics; an invertible map $T$ is **$\mathbb{Z}/2$-equivariant** with respect to an involution $\sigma$, $\sigma^2=\mathrm{id}$, when

$$
\sigma\circ T=T\circ\sigma ,
$$

and a flow is equivariant when $\sigma\circ\varphi_t=\varphi_t\circ\sigma$ for all $t$. The involution is a genuine order-two map of the phase space, and it is not the reversal of the preceding article: a reversor makes the system conjugate to its inverse, $RTR=T^{-1}$, while an equivariant symmetry leaves the arrow of time intact and only permutes the orbits. The consequence is immediate and strong: the **fixed-point subspace** $\mathrm{Fix}(\sigma)$ is invariant under the dynamics, a point fixed by $\sigma$ is carried by $T$ to a point fixed by $\sigma$; the symmetric subsystem is thus a dynamical system in its own right, of lower dimension, embedded in the full one, and the orbit structure of the full system is the orbit structure of that subsystem together with the orbits paired by $\sigma$. The group $\mathbb{Z}/2$ acts on the state space, the space of equivariant maps is the space of fixed points of the induced action on maps, and the linear theory is the isotypic decomposition of the representation into the trivial and the sign components.

The article develops the equivariant structure. It defines the commuting involution for maps and flows and proves the invariance of the fixed-point subspace and the restriction of the dynamics to it; it establishes the **$\mathbb{Z}/2$ orbit structure**: an orbit is either contained in $\mathrm{Fix}(\sigma)$ or paired with its image, the periodic orbit of an equivariant map is either contained in $\mathrm{Fix}(\sigma)$ or carries a free $\mathbb{Z}/2$-action, and the quotient dynamics is well defined; it decomposes a linear equivariant map into its blocks on the $+1$ and the $-1$ eigenspaces and states the equivariant version of the linear theory; it gives the examples — the doubling map with its reflection, the standard map with the central involution, the even and the odd maps of the interval, and the time-one maps of $\mathbb{Z}/2$-equivariant fields; and it closes with the consequences: symmetric attractors, the symmetric subsystem as the carrier of the homoclinic structure of a symmetric equilibrium, and the fixed-point subspace principle that reduces the dimension of a symmetric problem.

The groups, the actions, the quotients and the fixed-point sets are those of *Groups and Group Actions* and *Topological Groups*; the smooth involutions, the submanifolds and the transverse theory are those of *Differential Topology*; the maps, the flows and the periodic orbits are those of *Smooth Dynamical Systems* and *Topological Dynamics*; the symmetric bifurcations are those of *Equivariant Bifurcation Theory*, and the symmetric invariant tori are those of *Invariant Tori under an Involution*, both later in the `- * Theory` group of this category. The **reversing** involution is *Reversible Dynamical Systems and Time-Reversal Symmetry*, immediately preceding, and the two must not be conflated; the involution on the operators is *Reversible Operators and the Involution*, in the `- * Operator Theory` group.

No physics is invoked.

## Equivariance and the Fixed-Point Subspace

### Definition

**Definition.** Let $X$ be a set and let $\sigma:X\to X$ be an **involution**, $\sigma^2=\mathrm{id}$. A map $T:X\to X$ is **equivariant** with respect to $\sigma$ if $\sigma\circ T=T\circ\sigma$, and an invertible equivariant map $T$ generates the group $\mathbb{Z}/2\times\mathbb{Z}$ acting on $X$ by $\sigma^mT^n$; the pair $(T,\sigma)$ is a **$\mathbb{Z}/2$-equivariant dynamical system**. For a flow $\varphi_t$ on a manifold the condition is $\sigma\circ\varphi_t=\varphi_t\circ\sigma$ for all $t$, equivalently, for the generating field, $D\sigma(X(x))=X(\sigma x)$.

**Definition.** The **fixed-point subspace** of the involution is $\mathrm{Fix}(\sigma)=\{x:\sigma x=x\}$; for a linear representation of $\mathbb{Z}/2$ the **isotypic decomposition** of a vector space $V$ on which $\sigma$ acts linearly is $V=V_+\oplus V_-$, where $V_+$ is the $+1$-eigenspace (the symmetric part) and $V_-$ the $-1$-eigenspace (the antisymmetric part).

**Theorem (the fixed-point subspace is invariant).** Let $T$ be equivariant with respect to $\sigma$ and let $x\in\mathrm{Fix}(\sigma)$. Then $T(x)\in\mathrm{Fix}(\sigma)$, so the restriction $T|_{\mathrm{Fix}(\sigma)}$ is a well-defined dynamical system, the **symmetric subsystem**; the same holds for an equivariant flow and for an equivariant vector field, whose restriction to $\mathrm{Fix}(\sigma)$ is a vector field tangent to it. More generally $\sigma$ commutes with every power $T^n$ and with the whole flow, so the fixed-point subspace is invariant under the entire group.

*Proof.* If $\sigma x=x$ then $\sigma(Tx)=T(\sigma x)=Tx$, so $Tx$ is fixed; iterating gives $T^n(\mathrm{Fix}(\sigma))\subseteq\mathrm{Fix}(\sigma)$. For a flow, differentiating the relation $\sigma\varphi_t=\varphi_t\sigma$ in $t$ gives $D\sigma(X(\varphi_tx))=X(\varphi_t\sigma x)$, and at a fixed point the field is tangent to the fixed set.

### The Orbit Structure

**Theorem (the $\mathbb{Z}/2$ orbit structure).** Let $T$ be equivariant with respect to $\sigma$ and let $x\in X$. The orbit $\mathcal{O}(x)=\{T^nx\}$ is either contained in $\mathrm{Fix}(\sigma)$ — equivalently $x\in\mathrm{Fix}(\sigma)$ — or it is disjoint from $\mathrm{Fix}(\sigma)$ and $\sigma(\mathcal{O}(x))=\mathcal{O}(\sigma x)$ is a second orbit, so that the orbits of the quotient $X/\sigma$ are the pairs $\{\mathcal{O}(x),\mathcal{O}(\sigma x)\}$ and the single orbits inside the fixed set. If $x$ is periodic of period $n$ and $\sigma x=T^jx$ for some $j$, then $2j\equiv0\pmod n$; the involution acts on the periodic orbit either as the identity (the orbit is contained in $\mathrm{Fix}(\sigma)$) or as the shift by $n/2$, so a $\sigma$-invariant periodic orbit of odd period is contained in $\mathrm{Fix}(\sigma)$, while one of even period is either symmetric or a pair of orbits exchanged by $\sigma$.

*Proof.* If $x\in\mathrm{Fix}(\sigma)$ then the orbit is fixed by $\sigma$. If $x\notin\mathrm{Fix}(\sigma)$, then $\sigma x\ne x$ and no element of the orbit of $x$ is fixed, because $\sigma(T^nx)=T^n(\sigma x)$ and $T^nx=T^n(\sigma x)$ would give $x=\sigma x$. For the periodic case, $\sigma x=T^jx$ for some $j$ because $\sigma x$ lies on the orbit of $x$; applying $\sigma$ again gives $x=\sigma^2x=T^j(\sigma x)=T^{2j}x$, so $n\mid2j$, and the two possibilities $j\equiv0$ or $j\equiv n/2$ are the dichotomy stated.

**Corollary (the symmetric subsystem carries the symmetric periodic orbits).** A periodic orbit of the equivariant map is $\sigma$-invariant exactly when it contains a point of $\mathrm{Fix}(\sigma)$, and the even $\sigma$-invariant orbits are the pairs $\{p,T^{n/2}p\}$ with $p\in\mathrm{Fix}(\sigma)$ and $T^np=p$, while a $\sigma$-invariant orbit of odd period lies in the fixed set.

## The Linear Theory

**Theorem (the isotypic block decomposition).** Let $\sigma$ act linearly on a vector space $V$, $V=V_+\oplus V_-$ the isotypic decomposition, and let $A\in\mathrm{GL}(V)$ commute with $\sigma$. Then $A$ preserves each isotypic component, $A(V_\pm)\subseteq V_\pm$, and in the splitting $A=A_+\oplus A_-$; consequently the spectrum of $A$ is the union of the spectra of the two blocks and the symmetric and antisymmetric modes do not mix under the linearised dynamics.

*Proof.* If $v\in V_+$ then $\sigma(Av)=A(\sigma v)=Av$, so $Av\in V_+$; the argument for $V_-$ is the same with the sign reversed. The block diagonal form and the spectral statement follow.

**Corollary (the derivative at a symmetric fixed point).** Let $p\in\mathrm{Fix}(\sigma)$ be a fixed point of an equivariant diffeomorphism $T$, so that $D\sigma(p)$ and $D_pT$ commute. Then $T_pM$ splits into the symmetric and the antisymmetric subspaces of $D\sigma(p)$, the derivative preserves the splitting, and the stability of $p$ is the union of the stabilities of the two blocks; one of the modes is tangent to the fixed-point submanifold and the other is transverse to it, and the transverse block governs the motion off the symmetric subsystem.

## The Examples

**Example (the doubling map and the reflection, verified).** On the circle $\mathbb{T}=\mathbb{R}/\mathbb{Z}$ let $T x=2x\bmod1$ and $\sigma x=-x\bmod1$. Then $\sigma$ is an involution and $T\circ\sigma=\sigma\circ T$; the identity was checked numerically at three points to $10^{-16}$. The fixed set is $\mathrm{Fix}(\sigma)=\{0,\tfrac12\}$, a two-point set invariant under $T$, with $T(0)=0$ and $T(\tfrac12)=0$; the symmetric subsystem consists of the two fixed points collapsed by the doubling, while the rest of the circle is paired into $\{x,-x\}$ with the same orbit structure. The example shows that the fixed-point subspace may be as small as a finite set and still determine the symmetric part of the dynamics.

**Example (the standard map and the central involution, verified).** For the standard map $S(\theta,I)=(\theta+I+k\sin\theta,\,I+k\sin\theta)$ on the cylinder, the **central involution** $\Sigma(\theta,I)=(-\theta,-I)$ is an involution and $S\circ\Sigma=\Sigma\circ S$; the identity was checked numerically to $10^{-16}$. The fixed set is $\mathrm{Fix}(\Sigma)=\{(0,0),(\pi,0)\}$, and both points are fixed points of $S$, so the symmetric subsystem is the two fixed points; the standard map also has the **reversal** $R(\theta,I)=(-\theta,I+k\sin\theta)$ of the preceding article, and $R$ is not $\Sigma$: the two involutions play different roles, the reversor reversing the iteration and the central involution commuting with it.

**Example (even and odd maps of the interval).** For $\sigma(x)=-x$ on $\mathbb{R}$, an equivariant map is an **odd** map, $T(-x)=-T(x)$; the fixed-point subspace is $\{0\}$, and the symmetric subsystem is the fixed point at the origin. The odd maps $\dot x=-x^3$, $T(x)=x-x^3$ are the normal forms of a $\mathbb{Z}/2$-symmetric equilibrium, and the symmetric periodic orbits are those of the odd map that pass through the origin. An **even** map $T(-x)=T(x)$ is not equivariant for $\sigma(x)=-x$ unless $T\equiv0$; it is constant on the orbits of $\sigma$ and descends to the quotient half-line $[0,\infty)$, where it defines the folded dynamics $x\mapsto|T(x)|$.

**Example (time-one maps and the symmetric subsystems of a field).** Let $X$ be a $\mathbb{Z}/2$-equivariant vector field, $D\sigma\,X=X\circ\sigma$; then the flow is equivariant and its fixed-point subspace is an invariant submanifold carrying the restricted field. This is the mechanism by which a symmetric equilibrium of a physical system has its centre, stable and unstable manifolds constrained to lie within the fixed-point subspace (when the equilibrium is fixed by the symmetry), and it is the **fixed-point subspace principle** used to reduce the dimension of a symmetric problem before applying the invariant manifold theorems. The precise use of the principle in the homoclinic and the bifurcation theory is *Equivariant Bifurcation Theory*, later in this category.

## Consequences of the Equivariance

**Remark (symmetric attractors).** For an equivariant dissipative map, an attractor $\Lambda$ has the property that $\sigma(\Lambda)$ is again an attractor, because $\sigma$ conjugates the dynamics to itself and preserves the topology of the basins; hence the attractors come in $\sigma$-pairs, and an attractor with a non-symmetric shape is accompanied by its reflected image, while a **symmetric attractor** satisfies $\sigma(\Lambda)=\Lambda$ and carries a $\mathbb{Z}/2$-action of its own. This is the equivariant companion of the attractor/repeller pairing of the reversible theory, and the two must be distinguished: the reversible pairing sends an attractor to a repeller, the equivariant pairing sends an attractor to an attractor.

**Remark (the space of equivariant maps).** The equivariant maps of a representation form the fixed-point set of the action of $\mathbb{Z}/2$ on the space of maps, $T\mapsto\sigma^{-1}T\sigma$; genericity statements are therefore stated within the equivariant class rather than in the class of all maps, and the symmetric degeneracies that are non-generic in the class of all maps are generic in the equivariant class. This is the reason for the separate bifurcation theory of the next group: a symmetry forces eigenvalues of the linearisation to appear with multiplicity, and the forced multiplicity is exactly the isotypic structure of the representation.

## Summary

An **equivariant** involution $\sigma$ of a dynamical system is an involution of the phase space, $\sigma^2=\mathrm{id}$, that **commutes** with the dynamics, $\sigma T=T\sigma$ (for a flow, $\sigma\varphi_t=\varphi_t\sigma$, or $D\sigma\,X=X\circ\sigma$ for the field); it is not a reversal, which would make the system conjugate to its inverse. Its decisive consequence is that the **fixed-point subspace** $\mathrm{Fix}(\sigma)$ is invariant and carries the **symmetric subsystem** $T|_{\mathrm{Fix}(\sigma)}$; the involution is an order-two map on the elements and it permutes the orbits without changing the direction of time. The **orbit structure** is the dichotomy: an orbit lies in $\mathrm{Fix}(\sigma)$ or is paired with the distinct orbit of $\sigma x$; a periodic orbit of period $n$ with $\sigma x=T^jx$ has $2j\equiv0\pmod n$, so it is contained in the fixed set or shifted by $n/2$, and a $\sigma$-invariant orbit of odd period lies in the fixed set. A linear map commuting with $\sigma$ preserves the **isotypic decomposition** $V=V_+\oplus V_-$ and splits as $A_+\oplus A_-$, so the symmetric and antisymmetric modes never mix under the linearised dynamics; at a symmetric fixed point the derivative splits into a tangent block (on the fixed submanifold) and a transverse block. The examples are the doubling map with $\sigma x=-x$ (verified, $\mathrm{Fix}(\sigma)=\{0,\tfrac12\}$), the standard map with the central involution $\Sigma(\theta,I)=(-\theta,-I)$ (verified, $\mathrm{Fix}(\Sigma)=\{(0,0),(\pi,0)\}$), the odd and even maps of the interval, and the time-one maps of equivariant fields; the last supplies the **fixed-point subspace principle**, the reduction of a symmetric problem to its fixed set before the application of the invariant-manifold and bifurcation theorems. The reversible pairing sends an attractor to a repeller, while the equivariant pairing sends an attractor to an attractor, and the two involutions must not be conflated. The symmetric bifurcations are *Equivariant Bifurcation Theory*, the symmetric tori are *Invariant Tori under an Involution*, and the operator form of the involution is *Reversible Operators and the Involution*, later in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$ | Equivariant involution, $\sigma^2=\mathrm{id}$, $\sigma T=T\sigma$ |
| $\mathrm{Fix}(\sigma)$ | Fixed-point subspace, invariant under the dynamics |
| $T\|_{\mathrm{Fix}(\sigma)}$ | Symmetric subsystem |
| $V=V_+\oplus V_-$, $A_+\oplus A_-$ | Isotypic decomposition and the commuting linear map |
| $\mathcal{O}(x)$, $X/\sigma$ | Orbit and quotient by the involution |
| $T^jx=\sigma x$, $2j\equiv0\pmod n$ | Action of $\sigma$ on a periodic orbit |
| $\Sigma(\theta,I)=(-\theta,-I)$ | Central involution of the standard map |
| $R(\theta,I)=(-\theta,I+k\sin\theta)$ | Reversor of the standard map (contrast, not equivariance) |
| $\Lambda$, $\sigma(\Lambda)$ | Attractor and its reflected partner |

## Further Reading

- Martin Golubitsky, Ian Stewart and David G. Schaeffer, *Singularities and Groups in Bifurcation Theory*, Vol. II (Springer, 1988), for the equivariant dynamics and the fixed-point subspace principle.
- Martin Golubitsky and Ian Stewart, *The Symmetry Perspective* (Birkhäuser, 2002), for the dynamics of symmetric systems.
- Pascal Chossat and Reiner Lauterbach, *Methods in Equivariant Bifurcations and Dynamical Systems* (World Scientific, 2000).
- John Guckenheimer and Philip Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields* (Springer, 1983), for the symmetric examples and the invariant manifolds.
- Michael Field, *Dynamics and Symmetry* (Imperial College Press, 2007), for the lattice of isotropy subgroups and the equivariant flows.
- Jeff Moehlis and Edgar Knobloch, "Equivariant bifurcation theory" and the survey literature, for the symmetric bifurcations.
- Robert L. Devaney, *An Introduction to Chaotic Dynamical Systems* (Westview, 2nd ed. 2003), for the doubling map and its symmetries.
