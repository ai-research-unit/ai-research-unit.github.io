# __The Real Norm and the Units__

## Introduction

The algebra is $\mathbb R^8$ as a real vector space, and the Euclidean structure of that space is the natural topology of the real reading. This article records the Euclidean norm and its unit sphere $S^7$, the unit group and its maximal compact subgroup, and the compact slices of the real subalgebras.

## The Euclidean Norm and the Unit Sphere

**Definition.** On $\tilde Q=\sum_\mu q_\mu e_\mu+\sum_\mu q'_\mu\,ie_\mu$ the **Euclidean norm** is

$$
\lVert\tilde Q\rVert_E^2=\sum_\mu\bigl(q_\mu^2+(q'_\mu)^2\bigr)=\sum_\mu\lvert Q_\mu\rvert^2 ,
$$

the ordinary norm of $\mathbb R^8$. Its unit sphere

$$
S^7=\{\tilde Q:\lVert\tilde Q\rVert_E=1\}
$$

is compact; it is the boundary of the unit ball, and the ambient real vector space is contractible, so the sphere contributes no homotopy of its own. The Euclidean structure of the ambient space — its contractibility, its unit sphere and its sphere at infinity — belongs to *The Euclidean Topology of the Biquaternion Algebra*. The Euclidean norm is the norm of the Hermitian form $\langle\tilde Q,\tilde Q\rangle_*=\sum_\mu\lvert Q_\mu\rvert^2$; it is positive definite and is not one of the four complex forms.

## The Unit Group and Its Maximal Compact Subgroup

**Definition.** The **unit group** is $\mathbb B^\times=\{\tilde Q:N(\tilde Q)\neq0\}$, the elements that are not zero divisors.

As a real Lie group, $\mathbb B^\times$ is $\mathrm{GL}_2(\mathbb C)$: of real dimension $8$, non-compact and connected, with centre the scalars $\mathbb C^\times e_0$ and maximal compact subgroup $U(2)$, of real dimension $4$. The unit group retracts onto its maximal compact subgroup,

$$
\mathbb B^\times\simeq U(2),
$$

so its topology is that of $U(2)$, and the norm-one slice

$$
\{\tilde Q:\langle\tilde Q,\tilde Q\rangle_{\natural}=1\}=\mathrm{SL}_2(\mathbb C)
$$

retracts onto $SU(2)=Sp(1)=S^3$. The two retractions, that of $\mathbb B^\times$ onto $U(2)$ and of $\mathrm{SL}_2(\mathbb C)$ onto $S^3$, are the real content of the topology of the units and are used in *The Biquaternion Unit Group as a Topological Group*.

## The Compact Slices of the Real Subalgebras

Inside the algebra the real subalgebras carry the Euclidean spheres of their own dimensions. The **quaternion subspace** $\mathbb H_{\mathbb B}\cong\mathbb H$ has unit sphere $S^3$ with the group structure $Sp(1)$; the **centre** $\mathbb C_{\mathbb B}$ has unit circle $S^1$; the two **real forms** $\mathbb M_+$ and $\mathbb M_-$ are copies of Minkowski space, and their Euclidean spheres are the ordinary $S^3$ of the four real coordinates. These are the compact objects of the real reading, set against the non-compact unit group and the non-compact norm-one slice.

## Summary

The Euclidean norm on the eight real coordinates has unit sphere $S^7$, compact and the boundary of the unit ball; the Euclidean structure of the ambient space is *The Euclidean Topology of the Biquaternion Algebra*. The unit group $\mathbb B^\times=\{\tilde Q:N(\tilde Q)\neq0\}$ is $\mathrm{GL}_2(\mathbb C)$, of real dimension $8$ and maximal compact subgroup $U(2)$, onto which it retracts; the norm-one slice $\mathrm{SL}_2(\mathbb C)$ retracts onto $SU(2)=S^3$. The real subalgebras carry the spheres $S^3$ (quaternion subspace) and $S^1$ (centre).

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lVert\tilde Q\rVert_E^2=\sum_\mu\lvert Q_\mu\rvert^2$ | the Euclidean norm of the real reading |
| $S^7$ | its unit sphere, compact |
| $\mathbb B^\times\simeq U(2)$ | the unit group and its maximal compact subgroup |
| $\mathrm{SL}_2(\mathbb C)\simeq S^3$ | the norm-one slice and its retract |

## Further Reading

- *The Real Topology of the Biquaternion Algebra* (`articles_maths/the-real-topology-of-the-biquaternion-algebra.md`), for the real topology
- *The Biquaternion Unit Group as a Topological Group* (`articles_maths/the-biquaternion-unit-group-as-a-topological-group.md`), for the group of units
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm and the invertible elements
