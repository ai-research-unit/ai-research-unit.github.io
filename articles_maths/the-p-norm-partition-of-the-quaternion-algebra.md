# __The P-Norm Partition of the Quaternion Algebra__

## Introduction

The plain algebraic norm is
$$
P(\tilde q)=\mathrm{Sc}\bigl(\tilde q^2\bigr)=q_t^2-\lvert\vec q\rvert^2 ,
$$
the quadratic form of signature $(1,3)$ that the trace form of the plain product induces. Its sign cuts the algebra into three classes,
$$
\mathbb{H}=\{P>0\}\uplus\{P=0\}\uplus\{P<0\},
$$
the timelike, the null and the spacelike; the three are non-empty, of real dimensions four, three and four, and the middle one is not the set of the non-invertibles: every null element is invertible. The two other norms of the algebra cut it differently: the quaternion norm $N$ separates the origin alone, and the spectral data of the spectrally regular locus separate the real axis. The three cuts are independent, and the article states each of them and the exact sense in which they differ.

The algebra is that of [Norm and Invertibility in the Quaternion Algebra](norm-and-invertibility-in-the-quaternion-algebra.html), and the form is the one of [Quaternion Metrics](quaternion-metrics.html), where it appears as the member $g=e_t$ of the one-parameter family $\mathrm{Sc}(g\tilde xg\tilde x)$. The sectors it cuts are the subject of the four following articles.

## The Plain Algebraic Norm

**Definition.** The **plain algebraic norm** is $P(\tilde q)=\mathrm{Sc}(\tilde q^2)$, with polar form
$$
\langle\tilde q_1,\tilde q_2\rangle_P=\mathrm{Sc}\bigl(\tilde q_1\tilde q_2\bigr)=q_{1t}q_{2t}-(\vec q_1,\vec q_2).
$$

**Proposition (the form and its signature).** The form is symmetric, bilinear, of Gram matrix $\mathrm{diag}(1,-1,-1,-1)$ in the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$, of signature $(1,3)$ and rank four; its radical is $\{0\}$; and its quadratic form is $P$.

*Proof.* The scalar part of $\tilde q_1\tilde q_2$ is $q_{1t}q_{2t}-(\vec q_1,\vec q_2)$; the Gram matrix is read on the basis, where $\langle e_t,e_t\rangle_P=1$ and $\langle\vec e_k,\vec e_k\rangle_P=-1$ with all mixed entries zero. The polar form of $P$ is $\tfrac12(P(\tilde q_1+\tilde q_2)-P(\tilde q_1)-P(\tilde q_2))$, which is the display.

**Theorem (the norm is not multiplicative).** There are $\tilde q_1,\tilde q_2$ with
$$
P(\tilde q_1\tilde q_2)\neq P(\tilde q_1)P(\tilde q_2).
$$

*Proof.* Take $\tilde q_1=\vec e_x$ and $\tilde q_2=\vec e_y$. Then $\tilde q_1\tilde q_2=\vec e_z$ and $P(\vec e_z)=-1$, while $P(\vec e_x)P(\vec e_y)=(-1)(-1)=1$. The two differ by $2$. Verified exactly, and on random pairs the ratio is unbounded. The contrast with $N$ is the whole reason the two norms are kept apart: $N(\tilde q_1\tilde q_2)=N(\tilde q_1)N(\tilde q_2)$ for all pairs, and $P$ obeys no such law.

**Remark (why the failure is structural).** A multiplicative $P$ would make the null set closed under multiplication, since $P(\tilde q_1\tilde q_2)=0$ whenever one factor is null. The null set is not closed: $(e_t+\vec e_x)(e_t+\vec e_y)=e_t+\vec e_x+\vec e_y+\vec e_z$ has $P=1-3=-2$. So no argument about signs can repair the multiplicativity, and the failure is a failure of the product to respect an indefinite form rather than an accident of a chosen pair. **A definite form can be multiplicative, as $N$ is; an indefinite form over a division algebra cannot be.**

**Proposition (homogeneity and the invariance of the cut).** For every real $\lambda$, $P(\lambda\tilde q)=\lambda^2P(\tilde q)$ and $N(\lambda\tilde q)=\lambda^2N(\tilde q)$; the P-partition is therefore invariant under the multiplication by a non-zero real scalar, and the scalar $-e_t$ acts as the identity on the partition.

*Proof.* Each norm is a quadratic form. The two squares in the display are the statement. Verified on general elements.

**Remark (what the invariances are not).** The P-partition is invariant under the real scalars and under the conjugation, since $P(\tilde q^{\natural})=P(\tilde q)$, and it is *not* invariant under the group of invertibles: the versor $\tilde u$ sends $e_t$ to a unit of $P$-norm $1$, but a general unit sends the real line to a two-plane, and the timelike element $e_t+\tfrac12\vec e_x$ is sent by a suitable versor to an element of the spacelike class. **The cut is preserved by the scalars and the conjugation and by nothing else in the group, and this is the reason the isometry group of $P$, and not the group of invertibles, is the group of the partition.** The isometries are read in [The P Isometry Group and Its Cartan Decomposition](the-p-isometry-group-and-its-cartan-decomposition.html).

## The Partition

**Definition.** The three classes are
$$
\mathcal T=\{\tilde q:\ P>0\},\qquad \mathcal N=\{\tilde q:\ P=0\},\qquad \mathcal S=\{\tilde q:\ P<0\},
$$
the **timelike**, the **null** and the **spacelike** class.

**Theorem (the classes are non-empty and form a partition).** The three classes are disjoint, their union is $\mathbb{H}$, and each is non-empty: $e_t\in\mathcal T$, $e_t+\vec e_x\in\mathcal N$, $\vec e_x\in\mathcal S$.

*Proof.* The sign of a real number is one of the three, and $P$ is a continuous function, so the classes are disjoint and cover. The three witnesses give $P(e_t)=1$, $P(e_t+\vec e_x)=1-1=0$ and $P(\vec e_x)=-1$. Verified on the basis and on random elements.

**Proposition (the dimensions).** $\mathcal T$ and $\mathcal S$ are open of real dimension four; $\mathcal N$ is closed, of real dimension three, and its smooth part is a hypersurface.

*Proof.* The first two are the preimages of an open set under a continuous function, non-empty, hence open of the full dimension. The null set is the zero set of a non-zero quadratic form of signature $(1,3)$, a cone of dimension three; off the origin the gradient $2(q_t,-\vec q)$ is non-zero, so the cone is smooth there and its tangent space has dimension three.

**Remark (the partition of $N$).** The quaternion norm $N(\tilde q)=q_t^2+\lvert\vec q\rvert^2$ is positive definite, so its sign partitions the algebra as
$$
\mathbb{H}=\mathbb{H}^{\times}\uplus\{0\},
$$
the invertibles and the origin. The two partitions are as different as two partitions of the same set can be: one has three classes of dimensions four, three and four, the other has one class of dimension four and one point. **The P-partition is the partition of an indefinite form; the N-partition is the partition of a definite one, and a definite form has only two signs, one of which is attained at the origin alone.**

## The Three Classes Compared with the N-Partition

**Theorem (the null class is not the non-invertible class).** Every element of $\mathcal N$ is invertible, and
$$
N(\tilde q)=2q_t^2>0\ \ \text{on }\mathcal N\setminus\{0\}.
$$

*Proof.* On the cone $q_t^2=\lvert\vec q\rvert^2$, so $N=q_t^2+\lvert\vec q\rvert^2=2q_t^2$, which is positive unless $q_t=0$, and $q_t=0$ on the cone forces $\vec q=0$. So no non-zero null element is a zero divisor, and $\{0\}$ is the only non-invertible element of the algebra. Verified on the parametrised cone.

**Corollary (the three classes meet the invertibles in the same way).** Each of the three classes is contained in $\mathbb{H}^{\times}$ after the removal of the origin of $\mathcal N$, so the P-partition cuts the group of invertibles into three pieces and the N-partition cuts it into one.

*Proof.* $\mathbb{H}^{\times}=\mathbb{H}\setminus\{0\}$ and the three classes are contained in $\mathbb{H}$, with only $\mathcal N$ meeting the origin. Verified on the parametrisations.

**Remark (the two partitions are not nested).** The N-partition is coarser than the P-partition in the sense that each of its classes is a union of P-classes, and the passage is the passage from a definite form to an indefinite one. The information is not lost: $N$ and $P$ are independent functions, since $N=q_t^2+\lvert\vec q\rvert^2$ and $P=q_t^2-\lvert\vec q\rvert^2$ determine $q_t^2$ and $\lvert\vec q\rvert^2$, hence determine each other's level sets jointly but neither separately. **Two quadratic forms of different signatures cut the same space in two different ways, and neither refines the other except through the pair.**

## The Restriction to the Remarkable Subspaces

**Proposition (the real line).** On the real line, $P(\lambda e_t)=\lambda^2\geq0$, with equality only at the origin; the null class meets the line only at $0$, and the line minus the origin lies in the timelike class.

*Proof.* The formula, and the sign of a square. Verified on the line.

**Proposition (the vector subspace).** On the vector subspace, $P(\vec q)=-\lvert\vec q\rvert^2\leq0$, with equality only at the origin; the vector subspace minus the origin lies in the spacelike class.

*Proof.* The formula. So the two remarkable subspaces sit in the two open classes, and the cone touches each of them only at the origin: **the null cone of the algebra is transverse to both remarkable subspaces, and it is the object that joins them.**

**Proposition (the planes through the axis).** Fix a unit vector $\vec n$ and let $\Pi_{\vec n}=\mathbb{R}e_t\oplus\mathbb{R}\vec n$. On $\Pi_{\vec n}$, $P(\lambda e_t+\mu\vec n)=\lambda^2-\mu^2$, of signature $(1,1)$; the null class meets the plane in the two lines $\mathbb{R}(e_t\pm\vec n)$, and the two open quadrants are the two classes of the plane.

*Proof.* The formula, and the factorisation $\lambda^2-\mu^2=(\lambda-\mu)(\lambda+\mu)$. Verified on the plane. The planes $\Pi_{\vec n}$ are the maximal linear subspaces on which $P$ restricted is indefinite, and they are the planes in which the hyperbolic structure of the following articles is read.

**Proposition (the unit sphere).** On the sphere $S^3=\{N=1\}$, $P=2q_t^2-1$, so the three classes are cut by $\lvert q_t\rvert$ against $1/\sqrt2$: the timelike part is the pair of caps $\lvert q_t\rvert>1/\sqrt2$, the null part is the pair of two-spheres $\lvert q_t\rvert=1/\sqrt2$, and the spacelike part is the equatorial band between them.

*Proof.* $N=1$ gives $\lvert\vec q\rvert^2=1-q_t^2$, hence $P=q_t^2-(1-q_t^2)=2q_t^2-1$. Verified on points of the sphere. The pair of two-spheres is read again in [The Topology of the P-Null Cone of the Quaternion Algebra](the-topology-of-the-p-null-cone-of-the-quaternion-algebra.html).

## A Worked Check

**Example.** Take $\tilde q=(2,1,2,0)$, that is $\tilde q=2e_t+\vec e_x+2\vec e_y$. Then $q_t^2=4$ and $\lvert\vec q\rvert^2=1+4=5$, so $P=-1$ and the element is spacelike; $N=4+5=9$, so the element is a unit of modulus $3$. The element $\tilde q+\vec e_y=2e_t+\vec e_x+3\vec e_y$ has $P=4-10=-6$, spacelike; the element $\tilde q-\vec e_y=2e_t+\vec e_x+\vec e_y$ has $P=4-2=2$, timelike. So along the affine line $\tilde q+s\vec e_y$ the class changes twice, at $s=-1$ and $s=+1$ where $P$ vanishes, and the two crossings are the trace of the null cone on the line. The two crossings are computed by $4=(1+(2+s)^2)$, that is $(2+s)^2=3$.

**Example (the normalised null elements).** The element $\tilde n_+=\tfrac1{\sqrt2}(e_t+\vec e_x)$ has $P=0$ and $N=1$; the element $\tilde n_-=\tfrac1{\sqrt2}(e_t-\vec e_x)$ likewise; their product is $\tilde n_+\tilde n_-=\tfrac12(e_t-\vec e_x^2)=e_t$, a unit of $P$-norm $1$. So two null elements multiply to a timelike one, and the null set is not closed under the product, as the remark above says. The two elements are $\pm$-orthogonal in the sense of $N$ and not of $P$.

**Remark (the shape of the level sets).** The level sets are read in the basis: $\{P=c\}$ is the hyperboloid $q_t^2-\lvert\vec q\rvert^2=c$, two-sheeted for $c>0$ and one-sheeted for $c<0$, with the cone at $c=0$. Each is a smooth three-dimensional submanifold off the cone, and the three classes are the three regions they bound. The hyperbolic metrics they carry are the subject of [The P Level Sets and the Hyperbolic Structure of the Quaternion Algebra](the-p-level-sets-and-the-hyperbolic-structure-of-the-quaternion-algebra.html).

**Remark (what the example shows).** The class of an element is not a class of the element up to the multiplication by invertibles, it is a class of the element as a vector of the metric space; and the hyperbolic planes $\Pi_{\vec n}$ are the charts in which the classification is read by the two coordinates alone.

## The Third Cut and the Spectral Strata

**Remark (the spectral strata).** The spectrum of the left multiplication by $\tilde q$ is $q_t\pm i\lvert\vec q\rvert$, and the spectral strata of [The Three Sectors of the Quaternion Algebra](the-three-sectors-of-the-quaternion-algebra.html) are the non-real quaternions, the real axis minus the origin, and the origin. The three strata answer the question of the distinctness of the eigenvalues; the three P-classes answer the question of the sign of $q_t^2-\lvert\vec q\rvert^2$. The two questions are different, and the two partitions are independent.

**Proposition (the independence).** Each spectral stratum meets each P-class: the non-real quaternions meet all three, since $e_t+\tfrac12\vec e_x$ is timelike, $e_t+\vec e_x$ is null and $e_t+2\vec e_x$ is spacelike; the real axis minus the origin lies in the timelike class; the origin is null.

*Proof.* The three witnesses for the non-real stratum are computed by the formula, and the other two statements are the propositions on the real line and on the cone. Verified numerically.

**Remark (why the two cuts are kept apart).** The spectral strata are a stratification of the algebra by the discriminant $-4\lvert\vec q\rvert^2$ of the characteristic polynomial, and they are a property of the operator $L_{\tilde q}$. The P-classes are a partition by the value of a quadratic form, and they are a property of the algebra as a metric space. **A cut by a form and a cut by a spectrum are different instruments, and the quaternion algebra is the smallest algebra in which both can be made at once and disagree.** The four norms of the biquaternion block multiply the confusion by two, since the coefficient conjugation doubles the count both of the forms and of the spectra; the partition of the present article is the real case, and the comparison with the complex case is the subject of the following three articles.

**Remark (the map of the chapter).** The regular part $\{P\neq0\}$ is [The P-Regular Sector of the Quaternion Algebra](the-p-regular-sector-of-the-quaternion-algebra.html), the cone $\{P=0\}$ is [The P-Degenerate Sector of the Quaternion Algebra](the-p-degenerate-sector-of-the-quaternion-algebra.html), the level sets and their hyperbolic structure are [The P Level Sets and the Hyperbolic Structure of the Quaternion Algebra](the-p-level-sets-and-the-hyperbolic-structure-of-the-quaternion-algebra.html), and the topology of the cone is [The Topology of the P-Null Cone of the Quaternion Algebra](the-topology-of-the-p-null-cone-of-the-quaternion-algebra.html). The present article is the statement of the partition; the four following are its four readings.

## Summary

The plain algebraic norm is $P(\tilde q)=\mathrm{Sc}(\tilde q^2)=q_t^2-\lvert\vec q\rvert^2$, the quadratic form of the trace form of the plain product, of signature $(1,3)$ and rank four, and it is not multiplicative: $P(\vec e_x\vec e_y)=-1$ against $P(\vec e_x)P(\vec e_y)=1$.

Its sign partitions the algebra into the timelike class $\{P>0\}$, the null class $\{P=0\}$ and the spacelike class $\{P<0\}$, of real dimensions four, three and four; the first and the third are open, the second is a cone.

The null class is not the non-invertible class: every null element is invertible and has $N=2q_t^2>0$. The quaternion norm partitions the algebra as the invertibles and the origin, and the two partitions are as different as a definite cut and an indefinite one.

On the real line $P=\lambda^2\geq0$; on the vector subspace $P=-\lvert\vec q\rvert^2\leq0$; on a plane through the axis $P=\lambda^2-\mu^2$ of signature $(1,1)$ with the cone cut into the two lines $\mathbb{R}(e_t\pm\vec n)$; on the unit sphere $P=2q_t^2-1$, so the null class is a pair of circles.

The spectral strata of the three sectors are a third cut, by the discriminant and the spectrum, and the three cuts are independent: each spectral stratum meets each P-class in a non-empty set.

A worked line crosses the cone twice, at $s=-2\pm\sqrt3$, and two normalised null elements multiply to $e_t$: the null set is a cone of invertibles and not a set of zero divisors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra |
| $\tilde q=q_te_t+\vec q$ | the element, its scalar part and its vector part |
| $P(\tilde q)$ | the plain algebraic norm, $\mathrm{Sc}(\tilde q^2)$ |
| $N(\tilde q)$ | the quaternion norm, $\tilde q\tilde q^{\natural}$ |
| $\langle\cdot,\cdot\rangle_P$ | the polar form $\mathrm{Sc}(\tilde q_1\tilde q_2)$ |
| $\mathcal T,\mathcal N,\mathcal S$ | the timelike, null and spacelike classes |
| $\Pi_{\vec n}$ | the plane $\mathbb{R}e_t\oplus\mathbb{R}\vec n$ |

## Further Reading

- [Norm and Invertibility in the Quaternion Algebra](norm-and-invertibility-in-the-quaternion-algebra.html) for the two norms and the division property.
- [Quaternion Metrics](quaternion-metrics.html) for the family of forms $\mathrm{Sc}(g\tilde xg\tilde x)$ to which $P$ belongs.
- [The P-Regular Sector of the Quaternion Algebra](the-p-regular-sector-of-the-quaternion-algebra.html) and [The P-Degenerate Sector of the Quaternion Algebra](the-p-degenerate-sector-of-the-quaternion-algebra.html) for the two halves of the partition.
- [The Three Sectors of the Quaternion Algebra](the-three-sectors-of-the-quaternion-algebra.html) for the spectral cut that this one is kept apart from.
