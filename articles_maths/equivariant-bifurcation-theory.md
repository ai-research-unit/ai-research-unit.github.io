# __Equivariant Bifurcation Theory__

## Introduction

An **equivariant bifurcation** is a bifurcation of a dynamical system that commutes with a symmetry. The system is a parameter family $f=f(x,\lambda)$ **equivariant** with respect to a group $\Gamma$ acting on the state space, $f(\gamma x,\lambda)=\gamma f(x,\lambda)$ for all $\gamma\in\Gamma$, and the question is how the symmetry restricts the singularities, forces the generic bifurcations to be of special type, and organises the branches of the bifurcating solutions. The answer is structural and sharp. Because the symmetry commutes with the linearisation, the eigenvalues of the linearised problem at a symmetric solution come in **isotypic multiplets**, so that the codimension of a singular point is higher than in the non-symmetric problem and a one-parameter family meets it only after the symmetry has forced the degenerate terms to vanish; because the equation can be posed on the **fixed-point subspace** of a subgroup, the bifurcation problem is reduced to a lower-dimensional one, the **equivariant branching lemma** of Vanderbauwhede and Cicogna guarantees a branch of solutions with the isotropy of the subgroup whenever the eigenvalue crosses with the right multiplicity; and because the symmetry forces the **quadratic term** to vanish in a reflection-symmetric scalar problem, the generic one-dimensional bifurcation of a $\mathbb{Z}/2$-equivariant system is the **pitchfork**, the double branch $x=\pm\sqrt{\lambda-\lambda_0}$ that breaks the symmetry and is exchanged by the involution. The present article develops this theory in the case of the involution, with the general group statement given for reference; the symmetry-breaking bifurcations of the reversible and the equivariant theories are the same phenomenon in two different classes of systems.

The article treats the equivariant bifurcation theory of a symmetry group and its reduction to the involution. It states the **equivariant branching lemma** and the **fixed-point subspace principle**, the **pitchfork bifurcation** of a $\mathbb{Z}/2$-equivariant scalar family with the vanishing of the even terms and the supercritical/subcritical dichotomy, the **symmetry breaking** in which the branch loses the symmetry of the trivial solution while the branch as a whole is invariant, the equivariant **Hopf** and the **period-doubling** bifurcations of symmetric limit cycles, and the **reversible bifurcations**, where the reversor rather than an equivariant symmetry imposes the degeneracy. It gives the examples of the pitchfork normal form and the two-dimensional equivariant family, with the branch conditions recomputed, and it closes with the classification of the symmetric bifurcations in the low codimension.

The equivariant systems, the fixed-point subspaces, the isotypic decomposition, the orbit structure and the symmetric attractors are those of *Equivariant Dynamics under an Involution*; the reversors, the symmetric orbits and the reversible normal form are those of *Reversible Dynamical Systems and Time-Reversal Symmetry*, *Symmetric Periodic Orbits and the Involution* and *Reversible Systems and the KAM Theorem*; the bifurcation theory, the codimension, the versal unfoldings and the normal forms are those of *Bifurcation Theory*; the centre manifold, the Poincaré–Dulac normal form and the Hopf theorem are those of *Bifurcation Theory* and *Ordinary Differential Equations*; the equivariant singularity theory is the subject of *Invariant Theory* in the algebra of the system, and the group actions are those of *Groups and Group Actions*. The operator form of the involution is *Reversible Operators and the Involution*, in the `- * Operator Theory` group, and the symmetric tori are *Invariant Tori under an Involution*, later in this category. The non-symmetric bifurcation theory is not repeated here.

No physics is invoked.

## The Equivariant Setting

### Equivariance and the Reduction

**Definition.** Let a compact group $\Gamma$ act on a manifold $M$, and let $f:M\times\mathbb{R}\to TM$ be a parameter family of vector fields. The family is **$\Gamma$-equivariant** if

$$
f(\gamma x,\lambda)=\gamma f(x,\lambda) \qquad (\gamma\in\Gamma),
$$

so that the flow commutes with the action; a solution and its image under the action are both solutions, and the solution set carries the action. For a map $T$ the condition is $T(\gamma x)=\gamma T(x)$.

**Definition.** For a subgroup $\Sigma\subseteq\Gamma$ the **fixed-point subspace** is $\mathrm{Fix}(\Sigma)=\{x:\gamma x=x\ \text{for all }\gamma\in\Sigma\}$; it is invariant under the equivariant dynamics, and the **isotropy subgroup** of a solution $x$ is $\Gamma_x=\{\gamma:\gamma x=x\}$. A bifurcating solution with isotropy $\Sigma$ is **symmetric** with respect to $\Sigma$ and **breaks** the rest of the symmetry.

**Theorem (the fixed-point subspace principle).** Let $f$ be $\Gamma$-equivariant and let $\Sigma\subseteq\Gamma$ be a subgroup. Then $\mathrm{Fix}(\Sigma)$ is invariant under the flow, and the restriction $f|_{\mathrm{Fix}(\Sigma)}$ is a vector field on the fixed-point subspace; consequently every bifurcation that can be detected on $\mathrm{Fix}(\Sigma)$ takes place in a subsystem of dimension $\dim\mathrm{Fix}(\Sigma)$, and the solution branch found there has isotropy containing $\Sigma$.

*Proof.* If $x\in\mathrm{Fix}(\Sigma)$ then for $\gamma\in\Sigma$ one has $\gamma f(x,\lambda)=f(\gamma x,\lambda)=f(x,\lambda)$, so $f(x,\lambda)\in\mathrm{Fix}(\Sigma)$; the restriction is therefore a vector field, and a solution of the restricted field is a solution of the full field fixed by $\Sigma$.

### The Equivariant Branching Lemma

**Theorem (Vanderbauwhede–Cicogna, quoted).** Let $f$ be a sufficiently smooth $\Gamma$-equivariant family with $f(0,\lambda)=0$ and with the trivial solution losing stability at $\lambda=0$ through a zero eigenvalue of $D_xf(0,0)$. Let $\Sigma$ be an isotropy subgroup such that $\dim\mathrm{Fix}(\Sigma)=1$ and the kernel eigenvector $v$ lies in $\mathrm{Fix}(\Sigma)$. Then there is a branch of solutions of $f(x,\lambda)=0$ bifurcating from the trivial solution and lying in $\mathrm{Fix}(\Sigma)$, with isotropy containing $\Sigma$; the branch is a smooth curve parametrised by $\lambda$, and its direction is $v$.

*Proof.* Quoted. The proof restricts the equation to the one-dimensional fixed-point subspace and applies the equivariant implicit function theorem; the restriction converts the problem into a scalar one, where the crossing of the eigenvalue gives the branch by the intermediate value theorem, and the equivariance guarantees that the branch is a full solution. The general statement, the isotropy lattice and the equivariant transversality are those of the equivariant bifurcation theory of Golubitsky–Stewart–Schaeffer and Chossat–Lauterbach.

**Remark (the role of the involution).** For $\Gamma=\mathbb{Z}/2$ generated by an involution $\sigma$, the subgroup lattice is $\{1,\mathbb{Z}/2\}$, the fixed-point subspace of the full group is $\mathrm{Fix}(\sigma)$, and the branching lemma reduces to the statement that a one-dimensional fixed subspace of an antisymmetric mode carries a branch whenever the eigenvalue crosses; the higher isotropy groups of a larger $\Gamma$ give the finer branching, and the involution is the elementary case of the theory.

## The Pitchfork and Symmetry Breaking

### The Normal Form

**Theorem (the $\mathbb{Z}/2$ pitchfork).** Let $f(x,\lambda)$ be an odd function of $x$, $f(-x,\lambda)=-f(x,\lambda)$, the equivariance for the involution $\sigma(x)=-x$ on $\mathbb{R}$, with $f(0,\lambda)=0$ and $\partial f/\partial x(0,0)=0$, $\partial f/\partial x\partial\lambda(0,0)\neq0$. Then in the Taylor expansion of $f$ all the even powers of $x$ vanish, and the lowest non-trivial normal form is

$$
f(x,\lambda)=\lambda x+a x^3+\cdots ;
$$

the trivial solution $x=0$ is stable for $\lambda<0$ and unstable for $\lambda>0$, the bifurcating branches are $x=\pm\sqrt{-\lambda/a}$ (real for $\lambda>0$ when $a<0$, the **supercritical** case, and for $\lambda<0$ when $a>0$, the **subcritical** case), and the two branches are interchanged by the involution. The bifurcation is a **pitchfork**, and it is the generic one-parameter bifurcation of a $\mathbb{Z}/2$-equivariant scalar system.

*Proof.* The equivariance $f(-x,\lambda)=-f(x,\lambda)$ forces the even coefficients of the Taylor expansion to vanish, in particular the quadratic coefficient, so the linear term is followed by the cubic; the branch equation $x(\lambda+a x^2)=0$ has the roots $x=0$ and $x=\pm\sqrt{-\lambda/a}$, and the stability is read from $\partial f/\partial x=\lambda+3ax^2$ at each root. The two non-trivial roots differ by the sign of $x$, which is exactly the involution, so the two branches are exchanged by $\sigma$ and each has trivial isotropy: the bifurcation is **symmetry-breaking**.

**Verified example.** For the normal form $f(x,\lambda)=\lambda x-x^3$, checked numerically in exact floating point, the equivariance holds identically at all tested $(\lambda,x)$, the second derivative at the origin is zero to machine precision (a finite-difference check gave $0.0$), the trivial solution has stability $\lambda$, and the branch $x=\pm\sqrt\lambda$ has stability $\lambda-3\lambda=-2\lambda$, negative for $\lambda>0$ and positive for $\lambda<0$; the branches are real and stable exactly for $\lambda>0$, the supercritical case $a=-1$. This is the canonical picture of the symmetry-breaking bifurcation.

### Symmetry Breaking and the Branch as a Set

**Definition.** A bifurcating solution branch is **symmetry-breaking** if the individual solutions have a proper isotropy subgroup smaller than $\Gamma$, while the branch as a whole (the union of the images under $\Gamma$) is invariant. In the pitchfork the individual branches $x=+\sqrt{\lambda}$ and $x=-\sqrt{\lambda}$ have trivial isotropy, but the pair is $\sigma$-invariant: the symmetry is broken pointwise and preserved setwise.

**Theorem (the equivariant branch and the orbit).** For a $\Gamma$-equivariant family, the solutions of the branch found by the equivariant branching lemma are organised in the orbit $\Gamma\cdot x_0$ of one solution; the number of distinct solutions on the orbit is $|\Gamma|/|\Gamma_{x_0}|$, and the branch has the symmetry of the isotropy subgroup $\Gamma_{x_0}$. In the $\mathbb{Z}/2$ case, a symmetric branch in $\mathrm{Fix}(\sigma)$ has isotropy $\mathbb{Z}/2$ and consists of a single solution for each parameter, while a symmetry-breaking branch has trivial isotropy and is a pair.

*Proof.* The action preserves the solution set, so the orbit of any solution consists of solutions with the same parameter; the orbit-stabiliser count gives the number of distinct solutions, and the fixed-point subspace principle gives the isotropy of a branch found on $\mathrm{Fix}(\Sigma)$.

**Remark (implications for the bifurcation diagram).** The symmetry forces the bifurcation diagram to be symmetric under the group: the branches occur in orbits, the stability of the solutions on an orbit is the same because the linearisation is conjugated by the group, and the transition from the symmetric to the symmetry-breaking branch is accompanied by the creation of an orbit of solutions of size $|\Gamma|/|\Gamma_{x_0}|$. In the $\mathbb{Z}/2$ case this is the doubling of the branch into the pair $x=\pm\sqrt{-\lambda/a}$ and, in two dimensions, into the reflection of a pair of off-axis equilibria.

## The Symmetric Bifurcations of Periodic Orbits

**Theorem (equivariant Hopf, quoted).** Let $f$ be $\Gamma$-equivariant with a symmetric equilibrium, and let a pair of complex conjugate eigenvalues cross the imaginary axis at $\lambda=0$ with the eigenvector in a specified isotypic component. Then there is a branch of periodic solutions bifurcating from the equilibrium, and the isotropy subgroup of the branch in the **equivariant Hopf theory** is the subgroup that fixes the eigenvector in the appropriate sense (the subgroup $\Sigma$ satisfying $\dim\mathrm{Fix}(\Sigma)=2$ for the pair); in the $\mathbb{Z}/2$ case the symmetric limit cycle is the invariant cycle of the equivariant system, and its isotropy is $\mathbb{Z}/2$ when the eigenvector lies in the symmetric isotypic component.

*Proof.* Quoted from *Bifurcation Theory* with the equivariant refinement; the centre-manifold reduction of the equivariant family is equivariant, the Poincaré normal form is computed in the equivariant class, and the crossing of the pair of eigenvalues produces the invariant circle; the isotropy computation is the two-dimensional form of the branching lemma. The equivariant Hopf theorem and the classification of the symmetric cycles are the equivariant Hopf theory of the reference literature.

**Remark (the period-doubling of a symmetric orbit).** A symmetric limit cycle of a $\mathbb{Z}/2$-equivariant system may undergo a **period-doubling**: doubling the period of a cycle that is not contained in the fixed set, the second iterate loses the equivariance to the original action and becomes equivariant for a smaller symmetry; the bifurcation is the period-doubling of the family and it is constrained by the symmetry to happen on the symmetric cycles first, the mechanism of the symmetric routes to chaos. The details of the period-doubling and the Feigenbaum theory belong to *Bifurcation Theory*, and the symmetric version is the equivariant refinement.

## Reversible Bifurcations

**Definition.** A **reversible bifurcation** is a bifurcation of a reversible system, $RTR=T^{-1}$ (or the flow version) about a reversible equilibrium or periodic orbit, at which the reversor is preserved by the whole family. The reversor imposes the vanishing of the terms that are not invariant under its action on the Taylor coefficients, in the same way as the equivariant involution, but on the **reversible normal form**.

**Theorem (the reversible pitchfork, quoted).** Let a reversible family of planar vector fields have a reversible equilibrium at the origin with a zero eigenvalue and reversor $R$ with $\mathrm{Fix}(R)$ a curve. Then the generic one-parameter bifurcation is a **reversible pitchfork** in which a pair of off-axis symmetric equilibria is born, the two being images of one another under $R$; the reversor fixes the axis of the pitchfork, and the symmetry-breaking pattern is that of the $\mathbb{Z}/2$ case with the reversor in place of the commuting involution.

*Proof.* Quoted from the reversible singularity theory (Moser, Sevryuk and the reversible normal-form literature). The remark is that the reversible normal form is computed in the class of maps commuting with $R$, and the reversibility, like the equivariance, forces the quadratic term to vanish in the scalar amplitude equation; the resulting pitchfork is the reversible analogue of the equivariant one.

**Remark (the reversible and the equivariant theories are two classes).** The reversal and the equivariant symmmetry impose the same kind of constraint on the normal form — the vanishing of the non-invariant terms and the forced multiplicity of the eigenvalues — but the two act differently on the flow: the reversal conjugates the flow to its inverse, so the reversible normal form is time-reversal-symmetric while the equivariant one is not; the classification of the reversible bifurcations therefore differs from the equivariant classification, and the two must be kept separate. The reversible normal form and its resonances are *Symmetric Periodic Orbits and the Involution* and *Reversible Systems and the KAM Theorem*, above.

## Summary

An **equivariant bifurcation** is a bifurcation of a $\Gamma$-equivariant family $f(\gamma x,\lambda)=\gamma f(x,\lambda)$. The symmetry forces the eigenvalues of the linearisation at a symmetric solution into **isotypic multiplets**, raises the codimension, and organises the solution branches in orbits; the **fixed-point subspace principle** reduces the problem to a subsystem $\mathrm{Fix}(\Sigma)$, and the **equivariant branching lemma** of Vanderbauwhede and Cicogna produces a branch on a one-dimensional fixed-point subspace whenever the eigenvalue of the appropriate mode crosses. For the involution $\Gamma=\mathbb{Z}/2$ with $\sigma(x)=-x$ the generic one-parameter bifurcation is the **pitchfork**: the equivariance forces all the even Taylor coefficients, in particular the quadratic one, to vanish, the normal form is $\lambda x+ax^3$, the branches are $x=\pm\sqrt{-\lambda/a}$, and the bifurcation is **symmetry-breaking**, the two branches having trivial isotropy while the pair is $\sigma$-invariant. The verified normal form $\lambda x-x^3$ has the trivial stability $\lambda$ and the branch stability $-2\lambda$, so the branches are stable for $\lambda>0$ in the supercritical case. The symmetric limit cycles bifurcate by the **equivariant Hopf theorem**, the symmetric cycles undergo the constrained period-doubling, and the **reversible bifurcations** impose the same kind of constraint through the reversor on the reversible normal form, forming a separate classification because the reversal conjugates the flow to its inverse. The equivariant structure is *Equivariant Dynamics under an Involution*, the reversible structure is *Reversible Dynamical Systems and Time-Reversal Symmetry*, the non-equivariant bifurcation theory is *Bifurcation Theory*, and the symmetric tori are *Invariant Tori under an Involution*, later in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Gamma$, $\gamma$ | Symmetry group and its elements |
| $f(\gamma x,\lambda)=\gamma f(x,\lambda)$ | Equivariance of the family |
| $\Sigma$, $\mathrm{Fix}(\Sigma)$, $\Gamma_x$ | Subgroup, its fixed-point subspace, isotropy subgroup |
| $v$, $D_xf(0,0)$ | Kernel eigenvector and linearisation |
| $\lambda x+ax^3$ | $\mathbb{Z}/2$ pitchfork normal form |
| $x=\pm\sqrt{-\lambda/a}$ | The symmetry-breaking branch pair |
| $a<0$, $a>0$ | Supercritical and subcritical pitchfork |
| $R$ | Reversor of a reversible bifurcation |
| $\Gamma\cdot x_0$, $|\Gamma|/|\Gamma_{x_0}|$ | Orbit of a solution and its size |

## Further Reading

- Martin Golubitsky, Ian Stewart and David G. Schaeffer, *Singularities and Groups in Bifurcation Theory*, Vol. II (Springer, 1988), for the equivariant branching lemma and the symmetric bifurcations.
- Pascal Chossat and Reiner Lauterbach, *Methods in Equivariant Bifurcations and Dynamical Systems* (World Scientific, 2000), for the general equivariant theory.
- André Vanderbauwhede, *Local Bifurcation and Symmetry* (Pitman, 1982), for the branching lemma.
- Gianni Cicogna, "Symmetry breakdown from bifurcation", *Lettere al Nuovo Cimento* 31 (1981), 600–602, for the equivariant branching.
- Martin Golubitsky and Ian Stewart, *The Symmetry Perspective* (Birkhäuser, 2002), for the equivariant Hopf and the symmetric routes to chaos.
- John Guckenheimer and Philip Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields* (Springer, 1983), for the centre manifold, the Poincaré–Dulac normal form and the Hopf theorem.
- Michael B. Sevryuk, *Reversible Systems* (Springer Lecture Notes in Mathematics 1211, 1986), and John A. G. Roberts and G. R. W. Quispel, "Chaos and time-reversal symmetry", *Physics Reports* 216 (1992), 63–177, for the reversible bifurcations.
- Jeff Moehlis and Edgar Knobloch, "Equivariant bifurcation theory" (survey), and the literature on the reversible normal forms.
