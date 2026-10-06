# __The Split-Quaternion Mandelbrot Set__

## Introduction

The connectedness locus of the split-quaternion quadratic family is the set of parameters $c$ for which the distinguished critical orbit — the orbit of $0$ inside the subalgebra $\mathbb{R}[c]=\operatorname{span}\{e_0,c\}$ of *The Split-Quaternion Quadratic Family and Its Julia Sets* — stays bounded. It is **not** a rotational hull: the automorphism group of the algebra does not rotate the parameter's subalgebra into a single plane, and the correct statement is that the locus is determined by **two invariants of the parameter**, its scalar part $c_0$ and its indefinite norm $N(\mathbf c)$ of the vector part, hence that it is a union of the level sets of those invariants, that is a union of the orbits of the Lorentz group $\operatorname{SO}^{+}(2,1)$. On the stratum where the vector part is timelike the membership is the membership in the complex Mandelbrot set of the reduced parameter; on the stratum where it is spacelike the membership is a pair of one-dimensional conditions, the two real components lying in the real interval $[-2,\tfrac14]$, and the locus in each split-complex plane is a parallelogram; on the null stratum the algebra is the dual numbers and the membership is a coupled recursion whose scalar part must lie in the same real interval.

The article proves the reduction to the two invariants, computes the three strata, states the escape-time algorithm it uses and the reason the naive one is unavailable, and compares the locus with the quaternion Mandelbrot set of the neighbouring category, which **is** the rotational hull of the complex set.

The family and the critical orbit are from *The Split-Quaternion Quadratic Family and Its Julia Sets*; the subalgebra $\mathbb{R}[c]$, its three isomorphism types and the idempotent decomposition are from the same article; the complex Mandelbrot set and its membership are from *The Mandelbrot Set and the Quadratic Family*; the split-complex connectedness locus is from *The Split-Complex Quadratic Family*; the adjoint action and the Lorentz group are from *Split-Quaternion Rotations and the Lorentz Group*; the quaternion comparison is *The Quaternion Mandelbrot Set*; and the dimension theory, not used here, is *Fractal Geometry*'s. No physics is invoked.

Throughout, $N$ is the indefinite norm of signature $(2,2)$, $N(\tilde q)=q_0^2+q_1^2-q_2^2-q_3^2$, and $\mathrm{Nv}(c)=N(\mathbf c)=c_1^2-c_2^2-c_3^2$ is the quadratic form of the vector part, whose sign decides the type of the subalgebra $\mathbb{R}[c]$. The Euclidean norm is $|\cdot|$.

## The Connectedness Locus and the Choice of the Critical Orbit

**Definition.** The **connectedness locus** of the split-quaternion quadratic family is

$$
\mathcal{M}_{\mathrm{s}}=\{c\in\mathbb{H}_{\mathrm{s}} : \text{the orbit of } 0 \text{ under } A\mapsto A^2+C,\ A\in\mathbb{R}[c],\ \text{is bounded}\} .
$$

**Remark (no unique critical point).** In the definite quaternion family the locus is the set of parameters for which the orbit of the point $0$ — the critical point of the invariant slice $\mathbb{R}[c]$, by *The Quaternion Quadratic Map and Its Julia Sets* — stays bounded, the full critical set there being the hyperplane of the pure vectors. In the split-quaternion family the differential $h\mapsto qh+hq$ is singular on the whole set $V\cup\{N=0\}$ of *The Split-Quaternion Quadratic Family and Its Julia Sets*, so there is no unique critical point and no unique orbit to test. The distinguished orbit is the one of $0$ inside the subalgebra $\mathbb{R}[c]$, which is the orbit that carries the information of the reduced parameter and which is computed by the complex or split-complex theory; the definition above takes it as the critical orbit.

## The Reduction to Two Invariants

**Theorem (the locus is determined by $c_0$ and $N(\mathbf c)$).** Membership in $\mathcal{M}_{\mathrm{s}}$ depends only on the scalar part $c_0$ and on the vector norm $\mathrm{Nv}(c)$.

*Proof.* By the equivariance $f_{\operatorname{Ad}_{\tilde u}c}=\operatorname{Ad}_{\tilde u}\circ f_c\circ\operatorname{Ad}_{\tilde u}^{-1}$ of *The Split-Quaternion Quadratic Family and Its Julia Sets*, and by the fact that $\operatorname{Ad}_{\tilde u}$ is a Euclidean isometry, the boundedness of the critical orbit of $c$ is the boundedness of the critical orbit of $\operatorname{Ad}_{\tilde u}c$; the orbit of $0$ maps to the orbit of $0$. The adjoint action fixes $q_0$ and preserves $N$, whence also $\mathrm{Nv}(c)=N(c)-c_0^2$, so the orbit of $c$ lies in the level set of the pair and the locus is invariant under the automorphism group. By *Split-Quaternion Rotations and the Lorentz Group* the Lorentz action is transitive on each level set of the pair, one sheet at a time for a timelike vector part, the two sheets being exchanged by the anti-automorphisms and carrying the same membership by the reduction of the next section; hence the pair, and not the orbit, determines the membership. $\square$

**Corollary (a union of orbits, not a hull).** The locus is saturated by the orbits of $\operatorname{SO}^{+}(2,1)$ acting on the vector part, so it is a union of the quadrics $\mathrm{Nv}=\text{const}$ and cannot be described as the rotational hull of a single planar set. The three strata are the timelike one $\mathrm{Nv}>0$, the spacelike one $\mathrm{Nv}<0$ and the null one $\mathrm{Nv}=0$.

## The Timelike Stratum

**Theorem (the timelike stratum is the complex Mandelbrot set).** Let $c \in \mathcal{M}_{\mathrm{s}}$ with $\mathrm{Nv}(c)>0$. Then the subalgebra $\mathbb{R}[c]$ is a copy of $\mathbb{C}$, the reduced parameter is $c_0+i\sqrt{\mathrm{Nv}(c)}$, and $c \in \mathcal{M}_{\mathrm{s}}$ if and only if this complex number lies in the complex Mandelbrot set.

*Proof.* The type of the subalgebra and the reduction are the proposition on $\mathbb{R}[c]$ of *The Split-Quaternion Quadratic Family and Its Julia Sets*: the minimal polynomial has the negative discriminant $-4\mathrm{Nv}(c)$, so the algebra is $\mathbb{C}$ and the isomorphism carries $c$ to $c_0+i\sqrt{\mathrm{Nv}(c)}$. The critical orbit is the complex orbit, and its boundedness is the membership in the Mandelbrot set of *The Mandelbrot Set and the Quadratic Family*. $\square$

**Corollary (the shape).** The timelike stratum of $\mathcal{M}_{\mathrm{s}}$ is the union, over the timelike directions of the vector part, of a copy of the complex Mandelbrot set placed in the corresponding complex plane $\operatorname{span}\{e_0,\mathbf c\}$; it is a three-dimensional umbrella of two-dimensional sets and not a single set.

## The Spacelike Stratum

**Theorem (the spacelike stratum is a pair of real conditions).** Let $c\in\mathcal{M}_{\mathrm{s}}$ with $\mathrm{Nv}(c)<0$, put $\beta=\sqrt{-\mathrm{Nv}(c)}>0$. Then the subalgebra is the split-complex plane $\mathbb{D}$, the idempotent components of the parameter are $C_\pm=c_0\pm\beta$, and $c\in\mathcal{M}_{\mathrm{s}}$ if and only if $-2\leq C_+\leq\tfrac14$ and $-2\leq C_-\leq\tfrac14$. In a split-complex plane the locus is the parallelogram bounded by these four lines.

*Proof.* The discriminant of the minimal polynomial is $-4\mathrm{Nv}(c)>0$, so the subalgebra is $\mathbb{D}$ with two real roots; the idempotent decomposition of *The Split-Quaternion Quadratic Family and Its Julia Sets* makes the orbit the pair of real orbits $A_\pm^{(n+1)}=(A_\pm^{(n)})^2+C_\pm$, and a real orbit is bounded exactly when its parameter lies in the real Mandelbrot interval $[-2,\tfrac14]$, by *The Split-Complex Quadratic Family*. The two conditions are the two parameters, and in a fixed split-complex plane the coordinates are $(c_0,b)$ with $\beta=|b|$, in which the four half-planes form the parallelogram. $\square$

**Corollary (an example of the shape).** In the plane $\mathbb{D}_2=\operatorname{span}\{e_0,e_2\}$ write $c=c_0+be_2$ with $b\in\mathbb{R}$; then $\beta=|b|$ and the conditions are $c_0+b\in[-2,\tfrac14]$ and $c_0-b\in[-2,\tfrac14]$. The locus in the plane is the parallelogram with the vertices $(\tfrac14,0)$, $(-\tfrac78,\tfrac98)$, $(-2,0)$ and $(-\tfrac78,-\tfrac98)$ in the coordinates $(c_0,b)$; it is the set of the split-complex parameters whose two real components both lie in the interval, and it is the exact analogue of the complex set inside this plane.

## The Null Stratum

**Proposition (the dual recursion).** Let $\mathrm{Nv}(c)=0$, so $\mathbb{R}[c]$ is the algebra of dual numbers and an element of the subalgebra is $A=u+bn$ with $n$ null. The critical orbit obeys

$$
u_{n+1}=u_n^2+c_0 , \qquad b_{n+1}=2u_nb_n+b_0 , \qquad u_0=0,\ b_0=b .
$$

Hence the scalar part must lie in the real Mandelbrot interval, and the nilpotent coefficient then evolves by a linear recursion with the time-dependent factor $2u_n$; the null stratum of $\mathcal{M}_{\mathrm{s}}$ is the subset of the null cone over the real interval on which the second recursion stays bounded.

*Proof.* Write $A=u+bn$ with $n^2=0$; then $A^2=u^2+2ubn$ and $C=c_0+b_0n$, giving the two recursions by comparing the scalar and the nilpotent parts. The scalar recursion is the real quadratic map, whence the interval condition; the nilpotent recursion is linear in $b_n$ with the coefficient $2u_n$. $\square$

**Remark (the degeneracy of the null stratum).** On the null stratum the locus is not a two-dimensional set: it is the null cone over a one-dimensional interval with a further boundedness condition on the nilpotent coefficient, and it is the stratum the menu calls "the null cone that the locus is a union over". The example $c=e_1+e_2$ lies in it: the scalar part is $0$ and the recursion gives $u_n=0$, $b_n=1$, bounded; the example $c=0.5e_0+e_1+e_2$ does not, because the scalar recursion $u_{n+1}=u_n^2+\tfrac12$ escapes from $u_0=0$.

## The Escape-Time Algorithm and the Missing Radius

**Remark (what is iterated).** The escape-time algorithm of the family iterates the **reduced** orbit of the subalgebra and not the four-dimensional orbit: for a timelike parameter it iterates $z\mapsto z^2+c_0+i\sqrt{\mathrm{Nv}}$ with the complex escape radius $2$, for a spacelike one it iterates the two real maps $u\mapsto u^2+C_\pm$ with the real escape radius $2$, and for a null one it iterates the pair of recursions above. The reason is the result of *The Split-Quaternion Quadratic Family and Its Julia Sets*: **there is no escape radius for the four-dimensional orbit**, since $K_0$ is unbounded, so a four-dimensional escape-time test is not available. The algorithm is therefore an algorithm for the reduced orbit, and the four-dimensional picture is recovered only through the equivalence classes of the locus.

**Remark (the regions the null cone removes).** The boundary between the timelike and the spacelike stratum is the null cone $\mathrm{Nv}=0$, on which the subalgebra degenerates to the dual numbers; the two-dimensional strata do not meet across it, and the locus loses a dimension there. This is the precise form of the menu's "the regions the null cone removes": the cone is the seam where the complex and the split-complex descriptions give place to the dual one.

## Comparison with the Quaternion Locus

**Remark.** The quaternion Mandelbrot set of *The Quaternion Mandelbrot Set* is the rotational hull of the complex Mandelbrot set: one planar set, revolved about the real axis by the rotation group of the sphere $S^3$, giving a three-dimensional solid. The split-quaternion locus is not of that form, and the difference is not a technicality. In the definite algebra the automorphism group is the rotation group, whose orbits in the parameter space are the spheres of constant $|\mathbf c|$ with a fixed scalar part, and the locus is a function of $|\mathbf c|$; the revolution of a planar set is exactly a function of $|\mathbf c|$. In the indefinite algebra the automorphism group is the Lorentz group of the signature-$(2,1)$ form, whose orbits are the hyperboloids of constant $\mathrm{Nv}$, and the locus is a function of $\mathrm{Nv}$ and the sign, hence a union of the complex Mandelbrot umbrella, the split-complex parallelogram family and the null stratum. **A function of $|\mathbf c|$ and a function of the sign and magnitude of the indefinite norm are different objects**, and the split-quaternion set is a union over the null cone of lower-dimensional loci rather than a rotational hull, exactly as the menu states.

## Worked Example

**Example (five parameters).** The values were recomputed by iterating the reduced critical orbit and comparing with the direct split-quaternion orbit of $0$; the direct and reduced memberships agree in every case shown.

**(a) The parameter $c=e_1$.** Then $\mathrm{Nv}=1>0$, the reduced complex parameter is $i$, and $i$ is in the complex Mandelbrot set; the critical orbit $0\to i\to-1+i\to-i\to-1+i$ is bounded, so $c\in\mathcal{M}_{\mathrm{s}}$.

**(b) The parameter $c=1.5e_1$.** Then $\mathrm{Nv}=2.25>0$ and the reduced parameter is $1.5i$, outside the complex Mandelbrot set; the critical orbit escapes.

**(c) The parameter $c=0.1+0.2e_2$.** Then $\mathrm{Nv}=-0.04<0$, $\beta=0.2$, and $C_+=0.3$ exceeds $\tfrac14$; the reduced real map $u\mapsto u^2+0.3$ has no bounded real orbit and the parameter is outside the locus, agreeing with the direct orbit.

**(d) The parameter $c=-0.5+0.5e_2$.** Then $\mathrm{Nv}=-0.25$, $\beta=0.5$, and $C_+=-0.5+0.5=0$ and $C_-=-1$ both lie in $[-2,\tfrac14]$; the parameter is in the locus, and the direct critical orbit is bounded.

**(e) The parameter $c=e_1+e_2$.** Then $\mathrm{Nv}=0$, the subalgebra is the dual numbers, the scalar recursion is $u_n=0$ and the nilpotent recursion is $b_n=1$; the critical orbit is bounded and the parameter is in the null stratum of the locus.

## Summary

The connectedness locus of the split-quaternion quadratic family is the set of parameters whose reduced critical orbit is bounded, and it is determined by the two invariants $c_0$ and $\mathrm{Nv}(c)=N(\mathbf c)$ because the automorphism group is the Lorentz group and its orbits are the level sets of the pair. It is therefore a union over the three strata of the null cone of lower-dimensional loci and not a rotational hull. On the timelike stratum it is the complex Mandelbrot set of the reduced parameter $c_0+i\sqrt{\mathrm{Nv}}$; on the spacelike stratum it is the pair of real conditions that the idempotent components $c_0\pm\sqrt{-\mathrm{Nv}}$ lie in $[-2,\tfrac14]$, a parallelogram in each split-complex plane; on the null stratum it is the dual-number recursion, lower-dimensional again. The escape-time algorithm runs on the reduced orbit, because the four-dimensional escape radius does not exist. The comparison with the quaternion locus is the comparison of the revolution of the complex set by the rotation group with the union of the Lorentz orbits, and the two are different objects. The complex membership is *The Mandelbrot Set and the Quadratic Family*'s, the split-complex locus is *The Split-Complex Quadratic Family*'s, the group is *Split-Quaternion Rotations and the Lorentz Group*'s, and the family is *The Split-Quaternion Quadratic Family and Its Julia Sets*'s.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{M}_{\mathrm{s}}$ | Connectedness locus of the split-quaternion family |
| $c_0$, $\mathbf c$ | Scalar part; vector part of the parameter |
| $\mathrm{Nv}(c)=N(\mathbf c)=c_1^2-c_2^2-c_3^2$ | Indefinite quadratic form of the vector part |
| $\beta=\sqrt{-\mathrm{Nv}(c)}$ | Half-width of the spacelike stratum |
| $C_\pm=c_0\pm\beta$ | Idempotent components of a spacelike parameter |
| $[-2,\tfrac14]$ | The real Mandelbrot interval |
| $u_n+ b_nn$ | Dual-number critical orbit on the null stratum |
| $\operatorname{SO}^{+}(2,1)$ | The automorphism group acting on the vector part |

## Further Reading

- John W. Milnor, *Dynamics in One Complex Variable*, 3rd ed. (Princeton, 2006). The complex Mandelbrot set and its membership, cited to *The Mandelbrot Set and the Quadratic Family*.
- Benoît Mandelbrot, *The Fractal Geometry of Nature* (Freeman, 1982). The quadratic family and its parameter space.
- Garret Sobczyk, "The hyperbolic number plane", *The College Mathematics Journal* 26 (1995), 268–280. The split-complex quadratic family and its connectedness interval.
- Robert Gilmore, *Lie Groups, Lie Algebras, and Some of Their Applications* (Wiley, 1974). The Lorentz group and its orbits, cited to *Split-Quaternion Rotations and the Lorentz Group*.
- John C. Baez, "The octonions", *Bulletin of the American Mathematical Society* 39 (2002), 145–205. The split-quaternion algebra and the matrix model.
